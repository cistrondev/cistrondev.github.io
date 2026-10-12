import SwiftUI
import WidgetKit

@main
struct PedometerApp: App {
    init() {
        Updates.startIfAuthorized()
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

/// Keeps the lock screen widgets current. Apple Health wakes the app when new
/// steps or flights arrive; the app saves the new totals for the widgets and
/// asks them to redraw.
enum Updates {
    static func startIfAuthorized() {
        Task {
            guard HealthData.isAvailable else { return }
            let needsPermission = await HealthData.shared.needsAuthorization()
            if !needsPermission {
                start()
            }
        }
    }

    static func start() {
        HealthData.shared.observeChanges {
            _ = await Today.read()
            WidgetCenter.shared.reloadAllTimelines()
            await MainActor.run {
                NotificationCenter.default.post(name: .healthDataChanged, object: nil)
            }
        }
    }
}

extension Notification.Name {
    static let healthDataChanged = Notification.Name("healthDataChanged")
}
