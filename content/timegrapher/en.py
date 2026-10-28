# Timegrapher in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py. English page copy stays in APPS; this
# file adds the FAQ and the guide (how to check a watch's accuracy).
#
# Copy rules: plain sentences, one idea each. Button names are the app's own
# (Timegrapher/Localizable.xcstrings) and are written in **bold**. Never name a
# rival app. Facts to keep true: the first watch is free and Pro is a one-time
# purchase; audio is analysed live and never recorded; beat rate is detected
# from 18,000 to 36,000 bph; a measurement stops by itself at 0:30. The verdict
# bands are the app's own (Timegrapher's verdict code): rate under 5 s/d is the
# chronometer range, under 15 acceptable, 30+ needs regulation; beat error
# under 0.3 ms well in beat, 0.8-1.5 adjustment recommended; amplitude 250-315
# healthy, under 220 low, under 200 very low, over 315 risk of knocking.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "ui": {
        "summary": "At a glance",
    },
    "guide_link": "How to check your mechanical watch's accuracy with an iPhone",
    "faq": [
        ("Can an iPhone measure how accurate my mechanical watch is?", [
            "Yes. Timegrapher listens to the watch through the iPhone's own microphone and "
            "works like a watchmaker's timing machine. In about 30 seconds it shows the rate "
            "(seconds gained or lost per day), the amplitude (how far the balance wheel "
            "swings) and the beat error (the difference between tick and tock).",
            "It works with automatic and hand-wound watches. The first watch is free, and "
            "there is no subscription. [See it on the App Store](store).",
        ]),
        ("How do I measure my watch with Timegrapher?", [
            [
                "Wind the watch and go somewhere quiet.",
                "Tap **Add watch** and enter the movement and its lift angle, if you know it.",
                "Tap **Measure** and rest the bottom edge of the iPhone firmly on the watch, "
                "ideally on the glass.",
                "Keep still. The measurement stops by itself at 0:30 and shows the rate, "
                "amplitude, beat error and a verdict.",
            ],
            "[Step-by-step guide](guide).",
        ]),
        ("What are good values for rate, amplitude and beat error?", [
            "These are the bands Timegrapher uses for its verdict:",
            [
                "**Rate:** within ±5 seconds a day is chronometer territory. Up to ±15 is "
                "fine for daily wear. From ±30 the watch needs regulating.",
                "**Amplitude:** 250° to 315° is healthy for a wound watch lying dial up. "
                "Below 220° a service is due soon, and below 200° the oil has probably "
                "dried. Above 315° the balance risks knocking.",
                "**Beat error:** under 0.3 ms is well in beat. From 0.8 ms an adjustment is "
                "worth it, and above 1.5 ms the watch is noticeably out of beat.",
            ],
            "Rates differ between positions, so note whether the watch was dial up, dial "
            "down or crown down. **Measure in positions** takes each one in turn.",
        ]),
        ("How do I know if my watch is magnetized?", [
            "A magnetized hairspring is the most common reason a mechanical watch suddenly "
            "gains time, often minutes a day. Timegrapher checks with the iPhone's "
            "magnetometer: tap **Check magnetism**, measure the background field, then hold "
            "the watch against the back of the iPhone. The difference is the answer.",
            "Take off any magnetic case, wallet or mount first. Every check is saved, so a "
            "check before and after demagnetizing shows whether it worked.",
        ]),
        ("What lift angle should I use?", [
            "The lift angle is a property of the movement, and Timegrapher uses it to work "
            "out the amplitude. Many Swiss movements use 52°, but plenty use other values, "
            "so look up your calibre. A wrong lift angle is the usual reason a phone app "
            "shows the wrong amplitude. The rate and beat error do not depend on it.",
        ]),
        ("How accurate is a phone timegrapher compared to a bench machine?", [
            "Timegrapher times each tick to a fraction of a millisecond and fits thousands of "
            "them against the iPhone's clock, the same principle a bench machine uses. A "
            "quiet room and firm contact give the best readings. Bluetooth headphones "
            "compress the sound, so disconnect them and let the iPhone's own microphone "
            "listen.",
            "Treat the results as a guide. For a decision about a service, a bench machine "
            "and a watchmaker's judgement come first.",
        ]),
        ("Can I check how my watch runs on the wrist over a whole day?", [
            "Yes. **Rate from photos** compares two photos of the dial taken a day apart. "
            "Each photo records the exact time it was taken, so the position of the seconds "
            "hand shows how much the watch gained or lost while you wore it.",
        ]),
        ("Does it work with quartz watches?", [
            "No. A quartz watch keeps time with a crystal and moves its hand once a second, "
            "so there is no balance wheel to listen to. Timegrapher is for automatic and "
            "hand-wound mechanical watches.",
        ]),
        ("Is Timegrapher free?", [
            "Your first watch is free for good, with every measurement. **Timegrapher Pro** "
            "is a one-time purchase that removes the limit on watches. There is no "
            "subscription, and purchases restore on any device with the same Apple Account.",
        ]),
        ("Does Timegrapher record my audio?", [
            "No. The sound is analysed live and never recorded, saved or uploaded. Your "
            "collection stays on your iPhone. The optional price check searches Chrono24 for "
            "your watch's reference, and **Identify from Photo** sends that one photo to "
            "Apple's Private Cloud Compute only when you tap it. [Privacy policy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "check-watch-accuracy",
        "title": "How to check your mechanical watch's accuracy with an iPhone",
        "description": "Step by step: measure your automatic or hand-wound watch's rate, "
                       "amplitude and beat error with your iPhone's microphone, read the "
                       "results, and check it for magnetism.",
        "lead": "A timing machine tells you how fast or slow a mechanical watch runs and how "
                "healthy its movement is. Timegrapher turns your iPhone into one, using the "
                "microphone. Here is how to get a steady reading and what the numbers mean.",
        "choose": [
            ("Rate", "Seconds gained or lost per day"),
            ("Amplitude", "How far the balance swings"),
            ("Beat error", "Tick against tock, in ms"),
        ],
        "steps": [
            ("Install Timegrapher",
             "Download [Timegrapher from the App Store](store). Your first watch is free. "
             "Allow microphone access when it asks."),
            ("Wind the watch",
             "Give a hand-wound watch a full wind, or wear an automatic for a while first. "
             "Amplitude is lower on a watch that is nearly run down."),
            ("Add the watch",
             "Tap **Add watch** and enter the brand, reference and movement. Set the **Lift "
             "angle** for your calibre, because the amplitude depends on it. **Identify from "
             "Photo** can suggest the brand and model."),
            ("Find a quiet spot",
             "A fridge hum or traffic costs accuracy. Take off Bluetooth headphones so the "
             "iPhone's own microphone listens."),
            ("Measure",
             "Tap **Measure** and rest the bottom edge of the iPhone firmly on the watch, "
             "ideally on the glass. Direct contact carries the ticks far better than air. "
             "The measurement stops by itself at 0:30."),
            ("Read the result",
             "You get the rate in seconds per day, the amplitude in degrees, the beat error in "
             "milliseconds and the beat rate, with a verdict from Excellent to Service needed "
             "and the reasons for it. The **Guide** tab explains each number."),
            ("Try other positions",
             "Rates change with position. **Measure in positions** takes the watch dial up, "
             "dial down and on its edge, and shows the spread between them."),
            ("Check for magnetism",
             "If the watch suddenly gains a lot of time, tap **Check magnetism**. It uses the "
             "iPhone's magnetometer and tells you whether the watch needs demagnetizing."),
        ],
        "tips": [
            ("Watch it over time",
             "Every reading is saved and charted, so a movement that slowly drifts shows up "
             "before it stops."),
            ("A day on the wrist",
             "**Rate from photos** compares two dial photos taken a day apart and shows how "
             "the watch ran while you wore it."),
            ("What it's worth",
             "The price check gets current Chrono24 asking prices for your exact reference "
             "and keeps the median."),
            ("Pay once",
             "The first watch is free. Timegrapher Pro adds unlimited watches for one "
             "payment, with no subscription."),
        ],
        "updated": "Written for Timegrapher 2.7, October 2026.",
        "cta_title": "Time your watch tonight",
        "cta_text": "Rate, amplitude and beat error in 30 seconds, with the iPhone you "
                    "already have. First watch free, no subscription.",
    },
}
