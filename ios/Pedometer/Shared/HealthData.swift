import Foundation
import HealthKit

/// Read-only access to Apple Health. Used by the app and by the widgets,
/// which share the app's permission.
final class HealthData {
    static let shared = HealthData()

    let store = HKHealthStore()
    private var observers: [HKObserverQuery] = []

    static var isAvailable: Bool { HKHealthStore.isHealthDataAvailable() }

    private static let readTypes: Set<HKObjectType> = Set(Metric.allCases.map { $0.quantityType as HKObjectType })

    // MARK: Permission

    /// True until the person has seen the Health permission sheet. HealthKit
    /// never says whether reading was allowed, only whether it was asked.
    func needsAuthorization() async -> Bool {
        guard Self.isAvailable else { return false }
        let status = try? await store.statusForAuthorizationRequest(toShare: [], read: Self.readTypes)
        return status == .shouldRequest
    }

    func requestAuthorization() async throws {
        try await store.requestAuthorization(toShare: [], read: Self.readTypes)
    }

    // MARK: Queries

    /// The total (or average) for one metric between two dates, or nil when
    /// nothing was recorded. Throws while the iPhone is locked, because
    /// Health data is encrypted then.
    func total(_ metric: Metric, from start: Date, to end: Date) async throws -> Double? {
        let samples = HKQuery.predicateForSamples(withStart: start, end: end, options: .strictStartDate)
        let descriptor = HKStatisticsQueryDescriptor(
            predicate: .quantitySample(type: metric.quantityType, predicate: samples),
            options: metric.statisticsOptions
        )
        do {
            let statistics = try await descriptor.result(for: store)
            let quantity = metric.isCumulative ? statistics?.sumQuantity() : statistics?.averageQuantity()
            return quantity?.doubleValue(for: metric.healthUnit)
        } catch let error as HKError where error.code == .errorNoData {
            return nil
        }
    }

    /// Totals for each metric from `start` until now. Metrics with no data are left out.
    func totals(since start: Date, metrics: [Metric] = Metric.allCases) async throws -> [Metric: Double] {
        try await withThrowingTaskGroup(of: (Metric, Double?).self) { group in
            for metric in metrics {
                group.addTask {
                    let value = try await self.total(metric, from: start, to: .now)
                    return (metric, value)
                }
            }
            var totals: [Metric: Double] = [:]
            for try await (metric, value) in group {
                totals[metric] = value
            }
            return totals
        }
    }

    /// One value per day for the last `days` days, oldest first, today last.
    /// Days without data count as zero for totals and are skipped for averages.
    func daily(_ metric: Metric, days: Int) async throws -> [DayValue] {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: .now)
        guard let start = calendar.date(byAdding: .day, value: -(days - 1), to: today) else { return [] }

        let descriptor = HKStatisticsCollectionQueryDescriptor(
            predicate: .quantitySample(
                type: metric.quantityType,
                predicate: HKQuery.predicateForSamples(withStart: start, end: .now)
            ),
            options: metric.statisticsOptions,
            anchorDate: today,
            intervalComponents: DateComponents(day: 1)
        )
        let collection = try await descriptor.result(for: store)

        var values: [DayValue] = []
        collection.enumerateStatistics(from: start, to: .now) { statistics, _ in
            let quantity = metric.isCumulative ? statistics.sumQuantity() : statistics.averageQuantity()
            if let value = quantity?.doubleValue(for: metric.healthUnit) {
                values.append(DayValue(date: statistics.startDate, value: value))
            } else if metric.isCumulative {
                values.append(DayValue(date: statistics.startDate, value: 0))
            }
        }
        return values
    }

    // MARK: Updates

    /// Calls `onChange` whenever new steps or flights reach Apple Health,
    /// including when the app is in the background (at most about hourly,
    /// as iOS decides). Calling it again replaces the previous observers.
    func observeChanges(_ onChange: @escaping () async -> Void) {
        for query in observers {
            store.stop(query)
        }
        observers = [Metric.steps, .flights].map { metric in
            let query = HKObserverQuery(sampleType: metric.quantityType, predicate: nil) { _, completion, error in
                guard error == nil else {
                    completion()
                    return
                }
                Task {
                    await onChange()
                    completion()
                }
            }
            store.execute(query)
            store.enableBackgroundDelivery(for: metric.quantityType, frequency: .hourly) { _, _ in }
            return query
        }
    }
}
