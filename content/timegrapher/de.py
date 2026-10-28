# Timegrapher in German ("Sie", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# Button names are the app's German strings (Timegrapher Localizable.xcstrings):
# Uhr hinzufügen, Messen, In Lagen messen, Magnetismus prüfen, Gang per Foto,
# Hebungswinkel, Anhand des Fotos erkennen, Ratgeber (tab).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "de.py"))["L"]["ui"]

L = {
    "name": "Deutsch",
    "path": "de/",
    "og_locale": "de_DE",
    "ui": {
        **_ui,
        "summary": "Auf einen Blick",
        "what_people_say": "Was andere sagen.",
    },
    "page": {
        "shots_dir": "de",
        "tagline": "Die Zeitwaage eines Uhrmachers, in Ihrem iPhone.",
        "pricing": "Erste Uhr kostenlos · Pro einmalig freischalten",
        "intro": (
            "Gangabweichung, Amplitude und Abfallfehler in etwa dreißig Sekunden.",
            "Timegrapher hört Ihre mechanische Uhr über das Mikrofon des iPhones ab und "
            "verwaltet Ihre ganze Sammlung, jede Messung und den Wert jeder Uhr an einem Ort.",
        ),
        "features": [
            ("Die Werte, die zählen",
             "Sekunden Vor- oder Nachgang pro Tag, wie weit die Unruh ausschwingt, und die "
             "Symmetrie von Tic und Tac. Halbschwingungen von 18.000 bis 36.000 A/h werden "
             "automatisch erkannt."),
            ("Werte, die ruhig stehen",
             "Die App verfolgt den Geräuschpegel des Raumes und verwirft Störgeräusche. Die "
             "Amplitude kommt aus dem Hebungswinkel Ihres Kalibers."),
            ("Ihre Sammlung",
             "Jede Uhr mit Foto, Referenz, Werk und Hebungswinkel. Jede Messung wird "
             "gespeichert und als Diagramm gezeigt. „Anhand des Fotos erkennen“ schlägt "
             "Marke und Modell vor."),
            ("Der Gang über einen Tag am Handgelenk",
             "Fotografieren Sie das Zifferblatt heute und morgen. Timegrapher vergleicht "
             "die Fotos mit der Uhr des iPhones und zeigt, wie die Uhr am Handgelenk lief."),
            ("Wissen, was sie wert ist",
             "Aktuelle Chrono24-Angebotspreise für Ihre genaue Referenz, mit dem Median, "
             "auf Ihrem iPhone berechnet."),
            ("Magnetismus-Prüfung",
             "Eine magnetisierte Unruhspirale ist der häufigste Grund, warum eine Uhr "
             "plötzlich vorgeht. Das Magnetometer des iPhones zeigt, ob Ihre Uhr "
             "entmagnetisiert werden muss."),
        ],
        "privacy_title": "Nichts aufgezeichnet. Nichts gespeichert.",
        "privacy": [
            "Der Ton des Mikrofons wird live ausgewertet und nie aufgezeichnet oder gespeichert.",
            "Ihre Sammlung und Ihre Messungen liegen nur auf Ihrem iPhone.",
            "Die optionale Preisabfrage sucht die Referenz Ihrer Uhr auf Chrono24.",
            "„Anhand des Fotos erkennen“ schickt das Foto nur auf Ihr Tippen an Apples "
            "Private Cloud Compute. Apple behält es nicht, und der Entwickler sieht es nie.",
            "Der Tab „Atomuhr“ holt die Uhrzeit von Apples Zeitserver. Die Anfrage enthält "
            "keine persönlichen Daten.",
        ],
        "note": "",
        "reviews": [],
        "shots": [
            "Ihr iPhone ist eine Zeitwaage: Gangabweichung, Amplitude und Abfallfehler in 30 Sekunden.",
            "Werte, die ruhig stehen: auch leise Uhrwerke, auch in lauten Räumen.",
            "Ihre Sammlung an einem Ort: Alter, Zustand und Wert jeder Uhr.",
            "Die Drift sehen, bevor sie zählt: jede Messung gespeichert, als Diagramm.",
            "Wissen, was sie wert ist: der Chrono24-Median für Ihre genaue Referenz.",
            "Ist Ihre Uhr magnetisiert? In zehn Sekunden geprüft.",
            "Der Gang über einen Tag am Handgelenk: zwei Fotos, einen Tag auseinander.",
        ],
    },
    "guide_link": "So prüfen Sie die Ganggenauigkeit Ihrer mechanischen Uhr mit dem iPhone",
    "faq": [
        ("Kann ein iPhone messen, wie genau meine mechanische Uhr geht?", [
            "Ja. Timegrapher hört die Uhr über das eingebaute Mikrofon des iPhones ab und "
            "arbeitet wie die Zeitwaage eines Uhrmachers. In etwa 30 Sekunden zeigt die App "
            "die Gangabweichung (Sekunden Vor- oder Nachgang pro Tag), die Amplitude (wie "
            "weit die Unruh ausschwingt) und den Abfallfehler (den Unterschied zwischen Tic "
            "und Tac).",
            "Das funktioniert mit Automatik- und Handaufzugsuhren. Die erste Uhr ist "
            "kostenlos, und es gibt kein Abo. [Im App Store ansehen](store).",
        ]),
        ("Wie messe ich meine Uhr mit Timegrapher?", [
            [
                "Ziehen Sie die Uhr auf und suchen Sie sich einen ruhigen Ort.",
                "Tippen Sie auf **Uhr hinzufügen** und tragen Sie das Werk und, falls "
                "bekannt, seinen Hebungswinkel ein.",
                "Tippen Sie auf **Messen** und legen Sie die Unterkante des iPhones fest auf "
                "die Uhr, am besten auf das Glas.",
                "Halten Sie still. Die Messung stoppt bei 0:30 von selbst und zeigt "
                "Gangabweichung, Amplitude, Abfallfehler und ein Urteil.",
            ],
            "[Schritt-für-Schritt-Anleitung](guide).",
        ]),
        ("Welche Werte sind gut für Gang, Amplitude und Abfallfehler?", [
            "Nach diesen Bereichen urteilt Timegrapher:",
            [
                "**Gangabweichung:** innerhalb von ±5 Sekunden am Tag liegt im "
                "Chronometerbereich. Bis ±15 ist für den Alltag in Ordnung. Ab ±30 muss die "
                "Uhr reguliert werden.",
                "**Amplitude:** 250° bis 315° ist gesund, bei aufgezogener Uhr und "
                "Zifferblatt oben. Unter 220° ist bald eine Revision fällig, unter 200° sind "
                "die Öle vermutlich verharzt. Über 315° droht die Unruh zu prellen.",
                "**Abfallfehler:** unter 0,3 ms ist gut im Abfall. Ab 0,8 ms lohnt sich eine "
                "Justierung, über 1,5 ms ist die Uhr deutlich außer Abfall.",
            ],
            "Der Gang ändert sich mit der Lage. Notieren Sie also, ob die Uhr mit dem "
            "Zifferblatt nach oben, nach unten oder mit der Krone nach unten lag. **In Lagen "
            "messen** nimmt jede Lage nacheinander auf.",
        ]),
        ("Woran erkenne ich, ob meine Uhr magnetisiert ist?", [
            "Eine magnetisierte Unruhspirale ist der häufigste Grund, warum eine mechanische "
            "Uhr plötzlich vorgeht, oft um Minuten am Tag. Timegrapher prüft das mit dem "
            "Magnetometer des iPhones: Tippen Sie auf **Magnetismus prüfen**, messen Sie das "
            "Hintergrundfeld und halten Sie dann die Uhr an die Rückseite des iPhones. Die "
            "Differenz ist die Antwort.",
            "Nehmen Sie vorher magnetische Hüllen, Wallets oder Halterungen ab. Jede Prüfung "
            "wird gespeichert, sodass ein Vorher-Nachher zeigt, ob das Entmagnetisieren "
            "gewirkt hat.",
        ]),
        ("Welchen Hebungswinkel soll ich eintragen?", [
            "Der Hebungswinkel ist eine Eigenschaft des Werks, und Timegrapher berechnet "
            "damit die Amplitude. Viele Schweizer Werke haben 52°, viele aber auch andere "
            "Werte, also schlagen Sie Ihr Kaliber nach. Ein falscher Hebungswinkel ist der "
            "übliche Grund für falsche Amplituden in Handy-Apps. Gang und Abfallfehler "
            "hängen nicht davon ab.",
        ]),
        ("Wie genau ist eine Zeitwaage auf dem Handy im Vergleich zur Werkstattmaschine?", [
            "Timegrapher misst jedes Tic auf Bruchteile einer Millisekunde und gleicht "
            "Tausende davon gegen die Uhr des iPhones ab, nach demselben Prinzip wie die "
            "Maschine auf dem Werktisch. Ein ruhiger Raum und fester Kontakt geben die "
            "besten Werte. Bluetooth-Kopfhörer komprimieren den Ton, trennen Sie sie also, "
            "damit das Mikrofon des iPhones zuhört.",
            "Die Werte sind Anhaltspunkte. Für Entscheidungen über eine Revision bleiben "
            "eine Werkstattmaschine und das Urteil eines Uhrmachers maßgeblich.",
        ]),
        ("Kann ich prüfen, wie meine Uhr einen ganzen Tag am Handgelenk läuft?", [
            "Ja. **Gang per Foto** vergleicht zwei Fotos des Zifferblatts, die einen Tag "
            "auseinander liegen. Jedes Foto hält die genaue Aufnahmezeit fest, deshalb zeigt "
            "die Stellung des Sekundenzeigers, wie viel die Uhr beim Tragen vor- oder "
            "nachgegangen ist.",
        ]),
        ("Funktioniert die App mit Quarzuhren?", [
            "Nein. Eine Quarzuhr geht nach einem Quarzkristall und bewegt den Zeiger einmal "
            "pro Sekunde, es gibt also keine Unruh, die man abhören könnte. Timegrapher ist "
            "für mechanische Uhren mit Automatik oder Handaufzug.",
        ]),
        ("Ist Timegrapher kostenlos?", [
            "Ihre erste Uhr ist für immer kostenlos, mit allen Messungen. **Timegrapher Pro** "
            "ist ein einmaliger Kauf und hebt die Grenze bei der Zahl der Uhren auf. Es gibt "
            "kein Abo, und Käufe lassen sich auf jedem Gerät mit demselben Apple Account "
            "wiederherstellen.",
        ]),
        ("Nimmt Timegrapher meinen Ton auf?", [
            "Nein. Der Ton wird live ausgewertet und nie aufgezeichnet, gespeichert oder "
            "hochgeladen. Ihre Sammlung bleibt auf Ihrem iPhone. Die optionale Preisabfrage "
            "sucht die Referenz Ihrer Uhr auf Chrono24, und **Anhand des Fotos erkennen** "
            "schickt das eine Foto nur auf Ihr Tippen an Apples Private Cloud Compute. "
            "[Datenschutzerklärung (auf Englisch)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "ganggenauigkeit-pruefen",
        "title": "So prüfen Sie die Ganggenauigkeit Ihrer mechanischen Uhr mit dem iPhone",
        "description": "Schritt für Schritt: Gangabweichung, Amplitude und Abfallfehler "
                       "Ihrer Automatik- oder Handaufzugsuhr mit dem Mikrofon des iPhones "
                       "messen, die Werte lesen und die Uhr auf Magnetismus prüfen.",
        "lead": "Eine Zeitwaage zeigt, wie schnell oder langsam eine mechanische Uhr geht und "
                "wie gesund ihr Werk ist. Timegrapher macht Ihr iPhone mit dem Mikrofon zu "
                "einer Zeitwaage. So bekommen Sie ruhige Werte, und das bedeuten sie.",
        "choose": [
            ("Gangabweichung", "Sekunden Vor- oder Nachgang pro Tag"),
            ("Amplitude", "Wie weit die Unruh ausschwingt"),
            ("Abfallfehler", "Tic gegen Tac, in ms"),
        ],
        "steps": [
            ("Timegrapher laden",
             "Laden Sie [Timegrapher im App Store](store). Ihre erste Uhr ist kostenlos. "
             "Erlauben Sie den Zugriff auf das Mikrofon, wenn die App fragt."),
            ("Die Uhr aufziehen",
             "Ziehen Sie eine Handaufzugsuhr ganz auf, oder tragen Sie eine Automatikuhr "
             "vorher eine Weile. Bei einer fast abgelaufenen Uhr ist die Amplitude niedriger."),
            ("Die Uhr anlegen",
             "Tippen Sie auf **Uhr hinzufügen** und tragen Sie Marke, Referenz und Werk ein. "
             "Stellen Sie den **Hebungswinkel** Ihres Kalibers ein, denn die Amplitude hängt "
             "davon ab. **Anhand des Fotos erkennen** kann Marke und Modell vorschlagen."),
            ("Einen ruhigen Ort suchen",
             "Ein brummender Kühlschrank oder Verkehr kosten Genauigkeit. Trennen Sie "
             "Bluetooth-Kopfhörer, damit das Mikrofon des iPhones zuhört."),
            ("Messen",
             "Tippen Sie auf **Messen** und legen Sie die Unterkante des iPhones fest auf die "
             "Uhr, am besten auf das Glas. Direkter Kontakt überträgt die Ticks viel besser "
             "als Luft. Die Messung stoppt bei 0:30 von selbst."),
            ("Das Ergebnis lesen",
             "Sie sehen die Gangabweichung in Sekunden pro Tag, die Amplitude in Grad, den "
             "Abfallfehler in Millisekunden und die Schlagzahl, dazu ein Urteil von "
             "Ausgezeichnet bis Revision nötig, mit Begründung. Der Tab **Ratgeber** erklärt "
             "jeden Wert."),
            ("Andere Lagen messen",
             "Der Gang ändert sich mit der Lage. **In Lagen messen** misst die Uhr mit dem "
             "Zifferblatt nach oben, nach unten und auf der Kante und zeigt die Streuung."),
            ("Auf Magnetismus prüfen",
             "Geht die Uhr plötzlich stark vor, tippen Sie auf **Magnetismus prüfen**. Das "
             "Magnetometer des iPhones zeigt, ob die Uhr entmagnetisiert werden muss."),
        ],
        "tips": [
            ("Den Verlauf sehen",
             "Jede Messung wird gespeichert und als Diagramm gezeigt. So fällt ein Werk auf, "
             "das langsam nachlässt, bevor es stehen bleibt."),
            ("Ein Tag am Handgelenk",
             "**Gang per Foto** vergleicht zwei Fotos des Zifferblatts, einen Tag "
             "auseinander, und zeigt, wie die Uhr beim Tragen lief."),
            ("Was sie wert ist",
             "Die Preisabfrage holt aktuelle Chrono24-Angebotspreise für Ihre genaue "
             "Referenz und speichert den Median."),
            ("Einmal zahlen",
             "Die erste Uhr ist kostenlos. Timegrapher Pro schaltet unbegrenzt viele Uhren "
             "mit einer einzigen Zahlung frei, ohne Abo."),
        ],
        "updated": "Geschrieben für Timegrapher 2.7, Oktober 2026.",
        "cta_title": "Messen Sie Ihre Uhr noch heute",
        "cta_text": "Gangabweichung, Amplitude und Abfallfehler in 30 Sekunden, mit dem "
                    "iPhone, das Sie schon haben. Erste Uhr kostenlos, kein Abo.",
    },
}
