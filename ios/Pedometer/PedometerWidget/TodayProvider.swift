import WidgetKit

struct TodayEntry: TimelineEntry {
    let date: Date
    let today: TodaySnapshot
}

/// Shared by both widgets: today's totals, refreshed every 15 minutes, and
/// back to zero at midnight.
struct TodayProvider: TimelineProvider {
    func placeholder(in context: Context) -> TodayEntry {
        TodayEntry(date: .now, today: TodaySnapshot(steps: 6_480, distance: 4_700, flights: 8))
    }

    func getSnapshot(in context: Context, completion: @escaping (TodayEntry) -> Void) {
        guard !context.isPreview else {
            completion(placeholder(in: context))
            return
        }
        Task {
            let today = await Today.read()
            completion(TodayEntry(date: .now, today: today))
        }
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<TodayEntry>) -> Void) {
        Task {
            let today = await Today.read()
            let now = Date.now
            var entries = [TodayEntry(date: now, today: today)]

            let refresh = now.addingTimeInterval(15 * 60)
            let calendar = Calendar.current
            if let midnight = calendar.date(byAdding: .day, value: 1, to: calendar.startOfDay(for: now)),
               midnight < refresh {
                entries.append(TodayEntry(date: midnight, today: TodaySnapshot(date: midnight)))
            }
            completion(Timeline(entries: entries, policy: .after(refresh)))
        }
    }
}
