import Foundation
import HealthKit

/// Everything the app counts. Values are kept in `healthUnit` and converted
/// for display, so kilometres or miles follow the iPhone's region settings.
enum Metric: String, CaseIterable, Identifiable {
    case steps, distance, flights, energy, walkingSpeed

    var id: String { rawValue }

    var title: String {
        switch self {
        case .steps: "Steps"
        case .distance: "Distance"
        case .flights: "Flights"
        case .energy: "Active energy"
        case .walkingSpeed: "Walking speed"
        }
    }

    var symbol: String {
        switch self {
        case .steps: "figure.walk"
        case .distance: "figure.walk.motion"
        case .flights: "figure.stairs"
        case .energy: "flame"
        case .walkingSpeed: "gauge.with.needle"
        }
    }

    var quantityType: HKQuantityType {
        switch self {
        case .steps: HKQuantityType(.stepCount)
        case .distance: HKQuantityType(.distanceWalkingRunning)
        case .flights: HKQuantityType(.flightsClimbed)
        case .energy: HKQuantityType(.activeEnergyBurned)
        case .walkingSpeed: HKQuantityType(.walkingSpeed)
        }
    }

    var healthUnit: HKUnit {
        switch self {
        case .steps, .flights: .count()
        case .distance: .meter()
        case .energy: .kilocalorie()
        case .walkingSpeed: .meter().unitDivided(by: .second())
        }
    }

    /// Steps add up over a day; walking speed is averaged.
    var isCumulative: Bool { self != .walkingSpeed }

    var statisticsOptions: HKStatisticsOptions {
        isCumulative ? .cumulativeSum : .discreteAverage
    }

    /// Converts a value in `healthUnit` to the unit shown on screen.
    func displayValue(_ value: Double) -> Double {
        switch self {
        case .distance: Units.usesMiles ? value / 1_609.344 : value / 1_000
        case .walkingSpeed: Units.usesMiles ? value * 2.236_936 : value * 3.6
        case .steps, .flights, .energy: value
        }
    }

    func format(_ value: Double) -> String {
        let digits = (self == .distance || self == .walkingSpeed) ? 1 : 0
        return displayValue(value).formatted(.number.precision(.fractionLength(digits)))
    }

    func unit(for value: Double?) -> String {
        let isOne = value.map { format($0) == 1.formatted() } ?? false
        switch self {
        case .steps: return isOne ? "step" : "steps"
        case .distance: return Units.usesMiles ? "mi" : "km"
        case .flights: return isOne ? "flight" : "flights"
        case .energy: return "kcal"
        case .walkingSpeed: return Units.usesMiles ? "mph" : "km/h"
        }
    }
}

enum Units {
    /// The US and the UK measure walks in miles.
    static var usesMiles: Bool { Locale.current.measurementSystem != .metric }
}

enum Goal {
    /// The steps ring closes here.
    static let dailySteps: Double = 10_000
}

/// One bar or point on a chart: the total (or average) for the interval
/// starting at `date`.
struct DayValue: Identifiable, Hashable {
    let date: Date
    let value: Double

    var id: Date { date }
}

extension Array where Element == DayValue {
    var mean: Double? {
        isEmpty ? nil : map(\.value).reduce(0, +) / Double(count)
    }
}
