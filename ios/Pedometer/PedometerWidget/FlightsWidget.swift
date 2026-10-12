import SwiftUI
import WidgetKit

/// Lock screen: flights climbed today, under a small staircase.
struct FlightsWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: "Flights", provider: TodayProvider()) { entry in
            FlightsBadge(flights: entry.today.flights)
                .containerBackground(for: .widget) { Color.clear }
        }
        .configurationDisplayName("Flights climbed")
        .description("Flights of stairs climbed today.")
        .supportedFamilies([.accessoryCircular])
    }
}

struct FlightsBadge: View {
    let flights: Double

    var body: some View {
        ZStack {
            AccessoryWidgetBackground()
            VStack(spacing: 4) {
                StairsShape()
                    .stroke(style: StrokeStyle(lineWidth: 2.5, lineCap: .round, lineJoin: .round))
                    .frame(width: 24, height: 17)
                    .widgetAccentable()
                Text(Metric.flights.format(flights))
                    .font(.system(size: 20, weight: .semibold, design: .rounded))
                    .monospacedDigit()
                    .lineLimit(1)
                    .minimumScaleFactor(0.6)
            }
            .padding(.horizontal, 12)
            .padding(.top, 2)
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("\(Metric.flights.format(flights)) \(Metric.flights.unit(for: flights)) climbed today")
    }
}

/// A staircase rising to the right, drawn as a single line.
struct StairsShape: Shape {
    var steps = 3

    func path(in rect: CGRect) -> Path {
        let run = rect.width / CGFloat(steps)
        let rise = rect.height / CGFloat(steps)
        var path = Path()
        path.move(to: CGPoint(x: rect.minX, y: rect.maxY))
        for step in 0..<steps {
            let x = rect.minX + CGFloat(step) * run
            let y = rect.maxY - CGFloat(step + 1) * rise
            path.addLine(to: CGPoint(x: x, y: y))
            path.addLine(to: CGPoint(x: x + run, y: y))
        }
        return path
    }
}

#Preview(as: .accessoryCircular) {
    FlightsWidget()
} timeline: {
    TodayEntry(date: .now, today: TodaySnapshot(flights: 4))
    TodayEntry(date: .now, today: TodaySnapshot(flights: 12))
}
