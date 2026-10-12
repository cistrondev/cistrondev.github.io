import Combine
import SwiftUI

struct ContentView: View {
    @State var model = DashboardModel()
    @Environment(\.scenePhase) private var scenePhase

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 12) {
                header
                    .padding(.top, 28)
                    .padding(.bottom, 12)

                switch model.access {
                case .unknown:
                    EmptyView()
                case .needed:
                    ConnectCard {
                        Task { await model.connect() }
                    }
                case .unavailable:
                    Text("Apple Health isn't available on this device.")
                        .foregroundStyle(Theme.secondary)
                case .granted:
                    todayCards
                    HistoryHeader(range: $model.range)
                        .padding(.top, 28)
                        .padding(.bottom, 4)
                    ForEach(Metric.allCases) { metric in
                        TrendCard(metric: metric, range: model.range, series: model.series[metric])
                    }
                }

                Footer()
                    .padding(.vertical, 28)
            }
            .padding(.horizontal, 16)
        }
        .scrollIndicators(.hidden)
        .background(Theme.background.ignoresSafeArea())
        .task(id: scenePhase) {
            if scenePhase == .active {
                await model.refresh()
            }
        }
        .onChange(of: model.range) {
            Task { await model.rangeChanged() }
        }
        .onReceive(NotificationCenter.default.publisher(for: .healthDataChanged)) { _ in
            Task { await model.refreshToday() }
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("Today")
                .font(.system(size: 34, weight: .bold))
                .foregroundStyle(Theme.ink)
            Text(Date.now.formatted(.dateTime.weekday(.wide).day().month(.wide)))
                .font(.system(size: 17))
                .foregroundStyle(Theme.secondary)
        }
        .padding(.horizontal, 4)
    }

    private var todayCards: some View {
        VStack(spacing: 12) {
            StepsCard(steps: model.today[.steps] ?? 0)
            Grid(horizontalSpacing: 12, verticalSpacing: 12) {
                GridRow {
                    MetricTile(metric: .distance, value: model.today[.distance])
                    MetricTile(metric: .flights, value: model.today[.flights])
                }
                GridRow {
                    MetricTile(metric: .energy, value: model.today[.energy])
                    MetricTile(metric: .walkingSpeed, value: model.today[.walkingSpeed])
                }
            }
        }
    }
}

#Preview {
    ContentView(model: .preview)
}
