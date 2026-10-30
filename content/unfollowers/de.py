# Unfollowers in German ("du", as in the App Store text). Keys are explained in en.py.
# Instagram's German name for the "Followers and following" category could not be
# checked, so the guide describes it in plain words.

L = {
    "name": "Deutsch",
    "path": "de/",
    "og_locale": "de_DE",
    "ui": {
        "nav_apps": "Apps",
        "nav_privacy": "Datenschutz",
        "nav_about": "",   # no room on phones
        "nav_contact": "Kontakt",
        "trademark": "Instagram und Facebook sind Marken der Meta Platforms, Inc. Unfollowers "
                     "und Unfriended sind unabhängige Apps. Sie sind nicht mit Meta verbunden "
                     "und werden von Meta weder unterstützt noch gesponsert.",
        "rights": "Alle Rechte vorbehalten.",
        "overview": "Info",
        "privacy": "Datenschutz",
        "view_on_store": "Im App Store ansehen",
        "platform": "iPhone · iOS 17 oder neuer",
        "screenshots": "Bildschirmfotos",
        "prev": "Vorherige Bildschirmfotos",
        "next": "Nächste Bildschirmfotos",
        "privacy_eyebrow": "Datenschutz",
        "read_policy": "Datenschutzerklärung lesen (auf Englisch)",
        "more_apps": "Weitere Apps",
        "languages": "Sprachen",
        "faq": "Häufige Fragen",
        "summary": "Was du auswählst",
        "tips": "Gut zu wissen",
        "cta_more": "Mehr über {name}",
        "ratings": ("{n} Bewertung im App Store", "{n} Bewertungen im App Store"),
        "out_of_5": " von 5",
        "decimal": ",",
    },
    "page": {
        "shots_dir": "de",
        "tagline": "Sieh, wer dir auf Instagram entfolgt ist. Ohne Login.",
        "pricing": "Kostenlos · Einmalig freischalten",
        "intro": (
            "Instagram sagt dir nicht, wer dir entfolgt ist. Dein eigener Datenexport schon.",
            "Unfollowers liest den offiziellen Export, den du selbst bei Instagram "
            "herunterlädst, und zeigt dir, was sich geändert hat. Die App fragt nie nach "
            "deinem Passwort.",
        ),
        "features": [
            ("Wer dir entfolgt ist",
             "Von Import zu Import verfolgt, mit dem Datum, an dem jede Änderung gefunden "
             "wurde."),
            ("Hat dich wohl blockiert",
             "Konten, die gleichzeitig aus deinen Followern und deinen Gefolgt-Konten "
             "verschwunden sind. Die App markiert sie als wahrscheinliche Blockierung."),
            ("Wer dir nicht zurückfolgt",
             "Die klassische Liste, dazu Mutuals und Follow-Anfragen, die nie angenommen "
             "wurden."),
            ("Mit wem du am meisten interagierst",
             "Deine Likes, Kommentare und Story-Reaktionen, gezählt aus deinem eigenen Export."),
            ("Deine Historie als Diagramm",
             "Wachstums- und Follow-back-Diagramme aus jedem Export, den du importierst."),
            ("Kein Login",
             "Die App hat keinen Anmeldebildschirm. Dein Passwort bleibt bei dir."),
        ],
        "privacy_title": "Dein Export bleibt auf deinem iPhone.",
        "privacy": [
            "Dein Instagram-Export wird nur auf deinem iPhone gelesen und gespeichert.",
            "Kein Konto, keine Analytics, keine Werbung, kein Tracking.",
            "Um zu prüfen, ob ein Konto noch existiert, schickt die App nur diesen "
            "Benutzernamen an Instagram, ohne Anmeldung.",
        ],
        "note": "Unfollowers ist eine unabhängige App und nicht mit Instagram oder Meta verbunden.",
        "stats": [],
        "reviews": [],
        "why": (
            "Dein Passwort bleibt bei dir.",
            "Die meisten Follower-Tracker fragen nach deinem Instagram-Passwort und nutzen "
            "dann dein Konto im Hintergrund. Instagram warnt, dass nicht autorisierte Apps in "
            "deinem Konto ein Risiko sind. Wer solche Apps oft nutzt, berichtet von "
            "gesperrten oder vorübergehend deaktivierten Konten und blockierten Aktionen. "
            "Unfollowers fragt nie nach deinem Passwort und meldet sich nie in deinem Konto "
            "an. Die App liest den Datenexport, den dir Instagram selbst gibt. Und es gibt "
            "kein Abo: ein einziger optionaler Kauf schaltet alles frei.",
        ),
        "shots": [
            "Jeder Entfolger auf einen Blick: wer gegangen ist und wann, aus deinem eigenen "
            "Instagram-Datenexport.",
            "Hat dich wohl blockiert: Konten, die gleichzeitig aus deinen Followern und "
            "Gefolgt-Konten verschwunden sind.",
            "Sie folgen dir nicht zurück: durchsuchen, sortieren und jedes Profil öffnen.",
            "Wen du am meisten hypst: deine Likes, Kommentare und Story-Reaktionen, gezählt.",
            "Deine Stats als Charts: Wachstum und Follow-back aus deiner eigenen Historie.",
        ],
    },
    "guide_link": "So lädst du deine Instagram-Daten herunter",
    "faq": [
        ("Wie sehe ich, wer mir auf Instagram entfolgt ist?", [
            "Instagram zeigt nicht, wer dir entfolgt ist. Dein Instagram-Datenexport enthält "
            "alle, die dir an dem Tag folgen, an dem du ihn herunterlädst. Unfollowers "
            "vergleicht zwei solcher Exporte und zeigt dir, wer gegangen ist.",
            [
                "Lade deinen Datenexport bei Instagram herunter, mit deinen Followern und "
                "Gefolgt-Konten im JSON-Format. [So geht es](guide).",
                "Importiere die ZIP-Datei in Unfollowers. Du siehst sofort, wer dir nicht "
                "zurückfolgt.",
                "Ein paar Wochen später lädst du einen neuen Export herunter und importierst "
                "ihn auch. Unfollowers zeigt dir, wer dir seit dem ersten entfolgt ist, mit "
                "dem Datum, an dem jede Änderung gefunden wurde.",
            ],
            "Jeder neue Export, den du importierst, erweitert deine Historie.",
        ]),
        ("Gibt es einen sicheren Unfollow-Tracker ohne Login?", [
            "Unfollowers funktioniert ohne Login. Die App fragt nie nach deinem "
            "Instagram-Passwort und meldet sich nie in deinem Konto an. Sie liest den "
            "Datenexport, den du selbst bei Instagram herunterlädst.",
            "Viele Follower-Tracker fragen nach deinem Instagram-Passwort und nutzen dann "
            "dein Konto im Hintergrund. Instagram warnt, dass nicht autorisierte Apps in "
            "deinem Konto ein Risiko sind. Mit Unfollowers bleibt dein Passwort bei dir, und "
            "die App führt nie Aktionen in deinem Konto aus.",
            "Die Datei wird auf deinem iPhone gelesen und gespeichert. Kein Konto, keine "
            "Werbung, kein Tracking.",
        ]),
        ("Wie lade ich meinen Instagram-Datenexport herunter?", [
            "Öffne in der Instagram-App dein Profil und tippe auf das Menü. Geh dann zu "
            "Kontenübersicht › Deine Informationen und Berechtigungen › Deine Informationen "
            "exportieren › Export erstellen. Bei manchen Konten heißt die Kontenübersicht "
            "Meta-Konto. Wähle Zu Gerät exportieren. Wähle deine Follower und Gefolgt-Konten, "
            "den gesamten Zeitraum und das Format JSON, und tippe auf Export starten. "
            "Instagram meldet sich, wenn die Datei fertig ist, meist nach wenigen Minuten.",
            "[Die Anleitung Schritt für Schritt](guide).",
        ]),
        ("Kann ich sehen, wer mich auf Instagram blockiert hat?", [
            "Instagram meldet keine Blockierungen, deshalb kann keine App das sicher wissen. "
            "Wenn dich jemand blockiert, verschwindet die Person gleichzeitig aus deinen "
            "Followern und aus deinen Gefolgt-Konten. Unfollowers markiert diese Konten als "
            "wahrscheinliche Blockierung. Das klappt nur bei Leuten, die dir gefolgt sind und "
            "denen du auch gefolgt bist.",
            "Ein gelöschtes, deaktiviertes oder umbenanntes Konto verschwindet genauso. Die "
            "Profilprüfung (der Vibe-Check) fragt bei instagram.com nach, ob jeder "
            "Benutzername noch existiert, und verschiebt verschwundene Konten in eine eigene "
            "Liste.",
        ]),
        ("Ist Unfollowers kostenlos?", [
            "Der Download von Unfollowers ist kostenlos. Die kostenlose Version zeigt, wer "
            "dir nicht zurückfolgt, wem du nicht zurückfolgst und deine Mutuals. Ein "
            "einmaliger Kauf schaltet alles andere frei, auch die Listen, wer dir entfolgt ist "
            "und wer dich wohl blockiert hat. Es gibt kein Abo. Die App läuft auf dem iPhone "
            "mit iOS 17 oder neuer.",
        ]),
        ("Verlässt etwas mein iPhone?", [
            "Deine Exportdatei bleibt auf deinem iPhone. Die App liest und speichert sie dort, "
            "und der Entwickler betreibt keine Server. Die einzige Funktion, die das Internet "
            "nutzt, ist die Profilprüfung. Sie fragt bei instagram.com nach, ob ein Konto "
            "noch existiert, und schickt nur diesen Benutzernamen, ohne Anmeldung. Sie läuft, "
            "wenn du auf den Vibe-Check tippst, und nach dem Freischalten für bis zu 30 neue "
            "Konten nach jedem Import. [Datenschutzerklärung (auf Englisch)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "instagram-daten-herunterladen",
        "title": "So lädst du deine Instagram-Daten herunter (Export als JSON)",
        "description": "Schritt für Schritt auf dem iPhone: exportiere deine "
                       "Instagram-Follower und Gefolgt-Konten im JSON-Format, für den "
                       "gesamten Zeitraum, und sichere die ZIP-Datei. Dann siehst du mit "
                       "Unfollowers, wer dir entfolgt ist.",
        "lead": "Bei Instagram kannst du eine Kopie der Daten deines Kontos herunterladen. "
                "Der Export enthält die vollständigen Listen deiner Follower und der Konten, "
                "denen du folgst. Unfollowers liest diese Datei und zeigt dir, wer dir "
                "entfolgt ist. So bekommst du sie in der Instagram-App auf dem iPhone.",
        "choose": [
            ("Informationen", "Follower und Gefolgt-Konten"),
            ("Zeitraum", "Gesamter Zeitraum"),
            ("Format", "JSON"),
        ],
        "steps": [
            ("Öffne das Menü",
             "Tippe in der Instagram-App unten rechts auf dein Profilbild. Tippe dann oben "
             "rechts auf das Menü (☰)."),
            ("Kontenübersicht",
             "Tippe auf **Kontenübersicht**. Bei manchen Konten heißt sie **Meta-Konto**."),
            ("Deine Informationen",
             "Tippe auf **Deine Informationen und Berechtigungen** und dann auf **Deine "
             "Informationen exportieren**."),
            ("Export erstellen",
             "Tippe auf **Export erstellen**. Wähle dein Instagram-Profil und tippe auf "
             "**Weiter**."),
            ("Zu Gerät exportieren",
             "Wähle **Zu Gerät exportieren**. So wird die Datei auf deinem iPhone gespeichert."),
            ("Wähle die Daten",
             "Auf dem nächsten Bildschirm wählst du die Informationen für den Export. Hake "
             "die Kategorie mit deinen Followern und Gefolgt-Konten an, im Bereich "
             "Verbindungen. Wenn du sehen willst, mit wem du am meisten interagierst, hake "
             "auch Likes, Kommentare und Story-Interaktionen an. Den Rest kannst du abwählen, "
             "damit die Datei klein bleibt."),
            ("Gesamter Zeitraum, JSON",
             "Wähle beim Datumsbereich den gesamten Zeitraum, von Anfang an. Wähle beim "
             "Format **JSON**. Unfollowers kann das HTML-Format nicht lesen."),
            ("Export starten",
             "Tippe auf **Export starten**. Instagram bereitet die Datei vor. Das dauert meist "
             "ein paar Minuten."),
            ("Lade die ZIP-Datei herunter",
             "Instagram benachrichtigt dich, wenn die Datei fertig ist. Geh zurück zu **Deine "
             "Informationen exportieren** und lade die Datei herunter. Instagram fragt "
             "eventuell nach deinem Passwort. Du gibst es in Instagram selbst ein. Sichere die "
             "ZIP-Datei in der Dateien-App."),
            ("Importiere sie in Unfollowers",
             "Öffne Unfollowers, tippe auf den Import-Button und wähle die ZIP-Datei. Du "
             "musst sie nicht entpacken."),
        ],
        "tips": [
            ("Zwei Exporte zeigen, wer gegangen ist",
             "Ein Export enthält deine Follower an einem einzigen Tag. Importiere alle paar "
             "Wochen einen neuen Export. Unfollowers vergleicht sie und zeigt dir, wer seit "
             "dem letzten gegangen ist."),
            ("Die Datei bleibt vier Tage verfügbar",
             "Instagram hält einen fertigen Export vier Tage lang bereit. Danach erstellst du "
             "einen neuen."),
            ("„Keine Follower-Listen gefunden“",
             "Unfollowers zeigt diese Meldung, wenn der Export im HTML-Format ist oder wenn "
             "deine Follower und Gefolgt-Konten nicht angehakt waren. Erstelle einen neuen "
             "Export im JSON-Format mit dieser Kategorie."),
            ("Es kann länger dauern",
             "Die meisten Exporte sind nach wenigen Minuten fertig. Manchmal dauert es länger. "
             "Instagram benachrichtigt dich in der App und per E-Mail, wenn deiner fertig ist."),
        ],
        "updated": "Schritte im Instagram-Hilfebereich geprüft, Oktober 2026.",
        "cta_title": "Sieh, wer dir entfolgt ist",
        "cta_text": "Unfollowers liest diese Datei auf deinem iPhone. Die App zeigt dir, wer "
                    "dir entfolgt ist, wer dich wohl blockiert hat und wer dir nicht "
                    "zurückfolgt. Ohne Login und ohne Passwort.",
    },
}
