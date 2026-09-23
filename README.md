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
build.py                   generates every .html file above
```

## Editing

Copy for the apps lives in the `APPS` list at the top of `build.py`;
privacy policies live in `content/privacy/`. After changing either:

```bash
python3 build.py
```

Don't hand-edit the generated `.html` files. The next build overwrites them.

To add an app: add an entry to `APPS`, put its policy in
`content/privacy/<slug>.md`, and add `assets/img/<slug>/icon.png` (256×256)
plus screenshots as `01.webp`, `02.webp`, … at 642×1389 (half of a
1284×2778 App Store screenshot).

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
