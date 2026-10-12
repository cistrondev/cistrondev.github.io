import Foundation
import Observation
import WidgetKit

@MainActor
@Observable
final class DashboardModel {
    enum Access { case unknown, needed, unavailable, granted }

    var access: Access = .unknown
    var range: HistoryRange = .week
    private(set) var today: [Metric: Double] = [:]
    private(set) var history: [HistoryRange: [Metric: TrendSeries]] = [:]

    /// Previews show sample data and never touch HealthKit.
    private var isPreview = false

    var series: [Metric: TrendSeries] { history[range] ?? [:] }

    func refresh() async {
        guard !isPreview else { return }
        guard HealthData.isAvailable else {
            access = .unavailable
            return
        }
        let needsPermission = await HealthData.shared.needsAuthorization()
        guard !needsPermission else {
            access = .needed
            return
        }
        access = .granted
        await refreshToday()
        // Reload the range on screen; the others reload when picked.
        let shown = range
        let loaded = await loadSeries(for: shown)
        history = [shown: loaded]
    }

    func connect() async {
        try? await HealthData.shared.requestAuthorization()
        Updates.start()
        await refresh()
    }

    func refreshToday() async {
        guard !isPreview else { return }
        let start = Calendar.current.startOfDay(for: .now)
        let health = try? await HealthData.shared.totals(since: start)
        let best = await Today.combine(health)
        var values = health ?? [:]
        values[.steps] = best.steps
        values[.distance] = best.distance
        values[.flights] = best.flights
        today = values
        WidgetCenter.shared.reloadAllTimelines()
    }

    func rangeChanged() async {
        let shown = range
        guard access == .granted, history[shown] == nil else { return }
        let loaded = await loadSeries(for: shown)
        history[shown] = loaded
    }

    private func loadSeries(for range: HistoryRange) async -> [Metric: TrendSeries] {
        var result: [Metric: TrendSeries] = [:]
        for metric in Metric.allCases {
            var days = (try? await HealthData.shared.daily(metric, days: range.days * 2)) ?? []
            // Today's bar matches the number at the top, which may include
            // steps the motion sensors counted before they reached Health.
            if metric.isCumulative, let latest = today[metric], let last = days.last,
               Calendar.current.isDateInToday(last.date) {
                days[days.count - 1] = DayValue(date: last.date, value: max(last.value, latest))
            }
            result[metric] = TrendSeries(range: range, days: days)
        }
        return result
    }
}

#if DEBUG
extension DashboardModel {
    static var preview: DashboardModel {
        let model = DashboardModel()
        model.isPreview = true
        model.access = .granted
        model.today = [.steps: 7_240, .distance: 5_310, .flights: 9, .energy: 312, .walkingSpeed: 1.32]
        for range in HistoryRange.allCases {
            var series: [Metric: TrendSeries] = [:]
            for metric in Metric.allCases {
                series[metric] = TrendSeries(range: range, days: .sample(metric, days: range.days * 2))
            }
            model.history[range] = series
        }
        return model
    }
}

extension Array where Element == DayValue {
    /// Plausible, repeatable numbers for previews.
    static func sample(_ metric: Metric, days: Int) -> [DayValue] {
        let base: Double = switch metric {
        case .steps: 8_000
        case .distance: 6_000
        case .flights: 10
        case .energy: 350
        case .walkingSpeed: 1.35
        }
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: .now)
        return (0..<days).compactMap { offset in
            guard let date = calendar.date(byAdding: .day, value: offset - days + 1, to: today) else { return nil }
            let x = Double(offset)
            let swing = metric == .walkingSpeed ? 0.06 : 0.35
            let trend = 1 + 0.15 * x / Double(days)
            let value = base * trend * (1 + swing * sin(x * 1.7) * cos(x * 0.37))
            return DayValue(date: date, value: Swift.max(value, 0))
        }
    }
}
#endif
