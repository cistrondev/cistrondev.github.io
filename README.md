# Apps website

A static site for my iPhone apps: a landing page, one page per app, and
each app's privacy policy. Plain HTML and CSS with relative links, so it
works on GitHub Pages with no build step on GitHub's side.

## Layout

```
index.html                 landing page
privacy/index.html         what each app sends over the network + links
<app>/index.html           app page (screenshots, features, privacy summary)
<app>/privacy/index.html   full privacy policy
assets/site.css, site.js   styles and the screenshot-gallery buttons
assets/img/<app>/          icon.png + 01.webp, 02.webp, … screenshots
content/privacy/<app>.md   privacy policy sources
content/<app>/<lang>.py    translations, FAQ and export guide (Unfollowers only)
build.py                   generates every .html file above
```

Unfollowers also has these pages, one set per language (en, pt-BR, es, it,
fr, de, el, nl):

```
unfollowers/<lang>/                   app page with an FAQ (English: unfollowers/)
unfollowers/<lang>/<guide-slug>/      how to download the Instagram data export
assets/img/unfollowers/<lang>/        that language's screenshots (es, it, fr, de, el, nl)
```

Each language version links to the others with `hreflang` tags (English is
`x-default`) and carries schema.org data: SoftwareApplication and FAQPage on
the app page, HowTo on the guide. sitemap.xml lists the same alternates.

## Editing

Copy for the apps lives in the `APPS` list at the top of `build.py`;
privacy policies live in `content/privacy/`. After changing either:

```bash
python3 build.py
```

Don't hand-edit the generated `.html` files. The next build overwrites them.
The build also writes `sitemap.xml` (every page) and `robots.txt` (points
search engines at the sitemap), so new pages are listed automatically.

To add an app: add an entry to `APPS`, put its policy in
`content/privacy/<slug>.md`, and add `assets/img/<slug>/icon.png` (256×256)
plus screenshots as `01.webp`, `02.webp`, … at 642×1389 (half of a
1284×2778 App Store screenshot).

To change the Unfollowers translations, FAQ or guide, edit
`content/unfollowers/<lang>.py` (en.py explains every key and the copy rules)
and rebuild. English page copy stays in `APPS`; en.py holds only the English
FAQ and guide. To add a language, copy a language file, translate it, and add
its code to the app's `languages` list. On a phone the header and app-bar
links have little room, so check a new language at 375 px wide.

An app that is not on the App Store yet takes `"live": False` in its entry.
Its pages then say "Coming soon" where the App Store buttons and the price
would be. On release day, remove that line, fill in `pricing`, and rebuild.

## Publishing

The site is served by GitHub Pages from the `main` branch of
[cistrondev/cistrondev.github.io](https://github.com/cistrondev/cistrondev.github.io)
at **https://cistrondev.github.io**. `.nojekyll` makes GitHub serve the files exactly as they are.

To publish a change:

```bash
python3 build.py
git add -A
git commit -m "Describe the change"
git push
```

Commits in this folder are signed as "Cistron Development" with the account's
private GitHub address (set with `git config` in this repository only).

## Privacy policy URLs for App Store Connect

- https://cistrondev.github.io/aloud/privacy/
- https://cistrondev.github.io/lifetrends/privacy/
- https://cistrondev.github.io/timegrapher/privacy/
- https://cistrondev.github.io/unfollowers/privacy/
- https://cistrondev.github.io/unfriended/privacy/
