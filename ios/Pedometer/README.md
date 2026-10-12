# Pedometer

A small iPhone pedometer, styled like LifeTrends: black ink on light grey,
white cards, grey small-caps labels, and plain charts.

- **Today**: steps against a 10,000 goal, plus distance, flights climbed,
  active energy, and walking speed.
- **History**: one chart per metric for the last week, month, or year, with
  the daily average and the change from the period before. Touch a chart to
  read a single day (or a single week in the year view).
- **Two lock screen widgets**, both circular: steps inside a ring that closes
  at 10,000, and flights climbed under a small staircase.

The app only reads data. Nothing is written to Health, and nothing leaves the iPhone.

## Running it

Requires Xcode 16 or later and iOS 17 or later. Use a real iPhone: the
simulator has no Health data unless you add some in its Health app.

1. Open `Pedometer.xcodeproj`.
2. Select each target (**Pedometer** and **PedometerWidgetExtension**), open
   **Signing & Capabilities**, and choose your team. If Xcode reports a
   provisioning error for the App Group, tick `group.com.cistrondev.pedometer`
   under App Groups in the same tab (or add it with the refresh button).
3. Run on your iPhone, tap **Connect**, and allow Health and Motion & Fitness.
4. Add the widgets: touch and hold the lock screen, tap **Customize** >
   **Lock Screen**, tap the row under the clock, and pick **Pedometer**.

The bundle IDs are `com.cistrondev.pedometer` and
`com.cistrondev.pedometer.widget`, and the App Group is
`group.com.cistrondev.pedometer`. If you change the App Group, change it in
`Pedometer.entitlements`, `PedometerWidget.entitlements`, and
`SnapshotStore.appGroup` in `Shared/Today.swift`.

## How the lock screen stays current

Apple Health is encrypted while the iPhone is locked, which is when lock
screen widgets refresh. So the widgets combine three sources and show the
largest value for each (a day's totals only go up):

1. Apple Health, when it can be read. This includes Apple Watch steps.
2. The last Health reading, saved in the App Group by the app and the widgets.
3. The iPhone's motion coprocessor (Core Motion), which keeps counting while
   the iPhone is locked but only sees the iPhone's own steps.

The app also asks Health to wake it when new steps or flights arrive (iOS
allows this about hourly). It then saves the new totals and reloads the
widgets. The widgets refresh themselves every 15 minutes and go back to zero
at midnight.

## Files

```
Shared/            compiled into both the app and the widget
  Metric.swift       the five metrics: Health types, units, formatting
  HealthData.swift   HealthKit permission, totals, daily history, change observers
  Today.swift        today's snapshot, the App Group store, Core Motion
Pedometer/         the app
  ContentView.swift  the one screen: Today, then History
  TrendCard.swift    a metric's chart card
  History.swift      week / month / year ranges and their averages
  Components.swift   cards, labels, the goal bar, the Connect card
  DashboardModel.swift  loads everything; preview data for Xcode previews
  Theme.swift        colours (light and dark)
PedometerWidget/   the two lock screen widgets
```

The three folders are synchronized with Xcode, so a file added to one joins
its targets automatically.
