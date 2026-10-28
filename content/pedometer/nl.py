# Pedometer in Dutch ("je", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# App words from Shared/Localizable.xcstrings (Verbind, Wandelen, Hardlopen,
# Wandelen en hardlopen, Dagdoelen, Steun Pedometer, Instellingen); iOS words
# are Apple's Dutch (toegangsscherm, beginscherm, Pas aan, Wijzig, Gereed).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "nl.py"))["L"]["ui"]

L = {
    "name": "Nederlands",
    "path": "nl/",
    "og_locale": "nl_NL",
    "ui": {**_ui, "summary": "Widgets voor het toegangsscherm"},
    "page": {
        "shots_dir": "nl",
        "tagline": "Je stappen op je toegangsscherm.",
        "pricing": "Gratis",
        "intro": (
            "Stappen, afstand en traplopen, als duidelijke cijfers en grafieken.",
            "Pedometer leest Apple Gezondheid en zet de telling van vandaag op je "
            "toegangsscherm en beginscherm. Je iPhone telt je stappen zelf, en als je een "
            "Apple Watch draagt, tellen die stappen ook mee.",
        ),
        "features": [
            ("Vandaag",
             "Je stappen naast je doel, met wat er nog over is. Afstand en traplopen naast "
             "hun doelen, met actieve energie en wandelsnelheid ernaast."),
            ("Wandelen en hardlopen",
             "Leg een wandeling of hardlooprondje vast met gps: je route op de kaart, met "
             "snelheid of tempo, hoogte, stijging en calorieën. Elke tocht wordt met route "
             "in Apple Gezondheid bewaard."),
            ("Live hartslag",
             "Met AirPods Pro 3, Powerbeats Pro 2 of een Bluetooth-hartslagband zie je je "
             "hartslag live (iOS 26)."),
            ("Op het toegangsscherm",
             "Onderweg blijven tijd, afstand, snelheid, hartslag en calorieën op het "
             "toegangsscherm staan, met een pauzeknop."),
            ("Deel een wandeling",
             "Een plaatje van elke wandeling of loop, met de kaart en je cijfers, voor elke "
             "app."),
            ("Je eigen doelen",
             "Stel een dagdoel in voor stappen, afstand en traplopen. Ze beginnen bij 10.000 "
             "stappen, 8 km en 10 verdiepingen."),
            ("Geschiedenis",
             "Eén grafiek per cijfer voor de afgelopen week, maand of jaar, met het "
             "daggemiddelde en het verschil met de periode ervoor."),
            ("Widgets voor het toegangsscherm",
             "Stappen en afstand, elk in een ring die sluit bij je doel, en traplopen, met "
             "een poppetje dat een trap op loopt."),
            ("Widget voor het beginscherm",
             "Dezelfde kaart als in de app, klein, middelgroot of groot. Licht, donker of "
             "automatisch, en alleen met de stappen als je wilt."),
            ("Per uur",
             "De stappen van vandaag uur voor uur, naast je gewone dag van de afgelopen vier "
             "weken."),
            ("Records",
             "Totalen per maand en jaar, en je beste dag, week en maand voor stappen, "
             "traplopen en wandelsnelheid."),
            ("Je kleur",
             "Grafiet, blauw, groen, oranje, roze of paars voor de doelbalken, de grafieken "
             "en de widget."),
        ],
        "privacy_title": "Niets verlaat je iPhone.",
        "privacy": [
            "Leest Apple Gezondheid en schrijft er alleen de wandelingen en loopjes in die "
            "je vastlegt.",
            "Je locatie wordt alleen gebruikt tijdens het vastleggen en blijft op je iPhone.",
            "Alles wordt op je iPhone geteld en bewaard. Er wordt niets geüpload.",
            "Geen account, geen analyse, geen tracking.",
        ],
        "note": "Pedometer is geen medisch hulpmiddel en geeft geen medisch advies.",
        "shots": [
            "Je stappen op het toegangsscherm: een stappenteller-widget, met afstand en traplopen ernaast.",
            "Elke stap geteld: leest Apple Gezondheid, stappen van je Apple Watch tellen mee.",
            "Wandelen en lopen op de kaart: snelheid, hoogte, calorieën en hartslag.",
            "Live volgen, daarna delen: het toegangsscherm onderweg, een plaatje achteraf.",
            "Ook op je beginscherm: dezelfde kaart, klein of middelgroot.",
            "Je dag, uur voor uur: de stappen van vandaag naast een gewone dag.",
            "Je beste dag, week en maand: totalen per maand en jaar.",
            "Kies je kleur: zes kleuren voor de doelbalken, de grafieken en de widget.",
            "Je week in één oogopslag: dagelijkse balken, het gemiddelde en het verschil.",
            "Niets verlaat je iPhone: geen account, geen tracking.",
        ],
    },
    "guide_link": "Zo zet je een stappenteller op het toegangsscherm van je iPhone",
    "faq": [
        ("Is er een gratis stappenteller voor iPhone zonder abonnement?", [
            "Pedometer is gratis, zonder abonnement en zonder account. De app toont je "
            "stappen, afstand en traplopen als duidelijke cijfers en grafieken, en zet ze "
            "als widgets op je toegangsscherm en beginscherm. Ook legt hij wandelingen en "
            "hardlooprondjes vast met gps. Een vrijwillige fooi ontgrendelt niets. [Bekijk "
            "in de App Store](store).",
        ]),
        ("Hoe zet ik mijn stappen op het toegangsscherm van mijn iPhone?", [
            [
                "Installeer Pedometer, open de app en tik op **Verbind** zodat hij Apple "
                "Gezondheid mag lezen.",
                "Houd je vinger op het toegangsscherm, tik op **Pas aan** en kies het "
                "toegangsscherm.",
                "Tik op het widgetvak onder de klok, kies **Pedometer** en voeg stappen, "
                "afstand of traplopen toe.",
                "Tik op **Gereed**.",
            ],
            "De widgets voor stappen en afstand staan in een ring die sluit bij je doel. "
            "[Stap-voor-stap-uitleg](guide).",
        ]),
        ("Heb ik een Apple Watch nodig?", [
            "Nee. Je iPhone telt je stappen zelf als je hem bij je draagt. Draag je ook een "
            "Apple Watch, dan leest Pedometer Apple Gezondheid, dat de stappen van allebei "
            "samenvoegt zonder ze dubbel te tellen.",
        ]),
        ("Kan de app wandelingen en hardlooprondjes vastleggen met gps?", [
            "Ja. Tik op **Wandelen** of **Hardlopen** onder **Wandelen en hardlopen**. De "
            "kaart tekent je route en toont tijd, afstand, snelheid of tempo, calorieën, "
            "hoogte en stijging. Onderweg blijven de cijfers op het toegangsscherm, met een "
            "pauzeknop. Elke tocht wordt met route in Apple Gezondheid bewaard, en je kunt "
            "er een plaatje van delen.",
        ]),
        ("Kan de app mijn hartslag tonen zonder Apple Watch?", [
            "Ja, met iOS 26. Met AirPods Pro 3, Powerbeats Pro 2 of een "
            "Bluetooth-hartslagband zie je je hartslag live tijdens het wandelen of lopen.",
        ]),
        ("Kan ik mijn dagelijkse stappendoel aanpassen?", [
            "Ja. Onder **Dagdoelen** stel je doelen in voor stappen, afstand en traplopen. "
            "Ze beginnen bij 10.000 stappen, 8 km en 10 verdiepingen. De ringen van de "
            "widgets sluiten bij je doelen.",
        ]),
        ("Is Pedometer echt gratis?", [
            "Ja. Alle functies zijn gratis en er is geen abonnement. Onder **Instellingen** "
            "› **Steun Pedometer** kun je een fooi geven als je wilt. Die is vrijwillig en "
            "ontgrendelt niets.",
        ]),
        ("Uploadt Pedometer mijn gezondheidsgegevens?", [
            "Nee. Alles wordt op je iPhone geteld en bewaard, en er wordt niets geüpload. "
            "Pedometer leest Apple Gezondheid en schrijft er alleen de wandelingen en loopjes "
            "in die je vastlegt. Je locatie wordt alleen tijdens het vastleggen gebruikt. "
            "Geen account, geen analyse, geen tracking. [Privacybeleid (in het "
            "Engels)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "stappenteller-toegangsscherm",
        "title": "Zo zet je een stappenteller op het toegangsscherm van je iPhone",
        "description": "Stap voor stap: zet een gratis stappenteller-widget op het "
                       "toegangsscherm en beginscherm van je iPhone, met afstand en "
                       "traplopen ernaast. Zonder Apple Watch en zonder abonnement.",
        "lead": "Je iPhone telt je stappen al. Pedometer zet dat getal op je toegangsscherm, "
                "zodat je het ziet elke keer dat je je telefoon pakt. Het kost ongeveer een "
                "minuut, en je hebt geen Apple Watch nodig.",
        "choose": [
            ("Stappen", "In een ring die sluit bij je doel"),
            ("Afstand", "In een ring, in km of mijlen"),
            ("Traplopen", "Een poppetje loopt een trap op"),
        ],
        "steps": [
            ("Installeer Pedometer",
             "Download [Pedometer in de App Store](store). De app is gratis en vraagt geen "
             "account."),
            ("Verbind Apple Gezondheid",
             "Open Pedometer en tik op **Verbind**. Sta het lezen van stappen, afstand en "
             "traplopen toe. Je iPhone heeft die altijd al geteld, dus je geschiedenis staat "
             "er meteen."),
            ("Stel je doelen in",
             "Kies onder **Dagdoelen** een doel voor stappen, afstand en traplopen. De ringen "
             "van de widgets sluiten als je ze haalt."),
            ("Wijzig het toegangsscherm",
             "Vergrendel je iPhone, maak hem wakker en houd je vinger op het toegangsscherm. "
             "Tik op **Pas aan** en kies het toegangsscherm."),
            ("Voeg de widget toe",
             "Tik op het widgetvak onder de klok. Zoek **Pedometer** in de lijst en tik op "
             "stappen, afstand of traplopen. Je kunt er meer dan één toevoegen."),
            ("Tik op Gereed",
             "Je stappen staan nu op het toegangsscherm en worden de hele dag bijgewerkt."),
            ("Ook op het beginscherm",
             "Houd je vinger op een lege plek van het beginscherm, tik op **Wijzig** en dan "
             "op **Voeg widget toe**. Zoek Pedometer en kies klein, middelgroot of groot. "
             "Groot toont ook de dag uur voor uur."),
        ],
        "tips": [
            ("Licht, donker of alleen stappen",
             "Houd je vinger op de widget op het beginscherm en kies **Wijzig widget** om hem "
             "licht of donker te maken, of alleen de stappen te tonen."),
            ("Kies een kleur",
             "Grafiet, blauw, groen, oranje, roze of paars, voor de doelbalken, de grafieken "
             "en de widget."),
            ("Ga je wandelen?",
             "Tik in de app op **Wandelen** of **Hardlopen** om je route met gps vast te "
             "leggen. De cijfers blijven onderweg op het toegangsscherm."),
            ("Niets verlaat je iPhone",
             "Pedometer heeft geen account en uploadt niets. De app leest Apple Gezondheid "
             "op je iPhone."),
        ],
        "updated": "Geschreven voor Pedometer 1.5 op iOS 26, oktober 2026.",
        "cta_title": "Je stappen in één oogopslag",
        "cta_text": "Een gratis stappenteller voor je toegangsscherm en beginscherm, met "
                    "wandelingen en loopjes op de kaart. Geen account, geen abonnement.",
    },
}
