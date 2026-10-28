#!/usr/bin/env python3
"""Builds the static site from the APPS list below and content/privacy/*.md.

    python3 build.py

Writes index.html, privacy/index.html, and <slug>/index.html plus
<slug>/privacy/index.html for every app. The output is plain HTML with
relative links, so it works on GitHub Pages at a user site
(name.github.io) or a project site (name.github.io/repo) alike.
No dependencies beyond the Python standard library.
"""
import hashlib
import html
import json
import pathlib
import re
import runpy
import datetime

ROOT = pathlib.Path(__file__).resolve().parent
BRAND = "Cistron"                 # header wordmark and page titles
SITE_URL = "https://cistrondev.github.io/"   # canonical address; also used by sitemap.xml
COMPANY = "Cistron Development"   # copyright line
# Contact address. Leave empty to hide the Contact links and every policy's
# "## Contact" section; set it and rebuild to bring them back.
EMAIL = "cistron.support@icloud.com"
# Google Search Console ownership check (URL-prefix property for
# https://cistrondev.github.io/). Leave in place or verification lapses.
GOOGLE_SITE_VERIFICATION = "0HO-cftcZWuRyvlFjb1OlFsgFgWXaGyS6AsLK70I34Q"
# Proves to Toolradar (a software directory) that this site is ours, so the
# company profile can list the apps. Empty removes the tag.
TOOLRADAR_VERIFICATION = "toolradar-verify-rOrqezKzteNECKs2sFwvBf"
YEAR = 2026
SHOT_W, SHOT_H = 642, 1389  # screenshots are 1284×2778 exports at half size

# Screenshots live at assets/img/<slug>/01.webp, 02.webp, … in the order of
# `shots`; each entry is that image's alt text. `tile` picks which three
# appear on the home page.
#
# Optional: `stats` is a list of (figure, caption) pairs, and `reviews` a list
# of excerpts from real reviews — quote them word for word (trim with "…",
# never reword) and attribute by where they were posted, not by reviewer name.
# `stars` is optional: leave it out for sources without ratings, like Reddit.
#
# `dark_shots: True` means a dark-mode set exists at assets/img/<slug>/dark/
# (same numbering); the gallery then gets a Light/Dark switch.
#
# `duo` adds an "iPhone Duo" showcase under the gallery: a subtitle and up to
# three phones, each (pose, image, label, caption, alt). pose is "cover" (the
# folded cover screen, 699×1017), "book" (half open) or "flat" (open); the last
# two take a 1427×1004 inner-screen image. Images live at
# assets/img/<slug>/duo/<image>-light.webp, plus <image>-dark.webp when the app
# has `dark_shots`.
#
# Optional `why`: (heading, paragraph) on how the app differs from its
# competitors. Keep every claim true for this app and never name a rival.
#
# `live: False` is for an app that is not on the App Store yet: its pages say
# "Coming soon" where the App Store buttons and the price would be. On release
# day, remove the line and fill in `pricing`.
#
# `languages` lists the languages the app's page exists in, English first.
# Each has a file content/<slug>/<code>.py (see content/unfollowers/en.py):
# the page copy, an FAQ and a how-to guide. Every language version links to
# all the others with hreflang tags, and English is the x-default.
APPS = [
    {
        "slug": "aloud",
        "name": "Aloud",
        "store_name": "Aloud — Text to Speech Reader",
        "id": "6795773116",
        "tagline": "Anything you can read, read aloud.",
        "pricing": "Free to try · One-time unlock",
        "intro": (
            "Share an article, open a PDF, or paste any text.",
            "Aloud reads it to you in a natural voice generated on your iPhone, "
            "sentence by sentence, and always keeps your place.",
        ),
        "features": [
            ("Natural voices, on device",
             "Ten voices for English and four that read thirty more languages. No "
             "server does the talking, so Aloud keeps reading in airplane mode."),
            ("Articles, PDFs, books",
             "Share from any browser, open PDFs and EPUB books from Files, even "
             "scanned PDFs, or paste your own text."),
            ("A reader, not a player",
             "The sentence being spoken is lit. Hold the margin rail to scrub "
             "through the whole document."),
            ("Faster, if you like",
             "From 0.5× to 3× without the chipmunk voice, with pauses trimmed at "
             "every full stop if you want them."),
            ("Made for the move",
             "Keeps reading with the screen locked, with lock-screen and AirPods "
             "controls and a sleep timer that fades out."),
            ("On every device",
             "Optional iCloud sync keeps your shelf as plain text files in your "
             "own iCloud Drive."),
        ],
        "privacy_title": "Private by architecture.",
        "privacy": [
            "Speech is generated on your iPhone. Your documents are never uploaded.",
            "Voices download once from a public host. Articles you share are "
            "fetched from their own website, as a browser would.",
            "No account, no analytics, no ads, no tracking.",
        ],
        "network": (
            "Downloads each voice once from Hugging Face, and fetches articles you "
            "share from their own websites. Optional iCloud sync goes to your own "
            "iCloud. Your documents are never uploaded."
        ),
        "note": "",
        "reviews": [
            {"stars": 5, "source": "App Store review, United States",
             "quote": "I use this daily to listen to the Economist and New Yorker… "
                      "it sounds super natural and it just works"},
            {"source": "Review on Reddit",
             "quote": "Holy moly, that UI is beautiful. One of the most beautiful "
                      "apps I’ve seen!"},
        ],
        "tile": [1, 2, 6],
        "dark_shots": True,
        "platform": "iPhone and iPad · iOS 17 or later",
        "languages": ["en", "de", "es", "fr", "it", "pt-BR"],
        "category": "ProductivityApplication",   # schema.org applicationCategory
        "duo": {
            "sub": "Closed, it listens. Open, it reads.",
            "items": [
                ("cover", "cover", "Folded", "The voice keeps going on the cover screen.",
                 "Aloud on the iPhone Duo's cover screen: the voice keeps reading, with play controls."),
                ("book", "spread", "Half open", "Two facing pages, at any angle.",
                 "Aloud on the half-open iPhone Duo: two facing pages."),
                ("flat", "spread", "Open", "Translating? The original and the translation, side by side.",
                 "Aloud on the open iPhone Duo: the Spanish original on the left page, the English "
                 "translation on the right, row for row."),
            ],
        },
        "why": (
            "No cloud. No subscription.",
            "Many popular text-to-speech apps make their voices on their own "
            "servers, so the articles and documents you listen to are uploaded "
            "there first, and their premium plans can cost $139 a year, or $29 a "
            "month (nearly $350 a year). Aloud makes every voice right on your "
            "iPhone, so what you read is never sent anywhere to be spoken. And "
            "there is no subscription: one optional purchase, yours forever.",
        ),
        "shots": [
            "Anything you can read, it reads to you.",
            "Get through the reading list.",
            "Works offline. Anywhere.",
            "No subscription. No ads. No tracking.",
            "Natural voices. Every language.",
            "Reader mode: read it your way.",
            "Twice the speed. Half the time.",
            "Your shelf, on every device.",
            "Read it in your language: any piece translated on the device, sentence beside sentence.",
        ],
    },
    {
        "slug": "lifetrends",
        "name": "LifeTrends",
        "store_name": "LifeTrends: Health Insights",
        "id": "6787547184",
        "tagline": "The patterns hiding in your health data.",
        "pricing": "Free · One-time Pro unlock",
        "intro": (
            "You walk more on weekends. You sleep less on Sunday nights.",
            "LifeTrends reads the Apple Health history already on your iPhone, "
            "tells you in plain English what is actually in it, and shows the "
            "numbers behind every claim.",
        ),
        "features": [
            ("Findings, not guesses",
             "A pattern only appears when it is large enough to matter and "
             "unlikely to be chance. Thin evidence shows nothing."),
            ("Weekdays, seasons, body clock",
             "Weekday against weekend, month by month across your whole history, "
             "and your daily rhythm hour by hour."),
            ("Trips and places",
             "Worked out from photo dates and locations only, never the pictures, "
             "matched against cities built into the app."),
            ("Every number, charted",
             "Each metric over your entire history, plus the correlations between "
             "them that hold up."),
            ("The whole story",
             "Tap any finding for the gap, the sample sizes, and whether it still "
             "holds this year."),
            ("No score, no streaks",
             "No readiness number, no coaching voice, no advice you did not ask "
             "for."),
        ],
        "privacy_title": "Your health data never leaves your iPhone.",
        "privacy": [
            "Health data is read, analyzed, and kept on your iPhone. Never uploaded.",
            "From Photos it reads only dates and locations, never the images.",
            "No account, no analytics, no ads, no tracking.",
        ],
        "network": (
            "Nothing, unless you tap Current Location and are outside its built-in "
            "city list. Then one approximate position goes to Apple to name the "
            "city. Health data never leaves."
        ),
        "note": "LifeTrends is not a medical device and does not give medical advice.",
        "tile": [1, 2, 4],
        "languages": ["en"],
        "category": "HealthApplication",   # schema.org applicationCategory
        "shots": [
            "Your life has patterns, hiding in your health data.",
            "It knows where you were: the cities you move more in.",
            "It reads your body clock: jet lag, measured in your own sleep.",
            "Seasons leave marks: trends across your whole history.",
            "Tap in for the whole story: the gap, the sample size, and whether it holds.",
            "Every number, over time: each metric you track, charted.",
            "It connects the dots: correlations, only when significant.",
            "See how it thinks: statistics decide what you are shown.",
            "Your best days, on record, tagged with the city you were in.",
        ],
    },
    {
        "slug": "timegrapher",
        "name": "Timegrapher",
        "store_name": "Timegrapher — Watch Accuracy",
        "id": "6788081843",
        "tagline": "A watchmaker's timing machine, in your iPhone.",
        "pricing": "First watch free · One-time Pro unlock",
        "intro": (
            "Rate, amplitude, and beat error in about thirty seconds.",
            "Timegrapher listens to your mechanical watch through the iPhone's "
            "microphone, then keeps your whole collection, every reading, and what "
            "each watch is worth, in one place.",
        ),
        "features": [
            ("The numbers that matter",
             "Seconds gained or lost per day, how far the balance swings, and "
             "tick–tock symmetry. Beat rate detected from 18,000 to 36,000 bph."),
            ("Readings that hold steady",
             "It tracks the room's noise floor and rejects stray sounds. Amplitude "
             "comes from your calibre's own lift angle."),
            ("Your collection",
             "Every watch with its photo, reference, movement, and lift angle. "
             "Every reading is saved and charted. Identify from Photo suggests "
             "the brand and model."),
            ("Accuracy over a day of wear",
             "Take two photos of the watch a day apart. Timegrapher compares them "
             "with your iPhone's clock and shows how the watch ran on your wrist."),
            ("Know what it's worth",
             "Current Chrono24 asking prices for your exact reference, with the "
             "median worked out on your iPhone."),
            ("Magnetism check",
             "A magnetized hairspring is the most common reason a watch suddenly "
             "gains time. Sweep the watch across the back of your iPhone and its "
             "magnetometer tells you whether it needs demagnetizing."),
        ],
        "privacy_title": "Nothing recorded. Nothing kept.",
        "privacy": [
            "Microphone audio is analyzed live and is never recorded or saved.",
            "Your collection and measurements are stored only on your iPhone.",
            "The optional price check searches Chrono24 for your watch's "
            "reference.",
            "Identify from Photo sends the photo to Apple's Private Cloud "
            "Compute only when you tap it. Apple doesn't keep it, and the "
            "developer never sees it.",
            "The Clock tab gets the time from Apple's time server. The "
            "request carries no personal data.",
        ],
        "network": (
            "Only when you use a feature that needs it. The Clock tab asks "
            "time.apple.com for the time. The price check searches only your "
            "watch's brand and reference on Chrono24. Identify from Photo sends "
            "that one photo to Apple's Private Cloud Compute. Audio is never "
            "recorded."
        ),
        "note": "",
        "reviews": [
            {"source": "Review on Reddit",
             "quote": "Timegrapher is extremely reliable. I get an accurate measure of "
                      "the rate of my watches in no time! It also let’s me track the "
                      "price of my collection over the years"},
        ],
        "tile": [1, 3, 4],
        "languages": ["en", "de", "fr", "ja"],
        "category": "UtilitiesApplication",   # schema.org applicationCategory
        "shots": [
            "Your iPhone is a timing machine: rate, amplitude, and beat error in 30 seconds.",
            "Accurate readings, no matter what: quiet movements, even in noisy rooms.",
            "Your entire collection at a glance: age, health, and value.",
            "See the drift before it matters, and know when to service your watch.",
            "Know what it's worth: the Chrono24 median for your exact reference.",
            "Is your watch magnetized? Checked in ten seconds.",
            "Accuracy over a day of wear: two photos, a day apart, show how it ran on your wrist.",
        ],
    },
    {
        "slug": "unfollowers",
        "name": "Unfollowers",
        "store_name": "Unfollowers Tracker: No Login",
        "id": "6787521130",
        "tagline": "See who unfollowed you on Instagram. No login.",
        "pricing": "Free · One-time unlock",
        "intro": (
            "Instagram will never tell you who unfollowed you. Your own data export will.",
            "Unfollowers reads the official export you download from Instagram "
            "yourself and shows what changed, without ever asking for your "
            "password.",
        ),
        "features": [
            ("Who unfollowed you",
             "Tracked across imports, with the date each change was caught."),
            ("Probably blocked",
             "Accounts that left your followers and your following at the same "
             "moment, flagged as a likely block, never stated as fact."),
            ("Who doesn't follow back",
             "The classic list, plus mutuals and requests that were never "
             "accepted."),
            ("Who you interact with most",
             "Your likes, comments, and story reactions, counted from your own "
             "export."),
            ("Your history, charted",
             "Growth and follow-back trends built from every export you import."),
            ("No login, ever",
             "There is no sign-in screen anywhere in the app. Your password stays "
             "yours."),
        ],
        "privacy_title": "Your export never leaves your iPhone.",
        "privacy": [
            "Your Instagram export is read and stored only on your iPhone.",
            "No account, no analytics, no ads, no tracking.",
            "Checking whether an account still exists sends only that username to "
            "Instagram, anonymously.",
        ],
        "network": (
            "Only the usernames being checked, sent anonymously to Instagram when a "
            "profile check runs. Your export stays on your iPhone."
        ),
        "note": "Unfollowers is an independent app, not affiliated with Instagram or Meta.",
        "stats": [
            ("Tens of thousands", "of downloads"),
            ("#48", "in Social Networking on the App Store in Greece"),
        ],
        "reviews": [
            {"stars": 5, "source": "App Store review, United States",
             "quote": "This is what I call good UX and solving a problem that a "
                      "corporation doesn’t provide in a non-intrusive way."},
            {"stars": 5, "source": "App Store review, United States",
             "quote": "The best follower tracker out there. The only one that plots "
                      "your number of followers over the years"},
            {"stars": 5, "source": "App Store review, Greece",
             "quote": "Using this app I realised my fiancées mom unfollowed me!! "
                      "Love that no ads are involved!"},
        ],
        "tile": [1, 4, 5],
        "languages": ["en", "pt-BR", "es", "it", "fr", "de", "el", "nl"],
        "category": "SocialNetworkingApplication",   # schema.org applicationCategory
        "why": (
            "Your password stays yours.",
            "Most follower trackers ask for your Instagram password, then access "
            "your account in the background. Instagram warns that letting "
            "unauthorized apps into your account puts it at risk, and people who "
            "use them regularly report locked, suspended, or “action blocked” "
            "accounts. Unfollowers never asks for your password and never signs "
            "in as you: it reads the data export Instagram itself gives you. And "
            "there is no subscription: one optional purchase unlocks everything.",
        ),
        "shots": [
            "See every unfollower: who left, and when, read from your own Instagram export.",
            "Probably blocked you: accounts that left your followers and following at the same time.",
            "They don't follow back: search, sort, and tap through to any profile.",
            "Who you hype the most: your likes, comments, and story reactions, counted.",
            "Your stats, charted: growth and follow-back charts from your own history.",
        ],
    },
    {
        "slug": "unfriended",
        "name": "Unfriended",
        "store_name": "Unfriended: Who Deleted Me?",
        "id": "6792587859",
        "tagline": "Find out who unfriended you on Facebook.",
        "pricing": "Free",
        "intro": (
            "Facebook friendship is mutual, so no single snapshot can show who left.",
            "Unfriended compares two of your own Facebook data exports, a few "
            "weeks apart, and shows exactly what changed. All on your iPhone, "
            "with zero network requests.",
        ),
        "features": [
            ("Who dropped you",
             "Friends who unfriended you, deactivated, or deleted their account."),
            ("Renames, not false alarms",
             "Name changes are matched by the exact second a friendship began, so "
             "a new name never looks like an unfriend."),
            ("Your own removals",
             "Kept apart using Facebook's own record, with real dates."),
            ("Requests and followers",
             "Requests left unanswered, rejections, followers, and following."),
            ("Your friendship history",
             "Friends over time, your most social year, and your oldest friends, "
             "ranked."),
            ("A one-minute how-to",
             "The app shows every tap it takes to download your export from "
             "Facebook."),
        ],
        "privacy_title": "Zero network requests. Really.",
        "privacy": [
            "The app makes no network connections at all.",
            "Your Facebook export is read and stored only on your iPhone.",
            "No login, no account, no analytics, no ads.",
        ],
        "network": "Nothing. The app makes no network connections at all.",
        "note": "Unfriended is an independent app, not affiliated with Facebook or Meta.",
        "tile": [2, 4, 5],
        "languages": ["en"],
        "category": "SocialNetworkingApplication",   # schema.org applicationCategory
        "shots": [
            "Who dropped you? Import your Facebook export twice and the difference shows who left.",
            "They dropped you. Facebook won't say.",
            "New name, who dis? Renames matched by the exact friend-since second.",
            "Your friend eras, charted.",
            "Day-one besties: your oldest friends, ranked.",
            "Left on read: pending requests, rejections, followers, and following.",
            "No login. No leaks. Your export goes in; nothing goes out.",
        ],
    },
    {
        "slug": "pedometer",
        "name": "Pedometer",
        "store_name": "Pedometer: Step Counter Widget",
        "id": "6822166433",
        "tagline": "Your steps, on your Lock Screen.",
        "pricing": "Free",
        "intro": (
            "Steps, distance, and flights climbed, as plain numbers and charts.",
            "Pedometer reads Apple Health and puts today's count on your Lock "
            "Screen and Home Screen. Your iPhone counts steps on its own, and "
            "Apple Watch steps are included if you wear one.",
        ),
        "features": [
            ("Today",
             "Your steps against your goal, with what is left to go. Distance "
             "and flights climbed against their goals, with active energy and "
             "walking speed beside them."),
            ("Walks and runs",
             "Record a walk or run with GPS: your route on a map, with speed or "
             "pace, elevation, climb, and calories. Each one is saved to Apple "
             "Health with its route."),
            ("Live heart rate",
             "With AirPods Pro 3, Powerbeats Pro 2, or a Bluetooth heart rate "
             "strap, your heart rate shows live during a walk or run (iOS 26)."),
            ("On the Lock Screen",
             "While you walk, the time, distance, speed, heart rate, and "
             "calories stay on the Lock Screen, with a pause button."),
            ("Share a walk",
             "A picture of each walk or run, with the map and your numbers, for "
             "any app you like."),
            ("Your own goals",
             "Set a daily goal for steps, distance, and flights climbed. They "
             "start at 10,000 steps, 8 km or 5 miles, and 10 flights."),
            ("History",
             "One chart per number, for the last week, month, or year, with the "
             "daily average and the change from the period before."),
            ("Lock Screen widgets",
             "Steps and distance, each inside a ring that closes at your goal, "
             "and flights climbed, with a figure that climbs a staircase to "
             "your goal."),
            ("Home Screen widget",
             "The same card as the app, small, medium, or large. Set it to light, "
             "dark, or automatic, and show the steps alone if you like."),
            ("By hour",
             "Today's steps hour by hour, beside your usual day over the last "
             "four weeks."),
            ("Records",
             "Totals of steps, distance, and flights for every month and year, "
             "and your best day, week, and month for steps, flights climbed, "
             "and walking speed."),
            ("Your color",
             "Choose graphite, blue, green, orange, pink, or purple for the goal "
             "bars, the charts, and the Home Screen widget."),
        ],
        "privacy_title": "Nothing leaves your iPhone.",
        "privacy": [
            "Reads Apple Health, and writes to it only the walks and runs you record.",
            "Your location is used only while you record, and stays on your iPhone.",
            "Everything is counted and stored on your iPhone. Nothing is uploaded.",
            "No account, no analytics, no tracking.",
        ],
        "network": "Only the map, which Apple Maps draws. Nothing about you is sent.",
        "note": "Pedometer is not a medical device and does not give medical advice.",
        "tile": [1, 2, 3],
        "languages": ["en", "de", "es", "fr", "it", "nl", "pt-BR", "ja"],
        "category": "HealthApplication",   # schema.org applicationCategory
        "shots": [
            "Your steps on the Lock Screen: a step counter widget, with distance and stairs beside it.",
            "Every step, counted: reads Apple Health, Apple Watch steps included.",
            "Walks and runs, on a map: speed, elevation, calories, and heart rate.",
            "Watch it live, share it after: the Lock Screen while you go, a picture after.",
            "On your Home Screen, too: the same card, small or medium.",
            "Your day, hour by hour: today's steps beside a usual day.",
            "Your best day, week, and month: totals for every month and year, and all time.",
            "Choose your color: six colors for the goal bars, the charts, and the widget.",
            "Your week, at a glance: daily bars, the average, and the change.",
            "Nothing leaves your iPhone: no account, no tracking.",
        ],
    },
    {
        "slug": "voiceclone",
        "name": "Voice Clone",
        "store_name": "Voice Clone: Private & Offline",
        "id": "",
        "live": False,
        # The voice model needs 8 GB of memory, so newer iPhones only.
        "platform": "iPhone 15 Pro or later · iOS 18 or later",
        "tagline": "Text to speech in your own voice.",
        "pricing": "Free",
        "intro": (
            "Record a short sample of your voice, type any text, and hear it "
            "read in your voice.",
            "The voice model runs on your iPhone, so your recordings and clips "
            "stay with you. There is no account and nothing to buy.",
        ),
        "features": [
            ("Your voice in 15 seconds",
             "Talk for 10 to 15 seconds in your normal voice. The app learns "
             "your voice from that one sample, on your iPhone."),
            ("Type anything",
             "Type what it should say and tap Generate. A long text starts "
             "playing as soon as its first sentence is ready."),
            ("22 languages",
             "Record once, in any language, then make clips in 22 languages. "
             "When your text looks like another language, the app offers to "
             "switch."),
            ("Works offline",
             "The first time, the app downloads the voice model, about 1.9 GB. "
             "After that it works in airplane mode."),
            ("Your clips",
             "Every clip is saved with its text and language. Play it, share "
             "it, save it to Files, or delete it."),
            ("No account, no credits",
             "There is nothing to sign up for and no credits to buy."),
        ],
        "privacy_title": "Nothing leaves your iPhone.",
        "privacy": [
            "Your voice sample, your text, and your clips stay on your iPhone.",
            "The voice model runs on the phone. Nothing is uploaded.",
            "Each clip is labelled as AI-generated in its file information.",
            "No account, no analytics, no tracking.",
        ],
        "network": "Only the one-time download of the voice model from Hugging "
                   "Face. Nothing about you is sent.",
        "note": "Needs an iPhone 15 Pro or later, for its 8 GB of memory. Clone "
                "only your own voice, or the voice of someone who agreed to it.",
        "tile": [1, 3, 5],
        "languages": ["en"],
        "category": "MultimediaApplication",   # schema.org applicationCategory
        "shots": [
            "Clone your voice on your iPhone: the voice model runs on the phone.",
            "Record 15 seconds of your voice: say anything, in your normal voice.",
            "Type anything, hear it in your voice: long texts start after the first sentence.",
            "Works in airplane mode: after a one-time download, no internet needed.",
            "Speak 22 languages in your own voice: record once, in any language.",
            "No account, no credits: save clips to Files or share them.",
        ],
    },
    {
        "slug": "atlas",
        "name": "Atlas",
        "store_name": "Atlas: Travel Map From Photos",
        "id": "",
        "live": False,
        "tagline": "Every country you've been to, from your photos.",
        "pricing": "Free",
        "intro": (
            "Atlas finds the countries you've been to in the photos on your "
            "iPhone and puts them on a world map.",
            "It reads only the location and date saved with each photo, on the "
            "phone. There is no account, and nothing is uploaded.",
        ),
        "features": [
            ("Your map, filled in",
             "Every country in your photos, on a world map you can zoom into or "
             "on a turning globe. Tap any country to see how many times you've "
             "been, or to add one that isn't in your photos."),
            ("Every trip",
             "Each visit to a country, with its dates. Tap a trip to see its "
             "photos and hide any that aren't from it. Merge trips that were "
             "really one."),
            ("Lived here",
             "Countries with 90 or more days of photos within a year are marked "
             "as places you've lived, in a deeper colour, with how long you lived "
             "there. Moving somewhere new doesn't count as time away."),
            ("Stats",
             "Trips and days away, countries per year (tap a year to see where "
             "you went), your busiest years, the countries you go back to most, "
             "and your longest trips."),
            ("Share your map",
             "A picture of your map and flags for an Instagram post or Story, "
             "or all your flags as emoji for your bio."),
            ("Fewer false visits",
             "Pictures saved from Instagram, WhatsApp and other apps are left "
             "out. You can add, edit or remove any country yourself."),
        ],
        "duo": {
            "sub": "Unfold it for a globe of your travels.",
            "items": [
                ("cover", "cover", "Folded",
                 "Your count, the map and your countries on the cover screen.",
                 "Atlas on the iPhone Duo's cover screen: 34 countries, a world map with "
                 "them filled in, and the list of countries."),
                ("book", "map", "Half open",
                 "The whole world map, across both halves.",
                 "Atlas on the half-open iPhone Duo: a world map with the visited countries "
                 "filled in."),
                ("flat", "globe", "Open",
                 "A globe of your countries that turns slowly. Tap one to see your visits.",
                 "Atlas on the open iPhone Duo: a globe with the visited countries filled in, "
                 "and Italy tapped, showing 9 visits."),
            ],
        },
        "privacy_title": "Your photos stay on your iPhone.",
        "privacy": [
            "Atlas reads the location and date of your photos on the phone.",
            "There is no account, and nothing is uploaded.",
            "No analytics, no ads, no tracking.",
            "Deleting the app deletes everything it saved.",
        ],
        "network": "Nothing. Atlas makes no network connections. A photo kept "
                   "only in iCloud is downloaded by Photos when you open it, as "
                   "in the Photos app.",
        "note": "",
        "tile": [1, 3, 5],
        "languages": ["en"],
        "category": "TravelApplication",   # schema.org applicationCategory
        "shots": [
            "Every country you've been to, on one map: the count, the map and your list.",
            "Found in your photos, on your iPhone: nothing is uploaded.",
            "Tap any country to see your visits: zoom in anywhere on the map, or switch to the globe.",
            "Every trip, with its photos: each visit's dates and pictures.",
            "Your travels, year by year: trips, days away and your busiest years.",
            "Share your map as a Story: a post and a line of flags too.",
        ],
    },
    {
        "slug": "jobsitecalc",
        "name": "Jobsite Calc",
        "store_name": "Jobsite Calc: Feet Inch Math",
        "id": "",
        "live": False,
        "platform": "iPhone and iPad · iOS 17 or later",
        "category": "UtilitiesApplication",
        "tagline": "Feet, inches and fractions. Pay once.",
        "pricing": "Free · One-time unlock",
        "intro": (
            "A feet-inch-fraction calculator for framers, carpenters and "
            "contractors.",
            "Type a measurement the way you read it on the tape, see the whole "
            "calculation on screen, and lay out stairs, rafters and concrete from "
            "it. One purchase unlocks every tool, forever. No subscription, no "
            "account, no internet.",
        ),
        "features": [
            ("Feet, inches and fractions",
             "Enter 12' 3-1/2\" with the Feet, Inch and / keys. Add, subtract, "
             "multiply and divide, and get the answer to the nearest 1/16, or to "
             "any fraction you choose. The whole expression stays on screen, with "
             "parentheses."),
            ("Convert with one tap",
             "Tap the unit on the result to cycle feet-inches, inches, decimal "
             "feet, yards, metres, centimetres and millimetres. Areas, volumes and "
             "angles convert too."),
            ("Stairs with the code check",
             "Enter the total rise and get the risers, treads, stringer length, "
             "angle and stairwell opening, drawn as a stringer. A green or red "
             "check against the 7-3/4 inch riser, 10 inch tread and 6' 8\" "
             "headroom limits, which you can change."),
            ("Rafters and roofs",
             "Common, hip, valley and jack rafters from a pitch and a run, with "
             "the plumb and level cuts and the jack list. Irregular hips. Roof "
             "squares, bundles and sheets."),
            ("Concrete and materials",
             "Slabs, footings, columns and piers in cubic yards and bags. Drywall "
             "and sheathing sheets, block, brick, studs and plates, board feet "
             "and lumber cost."),
            ("Angles and a tape",
             "Crown and compound miters, polygons, circles and arcs. Every result "
             "goes on a tape you can reuse, copy or share."),
        ],
        "privacy_title": "Nothing leaves your phone.",
        "privacy": [
            "The app has no network code. Nothing is uploaded.",
            "No account, no analytics, no tracking, no ads.",
            "Your settings and your tape stay on your iPhone.",
            "The one purchase goes through Apple, and the price never renews.",
        ],
        "network": "No network connections at all. The one purchase goes through "
                   "the App Store.",
        "note": "Dark screen, big keys and key clicks, for gloves and sunlight. "
                "Works with no signal.",
        "tile": [1, 2, 3],
        "shots": [
            "Feet, inches and fractions, with the whole calculation on screen.",
            "Stairs from the total rise: risers, treads, stringer and the code check.",
            "Rafters from a pitch and a run, with the plumb and level cuts.",
            "Concrete slabs, footings and piers in cubic yards and bags.",
            "Big keys on a dark screen, built for gloves.",
            "Every result on a tape, to reuse, copy or share.",
        ],
        "languages": ["en", "es"],
    },
]

PRINCIPLES = [
    ("Minimal",
     "One job, done well. No feeds, no clutter, nothing fighting for your attention.",
     '<circle cx="14" cy="14" r="10"/><circle cx="14" cy="14" r="2.6" fill="currentColor" stroke="none"/>'),
    ("Local",
     "Your data is processed right on your iPhone. We run no servers, so we never see it.",
     '<rect x="8" y="3" width="12" height="22" rx="3"/><path d="M12.5 6h3"/>'),
    ("Safe",
     "No accounts, no sign-in, no passwords. There is nothing of yours to leak.",
     '<rect x="6" y="12.5" width="16" height="11.5" rx="2.5"/><path d="M9.5 12.5V9a4.5 4.5 0 0 1 9 0v3.5"/>'),
    ("Ad-free",
     "No ads, no analytics, and no tracking. Nothing is watching what you do.",
     '<circle cx="14" cy="14" r="10"/><path d="M7 21 21 7"/>'),
    ("Subscription-free",
     "No subscriptions, and no free trials that quietly turn into charges.",
     '<path d="M4.5 14.2 14.2 4.5H23.5v9.3L13.8 23.5z"/><circle cx="18.6" cy="9.4" r="1.7"/>'),
]

# The site's own words: navigation, footer, buttons. A language file's `ui`
# replaces any of these on that language's pages. On a 375-pixel phone the
# header links must stay within about 178px of text and the app bar's two
# links within about 112px, so long languages use short words there.
UI_EN = {
    "nav_apps": "Apps",
    "nav_privacy": "Privacy",
    "nav_about": "About",
    "nav_contact": "Contact",
    "trademark": "Instagram and Facebook are trademarks of Meta Platforms, Inc. Unfollowers "
                 "and Unfriended are independent apps and are not affiliated with, endorsed "
                 "by, or sponsored by Meta.",
    "rights": "All rights reserved.",
    "overview": "Overview",
    "privacy": "Privacy",
    "app_store": "App Store",
    "view_on_store": "View on the App Store",
    "coming_soon": "Coming soon to the App Store",
    "soon": "Coming soon",
    "platform": "iPhone · iOS 17 or later",
    "screenshots": "Screenshots",
    "prev": "Previous screenshots",
    "next": "Next screenshots",
    "privacy_eyebrow": "Privacy",
    "read_policy": "Read the privacy policy",
    "what_people_say": "What people say.",
    "more_apps": "More apps",
    "languages": "Languages",
    "faq": "Questions and answers",
    "summary": "What to choose",
    "tips": "Good to know",
    "cta_more": "About {name}",
    "appearance": "Screenshot appearance",
    "light": "Light",
    "dark": "Dark",
}

# ---------------------------------------------------------------- helpers

esc = html.escape


def versioned(path):
    """<path>?v=<content hash>, so browsers refetch a file after every change
    (GitHub Pages lets them reuse any file for 10 minutes otherwise)."""
    digest = hashlib.sha1((ROOT / path).read_bytes()).hexdigest()[:8]
    return f"{path}?v={digest}"


def asset(name):
    return versioned(f"assets/{name}")


def store_url(app):
    return f"https://apps.apple.com/app/id{app['id']}"


def is_live(app):
    """False for an app that is not on the App Store yet (`live: False`)."""
    return app.get("live", True)


def shot_path(app, n, dark=False):
    """A language with its own screenshots keeps them in a subfolder
    (`shots_dir`), e.g. assets/img/unfollowers/es/01.webp."""
    folder = app["slug"] + (f"/{app['shots_dir']}" if app.get("shots_dir") else "")
    return f"assets/img/{folder}/{'dark/' if dark else ''}{n:02d}.webp"


def shot(app, n, dark=False):
    return versioned(shot_path(app, n, dark))


def icon(app):
    return versioned(f"assets/img/{app['slug']}/icon.png")


def inline_md(text):
    text = esc(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(https?://[^\s)<]+)", r'<a href="\1">\1</a>', text)
    text = re.sub(r"(?<![\w/])([\w.+-]+@[\w-]+(?:\.[\w-]+)+)", r'<a href="mailto:\1">\1</a>', text)
    return text


LIST_ITEM = re.compile(r"^(- |\d+\. )")


def md_to_html(source):
    """Converts the small Markdown subset the privacy policies use.

    Returns (title, date, body_html). Handles # / ## headings, paragraphs,
    - and 1. lists with indented continuation lines, **bold**, bare URLs and
    email addresses.
    """
    title, date, out = "", "", []
    for block in re.split(r"\n\s*\n", source.strip()):
        lines = block.splitlines()
        first = lines[0]
        if first.startswith("# "):
            title = first[2:].strip()
        elif first.startswith("## "):
            out.append(f"<h2>{inline_md(first[3:].strip())}</h2>")
        elif re.fullmatch(r"\*\*(Effective date|Last updated): .+\*\*", first.strip()):
            date = first.strip().strip("*")
        elif LIST_ITEM.match(first):
            tag = "ol" if first[0].isdigit() else "ul"
            items = []
            for line in lines:
                if LIST_ITEM.match(line):
                    items.append(LIST_ITEM.sub("", line).strip())
                else:
                    items[-1] += " " + line.strip()
            lis = "".join(f"<li>{inline_md(i)}</li>" for i in items)
            out.append(f"<{tag}>{lis}</{tag}>")
        else:
            out.append(f"<p>{inline_md(' '.join(l.strip() for l in lines))}</p>")
    return title, date, "\n".join(out)


# ---------------------------------------------------------------- languages

def load_languages(app):
    """The app's language files, in the order of its `languages` list. Each
    file defines a dict L; this adds its `code`. The English page copy stays
    in APPS, so en.py adds only the FAQ and the guide."""
    langs = []
    for code in app.get("languages", []):
        L = runpy.run_path(str(ROOT / "content" / app["slug"] / f"{code}.py"))["L"]
        langs.append({**L, "code": code})
    return langs


def lang_dir(app, L):
    """Folder of an app's page in one language: unfollowers/ or unfollowers/es/."""
    return f"{app['slug']}/{L['path']}"


def guide_dir(app, L):
    return f"{lang_dir(app, L)}{L['guide']['slug']}/"


def up(folder):
    """Relative prefix from a page in `folder` back to the site root."""
    return "../" * folder.count("/")


def alternates(langs, url_of):
    """[(hreflang, URL)] for every language version, English first. A language
    file's `also` adds codes served by the same page (pt-BR also answers "pt")."""
    out = []
    for x in langs:
        out.append((x["code"], url_of(x)))
        out += [(code, url_of(x)) for code in x.get("also", [])]
    return out


def hreflang_links(cluster):
    """<link rel="alternate"> for every language version of a page, plus
    x-default (the English one, listed first). `cluster`: [(code, URL)]."""
    links = [f'  <link rel="alternate" hreflang="{code}" href="{url}">' for code, url in cluster]
    links.append(f'  <link rel="alternate" hreflang="x-default" href="{cluster[0][1]}">')
    return "\n".join(links)


def json_ld(data):
    """A schema.org block for search engines and chat assistants."""
    text = json.dumps({"@context": "https://schema.org", **data}, ensure_ascii=False, indent=1)
    text = text.replace("</", "<\\/")   # a string can't close the <script>
    return f'  <script type="application/ld+json">\n{text}\n  </script>'


LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def rich(text, links):
    """Language-file text to HTML: **bold**, and [label](key) links, where
    key is an entry of `links` (guide, store, privacy) or a URL."""
    text = esc(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return LINK.sub(lambda m: f'<a href="{esc(links.get(m.group(2), m.group(2)))}">{m.group(1)}</a>', text)


def plain(text):
    """The same text without markup, for structured data."""
    return LINK.sub(r"\1", text.replace("**", ""))


def blocks_html(blocks, links, sep="\n"):
    """An FAQ answer: each string is a paragraph, each list a numbered list."""
    out = []
    for b in blocks:
        if isinstance(b, str):
            out.append(f"<p>{rich(b, links)}</p>")
        else:
            out.append("<ol>" + "".join(f"<li>{rich(i, links)}</li>" for i in b) + "</ol>")
    return sep.join(out)


def language_nav(langs, current, p, folder_of):
    """Links to the same page in every language; `folder_of(L)` gives its folder."""
    ui = {**UI_EN, **current.get("ui", {})}

    def item(L):
        here = ' aria-current="page"' if L is current else ""
        return (f'        <li><a href="{p}{folder_of(L)}" hreflang="{L["code"]}" '
                f'lang="{L["code"]}"{here}>{esc(L["name"])}</a></li>')

    items = "\n".join(item(L) for L in langs)
    return f"""    <nav class="langs" aria-label="{esc(ui['languages'])}">
      <h2>{esc(ui['languages'])}</h2>
      <ul>
{items}
      </ul>
    </nav>
"""


def faq_section(L, links, ui):
    items = "\n".join(f"""        <div class="faq-item">
          <h3>{esc(q)}</h3>
          <div class="faq-answer">
            {blocks_html(a, links, chr(10) + "            ")}
          </div>
        </div>""" for q, a in L["faq"])
    return f"""    <section class="faq" id="faq">
      <h2>{esc(ui['faq'])}</h2>
      <div class="faq-list">
{items}
      </div>
    </section>

"""


# ---------------------------------------------------------------- chrome

def page(*, prefix, title, description, body, local_nav="", app_id=None, scripts=False,
         lang="en", ui=UI_EN, head=""):
    """`lang` and `ui` translate the page's frame; `head` adds tags to <head>
    (hreflang links, structured data)."""
    home = prefix or "./"
    google = (f'\n  <meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">'
              if GOOGLE_SITE_VERIFICATION else "")
    if TOOLRADAR_VERIFICATION:
        google += f'\n  <meta name="toolradar-verify" content="{TOOLRADAR_VERIFICATION}">'
    nav_contact = f'        <li><a href="mailto:{EMAIL}">{esc(ui["nav_contact"])}</a></li>\n' if EMAIL else ""
    footer_contact = f'          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>\n' if EMAIL else ""
    banner = f'\n  <meta name="apple-itunes-app" content="app-id={app_id}">' if app_id else ""
    script = f'\n  <script src="{prefix}{asset("site.js")}" defer></script>' if scripts else ""
    head = f"\n{head}" if head else ""
    # An empty nav_about leaves the link out, where longer words need the room on phones.
    about = f'        <li><a href="{home}#about">{esc(ui["nav_about"])}</a></li>\n' if ui["nav_about"] else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="#ffffff">{google}
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}{asset('favicon-32.png')}">
  <link rel="icon" type="image/png" sizes="16x16" href="{prefix}{asset('favicon-16.png')}">
  <link rel="icon" type="image/png" sizes="48x48" href="{prefix}{asset('favicon-48.png')}">
  <link rel="apple-touch-icon" href="{prefix}{asset('apple-touch-icon.png')}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">{banner}
  <link rel="stylesheet" href="{prefix}{asset('site.css')}">{script}{head}
</head>
<body>
  <header class="globalnav">
    <nav class="globalnav-inner" aria-label="Site">
      <a class="wordmark" href="{home}">{BRAND}</a>
      <ul>
        <li><a href="{home}#apps">{esc(ui["nav_apps"])}</a></li>
        <li><a href="{prefix}privacy/">{esc(ui["nav_privacy"])}</a></li>
{about}{nav_contact}      </ul>
    </nav>
  </header>
{local_nav}
  <main>
{body}
  </main>
  <footer class="footer">
    <div class="footer-inner">
      <p>{esc(ui["trademark"])}</p>
      <div class="footer-row">
        <p>Copyright © {YEAR} {COMPANY}. {esc(ui["rights"])}</p>
        <ul>
          <li><a href="{home}#apps">{esc(ui["nav_apps"])}</a></li>
          <li><a href="{prefix}privacy/">{esc(ui["nav_privacy"])}</a></li>
{footer_contact}        </ul>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def local_nav(app, prefix, current, ui=UI_EN, home=None):
    """`home` is the folder of the app page this nav leads back to (the
    page in the reader's language); the privacy policy is English only."""
    here = ' aria-current="page"'
    home = home or f"{app['slug']}/"
    store = (f'\n        <li><a class="pill pill-small" href="{store_url(app)}">{esc(ui["app_store"])}</a></li>'
             if is_live(app) else "")
    return f"""  <nav class="localnav" aria-label="{esc(app['name'])}">
    <div class="localnav-inner">
      <a class="localnav-title" href="{prefix}{home}">{esc(app['name'])}</a>
      <ul>
        <li><a href="{prefix}{home}"{here if current == 'overview' else ''}>{esc(ui["overview"])}</a></li>
        <li><a href="{prefix}{app['slug']}/privacy/"{here if current == 'privacy' else ''}>{esc(ui["privacy"])}</a></li>{store}
      </ul>
    </div>
  </nav>"""


# Every page's public address, collected as pages are written, for sitemap.xml.
PAGE_URLS = []
# Page URL -> the day its HTML last changed. A page whose HTML is the same as
# on disk keeps the date the previous sitemap.xml gave it.
TODAY = datetime.date.today().isoformat()
LASTMOD = {}


def _old_lastmod():
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    return dict(re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", text))


OLD_LASTMOD = _old_lastmod()

# Search and AI crawlers named in robots.txt. "User-agent: *" already allows
# them; naming them says plainly that answer engines are welcome.
AI_CRAWLERS = [
    "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "Google-Extended",
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot",
    "Claude-User", "PerplexityBot", "Perplexity-User", "DuckAssistBot",
    "Amazonbot", "meta-externalagent", "MistralAI-User", "CCBot",
]
# IndexNow key (Bing, Yandex, Seznam, Naver): the file <key>.txt at the site
# root proves the site is ours, so changed URLs can be pushed to Bing at once.
INDEXNOW_KEY = "c1a7f0e2b9d84d5fa3e6b2c4d8f1a903"
# Page URL -> its language versions [(code, URL)], repeated in sitemap.xml.
ALTERNATES = {}


def write(path, text):
    if path.endswith(".html"):
        # The one official address of the page, so search engines don't treat
        # /aloud/ and /aloud/index.html as two pages.
        url = SITE_URL + path.removesuffix("index.html")
        text = text.replace("</head>", f'  <link rel="canonical" href="{url}">\n'
                                       f'  <meta property="og:url" content="{url}">\n</head>', 1)
        PAGE_URLS.append(url)
        old = ROOT / path
        same = old.exists() and old.read_text(encoding="utf-8") == text
        LASTMOD[url] = OLD_LASTMOD.get(url, TODAY) if same else TODAY
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def search_files():
    """sitemap.xml lists every page; robots.txt allows everything and points
    crawlers at the sitemap. Both are rebuilt from the pages just written.
    Pages that exist in several languages list them all, as in their <head>."""
    def entry(u):
        cluster = ALTERNATES.get(u)
        mod = f"\n    <lastmod>{LASTMOD[u]}</lastmod>" if u in LASTMOD else ""
        links = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{code}" href="{esc(url)}"/>'
            for code, url in (cluster + [("x-default", cluster[0][1])] if cluster else []))
        return f"  <url>\n    <loc>{esc(u)}</loc>{mod}{links}\n  </url>"

    urls = "\n".join(entry(u) for u in PAGE_URLS)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
          ' xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          f"{urls}\n</urlset>\n")
    bots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_CRAWLERS)
    write("robots.txt", f"User-agent: *\nAllow: /\n\n{bots}Sitemap: {SITE_URL}sitemap.xml\n")


# ---------------------------------------------------------------- pages

def home_page():
    p = ""
    principles = "\n".join(
        f"""      <li class="principle">
        <svg viewBox="0 0 28 28" aria-hidden="true">{svg}</svg>
        <h3>{name}.</h3>
        <p>{text}</p>
      </li>""" for name, text, svg in PRINCIPLES)

    tiles = []
    for app in APPS:
        store = (f'<a class="pill pill-outline" href="{store_url(app)}">App Store</a>'
                 if is_live(app) else '<span class="pill pill-soon">Coming soon</span>')
        imgs = "".join(
            f'<img src="{p}{shot(app, n)}" width="{SHOT_W}" height="{SHOT_H}" alt="" loading="lazy" decoding="async">'
            for n in app["tile"])
        tiles.append(f"""      <article class="tile">
        <img class="app-icon" src="{p}{icon(app)}" width="256" height="256" alt="">
        <h3>{esc(app['name'])}</h3>
        <p class="tile-tagline">{esc(app['tagline'])}</p>
        <p class="tile-actions">
          <a class="pill" href="{p}{app['slug']}/">Learn more</a>
          {store}
        </p>
        <div class="tile-shots">{imgs}</div>
      </article>""")

    body = f"""    <section class="hero">
      <p class="eyebrow">Built for iPhone</p>
      <h1>Apps that mind <br>their own business.</h1>
      <p class="hero-sub">Powerful apps that respect your time, your money, and your privacy.</p>
    </section>

    <section class="principles-wrap" aria-label="Principles">
      <ul class="principles">
{principles}
      </ul>
    </section>

    <section class="apps" id="apps">
      <h2 class="section-title">The apps.</h2>
      <div class="tiles">
{chr(10).join(tiles)}
      </div>
    </section>

    <section class="closing">
      <h2>We respect your privacy.</h2>
      <p>We don't know who you are, and we'd like to keep it that way. With no accounts, no analytics, and no ads, there's nothing about you for us, advertisers, or data brokers to see. And the apps never ask for your Instagram or Facebook password.</p>
      <p><a class="more" href="privacy/">Read our privacy policies</a></p>
    </section>

    <section class="about" id="about">
      <p class="eyebrow">About the name</p>
      <h2 class="about-word">cis·tron</h2>
      <p>A cistron is the stretch of DNA that does one complete job: it carries the instructions for a single protein. The word comes from biology's <i>cis</i>–<i>trans</i> test, and <i>cis</i> is Latin for “on this side”. That's the idea behind every app here: each does one job well, and does it on your side, on your iPhone, not on someone else's server.</p>
    </section>"""

    org = {"@type": "Organization", "@id": f"{SITE_URL}#org", "name": COMPANY,
           "alternateName": BRAND, "url": SITE_URL,
           "logo": f"{SITE_URL}assets/apple-touch-icon.png",
           **({"email": EMAIL} if EMAIL else {}),
           "sameAs": ["https://apps.apple.com/developer/id6787521132"]}
    apps = {"@type": "ItemList", "name": f"iPhone apps by {COMPANY}",
            "itemListElement": [
                {"@type": "ListItem", "position": i, "url": f"{SITE_URL}{a['slug']}/",
                 "name": a["store_name"]} for i, a in enumerate(APPS, 1)]}
    write("index.html", page(
        prefix=p, title=f"{BRAND} · Apps for iPhone",
        description="Minimal, local, ad-free iPhone apps. No accounts, no ads, no tracking.",
        body=body, head=json_ld({"@graph": [org, apps]})))


def stars(review):
    if "stars" not in review:
        return ""
    n = review["stars"]
    return f'            <p class="stars" aria-label="{n} out of 5 stars">{"★" * n}</p>\n'


def duo_showcase(app, p):
    """A row under the gallery: the app on the iPhone Duo, folded, half open
    and open flat (see `duo` in the notes at the top). It sits inside the
    gallery section, so the Light/Dark switch swaps these images along with
    the screenshots."""
    duo = app.get("duo")
    if not duo:
        return "", ""
    slug = app["slug"]

    def img(name, size, alt=""):
        light = f"{p}{versioned(f'assets/img/{slug}/duo/{name}-light.webp')}"
        dark_path = f"assets/img/{slug}/duo/{name}-dark.webp"
        dark = f"{p}{versioned(dark_path)}" if (ROOT / dark_path).exists() else light
        return (f'<img src="{light}" data-light="{light}" data-dark="{dark}" {size} '
                f'alt="{esc(alt)}" loading="lazy" decoding="async">')

    cover = 'width="699" height="1017"'
    inner = 'width="1427" height="1004"'
    phones = []
    for pose, name, label, caption, alt in duo["items"]:
        if pose == "cover":
            art = (f'<div class="duo-closed"><div class="duo-screen">{img(name, cover, alt)}'
                   f'<span class="duo-camera"></span></div></div>')
        elif pose == "book":
            art = (f"""<div class="duo-book">
                <div class="duo-half duo-half-left">{img(name, inner, alt)}</div>
                <div class="duo-half duo-half-right">{img(name, inner)}</div>
              </div>""")
        else:
            art = f'<div class="duo-flat">{img(name, inner, alt)}</div>'
        phones.append(f"""          <li>
            <figure>
              {art}
              <figcaption><strong>{esc(label)}</strong> {esc(caption)}</figcaption>
            </figure>
          </li>""")
    items = "\n".join(phones)
    row = f"""
      <div class="duo-row">
        <h2 class="duo-title">{esc(duo.get("title", "On iPhone Duo"))}</h2>
        <p class="duo-sub">{esc(duo["sub"])}</p>
        <ul class="duo-track">
{items}
        </ul>
      </div>"""
    return "", row


def proof_section(app, ui=UI_EN):
    """Stats and review excerpts for an app page; empty when it has neither."""
    stats, reviews = app.get("stats", []), app.get("reviews", [])
    if not stats and not reviews:
        return ""
    parts = []
    if stats:
        items = "".join(
            f"<li><strong>{esc(fig)}</strong><span>{esc(cap)}</span></li>" for fig, cap in stats)
        parts.append(f'      <ul class="stats">{items}</ul>')
    if reviews:
        cards = "\n".join(f"""        <li>
          <figure class="review">
{stars(r)}            <blockquote><p>“{esc(r['quote'])}”</p></blockquote>
            <figcaption>{esc(r['source'])}</figcaption>
          </figure>
        </li>""" for r in reviews)
        single = " reviews-single" if len(reviews) == 1 else ""
        parts.append(f"""      <h2 class="proof-title">{esc(ui["what_people_say"])}</h2>
      <ul class="reviews{single}">
{cards}
      </ul>""")
    return '    <section class="proof">\n' + "\n".join(parts) + "\n    </section>\n"


def base_platform(app):
    """The platform line in English, e.g. "iPhone · iOS 17 or later"."""
    return next((a.get("platform") for a in APPS if a["slug"] == app["slug"]), None) \
        or UI_EN["platform"]


def app_structured_data(app, L, url, links):
    """schema.org SoftwareApplication + FAQPage for one language version."""
    store = store_url(app)
    lead, rest = app["intro"]
    software = {
        "@type": "SoftwareApplication",
        "@id": f"{SITE_URL}{app['slug']}/#app",
        "name": app["store_name"],
        "alternateName": app["name"],
        "url": url,
        "inLanguage": L["code"],
        "description": f"{lead} {rest}",
        "applicationCategory": app.get("category", "UtilitiesApplication"),
        "operatingSystem": "iOS {}.0 or later".format(
            (re.findall(r"iOS (\d+)", base_platform(app)) or ["17"])[0]),
        "availableOnDevice": "iPhone",
        **({"downloadUrl": store, "installUrl": store, "sameAs": store} if is_live(app) else {}),
        "image": f"{SITE_URL}assets/img/{app['slug']}/icon.png",
        "screenshot": [SITE_URL + shot_path(app, i) for i in range(1, len(app["shots"]) + 1)],
        "featureList": [title for title, _ in app["features"]],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@type": "Organization", "@id": f"{SITE_URL}#org", "name": COMPANY,
                      "url": SITE_URL},
    }
    faq = {
        "@type": "FAQPage",
        "@id": f"{url}#faq",
        "inLanguage": L["code"],
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": blocks_html(a, links, "")}}
                       for q, a in L["faq"]],
    }
    return json_ld({"@graph": [software, faq]})


def app_page(base, langs=(), L=None):
    """An app's page. With a language file `L`, its `page` entries replace the
    English copy in APPS, and the page gains the FAQ, a link to the export
    guide, the language list, hreflang links and structured data."""
    L = L or {}
    app = {**base, **L.get("page", {})}
    ui = {**UI_EN, **L.get("ui", {})}
    folder = lang_dir(base, L) if L else f"{base['slug']}/"
    p = up(folder)
    dark = app.get("dark_shots", False)

    def variants(i):
        if not dark:
            return ""
        return f' data-light="{p}{shot(app, i)}" data-dark="{p}{shot(app, i, dark=True)}"'

    shots = "\n".join(
        f'          <li><img src="{p}{shot(app, i)}"{variants(i)} width="{SHOT_W}" height="{SHOT_H}" alt="{esc(alt)}" loading="{"eager" if i < 4 else "lazy"}" decoding="async"></li>'
        for i, alt in enumerate(app["shots"], 1))
    toggle = f"""
        <div class="appearance-toggle" role="group" aria-label="{esc(ui["appearance"])}">
          <button type="button" data-appearance="light" aria-pressed="true">{esc(ui["light"])}</button>
          <button type="button" data-appearance="dark" aria-pressed="false">{esc(ui["dark"])}</button>
        </div>""" if dark else ""
    duo_button, duo_dialog = duo_showcase(app, p)
    features = "\n".join(
        f"""        <li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>""" for t, d in app["features"])
    privacy = "\n".join(f"          <li>{esc(b)}</li>" for b in app["privacy"])
    others = "\n".join(
        f"""        <li><a href="{p}{o['slug']}/"><img class="app-icon" src="{p}{icon(o)}" width="256" height="256" alt=""><span>{esc(o['name'])}</span></a></li>"""
        for o in APPS if o is not base)
    note = f'\n      <p class="note">{esc(app["note"])}</p>' if app["note"] else ""
    proof = proof_section(app, ui)
    why = ""
    if "why" in app:
        heading, text = app["why"]
        why = f"""    <section class="why">
      <h2>{esc(heading)}</h2>
      <p>{esc(text)}</p>
    </section>

"""
    lead, rest = app["intro"]
    if is_live(app):
        meta = app["pricing"]
        store = f'<a class="pill pill-large" href="{store_url(app)}">{esc(ui["view_on_store"])}</a>'
    else:
        meta = ui["soon"]
        store = f'<span class="pill pill-large pill-soon">{esc(ui["coming_soon"])}</span>'
    privacy_href = "privacy/" if folder == f"{base['slug']}/" else f"{p}{base['slug']}/privacy/"

    guide_link = faq = languages = head = ""
    if L:
        links = {"store": store_url(base), "privacy": f"{p}{base['slug']}/privacy/"}
        if "guide" in L:
            links["guide"] = f"{p}{guide_dir(base, L)}"
            guide_link = (f'\n      <p class="intro-link"><a class="more" href="{links["guide"]}">'
                          f'{esc(L["guide_link"])}</a></p>')
        faq = faq_section(L, links, ui)
        if len(langs) > 1:
            languages = "\n" + language_nav(langs, L, p, lambda x: lang_dir(base, x))
        url = SITE_URL + folder
        cluster = alternates(langs, lambda x: SITE_URL + lang_dir(base, x))
        ALTERNATES[url] = cluster
        absolute = {"store": store_url(base), "privacy": f"{SITE_URL}{base['slug']}/privacy/"}
        if "guide" in L:
            absolute["guide"] = SITE_URL + guide_dir(base, L)
        head = "\n".join([f'  <meta property="og:locale" content="{L["og_locale"]}">',
                          hreflang_links(cluster),
                          app_structured_data(app, L, url, absolute)])

    body = f"""    <section class="app-hero">
      <img class="app-icon app-icon-large" src="{p}{icon(app)}" width="256" height="256" alt="{esc(app['name'])} app icon">
      <h1>{esc(app['name'])}</h1>
      <p class="app-tagline">{esc(app['tagline'])}</p>
      <p class="app-meta">{esc(meta)} · {esc(app.get("platform", ui["platform"]))}</p>
      <p>{store}</p>
    </section>

    <section class="gallery" data-gallery aria-label="{esc(ui["screenshots"])}">
      <ul class="gallery-track" tabindex="0">
{shots}
      </ul>
      <div class="gallery-controls">{duo_button}{toggle}
        <div class="gallery-paddles">
          <button type="button" data-prev aria-label="{esc(ui["prev"])}"><svg viewBox="0 0 36 36" aria-hidden="true"><path d="M20.5 11 13.5 18l7 7"/></svg></button>
          <button type="button" data-next aria-label="{esc(ui["next"])}"><svg viewBox="0 0 36 36" aria-hidden="true"><path d="M15.5 11l7 7-7 7"/></svg></button>
        </div>
      </div>{duo_dialog}
    </section>

    <section class="intro">
      <p><strong>{esc(lead)}</strong> {esc(rest)}</p>{guide_link}
    </section>

    <section class="features">
      <ul>
{features}
      </ul>
    </section>

{why}{proof}{faq}
    <section class="privacy-card">
      <div>
        <p class="eyebrow">{esc(ui["privacy_eyebrow"])}</p>
        <h2>{esc(app['privacy_title'])}</h2>
        <p><a class="more" href="{privacy_href}">{esc(ui["read_policy"])}</a></p>
      </div>
      <ul class="checks">
{privacy}
      </ul>
    </section>
{note}{languages}
    <section class="more-apps">
      <h2>{esc(ui["more_apps"])}</h2>
      <ul>
{others}
      </ul>
    </section>"""

    write(f"{folder}index.html", page(
        prefix=p, title=f"{app['name']}: {app['tagline']}",
        description=f"{lead} {rest}", body=body,
        local_nav=local_nav(base, p, "overview", ui, folder),
        app_id=app["id"] if is_live(app) else None, scripts=True,
        lang=L.get("code", "en"), ui=ui, head=head))


def guide_page(base, langs, L):
    """Step by step: how to get the data the app reads, in one language."""
    app = {**base, **L.get("page", {})}
    ui = {**UI_EN, **L.get("ui", {})}
    g = L["guide"]
    folder = guide_dir(base, L)
    home = lang_dir(base, L)
    p = up(folder)
    store = store_url(base)
    links = {"app": f"{p}{home}", "store": store, "privacy": f"{p}{base['slug']}/privacy/"}
    store_pill = (f'<a class="pill" href="{store}">{esc(ui["view_on_store"])}</a>' if is_live(base)
                  else f'<span class="pill pill-soon">{esc(ui["coming_soon"])}</span>')

    summary = "\n".join(
        f"          <div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in g["choose"])
    steps = "\n".join(f"""        <li id="step-{i}">
          <h2>{esc(title)}</h2>
          <p>{rich(text, links)}</p>
        </li>""" for i, (title, text) in enumerate(g["steps"], 1))
    tips = "\n".join(f"""        <div>
          <h3>{esc(title)}</h3>
          <p>{rich(text, links)}</p>
        </div>""" for title, text in g["tips"])

    body = f"""    <article class="guide">
      <p class="eyebrow"><a href="{p}{home}">{esc(app['name'])}</a></p>
      <h1>{esc(g['title'])}</h1>
      <p class="guide-lead">{rich(g['lead'], links)}</p>
      <div class="guide-summary">
        <p class="guide-summary-title">{esc(ui['summary'])}</p>
        <dl>
{summary}
        </dl>
      </div>
      <ol class="guide-steps">
{steps}
      </ol>
      <h2 class="guide-tips-title">{esc(ui['tips'])}</h2>
      <div class="guide-tips">
{tips}
      </div>
      <p class="guide-updated">{esc(g['updated'])}</p>
      <aside class="guide-cta">
        <img class="app-icon" src="{p}{icon(base)}" width="256" height="256" alt="">
        <h2>{esc(g['cta_title'])}</h2>
        <p>{esc(g['cta_text'])}</p>
        <p class="guide-cta-actions">
          {store_pill}
          <a class="more" href="{p}{home}">{esc(ui['cta_more'].format(name=app['name']))}</a>
        </p>
      </aside>
    </article>

{language_nav(langs, L, p, lambda x: guide_dir(base, x))}"""

    url = SITE_URL + folder
    cluster = alternates(langs, lambda x: SITE_URL + guide_dir(base, x))
    ALTERNATES[url] = cluster
    howto = json_ld({
        "@type": "HowTo",
        "name": g["title"],
        "description": g["description"],
        "inLanguage": L["code"],
        "url": url,
        "step": [{"@type": "HowToStep", "position": i, "name": title, "text": plain(text),
                  "url": f"{url}#step-{i}"}
                 for i, (title, text) in enumerate(g["steps"], 1)],
    })
    head = "\n".join([f'  <meta property="og:locale" content="{L["og_locale"]}">',
                      hreflang_links(cluster), howto])
    write(f"{folder}index.html", page(
        prefix=p, title=g["title"], description=g["description"], body=body,
        local_nav=local_nav(base, p, "guide", ui, home),
        app_id=base["id"] if is_live(base) else None,
        lang=L["code"], ui=ui, head=head))


def privacy_page(app):
    p = "../../"
    source = (ROOT / "content/privacy" / f"{app['slug']}.md").read_text(encoding="utf-8")
    if EMAIL:
        source = source.replace("{{email}}", EMAIL)
    else:
        source = re.sub(r"\n## Contact\n.*?(?=\n## |\Z)", "\n", source, flags=re.S)
    _, date, content = md_to_html(source)
    body = f"""    <article class="policy">
      <p class="eyebrow"><a href="../">{esc(app['name'])}</a></p>
      <h1>Privacy Policy</h1>
      <p class="policy-date">{esc(date)}</p>
{content}
    </article>"""
    write(f"{app['slug']}/privacy/index.html", page(
        prefix=p, title=f"{app['name']} Privacy Policy",
        description=f"How {app['name']} handles your information: {app['network']}",
        body=body, local_nav=local_nav(app, p, "privacy"),
        app_id=app["id"] if is_live(app) else None))


def privacy_index():
    p = "../"
    rows = "\n".join(f"""        <li>
          <a class="policy-row" href="{p}{app['slug']}/privacy/">
            <img class="app-icon" src="{p}{icon(app)}" width="256" height="256" alt="">
            <span class="policy-row-text">
              <strong>{esc(app['name'])}</strong>
              <span>{esc(app['network'])}</span>
            </span>
            <span class="policy-row-link">Privacy policy</span>
          </a>
        </li>""" for app in APPS)
    body = f"""    <section class="privacy-hero">
      <h1>Privacy.</h1>
      <p class="hero-sub">None of these apps has accounts, analytics, advertising, or tracking. We run no servers, so your data never reaches us.</p>
    </section>

    <section class="policies">
      <h2>What leaves your iPhone</h2>
      <ul>
{rows}
      </ul>
    </section>"""
    write("privacy/index.html", page(
        prefix=p, title=f"Privacy · {BRAND}",
        description="What each app sends over the network, if anything, and links to every privacy policy.",
        body=body))


def faq_text(blocks):
    """An FAQ answer as plain Markdown, for llms-full.txt."""
    out = []
    for b in blocks:
        if isinstance(b, str):
            out.append(plain(b))
        else:
            out.append("\n".join(f"{i}. {plain(x)}" for i, x in enumerate(b, 1)))
    return "\n\n".join(out)


def llms_files(all_langs):
    """llms.txt (llmstxt.org): a short Markdown map of the site for AI
    assistants, and llms-full.txt with every app's facts, FAQ and guide in
    English, so an assistant can answer from one file."""
    short = [f"# {BRAND}",
             "",
             f"> {BRAND} ({COMPANY}) makes small iPhone apps that work on the device. "
             "None of them has accounts, ads, analytics or tracking, and none is a "
             "subscription: each is free to download, and some have one optional "
             "one-time purchase.",
             "",
             f"Contact: {EMAIL}" if EMAIL else "",
             "",
             "## Apps", ""]
    full = [f"# {BRAND}: every app, in full", "",
            f"> {BRAND} ({COMPANY}) makes small iPhone apps that work on the device, "
            "with no accounts, ads, analytics, tracking or subscriptions.", ""]
    for app in APPS:
        langs = all_langs[app["slug"]]
        url = f"{SITE_URL}{app['slug']}/"
        lead, rest = app["intro"]
        status = (f"{app['pricing']}. App Store: {store_url(app)}" if is_live(app)
                  else "Coming soon to the App Store")
        short.append(f"- [{app['store_name']}]({url}): {app['tagline']} {lead} "
                     f"{status}.")
        full += [f"## {app['store_name']}", "",
                 f"Page: {url}",
                 f"Price: {app['pricing'] if is_live(app) else 'not released yet'}",
                 f"Runs on: {app.get('platform', UI_EN['platform'])}",
                 *( [f"App Store: {store_url(app)}"] if is_live(app) else [] ),
                 f"Privacy policy: {url}privacy/",
                 f"What it sends over the network: {app['network']}"]
        if len(langs) > 1:
            full.append("This page in other languages: " + ", ".join(
                f"{L['name']} {SITE_URL}{lang_dir(app, L)}" for L in langs[1:]))
        full += ["", f"{lead} {rest}", "", "### Features", ""]
        full += [f"- **{t}.** {d}" for t, d in app["features"]]
        full += ["", f"### Privacy: {app['privacy_title']}", ""]
        full += [f"- {b}" for b in app["privacy"]]
        if app.get("note"):
            full += ["", app["note"]]
        en = next((L for L in langs if L["code"] == "en"), None)
        if en:
            full += ["", "### Questions and answers", ""]
            for q, a in en["faq"]:
                full += [f"**{q}**", "", faq_text(a), ""]
            if "guide" in en:
                g = en["guide"]
                full += [f"### {g['title']}", "", f"Guide: {SITE_URL}{guide_dir(app, en)}", "",
                         plain(g["lead"]), ""]
                full += [f"{i}. **{t}.** {plain(x)}" for i, (t, x) in enumerate(g["steps"], 1)]
                full += [""]
                short.append(f"  - Guide: [{g['title']}]({SITE_URL}{guide_dir(app, en)})")
        full.append("")
    short += ["", "## More", "",
              f"- [Privacy policies]({SITE_URL}privacy/): what each app sends over the network, if anything",
              f"- [Everything in one file]({SITE_URL}llms-full.txt): each app's features, privacy, FAQ and guide",
              ""]
    write("llms.txt", "\n".join(short))
    write("llms-full.txt", "\n".join(full))


if __name__ == "__main__":
    home_page()
    privacy_index()
    all_langs = {}
    for app in APPS:
        langs = all_langs[app["slug"]] = load_languages(app)
        for L in langs:
            app_page(app, langs, L)
            if "guide" in L:
                guide_page(app, langs, L)
        if not langs:
            app_page(app)
        privacy_page(app)
    llms_files(all_langs)
    write(f"{INDEXNOW_KEY}.txt", INDEXNOW_KEY)
    search_files()
