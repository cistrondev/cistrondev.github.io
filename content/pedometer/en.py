# Pedometer in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py. English page copy stays in APPS; this
# file adds the FAQ and the guide (a step counter on the Lock Screen).
#
# Copy rules: plain sentences, one idea each. Button names are the app's own
# (Pedometer Shared/Localizable.xcstrings) or Apple's, written in **bold**.
# Never name a rival. Facts to keep true: free, no subscription; the tip jar is
# optional and unlocks nothing; reads Apple Health and writes only recorded
# walks and runs; location only while recording; live heart rate needs iOS 26
# and AirPods Pro 3, Powerbeats Pro 2 or a Bluetooth strap; goals start at
# 10,000 steps, 8 km or 5 miles, 10 flights. Don't say "no ads": the app shows
# a card for LifeTrends.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "ui": {
        "summary": "Lock Screen widgets",
    },
    "guide_link": "How to put a step counter on your iPhone Lock Screen",
    "faq": [
        ("What is a free step counter app for iPhone without a subscription?", [
            "Pedometer is free, with no subscription and no account. It shows your steps, "
            "distance and flights climbed as plain numbers and charts, and puts them on "
            "your Lock Screen and Home Screen as widgets. It also records walks and runs "
            "with GPS. An optional tip jar unlocks nothing. [See it on the App Store](store).",
        ]),
        ("How do I show my step count on the iPhone Lock Screen?", [
            [
                "Install Pedometer, open it and tap **Connect** to let it read Apple Health.",
                "Touch and hold the Lock Screen, tap **Customize**, then choose the Lock "
                "Screen.",
                "Tap the widget area under the clock, choose **Pedometer**, and add Steps, "
                "Distance or Flights climbed.",
                "Tap **Done**.",
            ],
            "The steps and distance widgets sit in a ring that closes at your goal. "
            "[Step-by-step guide](guide).",
        ]),
        ("Do I need an Apple Watch?", [
            "No. Your iPhone counts your steps on its own when you carry it. If you also wear "
            "an Apple Watch, Pedometer reads Apple Health, which combines the steps from both "
            "without counting them twice.",
        ]),
        ("Can it record walks and runs with GPS?", [
            "Yes. Tap **Walk** or **Run** under **Walks and runs**. The map draws your route "
            "and shows time, distance, speed or pace, calories, elevation and climb. While "
            "you go, the numbers stay on the Lock Screen with a pause button. Each walk or "
            "run is saved to Apple Health with its route, and you can share a picture of it.",
        ]),
        ("Can it show my heart rate without an Apple Watch?", [
            "Yes, on iOS 26. With AirPods Pro 3, Powerbeats Pro 2 or a Bluetooth heart rate "
            "strap, your heart rate shows live during a walk or run.",
        ]),
        ("Can I change my daily step goal?", [
            "Yes. Set a daily goal for steps, distance and flights climbed. They start at "
            "10,000 steps, 8 km or 5 miles, and 10 flights. The widgets close their rings at "
            "your goals.",
        ]),
        ("Can I see my step history and records?", [
            "Yes. History shows one chart per number for the last week, month or year, with "
            "the daily average and the change from the period before. Records show your "
            "totals for every month and year, and your best day, week and month for steps, "
            "flights climbed and walking speed.",
        ]),
        ("Is Pedometer really free?", [
            "Yes. Every feature is free and there is no subscription. Under **Settings** › "
            "**Support Pedometer** you can leave a tip if you like. Tips are optional and "
            "unlock nothing.",
        ]),
        ("Does Pedometer upload my health data?", [
            "No. Everything is counted and stored on your iPhone, and nothing is uploaded. "
            "Pedometer reads Apple Health and writes to it only the walks and runs you "
            "record. Your location is used only while you record. There is no account, no "
            "analytics and no tracking. [Privacy policy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "step-counter-lock-screen",
        "title": "How to put a step counter on your iPhone Lock Screen",
        "description": "Step by step: add a free step counter widget to your iPhone Lock "
                       "Screen and Home Screen, with distance and flights climbed beside "
                       "it. No Apple Watch or subscription needed.",
        "lead": "Your iPhone already counts your steps. Pedometer puts that count on your "
                "Lock Screen, so you see it every time you pick up the phone. It takes about "
                "a minute, and you need no Apple Watch.",
        "choose": [
            ("Steps", "In a ring that closes at your goal"),
            ("Distance", "In a ring, in km or miles"),
            ("Flights climbed", "A figure climbs a staircase"),
        ],
        "steps": [
            ("Install Pedometer",
             "Download [Pedometer from the App Store](store). It is free, with no account."),
            ("Connect Apple Health",
             "Open Pedometer and tap **Connect**. Allow it to read steps, distance and "
             "flights climbed. Your iPhone has been counting these all along, so your "
             "history appears right away."),
            ("Set your goals",
             "Choose a daily goal for steps, distance and flights climbed under **Daily "
             "goals**. The widget rings close when you reach them."),
            ("Edit the Lock Screen",
             "Lock your iPhone, wake it, then touch and hold the Lock Screen. Tap "
             "**Customize** and choose the Lock Screen."),
            ("Add the widget",
             "Tap the widget area under the clock. Find **Pedometer** in the list and tap "
             "Steps, Distance or Flights climbed. You can add more than one."),
            ("Tap Done",
             "Your step count is now on the Lock Screen and updates through the day."),
            ("Add it to the Home Screen too",
             "Touch and hold an empty part of the Home Screen, tap **Edit**, then **Add "
             "Widget**. Search for Pedometer and choose small, medium or large. The large "
             "size adds today hour by hour."),
        ],
        "tips": [
            ("Light, dark or steps only",
             "Touch and hold the Home Screen widget and choose **Edit Widget** to make it "
             "light or dark, or to show the steps alone."),
            ("Pick a color",
             "Graphite, blue, green, orange, pink or purple, for the goal bars, the charts "
             "and the Home Screen widget."),
            ("Going for a walk?",
             "Tap **Walk** or **Run** in the app to record your route with GPS. The numbers "
             "stay on the Lock Screen while you go."),
            ("Nothing leaves your iPhone",
             "Pedometer has no account and uploads nothing. It reads Apple Health on your "
             "iPhone."),
        ],
        "updated": "Written for Pedometer 1.5 on iOS 26, October 2026.",
        "cta_title": "Your steps, at a glance",
        "cta_text": "A free step counter for your Lock Screen and Home Screen, with walks "
                    "and runs on a map. No account, no subscription.",
    },
}
