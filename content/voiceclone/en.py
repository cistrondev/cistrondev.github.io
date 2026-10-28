# Voice Clone in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py, without a guide (not released yet).
# English page copy stays in APPS; this file adds the FAQ. Facts to keep true:
# runs on the iPhone (iPhone 15 Pro or later, iOS 18); 10-15 second sample;
# 22 languages; one-time ~1.9 GB model download from Hugging Face; clips are
# labelled AI-generated in their file information; free, no account, no credits.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "faq": [
        ("Can I clone my voice on my iPhone without uploading it?", [
            "Yes. Voice Clone runs the voice model on the iPhone itself. Record 10 to 15 "
            "seconds of your voice, type any text, and hear it read in your voice. Your "
            "sample, your text and your clips never leave the phone. Voice Clone is coming "
            "soon to the App Store.",
        ]),
        ("Which iPhones can run it?", [
            "An iPhone 15 Pro or later, with iOS 18 or later. The voice model needs the 8 GB "
            "of memory those models have.",
        ]),
        ("Does it work offline?", [
            "Yes. The first time, the app downloads the voice model once, about 1.9 GB. After "
            "that it makes speech in airplane mode.",
        ]),
        ("Which languages can it speak?", [
            "Record once, in any language, and make clips in 22 languages in your own voice. "
            "When your text looks like another language, the app offers to switch.",
        ]),
        ("Is it free?", [
            "Yes. There is no account to make and there are no credits to buy.",
        ]),
        ("Can I clone someone else's voice?", [
            "Only with their permission. Clone your own voice, or the voice of someone who "
            "agreed to it. Every clip is labelled as AI-generated in its file information.",
        ]),
    ],
}
