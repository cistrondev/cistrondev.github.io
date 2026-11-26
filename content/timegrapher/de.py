# Timegrapher in German ("Sie", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# Button names are the app's German strings (Timegrapher Localizable.xcstrings):
# Uhr hinzufügen, Messen, In Lagen messen, Magnetismus prüfen, Gang per Foto,
# Hebungswinkel, Anhand des Fotos erkennen, Ratgeber (tab); for quartz watches
# Typ > Quarz, Anzeige > Zeiger | Digital, and Erneut lesen (reading screen);
# Atomuhr (clock tab) and Datum und Mondphase (the setting card on that tab).
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
            ("Gang, Amplitude, Abfallfehler",
             "Sekunden Vor- oder Nachgang pro Tag, wie weit die Unruh ausschwingt, und die "
             "Symmetrie von Tic und Tac. Halbschwingungen von 18.000 bis 36.000 A/h werden "
             "automatisch erkannt."),
            ("Werte, die ruhig stehen",
             "Die App verfolgt den Geräuschpegel des Raumes und verwirft Störgeräusche. Die "
             "Amplitude kommt aus dem Hebungswinkel Ihres Kalibers, einstellbar auf ein "
             "Zehntelgrad."),
            ("In Lagen messen",
             "Die App führt Sie durch sechs Lagen, oder vier für eine schnellere Prüfung, "
             "und zeigt die mittlere Gangabweichung und die Lagendifferenz, so wie ein "
             "Uhrmacher ein Werk prüft."),
            ("Ihre Sammlung",
             "Jede Uhr mit Referenz, Werk, Hebungswinkel und bis zu 13 Fotos. Jede Messung "
             "wird gespeichert und als Diagramm gezeigt, und eine Erinnerung sagt Ihnen, "
             "wann Sie wieder messen sollten. „Anhand des Fotos erkennen“ schlägt Marke und "
             "Modell vor."),
            ("Genauigkeit aus zwei Fotos",
             "Fotografieren Sie das Zifferblatt heute und morgen. Timegrapher vergleicht "
             "die Fotos mit der Uhr des iPhones und zeigt, wie die Uhr am Handgelenk lief. "
             "Auch Quarzuhren lassen sich so messen: Mit Fotos im Abstand von ein bis zwei "
             "Wochen sehen Sie, wie viele Sekunden pro Monat sie vor- oder nachgehen. "
             "Bei einer Digitaluhr liest Timegrapher die Uhrzeit auf der Anzeige ab, und "
             "Sie prüfen sie."),
            ("Gangbericht",
             "Teilen Sie einen einseitigen Bericht zu einer Uhr als PDF oder Bild, mit der "
             "letzten Messung, den Lagen und dem Verlauf. Ihre Messungen lassen sich als "
             "CSV-Datei exportieren."),
            ("Wissen, was sie wert ist",
             "Aktuelle Chrono24-Angebotspreise für Ihre genaue Referenz, mit dem Median, "
             "auf Ihrem iPhone berechnet."),
            ("Magnetismus-Prüfung",
             "Eine magnetisierte Unruhspirale ist der häufigste Grund, warum eine Uhr "
             "plötzlich vorgeht. Das Magnetometer des iPhones zeigt, ob Ihre Uhr "
             "entmagnetisiert werden muss."),
            ("Atomuhr, Datum und Mondphase",
             "Der Tab „Atomuhr“ zeigt die genaue Zeit von Apples Zeitserver und wie weit "
             "die Uhr Ihres iPhones abweicht. Countdown-Töne vor jeder Minute helfen, Ihre "
             "Uhr auf die Sekunde zu stellen. Das Zifferblatt zeigt außerdem Wochentag, "
             "Datum, Monat und Mondphase, und der Tab erklärt, wie Sie eine Kalender- "
             "oder Mondphasenuhr stellen."),
        ],
        "privacy_title": "Der Ton wird nie aufgezeichnet.",
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
            "Uhrzeit, Datum und Mondphase: alles, um eine Kalender- oder Mondphasenuhr zu stellen.",
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
            "hängen nicht davon ab. In Timegrapher stellen Sie ihn auf ein Zehntelgrad "
            "genau ein.",
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
        ("Funktioniert die App mit Quarz- und Digitaluhren?", [
            "Ja, über Fotos. Eine Quarzuhr geht nach einem Quarzkristall und bewegt den "
            "Sekundenzeiger einmal pro Sekunde, es gibt also keine Unruh, die das Mikrofon "
            "abhören könnte. Stellen Sie beim Anlegen der Uhr den **Typ** auf **Quarz**. "
            "Auf der Seite der Uhr fotografieren Sie dann mit **Gang per Foto** das "
            "Zifferblatt und in ein bis zwei Wochen noch einmal. Timegrapher zeigt, wie "
            "viele Sekunden pro Monat die Uhr vor- oder nachgeht.",
            "Fotos mit zwei Wochen Abstand sind auf weniger als eine Sekunde pro Monat "
            "genau. Lassen Sie zwischen den Fotos weniger als drei Wochen, denn eine "
            "Abweichung um eine ganze Minute kann ein Sekundenzeiger nicht zeigen. Eine Uhr "
            "mit Zeigern braucht einen Sekundenzeiger.",
            "Auch eine Digitaluhr lässt sich messen, wenn sie die Sekunden anzeigt. Stellen "
            "Sie zusätzlich die **Anzeige** auf **Digital**. Timegrapher liest die Uhrzeit "
            "aus jedem Foto, direkt auf Ihrem iPhone. Vergleichen Sie die Ziffern mit dem "
            "Foto und korrigieren Sie, was nicht stimmt, oder zoomen Sie die Uhrzeit heran "
            "und tippen Sie auf **Erneut lesen**. Die Anzeige zeigt die volle Uhrzeit, "
            "deshalb können zwischen den Fotos Wochen oder sogar Monate liegen. Je länger "
            "Sie warten, desto genauer ist das Ergebnis. Bei jeder Quarzuhr wird ein "
            "Ergebnis aus Fotos mit weniger als einem Tag Abstand angezeigt, aber nicht "
            "gespeichert.",
        ]),
        ("Wie stelle ich mit Timegrapher Datum und Mondphase meiner Uhr ein?", [
            "Öffnen Sie den Tab **Atomuhr**. Sein Zifferblatt zeigt neben der genauen "
            "Uhrzeit Wochentag, Datum, Monat und Mondphase. Unter dem Zifferblatt "
            "steht, wie viele Tage seit dem letzten Voll- oder Neumond vergangen sind.",
            "Der Abschnitt **Datum und Mondphase** im selben Tab nennt die Schritte "
            "für heute. Stellen Sie zuerst das Datum ein, denn bei manchen Uhren "
            "bewegt die Datumskorrektur auch den Mond. Stellen Sie dann den Mond auf "
            "Voll- oder Neumond, je nachdem, welcher zuletzt war, und schalten Sie ihn "
            "für jeden seither vergangenen Tag um einen Schritt weiter. Verstellen Sie "
            "das Datum nicht zwischen etwa 20 und 4 Uhr, denn dann ist das "
            "Datumsschaltwerk in Bewegung.",
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
        ("In welchen Sprachen gibt es Timegrapher?", [
            "Timegrapher gibt es auf Deutsch, Englisch, Spanisch, Französisch, "
            "brasilianischem Portugiesisch und Japanisch sowie auf vereinfachtem und "
            "traditionellem Chinesisch.",
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
             "auseinander, und zeigt, wie die Uhr beim Tragen lief. Bei einer Quarzuhr "
             "liegen ein bis zwei Wochen zwischen den Fotos. Bei einer Digitaluhr sollte "
             "mindestens eine Woche dazwischen liegen. Timegrapher liest die Uhrzeit aus "
             "jedem Foto."),
            ("Uhrzeit, Datum und Mond stellen",
             "Der Tab **Atomuhr** zeigt die genaue Uhrzeit, mit Countdown-Tönen vor "
             "jeder Minute. Das Zifferblatt zeigt außerdem Wochentag, Datum, Monat und "
             "Mondphase, und der Abschnitt **Datum und Mondphase** erklärt, wie Sie "
             "diese an Ihrer Uhr einstellen."),
            ("Was sie wert ist",
             "Die Preisabfrage holt aktuelle Chrono24-Angebotspreise für Ihre genaue "
             "Referenz und speichert den Median."),
            ("Einmal zahlen",
             "Die erste Uhr ist kostenlos. Timegrapher Pro schaltet unbegrenzt viele Uhren "
             "mit einer einzigen Zahlung frei, ohne Abo."),
        ],
        "updated": "Geschrieben für Timegrapher 2.14, November 2026.",
        "cta_title": "Messen Sie Ihre Uhr noch heute",
        "cta_text": "Gangabweichung, Amplitude und Abfallfehler in 30 Sekunden, mit dem "
                    "iPhone, das Sie schon haben. Erste Uhr kostenlos, kein Abo.",
    },
}
