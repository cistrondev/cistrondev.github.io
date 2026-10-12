import Foundation

enum HistoryRange: String, CaseIterable, Identifiable {
    case week, month, year

    var id: Self { self }

    var title: String {
        switch self {
        case .week: "Week"
        case .month: "Month"
        case .year: "Year"
        }
    }

    var days: Int {
        switch self {
        case .week: 7
        case .month: 30
        case .year: 365
        }
    }

    var caption: String {
        switch self {
        case .week: "Last 7 days"
        case .month: "Last 30 days"
        case .year: "Last 12 months"
        }
    }

    var comparison: String {
        switch self {
        case .week: "vs the 7 days before"
        case .month: "vs the 30 days before"
        case .year: "vs the year before"
        }
    }

    /// Week and month draw one bar a day; a year draws one point a week.
    var bin: Calendar.Component { self == .year ? .weekOfYear : .day }
}

/// One metric over one range, ready to chart.
struct TrendSeries {
    /// Daily values, or weekly averages for a year.
    let points: [DayValue]
    /// Average per day across the range.
    let average: Double?
    /// Average per day across the same length of time just before it.
    let previousAverage: Double?

    /// `days` holds twice the range: the period before it, then the range itself.
    init(range: HistoryRange, days: [DayValue]) {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: .now)
        let start = calendar.date(byAdding: .day, value: -(range.days - 1), to: today) ?? today

        let current = days.filter { $0.date >= start }
        // Leading zeros are days before the person's first recorded step;
        // they would make the earlier period look emptier than it was.
        let recorded = Array(days.drop(while: { $0.value == 0 }))
        average = recorded.filter { $0.date >= start }.mean
        previousAverage = recorded.filter { $0.date < start }.mean

        if range == .year {
            let weeks = Dictionary(grouping: current) { day in
                calendar.dateInterval(of: .weekOfYear, for: day.date)?.start ?? day.date
            }
            points = weeks
                .compactMap { week, values in values.mean.map { DayValue(date: week, value: $0) } }
                .sorted { $0.date < $1.date }
        } else {
            points = current
        }
    }

    /// Fractional change from the previous period, e.g. 0.12 for 12% more.
    var change: Double? {
        guard let average, let previousAverage, previousAverage > 0 else { return nil }
        return average / previousAverage - 1
    }
}
