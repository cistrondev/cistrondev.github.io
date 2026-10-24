# Unfollowers in English. build.py reads the dict L below.
#
# Every language file has the same keys:
#   name       the language's own name, for the language list
#   path       folder under unfollowers/ ("" for English, "es/" for Spanish)
#   og_locale  Open Graph locale
#   page       replaces entries of the app's APPS entry (tagline, intro, features,
#              privacy, why, shots ...). English has none: its copy is in APPS.
#   shots_dir  subfolder of assets/img/unfollowers/ with this language's
#              screenshots ("" uses the English ones). Goes inside `page`.
#   ui         replaces entries of UI_EN in build.py (navigation, buttons)
#   guide_link the link under the intro that leads to the guide
#   faq        [(question, [blocks])]: a string is a paragraph, a list is a
#              numbered list. [label](guide), [label](store), [label](privacy)
#              link to the guide, the App Store and the privacy policy.
#   guide      the step-by-step page on downloading the Instagram export.
#              **bold** marks Instagram's own button names, checked against
#              Instagram's help centre in that language (October 2026). Names we
#              could not check are written as plain words.
#
# Copy rules: plain sentences, one idea each. A block is always "probably".
# Never claim the app can't get an account banned, or that nothing leaves the
# iPhone: the profile check (vibe check) contacts instagram.com.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "guide_link": "How to download your Instagram data export",
    "faq": [
        ("How can I see who unfollowed me on Instagram?", [
            "Instagram doesn't show who unfollowed you. Your Instagram data export lists "
            "everyone who follows you on the day you download it. Unfollowers compares two "
            "of these exports and shows who left.",
            [
                "Download your data export from Instagram, with Followers and following in "
                "JSON format. [Here is how](guide).",
                "Import the ZIP file into Unfollowers. You see right away who doesn't follow "
                "you back.",
                "A few weeks later, download a new export and import it too. Unfollowers "
                "lists who unfollowed you since the first one, with the date each change "
                "was found.",
            ],
            "Each new export you import adds to your history.",
        ]),
        ("Is there a safe unfollow tracker without login?", [
            "Unfollowers works without a login. It never asks for your Instagram password "
            "and never signs in to your account. It reads the data export that you download "
            "from Instagram yourself.",
            "Many follower trackers ask for your Instagram password and then use your "
            "account in the background. Instagram warns that letting unauthorized apps into "
            "your account puts it at risk. With Unfollowers, your password stays with you, "
            "and the app never takes any action on your account.",
            "Your export file is read and stored on your iPhone. There is no account, no "
            "ads and no tracking.",
        ]),
        ("How do I download my Instagram data export?", [
            "In the Instagram app, open your profile and tap the menu. Then go to Accounts "
            "Center › Your information and permissions › Export your information › Create "
            "export. On some accounts, Accounts Center is called Meta Account. Choose Export "
            "to device. Pick Followers and following, the whole date range and the JSON "
            "format, then tap Start export. Instagram tells you when the file is ready, "
            "usually within minutes.",
            "[Step-by-step guide](guide).",
        ]),
        ("Can I see who blocked me on Instagram?", [
            "Instagram doesn't report blocks, so no app can know for sure. When someone "
            "blocks you, they disappear from your followers and from the accounts you follow "
            "at the same time. Unfollowers flags these accounts as probably blocked. This "
            "only works for people who followed you and whom you followed.",
            "An account that was deleted, deactivated or renamed disappears in the same "
            "way. The profile check (the vibe check) asks instagram.com whether each "
            "username still exists, and moves accounts that are gone to a separate list.",
        ]),
        ("Is Unfollowers free?", [
            "Unfollowers is free to download. The free version shows who doesn't follow you "
            "back, who you don't follow back, and your mutuals. A one-time purchase unlocks "
            "everything else, including the lists of who unfollowed you and who probably "
            "blocked you. There is no subscription. The app runs on iPhone with iOS 17 or "
            "later.",
        ]),
        ("Does anything leave my iPhone?", [
            "Your export file stays on your iPhone. The app reads and stores it there, and "
            "the developer runs no servers. The one feature that uses the internet is the "
            "profile check. It asks instagram.com whether an account still exists and sends "
            "only that username, without signing in. It runs when you tap the vibe check, "
            "and, once the app is unlocked, for up to 30 new accounts after each import. "
            "[Privacy policy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "download-instagram-data",
        "title": "How to download your Instagram data export (JSON)",
        "description": "Step by step on iPhone: export your Instagram followers and "
                       "following in JSON format, for all time, and save the ZIP file. "
                       "Then see who unfollowed you with Unfollowers.",
        "lead": "Instagram lets you download a copy of your account data. The export "
                "includes the full lists of your followers and of the accounts you follow. "
                "Unfollowers reads this file to show who unfollowed you. Here is how to get "
                "it in the Instagram app on iPhone.",
        "choose": [
            ("Information", "Followers and following"),
            ("Date range", "All time"),
            ("Format", "JSON"),
        ],
        "steps": [
            ("Open the menu",
             "In the Instagram app, tap your profile picture in the bottom right. Then tap "
             "the menu (☰) in the top right."),
            ("Accounts Center",
             "Tap **Accounts Center**. On some accounts it is called **Meta Account**."),
            ("Your information",
             "Tap **Your information and permissions**, then **Export your information**."),
            ("Create an export",
             "Tap **Create export**. Pick your Instagram profile and tap **Next**."),
            ("Export to device",
             "Choose **Export to device**. This saves the file on your iPhone."),
            ("Choose the data",
             "On the next screen, choose the information to export. Tick **Followers and "
             "following**, in the connections section. To see who you interact with most, "
             "also tick likes, comments and story interactions. You can untick the rest to "
             "keep the file small."),
            ("All time, JSON",
             "For the date range, choose all time. For the format, choose **JSON**. "
             "Unfollowers can't read the HTML format."),
            ("Start the export",
             "Tap **Start export**. Instagram prepares the file. This usually takes a few "
             "minutes."),
            ("Download the ZIP",
             "Instagram sends you a notification when the file is ready. Go back to "
             "**Export your information** and download the file. Instagram may ask for "
             "your password. You type it into Instagram itself. Save the ZIP file to the "
             "Files app."),
            ("Import it into Unfollowers",
             "Open Unfollowers, tap the import button and choose the ZIP file. You don't "
             "need to unzip it."),
        ],
        "tips": [
            ("Two exports show who left",
             "One export lists your followers on a single day. Import a new export every "
             "few weeks. Unfollowers compares them and shows who left since the last one."),
            ("The file stays available for four days",
             "Instagram keeps a finished export for four days. After that, create a new one."),
            ("“No follower lists found”",
             "Unfollowers shows this message when the export is in HTML format, or when "
             "Followers and following wasn't ticked. Create a new export in JSON with "
             "Followers and following."),
            ("It can take longer",
             "Most exports are ready within minutes. Sometimes it takes longer. Instagram "
             "tells you in the app and by email when yours is ready."),
        ],
        "updated": "Steps checked against Instagram's help center in October 2026.",
        "cta_title": "See who unfollowed you",
        "cta_text": "Unfollowers reads this file on your iPhone. It shows who unfollowed "
                    "you, who probably blocked you and who doesn't follow you back. No "
                    "login and no password.",
    },
}
