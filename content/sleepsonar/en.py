# Sleep Sonar in English. build.py reads the dict L below.
#
# Same keys as content/atlas/en.py: the FAQ only (no guide yet; the app isn't released). English page copy stays in
# APPS. Facts to keep true: microphone on only during a night or a placement check; only short clips are kept
# (3 s before to 2 s after a sound, 45 s at most); the sonar is an 18-20 kHz sweep; no network connections; not a
# medical device; breathing pauses are informational.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "faq": [
        ("Can my iPhone tell me whether I snore?", [
            "Yes. Put the phone on the nightstand and start the night. Sleep Sonar listens all night and keeps a "
            "short clip of each snore, each bit of sleep talk and each cough, with the time it happened. In the "
            "morning you see how long you snored and can play the clips. Sleep Sonar is coming soon to the App Store.",
        ]),
        ("Does it work if I don't snore?", [
            "Yes. Besides listening, the phone plays a sweep between 18 and 20 kHz, too high for adults to hear, and "
            "reads its echo from your chest. That shows your breathing rate, how restless you were and an estimate "
            "of how long you slept, whether or not you make a sound.",
        ]),
        ("Does it record me all night?", [
            "No. The sound is analysed as it happens and discarded. The app keeps only short clips of the sounds it "
            "recognises, from three seconds before to two seconds after each one. Everything stays on your iPhone: "
            "there is no account and nothing is uploaded.",
        ]),
        ("Can I hear the sonar? Can my dog?", [
            "Adults can't hear it: it sits between 18 and 20 kHz. Some dogs and cats can, so if a pet reacts, turn the "
            "sonar off on the home screen. The sound detection keeps working without it.",
        ]),
        ("Where should the phone go?", [
            "On the nightstand on your side of the bed, an arm's length from your chest (30 to 70 cm), face up with "
            "the bottom edge toward you, about mattress height, plugged in, with the volume at least halfway up. "
            "The placement check tells you within 15 seconds whether it can find your breathing.",
        ]),
        ("Does it detect sleep apnea?", [
            "No. Sleep Sonar is not a medical device. It can show stretches of ten seconds or more without a breath "
            "while you lie still, for your information, but it cannot diagnose sleep apnea or anything else. If you "
            "see many pauses on most nights, or someone has noticed you stop breathing in your sleep, talk to a doctor.",
        ]),
        ("Does Sleep Sonar upload anything?", [
            "No. Sleep Sonar makes no network connections. The sonar, the sound recognition and every report run on "
            "your iPhone, and deleting the app deletes everything it saved. [Privacy policy](privacy).",
        ]),
    ],
}
