# Pedometer in Italian ("tu", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# App words from Shared/Localizable.xcstrings (Collega, Camminata, Corsa,
# Camminate e corse, Obiettivi giornalieri, Sostieni Pedometer, Impostazioni);
# iOS words are Apple's Italian.
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "it.py"))["L"]["ui"]

L = {
    "name": "Italiano",
    "path": "it/",
    "og_locale": "it_IT",
    "ui": {**_ui, "summary": "Widget della schermata di blocco"},
    "page": {
        "shots_dir": "it",
        "tagline": "I tuoi passi sulla schermata di blocco.",
        "pricing": "Gratis",
        "intro": (
            "Passi, distanza e piani saliti, in numeri e grafici chiari.",
            "Pedometer legge Apple Salute e mette il conteggio di oggi sulla schermata di "
            "blocco e nella schermata Home. Il tuo iPhone conta i passi da solo, e se porti "
            "un Apple Watch anche i suoi passi vengono contati.",
        ),
        "features": [
            ("Oggi",
             "I tuoi passi rispetto all'obiettivo, con quanto manca. Distanza e piani "
             "rispetto ai loro obiettivi, con energia attiva e velocità di camminata."),
            ("Camminate e corse",
             "Registra una camminata o una corsa con il GPS: il percorso sulla mappa, con "
             "velocità o passo, altitudine, dislivello e calorie. Ognuna viene salvata in "
             "Apple Salute con il suo percorso."),
            ("Frequenza cardiaca in diretta",
             "Con AirPods Pro 3, Powerbeats Pro 2 o una fascia cardio Bluetooth vedi la "
             "frequenza cardiaca in diretta (iOS 26)."),
            ("Sulla schermata di blocco",
             "Mentre cammini, tempo, distanza, velocità, battito e calorie restano sulla "
             "schermata di blocco, con un pulsante di pausa."),
            ("Condividi una camminata",
             "Un'immagine di ogni camminata o corsa, con la mappa e i tuoi dati, per "
             "qualsiasi app."),
            ("I tuoi obiettivi",
             "Imposta un obiettivo giornaliero per passi, distanza e piani. Si parte da "
             "10.000 passi, 8 km e 10 piani."),
            ("Cronologia",
             "Un grafico per ogni dato per l'ultima settimana, l'ultimo mese o l'ultimo "
             "anno, con la media giornaliera e la variazione rispetto al periodo prima."),
            ("Widget della schermata di blocco",
             "Passi e distanza, ognuno in un anello che si chiude all'obiettivo, e i piani, "
             "con una figura che sale una scala."),
            ("Widget della schermata Home",
             "La stessa scheda dell'app, piccola, media o grande. Chiara, scura o "
             "automatica, e solo con i passi se preferisci."),
            ("Per ora",
             "I passi di oggi ora per ora, accanto alla tua giornata tipo delle ultime "
             "quattro settimane."),
            ("Record",
             "I totali di ogni mese e anno, e il tuo giorno, settimana e mese migliori per "
             "passi, piani e velocità di camminata."),
            ("Il tuo colore",
             "Grafite, blu, verde, arancione, rosa o viola per le barre degli obiettivi, i "
             "grafici e il widget."),
        ],
        "privacy_title": "Niente lascia il tuo iPhone.",
        "privacy": [
            "Legge Apple Salute e vi scrive solo le camminate e le corse che registri.",
            "La tua posizione si usa solo durante la registrazione e resta sul tuo iPhone.",
            "Tutto viene contato e salvato sul tuo iPhone. Non si carica nulla.",
            "Nessun account, nessuna analisi, nessun tracciamento.",
        ],
        "note": "Pedometer non è un dispositivo medico e non dà consigli medici.",
        "shots": [
            "I tuoi passi sulla schermata di blocco: un widget contapassi, con distanza e piani accanto.",
            "Ogni passo conta: legge Apple Salute, include i passi di Apple Watch.",
            "Camminate e corse sulla mappa: velocità, altitudine, calorie e frequenza cardiaca.",
            "In diretta, poi da condividere: la schermata di blocco mentre cammini, un'immagine dopo.",
            "Anche nella schermata Home: la stessa scheda, piccola o media.",
            "La tua giornata, ora per ora: i passi di oggi accanto a una giornata tipo.",
            "I tuoi record: il giorno, la settimana e il mese migliori, e i totali.",
            "Scegli il tuo colore: sei colori per le barre, i grafici e il widget.",
            "La tua settimana a colpo d'occhio: barre giornaliere, la media e la variazione.",
            "Niente lascia il tuo iPhone: nessun account, nessun tracciamento.",
        ],
    },
    "guide_link": "Come mettere un contapassi sulla schermata di blocco dell'iPhone",
    "faq": [
        ("Esiste un contapassi gratis per iPhone senza abbonamento?", [
            "Pedometer è gratis, senza abbonamento e senza account. Mostra passi, distanza "
            "e piani saliti in numeri e grafici chiari, e li mette come widget sulla "
            "schermata di blocco e nella schermata Home. Registra anche camminate e corse "
            "con il GPS. Una mancia facoltativa non sblocca nulla. [Vedi su App Store](store).",
        ]),
        ("Come mostro i miei passi sulla schermata di blocco dell'iPhone?", [
            [
                "Installa Pedometer, aprilo e tocca **Collega** per permettergli di leggere "
                "Apple Salute.",
                "Tieni premuta la schermata di blocco, tocca **Personalizza** e scegli la "
                "schermata di blocco.",
                "Tocca l'area dei widget sotto l'ora, scegli **Pedometer** e aggiungi passi, "
                "distanza o piani saliti.",
                "Tocca **Fine**.",
            ],
            "I widget di passi e distanza stanno in un anello che si chiude all'obiettivo. "
            "[La guida passo passo](guide).",
        ]),
        ("Serve un Apple Watch?", [
            "No. Il tuo iPhone conta i passi da solo quando lo porti con te. Se porti anche "
            "un Apple Watch, Pedometer legge Apple Salute, che unisce i passi dei due senza "
            "contarli due volte.",
        ]),
        ("Può registrare camminate e corse con il GPS?", [
            "Sì. Tocca **Camminata** o **Corsa** in **Camminate e corse**. La mappa disegna "
            "il percorso e mostra tempo, distanza, velocità o passo, calorie, altitudine e "
            "dislivello. Mentre cammini, i dati restano sulla schermata di blocco con un "
            "pulsante di pausa. Ognuna viene salvata in Apple Salute con il percorso, e puoi "
            "condividerne un'immagine.",
        ]),
        ("Può mostrare la frequenza cardiaca senza Apple Watch?", [
            "Sì, con iOS 26. Con AirPods Pro 3, Powerbeats Pro 2 o una fascia cardio "
            "Bluetooth vedi la frequenza cardiaca in diretta durante una camminata o una "
            "corsa.",
        ]),
        ("Posso cambiare l'obiettivo giornaliero di passi?", [
            "Sì. In **Obiettivi giornalieri** imposti un obiettivo per passi, distanza e "
            "piani. Si parte da 10.000 passi, 8 km e 10 piani. Gli anelli dei widget si "
            "chiudono ai tuoi obiettivi.",
        ]),
        ("Pedometer è davvero gratis?", [
            "Sì. Tutte le funzioni sono gratis e non c'è abbonamento. In **Impostazioni** › "
            "**Sostieni Pedometer** puoi lasciare una mancia, se vuoi. È facoltativa e non "
            "sblocca nulla.",
        ]),
        ("Pedometer carica i miei dati sanitari?", [
            "No. Tutto viene contato e salvato sul tuo iPhone, e non si carica nulla. "
            "Pedometer legge Apple Salute e vi scrive solo le camminate e le corse che "
            "registri. La posizione si usa solo durante la registrazione. Nessun account, "
            "nessuna analisi, nessun tracciamento. [Informativa sulla privacy (in "
            "inglese)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "contapassi-schermata-blocco",
        "title": "Come mettere un contapassi sulla schermata di blocco dell'iPhone",
        "description": "Passo passo: aggiungi un widget contapassi gratis alla schermata di "
                       "blocco e alla schermata Home dell'iPhone, con distanza e piani "
                       "accanto. Senza Apple Watch e senza abbonamento.",
        "lead": "Il tuo iPhone conta già i passi. Pedometer mette quel numero sulla schermata "
                "di blocco, così lo vedi ogni volta che prendi il telefono. Ci vuole circa un "
                "minuto, e non serve un Apple Watch.",
        "choose": [
            ("Passi", "In un anello che si chiude all'obiettivo"),
            ("Distanza", "In un anello, in km o miglia"),
            ("Piani saliti", "Una figura sale una scala"),
        ],
        "steps": [
            ("Installa Pedometer",
             "Scarica [Pedometer da App Store](store). È gratis e non chiede un account."),
            ("Collega Apple Salute",
             "Apri Pedometer e tocca **Collega**. Consenti la lettura di passi, distanza e "
             "piani saliti. Il tuo iPhone li ha sempre contati, quindi la cronologia appare "
             "subito."),
            ("Imposta gli obiettivi",
             "Scegli un obiettivo giornaliero per passi, distanza e piani in **Obiettivi "
             "giornalieri**. Gli anelli dei widget si chiudono quando li raggiungi."),
            ("Modifica la schermata di blocco",
             "Blocca l'iPhone, riattivalo e tieni premuta la schermata di blocco. Tocca "
             "**Personalizza** e scegli la schermata di blocco."),
            ("Aggiungi il widget",
             "Tocca l'area dei widget sotto l'ora. Trova **Pedometer** nell'elenco e tocca "
             "passi, distanza o piani saliti. Puoi aggiungerne più di uno."),
            ("Tocca Fine",
             "I tuoi passi ora sono sulla schermata di blocco e si aggiornano durante il "
             "giorno."),
            ("Anche nella schermata Home",
             "Tieni premuta un'area vuota della schermata Home, tocca **Modifica** e poi "
             "**Aggiungi widget**. Cerca Pedometer e scegli piccolo, medio o grande. Il "
             "grande aggiunge la giornata ora per ora."),
        ],
        "tips": [
            ("Chiaro, scuro o solo passi",
             "Tieni premuto il widget della schermata Home e scegli **Modifica widget** per "
             "renderlo chiaro o scuro, o mostrare solo i passi."),
            ("Scegli un colore",
             "Grafite, blu, verde, arancione, rosa o viola, per le barre degli obiettivi, i "
             "grafici e il widget."),
            ("Esci a camminare?",
             "Tocca **Camminata** o **Corsa** nell'app per registrare il percorso con il "
             "GPS. I dati restano sulla schermata di blocco mentre cammini."),
            ("Niente lascia il tuo iPhone",
             "Pedometer non ha account e non carica nulla. Legge Apple Salute sul tuo iPhone."),
        ],
        "updated": "Scritto per Pedometer 1.5 su iOS 26, ottobre 2026.",
        "cta_title": "I tuoi passi, a colpo d'occhio",
        "cta_text": "Un contapassi gratis per la schermata di blocco e la schermata Home, con "
                    "camminate e corse sulla mappa. Nessun account, nessun abbonamento.",
    },
}
