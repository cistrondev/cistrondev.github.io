# Aloud in German ("du", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# Button names are the app's German strings (Aloud/Localizable.xcstrings).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "de.py"))["L"]["ui"]

L = {
    "name": "Deutsch",
    "path": "de/",
    "og_locale": "de_DE",
    "ui": {
        **_ui,
        "summary": "Was Aloud vorliest",
        "tips": "Gut zu wissen",
        "appearance": "Darstellung der Bildschirmfotos",
        "light": "Hell",
        "dark": "Dunkel",
        "what_people_say": "Was andere sagen.",
    },
    "page": {
        "shots_dir": "de",
        "tagline": "Alles, was du lesen kannst, vorgelesen.",
        "pricing": "Kostenlos testen · Einmalig freischalten",
        "platform": "iPhone und iPad · iOS 17 oder neuer",
        "intro": (
            "Teile einen Artikel, öffne ein PDF oder setz einen Text ein.",
            "Aloud liest ihn dir mit einer natürlichen Stimme vor, die auf deinem iPhone "
            "entsteht, Satz für Satz, und merkt sich immer, wo du warst.",
        ),
        "features": [
            ("Natürliche Stimmen, auf dem Gerät",
             "Zehn Stimmen für Englisch und vier, die dreißig weitere Sprachen lesen, "
             "darunter Deutsch. Kein Server spricht mit, deshalb liest Aloud auch im "
             "Flugmodus weiter."),
            ("Artikel, PDFs, Bücher",
             "Teile aus jedem Browser, öffne PDFs und EPUB-Bücher aus „Dateien“, auch "
             "eingescannte PDFs, oder setz deinen eigenen Text ein."),
            ("Zum Mitlesen",
             "Der Satz, der gerade gesprochen wird, ist hervorgehoben. Halte die Leiste am "
             "Rand gedrückt, um durch den ganzen Text zu springen."),
            ("Schneller, wenn du willst",
             "Von 0,5× bis 3× ohne Mickymaus-Stimme. Auf Wunsch werden die Pausen nach "
             "jedem Satz gekürzt."),
            ("Für unterwegs",
             "Liest bei gesperrtem Bildschirm weiter, mit Steuerung auf dem Sperrbildschirm "
             "und über AirPods und einem Sleeptimer, der leise ausblendet."),
            ("Auf jedem Gerät",
             "Die iCloud-Synchronisierung ist optional und legt dein Regal als einfache "
             "Textdateien in dein eigenes iCloud Drive."),
        ],
        "privacy_title": "Privat, weil es so gebaut ist.",
        "privacy": [
            "Die Sprache entsteht auf deinem iPhone. Deine Dokumente werden nie hochgeladen.",
            "Die Stimmen werden einmal von einem öffentlichen Server geladen. Geteilte "
            "Artikel holt Aloud von ihrer eigenen Website, wie ein Browser.",
            "Kein Konto, keine Analytics, keine Werbung, kein Tracking.",
        ],
        "note": "",
        "reviews": [],
        "why": (
            "Keine Cloud. Kein Abo.",
            "Viele bekannte Vorlese-Apps erzeugen ihre Stimmen auf eigenen Servern. Die "
            "Artikel und Dokumente, die du hörst, werden also zuerst dorthin hochgeladen, "
            "und ihre Premium-Abos kosten bis zu 139 $ im Jahr oder 29 $ im Monat, fast "
            "350 $ im Jahr. Aloud erzeugt jede Stimme direkt auf deinem iPhone. Was du "
            "liest, wird zum Vorlesen nirgendwohin geschickt. Und es gibt kein Abo: ein "
            "einziger optionaler Kauf, der dir für immer gehört.",
        ),
        "shots": [
            "Alles, was du lesen kannst, liest es dir vor. Artikel, PDFs, Notizen, gesprochen von einer natürlichen Stimme, Satz für Satz.",
            "Komm durch deine Leseliste. Zum Anhören beim Pendeln, Spazieren, Abwaschen.",
            "Funktioniert offline. Überall. Die Stimme wird einmal geladen, danach liest Aloud jederzeit offline.",
            "Kein Abo. Keine Werbung. Kein Tracking.",
            "Natürliche Stimmen. Jede Sprache. Zehn Stimmen für Englisch, vier für dreißig weitere Sprachen, alle auf deinem iPhone erzeugt.",
            "Lesemodus: lies auf deine Art.",
            "Doppeltes Tempo. Halbe Zeit. Von 0,5× bis 3×, mit kürzeren Pausen zwischen den Sätzen.",
            "Dein Regal, auf jedem Gerät, als einfache Textdateien in iCloud Drive.",
            "Lies es in deiner Sprache: jeder Text auf dem Gerät übersetzt, Satz neben Satz.",
        ],
        "duo": {
            "title": "Auf dem iPhone Duo",
            "sub": "Zugeklappt hörst du zu. Aufgeklappt liest du.",
            "items": [
                ("cover", "cover", "Zugeklappt", "Die Stimme liest auf dem Außendisplay weiter.",
                 "Aloud auf dem Außendisplay des iPhone Duo: die Stimme liest weiter, mit Wiedergabesteuerung."),
                ("book", "spread", "Halb offen", "Zwei gegenüberliegende Seiten, in jedem Winkel.",
                 "Aloud auf dem halb geöffneten iPhone Duo: zwei gegenüberliegende Seiten."),
                ("flat", "spread", "Offen", "Mit Übersetzung? Original und Übersetzung nebeneinander.",
                 "Aloud auf dem geöffneten iPhone Duo: links das spanische Original, rechts die "
                 "englische Übersetzung, Zeile für Zeile."),
            ],
        },
    },
    "guide_link": "So hörst du Artikel, PDFs und EPUB-Bücher auf dem iPhone",
    "faq": [
        ("Welche Vorlese-App fürs iPhone gibt es ohne Abo?", [
            "Aloud liest Artikel, PDFs, EPUB-Bücher und jeden Text mit einer natürlichen "
            "Stimme vor. Die App ist kostenlos, und ein einziger In-App-Kauf hebt das Limit "
            "für immer auf. Es gibt kein Abo, und nichts verlängert sich.",
            "Die Stimmen entstehen auf deinem iPhone oder iPad. Was du liest, wird also nie "
            "zum Vorlesen hochgeladen, und Aloud liest auch ohne Internet. Es gibt kein "
            "Konto, keine Werbung und kein Tracking.",
        ]),
        ("Wie lasse ich mir einen Artikel auf dem iPhone vorlesen?", [
            [
                "Öffne den Artikel in Safari oder einer anderen App.",
                "Tippe auf **Teilen** und dann auf **Aloud**.",
                "Öffne Aloud und tippe auf Wiedergabe. Der Satz, der gerade gelesen wird, "
                "ist hervorgehoben.",
            ],
            "Wenn du aus Safari teilst, liest Aloud die Seite so, wie Safari sie zeigt. Das "
            "klappt auch bei Artikeln auf Seiten, bei denen du angemeldet bist. Links aus "
            "den Apps Facebook, Messenger und Instagram funktionieren ebenfalls. "
            "[Schritt-für-Schritt-Anleitung](guide).",
        ]),
        ("Kann Aloud aus einem EPUB ein Hörbuch machen?", [
            "Ja. Öffne eine EPUB-Datei aus der App „Dateien“ oder tippe auf **+** › "
            "**Datei importieren**. Aloud behält das Cover und die Kapitel. Die Liste "
            "**Kapitel** zeigt, wie lange jedes Kapitel zum Anhören dauert, und du kannst "
            "bei jedem beginnen. Deine Stelle bleibt gemerkt, so läuft ein langes Buch wie "
            "ein Hörbuch.",
            "Kopiergeschützte Bücher aus Shops lassen sich in keiner anderen App öffnen, "
            "auch nicht in Aloud. EPUBs ohne DRM, etwa von Project Gutenberg oder Standard "
            "Ebooks, funktionieren.",
        ]),
        ("Liest Aloud PDFs vor, auch eingescannte?", [
            "Ja. Öffne ein PDF aus „Dateien“ oder teile es mit Aloud. Aloud liest den Text "
            "in der richtigen Reihenfolge. Bei einem eingescannten PDF erkennt es den Text "
            "vorher auf dem Gerät.",
        ]),
        ("Funktioniert Aloud offline?", [
            "Ja. Jede Stimme wird einmal geladen, wenn du sie zum ersten Mal nutzt. Danach "
            "entsteht die Sprache auf deinem iPhone, und Aloud liest im Flugmodus, in der "
            "U-Bahn oder im Flugzeug. Einen neuen Artikel abzurufen braucht weiterhin "
            "Internet. Was schon im Regal liegt, nicht.",
        ]),
        ("Welche Sprachen kann Aloud vorlesen?", [
            "Zehn natürliche Stimmen lesen Englisch, vier weitere lesen über dreißig andere "
            "Sprachen, darunter Deutsch, Spanisch, Französisch, Italienisch und "
            "Portugiesisch. Die App selbst gibt es auf Deutsch, Englisch, Spanisch, "
            "Französisch, Italienisch und Portugiesisch.",
        ]),
        ("Kann Aloud übersetzen, was ich lese?", [
            "Ja, ab iOS 18. Tippe im Leser auf die Übersetzen-Taste und wähle eine Sprache "
            "unter **Übersetzen in**. Apples Übersetzer arbeitet auf deinem iPhone, es wird "
            "nichts verschickt. Die Seite zeigt dann jeden Satz mit seiner Übersetzung, und "
            "mit **Übersetzung vorlesen** liest die Stimme die andere Sprache.",
        ]),
        ("Wie schnell kann Aloud lesen?", [
            "Von 0,5× bis 3×, ohne Mickymaus-Stimme. **Pausen kürzen** schneidet die Stille "
            "zwischen den Sätzen weg. So passt ein 30-Minuten-Artikel in einen "
            "15-Minuten-Spaziergang.",
        ]),
        ("Ist Aloud kostenlos?", [
            "Aloud ist kostenlos, mit allen Stimmen und Funktionen. Im kostenlosen Regal "
            "haben drei Texte gleichzeitig Platz. Ein einmaliger Kauf, **Aloud "
            "freischalten**, hebt das Limit auf. Es gibt kein Abo. [Im App Store "
            "ansehen](store).",
        ]),
        ("Kann ich meine Leseliste aus Pocket oder Instapaper mitnehmen?", [
            "Ja. Exportiere deine gespeicherten Links aus Pocket, Instapaper, Raindrop oder "
            "die Lesezeichen deines Browsers. Öffne dann in Aloud **Einstellungen** › **Aus "
            "einer Datei importieren**. Jeder Link landet im Regal, und Aloud holt die "
            "Artikel im Hintergrund.",
        ]),
        ("Lädt Aloud meine Dokumente hoch?", [
            "Nein. Die Sprache entsteht auf deinem iPhone. Aloud lädt jede Stimme einmal von "
            "einem öffentlichen Server und holt geteilte Artikel von ihrer eigenen Website, "
            "wie ein Browser. **Mit iCloud synchronisieren** ist optional und legt dein "
            "Regal als einfache Textdateien in dein eigenes iCloud Drive. "
            "[Datenschutzerklärung](privacy).",
        ]),
    ],
    "guide": {
        "slug": "artikel-und-buecher-anhoeren",
        "title": "So hörst du Artikel, PDFs und EPUB-Bücher auf dem iPhone",
        "description": "Schritt für Schritt: einen Artikel aus Safari teilen, ein PDF oder "
                       "EPUB öffnen, beliebigen Text einsetzen und ihn dir von Aloud mit "
                       "einer natürlichen Stimme vorlesen lassen, auf dem iPhone erzeugt, "
                       "in deinem Tempo, offline.",
        "lead": "Aloud liest alles vor, was du lesen kannst: einen Artikel, ein PDF, ein "
                "EPUB-Buch oder Text, den du einsetzt. Die Stimme entsteht auf deinem "
                "iPhone, deshalb funktioniert sie offline, und nichts wird hochgeladen. So "
                "bekommst du jede Art von Text in die App und hörst ihn dir an.",
        "choose": [
            ("Artikel", "Aus Safari oder jeder App teilen"),
            ("PDFs und EPUBs", "Aus „Dateien“ öffnen"),
            ("Jeder Text", "Einsetzen"),
        ],
        "steps": [
            ("Aloud installieren",
             "Lade [Aloud aus dem App Store](store). Die App läuft auf iPhone und iPad ab "
             "iOS 17. Beim ersten Abspielen wird die Stimme einmal geladen. Danach "
             "funktioniert sie offline."),
            ("Einen Artikel teilen",
             "Öffne den Artikel in Safari oder einer anderen App, tippe auf **Teilen** und "
             "dann auf **Aloud**. Der Artikel landet ohne Menüs, Werbung und Kommentare im "
             "Regal. Aus Safari liest Aloud die Seite so, wie du sie siehst, also auch "
             "Artikel, bei denen du angemeldet bist."),
            ("Ein PDF oder EPUB öffnen",
             "Tippe in Aloud auf **+** › **Datei importieren** und wähle die Datei, oder "
             "teile sie aus der App „Dateien“ mit Aloud. Eingescannte PDFs werden auf dem "
             "Gerät erkannt. EPUB-Bücher behalten ihr Cover und ihre Kapitel."),
            ("Beliebigen Text einsetzen",
             "Tippe auf **+** › **Text einsetzen** für Notizen, E-Mails oder alles, was du "
             "kopiert hast. **Link einsetzen** nimmt eine Webadresse."),
            ("Abspielen",
             "Öffne einen Text und tippe auf Wiedergabe. Der Satz, der gerade gelesen wird, "
             "ist hervorgehoben, der Rest bleibt blass. Halte die Leiste am Rand gedrückt, "
             "um durch den ganzen Text zu springen. In einem Buch tippst du im ••• Menü auf "
             "**Kapitel** und beginnst bei jedem Kapitel."),
            ("Das Tempo wählen",
             "Tippe auf die Tempo-Taste und wähle zwischen 0,5× und 3×. Schalte **Pausen "
             "kürzen** ein, um die Stille zwischen den Sätzen zu verkürzen."),
            ("Das iPhone sperren",
             "Aloud liest bei gesperrtem Bildschirm weiter. Nutze die Steuerung auf dem "
             "Sperrbildschirm oder an den AirPods und stell den **Sleeptimer**, wenn du im "
             "Bett hörst: Am Ende blendet die Stimme leise aus."),
            ("Übersetzen, wenn du willst",
             "Ab iOS 18 tippst du auf die Übersetzen-Taste und wählst eine Sprache unter "
             "**Übersetzen in**. Jeder Satz erscheint mit seiner Übersetzung, und "
             "**Übersetzung vorlesen** wechselt die Stimme in die andere Sprache."),
        ],
        "tips": [
            ("Deine Stelle bleibt gemerkt",
             "Jeder Text merkt sich, wo du aufgehört hast. Du kannst zwischen Artikel und "
             "Buch wechseln und kommst zum selben Satz zurück."),
            ("Lesemodus",
             "Tippe auf die Brillen-Taste, um den Player auszublenden und selbst zu lesen, "
             "mit Schrift, Größe und Papier nach Wahl unter **Darstellung**."),
            ("Deine Leseliste",
             "Gespeicherte Links aus Pocket, Instapaper, Raindrop oder Browser-Lesezeichen "
             "kommen über **Einstellungen** › **Aus einer Datei importieren** in die App."),
            ("Kostenlos testen",
             "Im kostenlosen Regal haben drei Texte Platz. Ein einziger Kauf hebt das Limit "
             "auf, und es gibt kein Abo."),
        ],
        "updated": "Geschrieben für Aloud 3.2, Oktober 2026.",
        "cta_title": "Hör dir deine Leseliste an",
        "cta_text": "Aloud liest Artikel, PDFs und EPUB-Bücher mit einer natürlichen Stimme "
                    "vor, die auf deinem iPhone entsteht. Offline. Einmal zahlen, kein Abo.",
    },
}
