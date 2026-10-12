import SwiftUI
import WidgetKit

@main
struct PedometerWidgetBundle: WidgetBundle {
    var body: some Widget {
        StepsWidget()
        FlightsWidget()
    }
}
