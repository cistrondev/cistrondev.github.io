# Pedometer in German ("du", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# App words from Shared/Localizable.xcstrings (Verbinden, Gehen, Laufen, Gehen
# und Laufen, Tagesziele, Pedometer unterstützen); iOS words are Apple's German.
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "de.py"))["L"]["ui"]

L = {
    "name": "Deutsch",
    "path": "de/",
    "og_locale": "de_DE",
    "ui": {**_ui, "summary": "Widgets für den Sperrbildschirm"},
    "page": {
        "shots_dir": "de",
        "tagline": "Deine Schritte auf dem Sperrbildschirm.",
        "pricing": "Kostenlos",
        "intro": (
            "Schritte, Strecke und Stockwerke, als klare Zahlen und Diagramme.",
            "Pedometer liest Apple Health und zeigt die heutigen Werte auf deinem "
            "Sperrbildschirm und Home-Bildschirm. Dein iPhone zählt deine Schritte selbst, "
            "und wenn du eine Apple Watch trägst, zählen ihre Schritte mit.",
        ),
        "features": [
            ("Heute",
             "Deine Schritte neben deinem Ziel, mit dem, was noch fehlt. Strecke und "
             "Stockwerke neben ihren Zielen, dazu Aktivitätsenergie und Gehtempo."),
            ("Gehen und Laufen",
             "Zeichne einen Spaziergang oder Lauf per GPS auf: deine Route auf der Karte, "
             "mit Tempo oder Pace, Höhe, Anstieg und Kalorien. Jeder wird mit Route in "
             "Apple Health gesichert."),
            ("Herzfrequenz live",
             "Mit AirPods Pro 3, Powerbeats Pro 2 oder einem Bluetooth-Brustgurt siehst du "
             "deine Herzfrequenz live beim Gehen und Laufen (iOS 26)."),
            ("Auf dem Sperrbildschirm",
             "Unterwegs bleiben Zeit, Strecke, Tempo, Herzfrequenz und Kalorien auf dem "
             "Sperrbildschirm, mit einer Pausetaste."),
            ("Einen Spaziergang teilen",
             "Ein Bild von jedem Spaziergang oder Lauf, mit der Karte und deinen Werten, "
             "für jede App."),
            ("Deine eigenen Ziele",
             "Lege ein Tagesziel für Schritte, Strecke und Stockwerke fest. Sie beginnen "
             "bei 10.000 Schritten, 8 km und 10 Stockwerken."),
            ("Verlauf",
             "Ein Diagramm pro Wert für die letzte Woche, den letzten Monat oder das letzte "
             "Jahr, mit Tagesdurchschnitt und Vergleich zum Zeitraum davor."),
            ("Widgets für den Sperrbildschirm",
             "Schritte und Strecke, jeweils in einem Ring, der sich bei deinem Ziel "
             "schließt, und Stockwerke mit einer Figur, die eine Treppe hinaufsteigt."),
            ("Widget für den Home-Bildschirm",
             "Dieselbe Karte wie in der App, klein, mittelgroß oder groß. Hell, dunkel oder "
             "automatisch, und auf Wunsch nur mit den Schritten."),
            ("Pro Stunde",
             "Die heutigen Schritte Stunde für Stunde, neben deinem üblichen Tag der "
             "letzten vier Wochen."),
            ("Rekorde",
             "Summen für jeden Monat und jedes Jahr, und deine besten Tage, Wochen und "
             "Monate für Schritte, Stockwerke und Gehtempo."),
            ("Deine Farbe",
             "Graphit, Blau, Grün, Orange, Pink oder Lila für die Zielbalken, die "
             "Diagramme und das Widget."),
        ],
        "privacy_title": "Nichts verlässt dein iPhone.",
        "privacy": [
            "Liest Apple Health und schreibt nur die Spaziergänge und Läufe hinein, die du "
            "aufzeichnest.",
            "Dein Standort wird nur während einer Aufzeichnung verwendet und bleibt auf "
            "deinem iPhone.",
            "Alles wird auf deinem iPhone gezählt und gespeichert. Nichts wird hochgeladen.",
            "Kein Konto, keine Analyse, kein Tracking.",
        ],
        "note": "Pedometer ist kein Medizinprodukt und gibt keine medizinischen Ratschläge.",
        "shots": [
            "Schritte auf dem Sperrbildschirm: ein Schrittzähler-Widget, daneben Strecke und Treppen.",
            "Jeder Schritt zählt: liest Apple Health, Schritte der Apple Watch zählen mit.",
            "Gehen und Laufen auf der Karte: Tempo, Höhe, Kalorien und Herzfrequenz.",
            "Live verfolgen, danach teilen: der Sperrbildschirm unterwegs, ein Bild danach.",
            "Auch auf dem Home-Bildschirm: dieselbe Karte, klein oder mittelgroß.",
            "Dein Tag, Stunde für Stunde: die heutigen Schritte neben einem üblichen Tag.",
            "Dein bester Tag, Woche und Monat: Summen für jeden Monat und jedes Jahr.",
            "Wähle deine Farbe: sechs Farben für Zielbalken, Diagramme und Widget.",
            "Deine Woche auf einen Blick: Tagesbalken, Durchschnitt und Veränderung.",
            "Nichts verlässt dein iPhone: kein Konto, kein Tracking.",
        ],
    },
    "guide_link": "So bringst du einen Schrittzähler auf den Sperrbildschirm deines iPhones",
    "faq": [
        ("Gibt es einen kostenlosen Schrittzähler fürs iPhone ohne Abo?", [
            "Pedometer ist kostenlos, ohne Abo und ohne Konto. Die App zeigt Schritte, "
            "Strecke und Stockwerke als klare Zahlen und Diagramme und legt sie als Widgets "
            "auf den Sperrbildschirm und den Home-Bildschirm. Sie zeichnet auch Spaziergänge "
            "und Läufe per GPS auf. Eine optionale Trinkgeldkasse schaltet nichts frei. "
            "[Im App Store ansehen](store).",
        ]),
        ("Wie zeige ich meine Schritte auf dem Sperrbildschirm des iPhones?", [
            [
                "Lade Pedometer, öffne die App und tippe auf **Verbinden**, damit sie Apple "
                "Health lesen darf.",
                "Halte den Sperrbildschirm gedrückt, tippe auf **Anpassen** und wähle den "
                "Sperrbildschirm.",
                "Tippe auf den Bereich für Widgets unter der Uhr, wähle **Pedometer** und "
                "füge Schritte, Strecke oder Treppensteigen hinzu.",
                "Tippe auf **Fertig**.",
            ],
            "Die Widgets für Schritte und Strecke stehen in einem Ring, der sich bei deinem "
            "Ziel schließt. [Schritt-für-Schritt-Anleitung](guide).",
        ]),
        ("Brauche ich eine Apple Watch?", [
            "Nein. Dein iPhone zählt deine Schritte selbst, wenn du es bei dir trägst. Wenn "
            "du auch eine Apple Watch trägst, liest Pedometer Apple Health, das die Schritte "
            "beider Geräte zusammenführt, ohne sie doppelt zu zählen.",
        ]),
        ("Kann die App Spaziergänge und Läufe per GPS aufzeichnen?", [
            "Ja. Tippe unter **Gehen und Laufen** auf **Gehen** oder **Laufen**. Die Karte "
            "zeichnet deine Route und zeigt Zeit, Strecke, Tempo oder Pace, Kalorien, Höhe "
            "und Anstieg. Unterwegs bleiben die Werte auf dem Sperrbildschirm, mit einer "
            "Pausetaste. Jeder Spaziergang wird mit Route in Apple Health gesichert, und du "
            "kannst ein Bild davon teilen.",
        ]),
        ("Kann sie meine Herzfrequenz ohne Apple Watch zeigen?", [
            "Ja, mit iOS 26. Mit AirPods Pro 3, Powerbeats Pro 2 oder einem "
            "Bluetooth-Brustgurt siehst du deine Herzfrequenz live beim Gehen und Laufen.",
        ]),
        ("Kann ich mein tägliches Schrittziel ändern?", [
            "Ja. Unter **Tagesziele** legst du Ziele für Schritte, Strecke und Stockwerke "
            "fest. Sie beginnen bei 10.000 Schritten, 8 km und 10 Stockwerken. Die Ringe "
            "der Widgets schließen sich bei deinen Zielen.",
        ]),
        ("Ist Pedometer wirklich kostenlos?", [
            "Ja. Alle Funktionen sind kostenlos, und es gibt kein Abo. Unter "
            "**Einstellungen** › **Pedometer unterstützen** kannst du ein Trinkgeld geben, "
            "wenn du möchtest. Es ist freiwillig und schaltet nichts frei.",
        ]),
        ("Lädt Pedometer meine Gesundheitsdaten hoch?", [
            "Nein. Alles wird auf deinem iPhone gezählt und gespeichert, nichts wird "
            "hochgeladen. Pedometer liest Apple Health und schreibt nur die Spaziergänge und "
            "Läufe hinein, die du aufzeichnest. Dein Standort wird nur während einer "
            "Aufzeichnung verwendet. Kein Konto, keine Analyse, kein Tracking. "
            "[Datenschutzerklärung (auf Englisch)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "schrittzaehler-sperrbildschirm",
        "title": "So bringst du einen Schrittzähler auf den Sperrbildschirm deines iPhones",
        "description": "Schritt für Schritt: ein kostenloses Schrittzähler-Widget auf den "
                       "Sperrbildschirm und den Home-Bildschirm des iPhones legen, mit "
                       "Strecke und Stockwerken daneben. Ohne Apple Watch und ohne Abo.",
        "lead": "Dein iPhone zählt deine Schritte schon. Pedometer zeigt die Zahl auf dem "
                "Sperrbildschirm, sodass du sie bei jedem Blick aufs Handy siehst. Das "
                "dauert etwa eine Minute, und du brauchst keine Apple Watch.",
        "choose": [
            ("Schritte", "In einem Ring, der sich beim Ziel schließt"),
            ("Strecke", "In einem Ring, in km oder Meilen"),
            ("Treppensteigen", "Eine Figur steigt eine Treppe hinauf"),
        ],
        "steps": [
            ("Pedometer laden",
             "Lade [Pedometer im App Store](store). Die App ist kostenlos und braucht kein "
             "Konto."),
            ("Apple Health verbinden",
             "Öffne Pedometer und tippe auf **Verbinden**. Erlaube das Lesen von Schritten, "
             "Strecke und Stockwerken. Dein iPhone hat sie die ganze Zeit gezählt, deshalb "
             "ist dein Verlauf sofort da."),
            ("Ziele festlegen",
             "Wähle unter **Tagesziele** ein Ziel für Schritte, Strecke und Stockwerke. Die "
             "Ringe der Widgets schließen sich, wenn du es erreichst."),
            ("Den Sperrbildschirm bearbeiten",
             "Sperre dein iPhone, wecke es, und halte dann den Sperrbildschirm gedrückt. "
             "Tippe auf **Anpassen** und wähle den Sperrbildschirm."),
            ("Das Widget hinzufügen",
             "Tippe auf den Bereich für Widgets unter der Uhr. Suche **Pedometer** in der "
             "Liste und tippe auf Schritte, Strecke oder Treppensteigen. Du kannst mehrere "
             "hinzufügen."),
            ("Auf Fertig tippen",
             "Deine Schritte stehen jetzt auf dem Sperrbildschirm und werden über den Tag "
             "aktualisiert."),
            ("Auch auf den Home-Bildschirm",
             "Halte eine freie Stelle des Home-Bildschirms gedrückt, tippe auf "
             "**Bearbeiten** und dann auf **Widget hinzufügen**. Suche Pedometer und wähle "
             "klein, mittelgroß oder groß. Das große Widget zeigt dazu den Tag Stunde für "
             "Stunde."),
        ],
        "tips": [
            ("Hell, dunkel oder nur Schritte",
             "Halte das Widget auf dem Home-Bildschirm gedrückt und wähle **Widget "
             "bearbeiten**, um es hell oder dunkel zu machen oder nur die Schritte zu zeigen."),
            ("Eine Farbe wählen",
             "Graphit, Blau, Grün, Orange, Pink oder Lila, für die Zielbalken, die "
             "Diagramme und das Widget."),
            ("Unterwegs?",
             "Tippe in der App auf **Gehen** oder **Laufen**, um deine Route per GPS "
             "aufzuzeichnen. Die Werte bleiben unterwegs auf dem Sperrbildschirm."),
            ("Nichts verlässt dein iPhone",
             "Pedometer hat kein Konto und lädt nichts hoch. Die App liest Apple Health auf "
             "deinem iPhone."),
        ],
        "updated": "Geschrieben für Pedometer 1.5 unter iOS 26, Oktober 2026.",
        "cta_title": "Deine Schritte auf einen Blick",
        "cta_text": "Ein kostenloser Schrittzähler für Sperrbildschirm und Home-Bildschirm, "
                    "mit Spaziergängen und Läufen auf der Karte. Kein Konto, kein Abo.",
    },
}
