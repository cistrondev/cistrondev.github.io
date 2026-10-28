# Atlas in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py, without a guide (Atlas isn't released
# yet; add a how-to once button names are final). English page copy stays in
# APPS; this file adds the FAQ. Facts to keep true: reads only location and date
# on the device; no network connections; 90+ days of photos within a year marks
# a country as lived in; saved pictures from Instagram, WhatsApp and similar
# apps are left out.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "faq": [
        ("Is there an app that shows every country I've visited from my photos?", [
            "Atlas finds the countries you've been to in the photos on your iPhone and fills "
            "them in on a world map. It works from the location and date saved with each "
            "photo, so there is nothing to type in. Atlas is coming soon to the App Store.",
        ]),
        ("How does Atlas know where I've been?", [
            "Most iPhone photos carry the place and time they were taken. Atlas reads those "
            "two details, works out the country, and groups photos taken close together "
            "into trips. It never looks at what is in the pictures.",
        ]),
        ("Will pictures people sent me count as visits?", [
            "No. Pictures saved from Instagram, WhatsApp and other apps are left out, so a "
            "friend's holiday photo doesn't add a country to your map. You can also hide any "
            "photo from a trip, and add, edit or remove any country yourself.",
        ]),
        ("Does it count the countries I've lived in?", [
            "Yes. A country with 90 or more days of photos within a year is marked as a "
            "place you've lived, in a deeper colour, with how long you lived there. Moving "
            "somewhere new doesn't count as time away.",
        ]),
        ("Can I share my travel map?", [
            "Yes. Atlas makes a picture of your map and flags for an Instagram post or Story, "
            "and a line of flag emoji for your bio.",
        ]),
        ("Does Atlas upload my photos?", [
            "No. Atlas makes no network connections. It reads the location and date of your "
            "photos on the phone, has no account, and deleting the app deletes everything it "
            "saved. [Privacy policy](privacy).",
        ]),
    ],
}
