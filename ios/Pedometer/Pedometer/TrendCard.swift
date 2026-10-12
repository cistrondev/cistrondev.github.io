import Charts
import SwiftUI

/// One metric over the chosen range: its daily average, the change from the
/// period before, and a chart. Touch the chart to read a single day.
struct TrendCard: View {
    let metric: Metric
    let range: HistoryRange
    let series: TrendSeries?

    @State private var selection: Date?

    private var points: [DayValue] { series?.points ?? [] }

    private var selected: DayValue? {
        guard let selection else { return nil }
        return points.first { Calendar.current.isDate($0.date, equalTo: selection, toGranularity: range.bin) }
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            HStack {
                MetricLabel(metric: metric)
                Spacer()
                Text(caption.uppercased())
                    .font(.system(size: 13, weight: .semibold))
                    .tracking(1)
                    .foregroundStyle(Theme.secondary)
                    .lineLimit(1)
            }
            Reading(value: shownValue.map(metric.format) ?? "–", unit: unitText)
                .padding(.top, 12)
            changeRow
                .padding(.top, 4)
            chart
                .frame(height: 140)
                .padding(.top, 18)
        }
        .card()
        .onChange(of: range) { selection = nil }
    }

    // MARK: Text

    private var shownValue: Double? { selected?.value ?? series?.average }

    private var unitText: String {
        let unit = metric.unit(for: shownValue)
        guard metric.isCumulative else { return selected == nil ? "\(unit) on average" : unit }
        // A selected day shows its total; a selected week, like the range, its daily average.
        return selected != nil && range != .year ? unit : "\(unit) a day"
    }

    private var caption: String {
        guard let selected else { return range.caption }
        if range == .year {
            return "Week of " + selected.date.formatted(.dateTime.day().month(.abbreviated))
        }
        return selected.date.formatted(.dateTime.weekday(.abbreviated).day().month(.abbreviated))
    }

    @ViewBuilder private var changeRow: some View {
        if let change = series?.change {
            HStack(spacing: 4) {
                Image(systemName: arrow(for: change))
                    .font(.system(size: 13, weight: .semibold))
                Text(abs(change).formatted(.percent.precision(.fractionLength(0))))
                    .font(.system(size: 15, weight: .semibold))
                Text(range.comparison)
                    .font(.system(size: 15))
                    .foregroundStyle(Theme.secondary)
            }
            .foregroundStyle(Theme.ink)
        } else {
            // Keeps every card the same height before there is a period to compare with.
            Text(" ").font(.system(size: 15))
        }
    }

    private func arrow(for change: Double) -> String {
        if change >= 0.005 { return "arrow.up.right" }
        if change <= -0.005 { return "arrow.down.right" }
        return "arrow.right"
    }

    // MARK: Chart

    private var chart: some View {
        Chart {
            ForEach(points) { point in
                let value = metric.displayValue(point.value)
                if range == .year {
                    AreaMark(x: .value("Week", point.date), y: .value(metric.title, value))
                        .foregroundStyle(LinearGradient(
                            colors: [Theme.ink.opacity(0.10), Theme.ink.opacity(0)],
                            startPoint: .top,
                            endPoint: .bottom
                        ))
                        .interpolationMethod(.catmullRom)
                    LineMark(x: .value("Week", point.date), y: .value(metric.title, value))
                        .foregroundStyle(Theme.ink)
                        .lineStyle(StrokeStyle(lineWidth: 2, lineCap: .round, lineJoin: .round))
                        .interpolationMethod(.catmullRom)
                } else {
                    BarMark(x: .value("Day", point.date, unit: .day), y: .value(metric.title, value))
                        .foregroundStyle(barColor(for: point))
                        .cornerRadius(range == .week ? 5 : 2)
                }
            }

            if let selected {
                if range == .year {
                    RuleMark(x: .value("Week", selected.date))
                        .foregroundStyle(Theme.track)
                    PointMark(
                        x: .value("Week", selected.date),
                        y: .value(metric.title, metric.displayValue(selected.value))
                    )
                    .foregroundStyle(Theme.ink)
                    .symbolSize(60)
                }
            } else if let average = series?.average {
                RuleMark(y: .value("Average", metric.displayValue(average)))
                    .foregroundStyle(Theme.secondary.opacity(0.6))
                    .lineStyle(StrokeStyle(lineWidth: 1, dash: [3, 4]))
            }
        }
        .chartXSelection(value: $selection)
        .chartYAxis(.hidden)
        .chartXAxis {
            AxisMarks(values: axisValues) { _ in
                AxisValueLabel(format: axisFormat, centered: range != .year)
                    .font(.system(size: 11))
                    .foregroundStyle(Theme.secondary)
            }
        }
    }

    /// While a day is selected, the other bars fade.
    private func barColor(for point: DayValue) -> Color {
        guard let selected, selected != point else { return Theme.ink }
        return Theme.ink.opacity(0.15)
    }

    private var axisValues: AxisMarkValues {
        switch range {
        case .week: .stride(by: .day)
        case .month: .stride(by: .day, count: 7)
        case .year: .stride(by: .month, count: 3)
        }
    }

    private var axisFormat: Date.FormatStyle {
        switch range {
        case .week: .dateTime.weekday(.narrow)
        case .month: .dateTime.day().month(.abbreviated)
        case .year: .dateTime.month(.abbreviated)
        }
    }
}
