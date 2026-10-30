# Unfollowers in Dutch ("je", as in the App Store text). Keys are explained in en.py.

L = {
    "name": "Nederlands",
    "path": "nl/",
    "og_locale": "nl_NL",
    "ui": {
        "nav_apps": "Apps",
        "nav_privacy": "Privacy",
        "nav_about": "Over",
        "nav_contact": "Contact",
        "trademark": "Instagram en Facebook zijn handelsmerken van Meta Platforms, Inc. "
                     "Unfollowers en Unfriended zijn onafhankelijke apps en zijn niet gelieerd "
                     "aan, goedgekeurd door of gesponsord door Meta.",
        "rights": "Alle rechten voorbehouden.",
        "overview": "Overzicht",
        "privacy": "Privacy",
        "view_on_store": "Bekijk in de App Store",
        "platform": "iPhone · iOS 17 of nieuwer",
        "screenshots": "Schermafbeeldingen",
        "prev": "Vorige schermafbeeldingen",
        "next": "Volgende schermafbeeldingen",
        "privacy_eyebrow": "Privacy",
        "read_policy": "Lees het privacybeleid (in het Engels)",
        "more_apps": "Meer apps",
        "languages": "Talen",
        "faq": "Veelgestelde vragen",
        "summary": "Wat je kiest",
        "tips": "Goed om te weten",
        "cta_more": "Over {name}",
        "ratings": ("{n} beoordeling in de App Store", "{n} beoordelingen in de App Store"),
        "out_of_5": " van 5",
        "decimal": ",",
    },
    "page": {
        "shots_dir": "nl",
        "tagline": "Zie wie je ontvolgde op Instagram. Zonder login.",
        "pricing": "Gratis · Eenmalig ontgrendelen",
        "intro": (
            "Instagram vertelt je niet wie je ontvolgde. Je eigen data-export wel.",
            "Unfollowers leest de officiële export die je zelf bij Instagram downloadt en "
            "laat zien wat er veranderd is. De app vraagt nooit om je wachtwoord.",
        ),
        "features": [
            ("Wie je ontvolgde",
             "Bijgehouden van import tot import, met de datum waarop elke verandering is "
             "gevonden."),
            ("Blokkeerde je waarschijnlijk",
             "Accounts die tegelijk uit je volgers en je volgend verdwenen. De app markeert "
             "ze als waarschijnlijke blokkade."),
            ("Wie jou niet terugvolgt",
             "De bekende lijst, plus mutuals en volgverzoeken die nooit zijn geaccepteerd."),
            ("Met wie je het meest interacteert",
             "Je likes, reacties en story-reacties, geteld uit je eigen export."),
            ("Je geschiedenis in grafieken",
             "Groei- en follow-back-grafieken uit elke export die je importeert."),
            ("Geen login",
             "De app heeft nergens een inlogscherm. Je wachtwoord blijft van jou."),
        ],
        "privacy_title": "Je export blijft op je iPhone.",
        "privacy": [
            "Je Instagram-export wordt alleen op je iPhone gelezen en bewaard.",
            "Geen account, geen analytics, geen advertenties, geen tracking.",
            "Om te controleren of een account nog bestaat, stuurt de app alleen die "
            "gebruikersnaam naar Instagram, zonder in te loggen.",
        ],
        "note": "Unfollowers is een onafhankelijke app en niet gelieerd aan Instagram of Meta.",
        "stats": [],
        "reviews": [],
        "why": (
            "Je wachtwoord blijft van jou.",
            "De meeste volgertrackers vragen om je Instagram-wachtwoord en gebruiken daarna "
            "je account op de achtergrond. Instagram waarschuwt dat apps zonder toestemming "
            "in je account een risico zijn. Wie ze vaak gebruikt, meldt vergrendelde of "
            "geschorste accounts en geblokkeerde acties. Unfollowers vraagt nooit om je "
            "wachtwoord en logt nooit in op je account. De app leest de data-export die "
            "Instagram je zelf geeft. En er is geen abonnement: één optionele aankoop "
            "ontgrendelt alles.",
        ),
        "shots": [
            "Zie elke ontvolger: wie wegging en wanneer, gelezen uit je eigen "
            "Instagram-data-export.",
            "Waarschijnlijk geblokkeerd: accounts die tegelijk uit je volgers en je volgend "
            "verdwenen.",
            "Ze volgen je niet terug: zoek, sorteer en tik door naar elk profiel.",
            "Wie jij het meest hypet: je likes, reacties en story-reacties, geteld.",
            "Jouw stats in grafieken: groei en follow-back uit je eigen geschiedenis.",
        ],
    },
    "guide_link": "Zo download je je Instagram-gegevens",
    "faq": [
        ("Hoe zie ik wie mij heeft ontvolgd op Instagram?", [
            "Instagram laat niet zien wie je ontvolgde. Je Instagram-data-export bevat "
            "iedereen die je volgt op de dag dat je hem downloadt. Unfollowers vergelijkt "
            "twee van die exports en laat zien wie er wegging.",
            [
                "Download je data-export bij Instagram, met Volgers en volgend in "
                "JSON-formaat. [Zo doe je dat](guide).",
                "Importeer het ZIP-bestand in Unfollowers. Je ziet meteen wie jou niet "
                "terugvolgt.",
                "Een paar weken later download je een nieuwe export en importeer je die ook. "
                "Unfollowers laat zien wie je sinds de eerste ontvolgde, met de datum waarop "
                "elke verandering is gevonden.",
            ],
            "Elke nieuwe export die je importeert, vult je geschiedenis aan.",
        ]),
        ("Is er een veilige unfollow-tracker zonder login?", [
            "Unfollowers werkt zonder login. De app vraagt nooit om je Instagram-wachtwoord "
            "en logt nooit in op je account. Hij leest de data-export die je zelf bij "
            "Instagram downloadt.",
            "Veel volgertrackers vragen om je Instagram-wachtwoord en gebruiken daarna je "
            "account op de achtergrond. Instagram waarschuwt dat apps zonder toestemming in "
            "je account een risico zijn. Met Unfollowers blijft je wachtwoord van jou, en de "
            "app voert nooit acties uit op je account.",
            "Het bestand wordt op je iPhone gelezen en bewaard. Geen account, geen "
            "advertenties, geen tracking.",
        ]),
        ("Hoe download ik mijn Instagram-gegevens?", [
            "Open in de Instagram-app je profiel en tik op het menu. Ga dan naar "
            "Accountcentrum › Je gegevens en toestemmingen › Je gegevens exporteren › Export "
            "maken. Bij sommige accounts heet het Accountcentrum Meta-account. Kies "
            "Exporteren naar apparaat. Vink Volgers en volgend aan, kies de hele periode en "
            "het formaat JSON, en tik op Export starten. Instagram laat je weten wanneer het "
            "bestand klaar is, meestal binnen een paar minuten.",
            "[Stap-voor-stap-handleiding](guide).",
        ]),
        ("Kan ik zien wie mij heeft geblokkeerd op Instagram?", [
            "Instagram meldt geen blokkades, dus geen enkele app kan het zeker weten. Als "
            "iemand je blokkeert, verdwijnt die persoon tegelijk uit je volgers en uit je "
            "volgend. Unfollowers markeert die accounts als waarschijnlijke blokkade. Dat "
            "werkt alleen bij mensen die jou volgden en die jij ook volgde.",
            "Een account dat verwijderd, gedeactiveerd of hernoemd is, verdwijnt op dezelfde "
            "manier. De profielcheck (de vibe check) vraagt aan instagram.com of elke "
            "gebruikersnaam nog bestaat en zet verdwenen accounts in een aparte lijst.",
        ]),
        ("Is Unfollowers gratis?", [
            "Unfollowers downloaden is gratis. De gratis versie laat zien wie jou niet "
            "terugvolgt, wie jij niet terugvolgt en je mutuals. Eén eenmalige aankoop "
            "ontgrendelt de rest, ook de lijsten van wie je ontvolgde en wie je "
            "waarschijnlijk blokkeerde. Er is geen abonnement. De app werkt op iPhone met "
            "iOS 17 of nieuwer.",
        ]),
        ("Verlaat er iets mijn iPhone?", [
            "Je exportbestand blijft op je iPhone. De app leest en bewaart het daar, en de "
            "ontwikkelaar heeft geen servers. De enige functie die internet gebruikt, is de "
            "profielcheck. Die vraagt aan instagram.com of een account nog bestaat en stuurt "
            "alleen die gebruikersnaam, zonder in te loggen. Hij draait als je op de vibe "
            "check tikt en, na ontgrendeling, voor maximaal 30 nieuwe accounts na elke "
            "import. [Privacybeleid (in het Engels)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "instagram-gegevens-downloaden",
        "title": "Zo download je je Instagram-gegevens (export in JSON)",
        "description": "Stap voor stap op iPhone: exporteer je Instagram-volgers en volgend "
                       "in JSON-formaat, voor de hele periode, en bewaar het ZIP-bestand. "
                       "Zie daarna met Unfollowers wie je ontvolgde.",
        "lead": "Bij Instagram kun je een kopie van de gegevens van je account downloaden. "
                "De export bevat de volledige lijsten van je volgers en van de accounts die "
                "je volgt. Unfollowers leest dit bestand en laat zien wie je ontvolgde. Zo "
                "krijg je het in de Instagram-app op iPhone.",
        "choose": [
            ("Gegevens", "Volgers en volgend"),
            ("Datumbereik", "Altijd"),
            ("Formaat", "JSON"),
        ],
        "steps": [
            ("Open het menu",
             "Tik in de Instagram-app rechtsonder op je profielfoto. Tik daarna rechtsboven "
             "op het menu (☰)."),
            ("Accountcentrum",
             "Tik op **Accountcentrum**. Bij sommige accounts heet het **Meta-account**."),
            ("Je gegevens",
             "Tik op **Je gegevens en toestemmingen** en dan op **Je gegevens exporteren**."),
            ("Maak de export",
             "Tik op **Export maken**. Kies je Instagram-profiel en tik op **Volgende**."),
            ("Exporteren naar apparaat",
             "Kies **Exporteren naar apparaat**. Zo wordt het bestand op je iPhone bewaard."),
            ("Kies de gegevens",
             "Op het volgende scherm kies je welke gegevens je exporteert. Vink **Volgers en "
             "volgend** aan, bij de connecties. Wil je zien met wie je het meest "
             "interacteert, vink dan ook vind-ik-leuks, reacties en story-interacties aan. De "
             "rest kun je uitvinken, dan blijft het bestand klein."),
            ("Hele periode, JSON",
             "Kies bij het datumbereik de hele periode, vanaf het begin. Kies bij het formaat "
             "**JSON**. Unfollowers kan het HTML-formaat niet lezen."),
            ("Start de export",
             "Tik op **Export starten**. Instagram maakt het bestand klaar. Dat duurt meestal "
             "een paar minuten."),
            ("Download de ZIP",
             "Instagram stuurt een melding als het bestand klaar is. Ga terug naar **Je "
             "gegevens exporteren** en download het bestand. Instagram kan om je wachtwoord "
             "vragen. Dat typ je in Instagram zelf. Bewaar het ZIP-bestand in de "
             "Bestanden-app."),
            ("Importeer hem in Unfollowers",
             "Open Unfollowers, tik op de importknop en kies het ZIP-bestand. Je hoeft het "
             "niet uit te pakken."),
        ],
        "tips": [
            ("Twee exports laten zien wie wegging",
             "Eén export bevat je volgers op één dag. Importeer om de paar weken een nieuwe "
             "export. Unfollowers vergelijkt ze en laat zien wie er sinds de vorige wegging."),
            ("Het bestand blijft vier dagen beschikbaar",
             "Instagram bewaart een klare export vier dagen. Maak daarna een nieuwe."),
            ("„Geen volgerslijsten gevonden”",
             "Unfollowers toont deze melding als de export in HTML-formaat is, of als Volgers "
             "en volgend niet was aangevinkt. Maak een nieuwe export in JSON met Volgers en "
             "volgend."),
            ("Het kan langer duren",
             "De meeste exports zijn binnen een paar minuten klaar. Soms duurt het langer. "
             "Instagram laat het je in de app en per e-mail weten als die van jou klaar is."),
        ],
        "updated": "Stappen gecontroleerd in het Instagram-helpcentrum, oktober 2026.",
        "cta_title": "Zie wie je ontvolgde",
        "cta_text": "Unfollowers leest dit bestand op je iPhone. De app laat zien wie je "
                    "ontvolgde, wie je waarschijnlijk blokkeerde en wie jou niet terugvolgt. "
                    "Zonder login en zonder wachtwoord.",
    },
}
