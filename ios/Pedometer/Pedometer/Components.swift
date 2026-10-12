import SwiftUI

/// Small grey capitals above a group of cards, as in "HISTORY".
struct SectionLabel: View {
    let text: String

    var body: some View {
        Text(text.uppercased())
            .font(.system(size: 13, weight: .semibold))
            .tracking(1)
            .foregroundStyle(Theme.secondary)
    }
}

/// A metric's icon and name, as in "STEPS".
struct MetricLabel: View {
    let metric: Metric

    var body: some View {
        HStack(spacing: 6) {
            Image(systemName: metric.symbol)
                .font(.system(size: 13, weight: .medium))
            Text(metric.title.uppercased())
                .font(.system(size: 13, weight: .semibold))
                .tracking(1)
        }
        .foregroundStyle(Theme.secondary)
        .lineLimit(1)
        .minimumScaleFactor(0.75)
    }
}

/// A large number with its unit beside it in grey.
struct Reading: View {
    let value: String
    let unit: String
    var size: CGFloat = 34

    var body: some View {
        HStack(alignment: .firstTextBaseline, spacing: size / 6) {
            Text(value)
                .font(.system(size: size, weight: .semibold))
                .monospacedDigit()
                .contentTransition(.numericText())
            Text(unit)
                .font(.system(size: max(15, size * 0.32)))
                .foregroundStyle(Theme.secondary)
        }
        .foregroundStyle(Theme.ink)
        .lineLimit(1)
        .minimumScaleFactor(0.6)
    }
}

/// An outlined capsule holding a short figure, as in "72%".
struct Pill<Content: View>: View {
    @ViewBuilder let content: Content

    var body: some View {
        content
            .font(.system(size: 15, weight: .semibold))
            .foregroundStyle(Theme.ink)
            .padding(.horizontal, 10)
            .padding(.vertical, 4)
            .overlay(Capsule().strokeBorder(Theme.track, lineWidth: 1))
    }
}

struct CapsuleBar: View {
    let progress: Double

    var body: some View {
        GeometryReader { proxy in
            ZStack(alignment: .leading) {
                Capsule().fill(Theme.track)
                if progress > 0 {
                    Capsule()
                        .fill(Theme.ink)
                        .frame(width: max(proxy.size.height, proxy.size.width * min(progress, 1)))
                }
            }
        }
        .frame(height: 8)
    }
}

// MARK: - Today

struct StepsCard: View {
    let steps: Double

    private var progress: Double { steps / Goal.dailySteps }
    private var remaining: Double { max(Goal.dailySteps - steps, 0) }

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack {
                MetricLabel(metric: .steps)
                Spacer()
                Pill {
                    if remaining == 0 {
                        Label("Goal", systemImage: "checkmark")
                    } else {
                        Text(progress.formatted(.percent.precision(.fractionLength(0))))
                    }
                }
            }
            Reading(value: Metric.steps.format(steps), unit: Metric.steps.unit(for: steps), size: 56)
            CapsuleBar(progress: progress)
            HStack {
                Text("Goal \(Metric.steps.format(Goal.dailySteps))")
                Spacer()
                Text(remaining == 0 ? "Done for today" : "\(Metric.steps.format(remaining)) to go")
            }
            .font(.footnote)
            .foregroundStyle(Theme.secondary)
        }
        .card()
        .animation(.snappy, value: steps)
    }
}

struct MetricTile: View {
    let metric: Metric
    let value: Double?

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            MetricLabel(metric: metric)
            Reading(value: value.map(metric.format) ?? "–", unit: metric.unit(for: value), size: 28)
        }
        .card(padding: 16)
        .animation(.snappy, value: value)
    }
}

struct ConnectCard: View {
    let connect: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(spacing: 12) {
                Image(systemName: "heart")
                    .font(.system(size: 15, weight: .medium))
                    .frame(width: 36, height: 36)
                    .background(Theme.well, in: Circle())
                Text("Connect Apple Health")
                    .font(.headline)
            }
            Text("Pedometer reads your steps, distance, flights climbed, active energy, and walking speed from Apple Health, and today's count from the iPhone's motion sensors. It never writes to Health.")
                .font(.subheadline)
                .foregroundStyle(Theme.secondary)
                .fixedSize(horizontal: false, vertical: true)
            Button(action: connect) {
                Text("Connect")
                    .font(.headline)
                    .foregroundStyle(Theme.card)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
                    .background(Theme.ink, in: Capsule())
            }
            .buttonStyle(.plain)
            .padding(.top, 4)
        }
        .foregroundStyle(Theme.ink)
        .card()
    }
}

// MARK: - History

/// "HISTORY" with Week · Month · Year beside it.
struct HistoryHeader: View {
    @Binding var range: HistoryRange

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            SectionLabel(text: "History")
            Spacer()
            HStack(spacing: 16) {
                ForEach(HistoryRange.allCases) { option in
                    Button(option.title) {
                        withAnimation(.snappy) { range = option }
                    }
                    .font(.system(size: 15, weight: option == range ? .semibold : .regular))
                    .foregroundStyle(option == range ? Theme.ink : Theme.secondary)
                    .accessibilityAddTraits(option == range ? .isSelected : [])
                }
            }
            .buttonStyle(.plain)
        }
        .padding(.horizontal, 4)
    }
}

struct Footer: View {
    var body: some View {
        Label("Counted on this iPhone — nothing is uploaded", systemImage: "lock")
            .font(.footnote)
            .foregroundStyle(Theme.secondary)
            .frame(maxWidth: .infinity)
    }
}
