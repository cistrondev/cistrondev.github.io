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
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
BRAND = "Cistron"                 # header wordmark and page titles
COMPANY = "Cistron Development"   # copyright line
# Contact address. Leave empty to hide the Contact links and every policy's
# "## Contact" section; set it and rebuild to bring them back.
EMAIL = ""
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
             "Fourteen voices for English and thirty more languages. No server does "
             "the talking, so Aloud keeps reading in airplane mode."),
            ("Articles, PDFs, anything",
             "Share from any browser, open PDFs from Files, even scanned ones, or "
             "paste your own text."),
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
        "shots": [
            "Anything you can read, it reads to you.",
            "Get through the reading list.",
            "Works offline. Anywhere.",
            "No subscription. No ads. No tracking.",
            "Natural voices. Every language.",
            "Reader mode: read it your way.",
            "Twice the speed. Half the time.",
            "Your shelf, on every device.",
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
            "Health data is read, analyzed and kept on your iPhone. Never uploaded.",
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
            "Rate, amplitude and beat error in about thirty seconds.",
            "Timegrapher listens to your mechanical watch through the iPhone's "
            "microphone, then keeps your whole collection, every reading and what "
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
             "Every watch with its photo, reference, movement and lift angle, and "
             "every measurement saved."),
            ("See the drift",
             "Charts show the rate across months and years, with a plain-language "
             "verdict after each reading."),
            ("Know what it's worth",
             "Current Chrono24 asking prices for your exact reference, with the "
             "median worked out on your iPhone."),
            ("Magnetism check",
             "A magnetized hairspring is the most common reason a watch suddenly "
             "gains time. Sweep the watch across the back of your iPhone and its "
             "magnetometer tells you whether it needs demagnetizing."),
        ],
        "privacy_title": "Nothing recorded. Nothing uploaded.",
        "privacy": [
            "Microphone audio is analyzed live and is never recorded or saved.",
            "Your collection and measurements are stored only on your iPhone.",
            "The optional price check searches Chrono24 for your watch's "
            "reference. Nothing else is sent.",
        ],
        "network": (
            "Nothing, unless you run the Chrono24 price check. Then only your "
            "watch's brand and reference are searched. Audio is never recorded."
        ),
        "note": "",
        "reviews": [
            {"source": "Review on Reddit",
             "quote": "Timegrapher is extremely reliable. I get an accurate measure of "
                      "the rate of my watches in no time! It also let’s me track the "
                      "price of my collection over the years"},
        ],
        "tile": [1, 3, 4],
        "shots": [
            "Your iPhone is a timing machine: rate, amplitude and beat error in 30 seconds.",
            "Readings that hold steady, with amplitude from lift angle.",
            "Your collection, one bench.",
            "See the drift before it matters.",
            "Know what it's worth: the Chrono24 median for your exact reference.",
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
             "Your likes, comments and story reactions, counted from your own "
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
        "shots": [
            "See every unfollower: who left, and when, read from your own Instagram export.",
            "Probably blocked you: accounts that left your followers and following at the same time.",
            "They don't follow back: search, sort, and tap through to any profile.",
            "Who you hype the most: your likes, comments and story reactions, counted.",
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
             "Requests left unanswered, rejections, followers and following."),
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
        "shots": [
            "Who dropped you? Import your Facebook export twice and the difference shows who left.",
            "They dropped you. Facebook won't say.",
            "New name, who dis? Renames matched by the exact friend-since second.",
            "Your friend eras, charted.",
            "Day-one besties: your oldest friends, ranked.",
            "Left on read: pending requests, rejections, followers and following.",
            "No login. No leaks. Your export goes in; nothing goes out.",
        ],
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
     "No ads, no analytics, no tracking, and no subscriptions.",
     '<circle cx="14" cy="14" r="10"/><path d="M7 21 21 7"/>'),
]

# ---------------------------------------------------------------- helpers

esc = html.escape


def asset(name):
    """assets/<name>?v=<content hash>, so browsers refetch it after every change."""
    digest = hashlib.sha1((ROOT / "assets" / name).read_bytes()).hexdigest()[:8]
    return f"assets/{name}?v={digest}"


def store_url(app):
    return f"https://apps.apple.com/app/id{app['id']}"


def shot(app, n):
    return f"assets/img/{app['slug']}/{n:02d}.webp"


def icon(app):
    return f"assets/img/{app['slug']}/icon.png"


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


# ---------------------------------------------------------------- chrome

def page(*, prefix, title, description, body, local_nav="", app_id=None, scripts=False):
    home = prefix or "./"
    nav_contact = f'        <li><a href="mailto:{EMAIL}">Contact</a></li>\n' if EMAIL else ""
    footer_contact = f'          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>\n' if EMAIL else ""
    banner = f'\n  <meta name="apple-itunes-app" content="app-id={app_id}">' if app_id else ""
    script = f'\n  <script src="{prefix}{asset("site.js")}" defer></script>' if scripts else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="#ffffff">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">{banner}
  <link rel="stylesheet" href="{prefix}{asset('site.css')}">{script}
</head>
<body>
  <header class="globalnav">
    <nav class="globalnav-inner" aria-label="Site">
      <a class="wordmark" href="{home}">{BRAND}</a>
      <ul>
        <li><a href="{home}#apps">Apps</a></li>
        <li><a href="{prefix}privacy/">Privacy</a></li>
        <li><a href="{home}#about">About</a></li>
{nav_contact}      </ul>
    </nav>
  </header>
{local_nav}
  <main>
{body}
  </main>
  <footer class="footer">
    <div class="footer-inner">
      <p>Instagram and Facebook are trademarks of Meta Platforms, Inc. Unfollowers and Unfriended are independent apps and are not affiliated with, endorsed by, or sponsored by Meta.</p>
      <div class="footer-row">
        <p>Copyright © {YEAR} {COMPANY}. All rights reserved.</p>
        <ul>
          <li><a href="{home}#apps">Apps</a></li>
          <li><a href="{prefix}privacy/">Privacy</a></li>
{footer_contact}        </ul>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def local_nav(app, prefix, current):
    here = ' aria-current="page"'
    return f"""  <nav class="localnav" aria-label="{esc(app['name'])}">
    <div class="localnav-inner">
      <a class="localnav-title" href="{prefix}{app['slug']}/">{esc(app['name'])}</a>
      <ul>
        <li><a href="{prefix}{app['slug']}/"{here if current == 'overview' else ''}>Overview</a></li>
        <li><a href="{prefix}{app['slug']}/privacy/"{here if current == 'privacy' else ''}>Privacy</a></li>
        <li><a class="pill pill-small" href="{store_url(app)}">App Store</a></li>
      </ul>
    </div>
  </nav>"""


def write(path, text):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


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
        imgs = "".join(
            f'<img src="{p}{shot(app, n)}" width="{SHOT_W}" height="{SHOT_H}" alt="" loading="lazy" decoding="async">'
            for n in app["tile"])
        tiles.append(f"""      <article class="tile">
        <img class="app-icon" src="{p}{icon(app)}" width="256" height="256" alt="">
        <h3>{esc(app['name'])}</h3>
        <p class="tile-tagline">{esc(app['tagline'])}</p>
        <p class="tile-actions">
          <a class="pill" href="{p}{app['slug']}/">Learn more</a>
          <a class="pill pill-outline" href="{store_url(app)}">App Store</a>
        </p>
        <div class="tile-shots">{imgs}</div>
      </article>""")

    body = f"""    <section class="hero">
      <p class="eyebrow">Apps for iPhone</p>
      <h1>Apps that mind <br>their own business.</h1>
      <p class="hero-sub">Powerful, focused tools that do one job well, on your iPhone, with no accounts, no ads and no tracking.</p>
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
      <h2>Honest about the network.</h2>
      <p>Some features have to reach out: a price check, a voice download, an article you shared. They run only in response to something you do, and each app's privacy policy says exactly what is sent, and to whom.</p>
      <p><a class="more" href="privacy/">See what each app sends</a></p>
    </section>

    <section class="about" id="about">
      <p class="eyebrow">About the name</p>
      <h2 class="about-word">cis·tron</h2>
      <p>A cistron is the stretch of DNA that does one complete job: it carries the instructions for a single protein. The word comes from biology's <i>cis</i>–<i>trans</i> test, and <i>cis</i> is Latin for “on this side”. That's the idea behind every app here: each does one job well, and does it on your side, on your iPhone, not on someone else's server.</p>
    </section>"""

    write("index.html", page(
        prefix=p, title=f"{BRAND} · Apps for iPhone",
        description="Minimal, local, ad-free iPhone apps. No accounts, no ads, no tracking.",
        body=body))


def stars(review):
    if "stars" not in review:
        return ""
    n = review["stars"]
    return f'            <p class="stars" aria-label="{n} out of 5 stars">{"★" * n}</p>\n'


def proof_section(app):
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
        parts.append(f"""      <h2 class="proof-title">What people say.</h2>
      <ul class="reviews{single}">
{cards}
      </ul>""")
    return '    <section class="proof">\n' + "\n".join(parts) + "\n    </section>\n"


def app_page(app):
    p = "../"
    shots = "\n".join(
        f'          <li><img src="{p}{shot(app, i)}" width="{SHOT_W}" height="{SHOT_H}" alt="{esc(alt)}" loading="{"eager" if i < 4 else "lazy"}" decoding="async"></li>'
        for i, alt in enumerate(app["shots"], 1))
    features = "\n".join(
        f"""        <li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>""" for t, d in app["features"])
    privacy = "\n".join(f"          <li>{esc(b)}</li>" for b in app["privacy"])
    others = "\n".join(
        f"""        <li><a href="{p}{o['slug']}/"><img class="app-icon" src="{p}{icon(o)}" width="256" height="256" alt=""><span>{esc(o['name'])}</span></a></li>"""
        for o in APPS if o is not app)
    note = f'\n      <p class="note">{esc(app["note"])}</p>' if app["note"] else ""
    proof = proof_section(app)
    lead, rest = app["intro"]

    body = f"""    <section class="app-hero">
      <img class="app-icon app-icon-large" src="{p}{icon(app)}" width="256" height="256" alt="{esc(app['name'])} app icon">
      <h1>{esc(app['name'])}</h1>
      <p class="app-tagline">{esc(app['tagline'])}</p>
      <p class="app-meta">{esc(app['pricing'])} · iPhone · iOS 17 or later</p>
      <p><a class="pill pill-large" href="{store_url(app)}">View on the App Store</a></p>
    </section>

    <section class="gallery" data-gallery aria-label="Screenshots">
      <ul class="gallery-track" tabindex="0">
{shots}
      </ul>
      <div class="gallery-paddles">
        <button type="button" data-prev aria-label="Previous screenshots"><svg viewBox="0 0 36 36" aria-hidden="true"><path d="M20.5 11 13.5 18l7 7"/></svg></button>
        <button type="button" data-next aria-label="Next screenshots"><svg viewBox="0 0 36 36" aria-hidden="true"><path d="M15.5 11l7 7-7 7"/></svg></button>
      </div>
    </section>

    <section class="intro">
      <p><strong>{esc(lead)}</strong> {esc(rest)}</p>
    </section>

    <section class="features">
      <ul>
{features}
      </ul>
    </section>

{proof}
    <section class="privacy-card">
      <div>
        <p class="eyebrow">Privacy</p>
        <h2>{esc(app['privacy_title'])}</h2>
        <p><a class="more" href="privacy/">Read the privacy policy</a></p>
      </div>
      <ul class="checks">
{privacy}
      </ul>
    </section>
{note}
    <section class="more-apps">
      <h2>More apps</h2>
      <ul>
{others}
      </ul>
    </section>"""

    write(f"{app['slug']}/index.html", page(
        prefix=p, title=f"{app['name']}: {app['tagline']}",
        description=f"{lead} {rest}", body=body,
        local_nav=local_nav(app, p, "overview"), app_id=app["id"], scripts=True))


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
        body=body, local_nav=local_nav(app, p, "privacy"), app_id=app["id"]))


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
      <p class="hero-sub">None of these apps has accounts, analytics, advertising or tracking. We run no servers, so your data never reaches us.</p>
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


if __name__ == "__main__":
    home_page()
    privacy_index()
    for app in APPS:
        app_page(app)
        privacy_page(app)
