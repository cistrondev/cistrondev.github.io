#!/usr/bin/env python3
"""Fetches every live app's App Store star rating into content/ratings.json.

    python3 ratings.py

The App Store keeps ratings per country, so this asks Apple's public lookup
for each storefront and combines them into one average weighted by the number
of ratings. Codes that are not App Store storefronts come back as HTTP 400 and
are skipped. build.py reads the file; run this, then build.py, to refresh the
stars on the site. Takes about ten minutes because the lookup is rate limited.
"""
import datetime
import json
import pathlib
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "content" / "ratings.json"
ARTIST_ID = "6787521132"
PAUSE = 2.5   # seconds between requests; the lookup allows about 20 a minute

# Every ISO 3166-1 alpha-2 code. Apple's storefronts are a subset.
COUNTRIES = """
ad ae af ag ai al am ao aq ar as at au aw ax az ba bb bd be bf bg bh bi bj bl
bm bn bo bq br bs bt bv bw by bz ca cc cd cf cg ch ci ck cl cm cn co cr cu cv
cw cx cy cz de dj dk dm do dz ec ee eg eh er es et fi fj fk fm fo fr ga gb gd
ge gf gg gh gi gl gm gn gp gq gr gs gt gu gw gy hk hm hn hr ht hu id ie il im
in io iq ir is it je jm jo jp ke kg kh ki km kn kp kr kw ky kz la lb lc li lk
lr ls lt lu lv ly ma mc md me mf mg mh mk ml mm mn mo mp mq mr ms mt mu mv mw
mx my mz na nc ne nf ng ni nl no np nr nu nz om pa pe pf pg ph pk pl pm pn pr
ps pt pw py qa re ro rs ru rw sa sb sc sd se sg sh si sj sk sl sm sn so sr ss
st sv sx sy sz tc td tf tg th tj tk tl tm tn to tr tt tv tw tz ua ug um us uy
uz va vc ve vg vi vn vu wf ws xk ye yt za zm zw
""".split()


def lookup(country):
    url = (f"https://itunes.apple.com/lookup?id={ARTIST_ID}"
           f"&entity=software&country={country}")
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return json.load(response)["results"]
        except urllib.error.HTTPError as error:
            if error.code == 400:          # not a storefront
                return None
            if attempt == 3:
                raise
            time.sleep(60 * (attempt + 1))   # rate limited or a server hiccup
        except urllib.error.URLError:
            if attempt == 3:
                raise
            time.sleep(30)


def main():
    apps = {}
    stores = 0
    for i, country in enumerate(COUNTRIES):
        if i:
            time.sleep(PAUSE)
        results = lookup(country)
        if results is None:
            continue
        stores += 1
        for r in results:
            if r.get("wrapperType") != "software":
                continue
            entry = apps.setdefault(str(r["trackId"]), {"name": r["trackName"], "by_store": {}})
            count = r.get("userRatingCount") or 0
            if count:
                entry["by_store"][country] = [r["averageUserRating"], count]
        print(f"{country}: {sum(1 for a in apps.values() if country in a['by_store'])} "
              f"apps rated", flush=True)

    for entry in apps.values():
        pairs = entry["by_store"].values()
        count = sum(n for _, n in pairs)
        entry["count"] = count
        entry["average"] = round(sum(avg * n for avg, n in pairs) / count, 3) if count else None

    data = {"fetched": datetime.date.today().isoformat(), "storefronts": stores,
            "apps": dict(sorted(apps.items(), key=lambda kv: kv[1]["name"]))}
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"\n{stores} storefronts, written to {OUT.relative_to(ROOT)}")
    for app_id, entry in data["apps"].items():
        print(f"  {entry['name'][:40]:40} {entry['average']}  ({entry['count']} ratings)")


if __name__ == "__main__":
    main()
