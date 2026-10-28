# Unfriended in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py. English page copy stays in APPS; this
# file adds the FAQ and the guide (downloading the Facebook export).
#
# Facebook's menu names come from the app's own HOW-TO (Unfriended/TutorialView
# .swift, checked against Facebook in 2026) and are written in **bold**. Facts to
# keep true: the app makes no network connections; it needs two exports a few
# weeks apart to show who left; renames are matched by the friend-since second;
# 1.2 has no purchases at all (its App Store description still mentions an
# unlock: leave pricing out of the copy beyond "free").

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "ui": {
        "summary": "What to choose",
    },
    "guide_link": "How to download your Facebook friends list",
    "faq": [
        ("How can I see who unfriended me on Facebook?", [
            "Facebook doesn't tell you, and there is no list of people who left. Your own "
            "Facebook data export lists everyone who is your friend on the day you download "
            "it. Unfriended compares two of these exports and shows who is missing.",
            [
                "Download your Friends and followers from Facebook in JSON format. [Here is "
                "how](guide).",
                "Import the ZIP file into Unfriended.",
                "A few weeks later, download a new export and import it too. Unfriended "
                "shows who unfriended you, deactivated or deleted their account.",
            ],
        ]),
        ("Why does Unfriended need two exports?", [
            "Facebook friendship is mutual, so a single list can't show who left: someone who "
            "unfriended you is simply not on it. Two exports taken a few weeks apart show the "
            "difference. Your own removals are kept apart, using Facebook's own record of "
            "them.",
        ]),
        ("Will a friend who changed their name show up as an unfriend?", [
            "No. Unfriended matches people by the exact second your friendship began, which "
            "Facebook records. A friend with a new name keeps the same friend-since second, "
            "so they show up as a rename, not as someone who left.",
        ]),
        ("Can I tell whether someone unfriended me or deleted their account?", [
            "Not from the export alone, so Unfriended lists people who dropped you together "
            "with those who deactivated or deleted their account. A quick look at their "
            "profile on Facebook settles it.",
        ]),
        ("Does Unfriended need my Facebook password?", [
            "No. There is no login screen anywhere in the app, and it never contacts "
            "Facebook. It reads only the export file that you download from Facebook "
            "yourself.",
        ]),
        ("Is Unfriended free?", [
            "Yes. Unfriended is free, with no subscription, no ads and no account. "
            "[See it on the App Store](store).",
        ]),
        ("Is my Facebook data uploaded anywhere?", [
            "No. The app makes no network connections at all. Your export is read and stored "
            "only on your iPhone, and deleting the app deletes it. [Privacy policy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "download-facebook-friends-list",
        "title": "How to download your Facebook friends list",
        "description": "Step by step: download your Facebook friends and followers as a "
                       "JSON file from Accounts Centre on iPhone, then see who unfriended "
                       "you by comparing two exports.",
        "lead": "Facebook lets you download a copy of your friends list, with the date each "
                "friendship began. It takes about a minute to ask for, and Facebook "
                "prepares the file within minutes to a few hours. Here is every tap, in the "
                "Facebook app on iPhone.",
        "choose": [
            ("Information", "Friends, and Followers"),
            ("Date range", "All time"),
            ("Format", "JSON"),
        ],
        "steps": [
            ("Open the menu",
             "In the Facebook app, go to your profile and tap the menu (☰) in the top left."),
            ("Settings & privacy",
             "Scroll to the bottom of the menu and tap **Settings & privacy**, then "
             "**Settings**."),
            ("Accounts Centre",
             "Under Your account, tap **Accounts Centre**."),
            ("Your information",
             "Tap **Your information and permissions**, then **Export your information**."),
            ("Create an export",
             "Tap **Create export**. Pick your Facebook profile, not Instagram, then choose "
             "**Export to device**."),
            ("Pick the data",
             "Under Connections, tick **Friends** and **Followers** (two separate boxes), "
             "then save."),
            ("JSON, all time",
             "Set **Date range** to **All time** and **Format** to **JSON**, then tap "
             "**Start export**."),
            ("Download and import",
             "Facebook tells you when the file is ready. Tap **Download**, save the ZIP to "
             "Files, and import it into [Unfriended](app). You have 4 days to download it."),
        ],
        "tips": [
            ("Do it twice",
             "One export shows your friends today. A second one a few weeks later shows who "
             "left in between."),
            ("JSON, not HTML",
             "Unfriended reads the JSON format. An HTML export can't be compared."),
            ("Names change",
             "Friends who renamed themselves are matched by the second your friendship "
             "began, so they don't look like unfriends."),
            ("Nothing leaves your iPhone",
             "Unfriended makes no network connections. Your export stays on the phone."),
        ],
        "updated": "Checked against the Facebook app, October 2026.",
        "cta_title": "Find out who left",
        "cta_text": "Import two Facebook exports and see who unfriended you. No login, no "
                    "network connections, free.",
    },
}
