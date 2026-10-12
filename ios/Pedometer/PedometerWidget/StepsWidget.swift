import SwiftUI
import WidgetKit

/// Lock screen: today's steps inside a ring that closes at 10,000.
struct StepsWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: "Steps", provider: TodayProvider()) { entry in
            StepsRing(steps: entry.today.steps)
                .containerBackground(for: .widget) { Color.clear }
        }
        .configurationDisplayName("Steps")
        .description("Today's steps. The ring closes at \(Metric.steps.format(Goal.dailySteps)).")
        .supportedFamilies([.accessoryCircular])
    }
}

struct StepsRing: View {
    let steps: Double

    private let line: CGFloat = 5
    private var progress: Double { min(steps / Goal.dailySteps, 1) }

    var body: some View {
        ZStack {
            AccessoryWidgetBackground()
            Group {
                Circle()
                    .stroke(.white.opacity(0.22), lineWidth: line)
                Circle()
                    .trim(from: 0, to: progress)
                    .stroke(.white, style: StrokeStyle(lineWidth: line, lineCap: .round))
                    .rotationEffect(.degrees(-90))
                    .widgetAccentable()
            }
            .padding(3 + line / 2)

            VStack(spacing: 1) {
                Image(systemName: "figure.walk")
                    .font(.system(size: 12, weight: .semibold))
                Text(Metric.steps.format(steps))
                    .font(.system(size: 15, weight: .semibold, design: .rounded))
                    .monospacedDigit()
                    .lineLimit(1)
                    .minimumScaleFactor(0.6)
            }
            .padding(.horizontal, 12)
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("\(Metric.steps.format(steps)) steps, \(progress.formatted(.percent.precision(.fractionLength(0)))) of today's goal")
    }
}

#Preview(as: .accessoryCircular) {
    StepsWidget()
} timeline: {
    TodayEntry(date: .now, today: TodaySnapshot(steps: 7_240))
    TodayEntry(date: .now, today: TodaySnapshot(steps: 10_480))
}
