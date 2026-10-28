# Aloud in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py. English page copy stays in APPS; this
# file adds the FAQ and the guide (how to listen to articles, PDFs and EPUBs).
#
# Copy rules: plain sentences, one idea each. Button names are the app's own
# (Aloud/Localizable.xcstrings) and are written in **bold**. Never name a rival.
# Facts to keep true: the free shelf holds 3 pieces; one purchase unlocks it,
# no subscription; ten English voices and four that read thirty more languages,
# made on the device; the voice downloads once; translation needs iOS 18 and
# uses Apple's on-device translator; iCloud sync is optional plain text files.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "ui": {
        "summary": "What Aloud reads",
    },
    "guide_link": "How to listen to articles, PDFs and EPUB books on iPhone",
    "faq": [
        ("What is a good text-to-speech app for iPhone without a subscription?", [
            "Aloud reads articles, PDFs, EPUB books and any text aloud in a natural voice. "
            "It is free to download, and one in-app purchase removes the limit for good. "
            "There is no subscription and nothing renews.",
            "The voices are made on your iPhone or iPad, so what you read is never "
            "uploaded to be spoken, and Aloud keeps reading without an internet "
            "connection. There is no account, no ads and no tracking.",
        ]),
        ("How do I listen to an article on my iPhone?", [
            [
                "Open the article in Safari or any other app.",
                "Tap **Share**, then **Aloud**.",
                "Open Aloud and press play. The sentence being read is lit on the page.",
            ],
            "When you share from Safari, Aloud reads the page as Safari shows it, so "
            "articles on sites you are signed in to come through too. Links shared from "
            "the Facebook, Messenger or Instagram apps work as well. [Step-by-step "
            "guide](guide).",
        ]),
        ("Can Aloud turn an EPUB into an audiobook?", [
            "Yes. Open an EPUB file from the Files app, or tap **+** › **Import a file**. "
            "Aloud keeps the book's cover and chapters. The **Chapters** list shows how "
            "long each chapter takes to hear, and you can start from any of them. Your "
            "place is kept, so a long book plays like an audiobook.",
            "Books bought with copy protection cannot be opened by other apps, Aloud "
            "included. DRM-free EPUBs, like the ones from Project Gutenberg or Standard "
            "Ebooks, work.",
        ]),
        ("Can it read PDFs, including scanned ones?", [
            "Yes. Open a PDF from Files or share it to Aloud. Aloud reads the text in "
            "order, and for a scanned PDF it recognises the text on the device first.",
        ]),
        ("Does Aloud work offline?", [
            "Yes. Each voice downloads once, the first time you use it. After that the "
            "speech is made on your iPhone, so Aloud reads in airplane mode, on the "
            "underground or on a flight. Fetching a new article still needs the internet; "
            "anything already on your shelf does not.",
        ]),
        ("Which languages can it read?", [
            "Ten natural voices read English, and four more read over thirty other "
            "languages, including German, Spanish, French, Italian and Portuguese. The "
            "app itself is in English, German, Spanish, French, Italian and Portuguese.",
        ]),
        ("Can it translate what I'm reading?", [
            "Yes, on iOS 18 or later. Tap the translate button in the reader and choose a "
            "language under **Translate into**. Apple's translator does the work on your "
            "iPhone, so nothing is sent anywhere. The page then shows each sentence with "
            "its translation, and **Read the translation aloud** lets the voice read "
            "either language.",
        ]),
        ("How fast can it read?", [
            "From 0.5× to 3×, without the chipmunk sound. **Shorten pauses** trims the "
            "silence between sentences, so a 30-minute article fits a 15-minute walk.",
        ]),
        ("Is Aloud free?", [
            "Aloud is free to download, with every voice and feature. The free shelf holds "
            "three pieces at a time. A one-time purchase, **Unlock Aloud**, removes the "
            "limit. There is no subscription. [See it on the App Store](store).",
        ]),
        ("Can I bring my reading list from Pocket or Instapaper?", [
            "Yes. Export your saves from Pocket, Instapaper, Raindrop or your browser's "
            "bookmarks, then in Aloud open **Settings** › **Import from a file**. Every "
            "link lands on your shelf, and Aloud fetches the articles in the background.",
        ]),
        ("Does Aloud upload my documents?", [
            "No. Speech is made on your iPhone. Aloud downloads each voice once from a "
            "public host, and fetches articles you share from their own websites, as a "
            "browser would. **Sync with iCloud** is optional and keeps your shelf as plain "
            "text files in your own iCloud Drive. [Privacy policy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "listen-to-articles-and-books",
        "title": "How to listen to articles, PDFs and EPUB books on iPhone",
        "description": "Step by step: share an article from Safari, open a PDF or an "
                       "EPUB, paste any text, and have Aloud read it aloud in a natural "
                       "voice made on your iPhone, at your speed, offline.",
        "lead": "Aloud reads anything you can read: a web article, a PDF, an EPUB book or "
                "text you paste. The voice is made on your iPhone, so it works offline and "
                "nothing you read is uploaded. The steps below cover each kind of text.",
        "choose": [
            ("Articles", "Share from Safari or any app"),
            ("PDFs and EPUBs", "Open from Files"),
            ("Any text", "Paste it in"),
        ],
        "steps": [
            ("Install Aloud",
             "Download [Aloud from the App Store](store). It runs on iPhone and iPad with "
             "iOS 17 or later. The first time you press play, the voice downloads once. "
             "After that it works offline."),
            ("Share an article",
             "Open the article in Safari or another app, tap **Share**, then **Aloud**. "
             "The article goes on your shelf without menus, ads or comments. From Safari, "
             "Aloud reads the page as you see it, so articles you are signed in to work."),
            ("Open a PDF or an EPUB",
             "In Aloud, tap **+** › **Import a file** and pick the file, or share it to "
             "Aloud from the Files app. Scanned PDFs are recognised on the device. EPUB "
             "books keep their cover and chapters."),
            ("Paste any text",
             "Tap **+** › **Paste text** for notes, emails or anything you copied. "
             "**Paste a link** takes a web address."),
            ("Press play",
             "Open a piece and press play. The sentence being read is lit, and the rest "
             "stays dim. Hold the rail in the margin to move through the whole piece. In a "
             "book, tap **Chapters** in the ••• menu to start from any chapter."),
            ("Set the speed",
             "Tap the speed button and choose anything from 0.5× to 3×. Turn on **Shorten "
             "pauses** to trim the silence between sentences."),
            ("Lock your iPhone",
             "Aloud keeps reading with the screen locked. Use the lock-screen or AirPods "
             "controls, and set the **Sleep timer** if you listen in bed: the voice fades "
             "out at the end."),
            ("Translate it, if you like",
             "On iOS 18 or later, tap the translate button and pick a language under "
             "**Translate into**. Each sentence appears with its translation, and **Read "
             "the translation aloud** switches the voice to the other language."),
        ],
        "tips": [
            ("Your place is kept",
             "Every piece remembers where you stopped, so you can switch between an "
             "article and a book and come back to the same sentence."),
            ("Reader mode",
             "Tap the glasses button to hide the player and read the page yourself, with "
             "your choice of font, size and paper under **Appearance**."),
            ("Your reading list",
             "Saves from Pocket, Instapaper, Raindrop or browser bookmarks come in through "
             "**Settings** › **Import from a file**."),
            ("Free to try",
             "The free shelf holds three pieces. One purchase removes the limit, and there "
             "is no subscription."),
        ],
        "updated": "Written for Aloud 3.2, October 2026.",
        "cta_title": "Listen to your reading list",
        "cta_text": "Aloud reads articles, PDFs and EPUB books in a natural voice made on "
                    "your iPhone. It works offline. Pay once, no subscription.",
    },
}
