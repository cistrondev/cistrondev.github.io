import CoreMotion
import Foundation

/// Today's steps, distance (metres) and flights climbed.
struct TodaySnapshot: Codable, Equatable {
    /// Start of the day these totals belong to.
    var date: Date
    var steps: Double
    var distance: Double
    var flights: Double

    init(date: Date = Calendar.current.startOfDay(for: .now), steps: Double = 0, distance: Double = 0, flights: Double = 0) {
        self.date = date
        self.steps = steps
        self.distance = distance
        self.flights = flights
    }

    init(totals: [Metric: Double]) {
        self.init(steps: totals[.steps] ?? 0, distance: totals[.distance] ?? 0, flights: totals[.flights] ?? 0)
    }

    /// Keeps the larger of each value when both readings are from the same
    /// day. A day's totals only grow, so the larger one is the more recent.
    func merged(with other: TodaySnapshot?) -> TodaySnapshot {
        guard let other, Calendar.current.isDate(other.date, inSameDayAs: date) else { return self }
        return TodaySnapshot(
            date: date,
            steps: max(steps, other.steps),
            distance: max(distance, other.distance),
            flights: max(flights, other.flights)
        )
    }
}

/// The best numbers for today, wherever they can be read from.
///
/// Apple Health is the main source, but it is encrypted while the iPhone is
/// locked, which is exactly when lock screen widgets refresh. So the last
/// Health reading is saved where the widgets can see it, and the motion
/// coprocessor, which keeps counting while locked, tops it up.
enum Today {
    static func read() async -> TodaySnapshot {
        let start = Calendar.current.startOfDay(for: .now)
        let health = try? await HealthData.shared.totals(since: start, metrics: [.steps, .distance, .flights])
        return await combine(health)
    }

    /// Combines totals already read from Apple Health (nil if it could not be
    /// read) with the saved reading and the motion coprocessor, and saves the result.
    static func combine(_ health: [Metric: Double]?) async -> TodaySnapshot {
        let motion = await MotionData.today()
        let best = TodaySnapshot(totals: health ?? [:])
            .merged(with: SnapshotStore.load())
            .merged(with: motion)
        SnapshotStore.save(best)
        return best
    }
}

/// The latest snapshot, shared between the app and its widgets through an App Group.
enum SnapshotStore {
    /// Must match the App Group in both .entitlements files.
    static let appGroup = "group.com.cistrondev.pedometer"

    private static let key = "today"
    private static var defaults: UserDefaults? { UserDefaults(suiteName: appGroup) }

    /// Today's saved snapshot, or nil if the last one is from an earlier day.
    static func load() -> TodaySnapshot? {
        guard let data = defaults?.data(forKey: key),
              let snapshot = try? JSONDecoder().decode(TodaySnapshot.self, from: data),
              Calendar.current.isDateInToday(snapshot.date)
        else { return nil }
        return snapshot
    }

    static func save(_ snapshot: TodaySnapshot) {
        guard let data = try? JSONEncoder().encode(snapshot) else { return }
        defaults?.set(data, forKey: key)
    }
}

/// The iPhone's own step counter. It only covers the iPhone (not an Apple
/// Watch), but it can be read while the iPhone is locked.
enum MotionData {
    static func today() async -> TodaySnapshot? {
        let status = CMPedometer.authorizationStatus()
        guard CMPedometer.isStepCountingAvailable(), status != .denied, status != .restricted else { return nil }

        let start = Calendar.current.startOfDay(for: .now)
        let pedometer = CMPedometer()
        return await withCheckedContinuation { continuation in
            pedometer.queryPedometerData(from: start, to: .now) { data, _ in
                withExtendedLifetime(pedometer) {}
                guard let data else {
                    continuation.resume(returning: nil)
                    return
                }
                continuation.resume(returning: TodaySnapshot(
                    date: start,
                    steps: data.numberOfSteps.doubleValue,
                    distance: data.distance?.doubleValue ?? 0,
                    flights: data.floorsAscended?.doubleValue ?? 0
                ))
            }
        }
    }
}
