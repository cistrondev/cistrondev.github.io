# Aloud in Italian ("tu", as in the app). Keys are explained in
# content/unfollowers/en.py; facts to keep true are in en.py. Button names are
# the app's Italian strings (Aloud/Localizable.xcstrings).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "it.py"))["L"]["ui"]

L = {
    "name": "Italiano",
    "path": "it/",
    "og_locale": "it_IT",
    "ui": {
        **_ui,
        "summary": "Cosa legge Aloud",
        "tips": "Buono a sapersi",
        "appearance": "Aspetto degli screenshot",
        "light": "Chiaro",
        "dark": "Scuro",
        "what_people_say": "Cosa dicono gli utenti.",
    },
    "page": {
        "shots_dir": "it",
        "tagline": "Tutto ciò che puoi leggere, letto ad alta voce.",
        "pricing": "Prova gratis · Sblocco una tantum",
        "platform": "iPhone e iPad · iOS 17 o successivo",
        "intro": (
            "Condividi un articolo, apri un PDF o incolla un testo qualsiasi.",
            "Aloud te lo legge con una voce naturale creata sul tuo iPhone, frase per frase, "
            "e ricorda sempre dove eri arrivato.",
        ),
        "features": [
            ("Voci naturali, sul dispositivo",
             "Dieci voci per l'inglese e quattro che leggono altre trenta lingue, tra cui "
             "l'italiano. Nessun server parla al posto tuo, quindi Aloud continua a leggere "
             "anche in modalità aereo."),
            ("Articoli, PDF, libri",
             "Condividi da qualsiasi browser, apri PDF e libri EPUB da File, anche PDF "
             "scansionati, oppure incolla il tuo testo."),
            ("Per seguire la lettura",
             "La frase che viene letta è evidenziata. Tieni premuta la barra sul margine per "
             "scorrere tutto il documento."),
            ("Più veloce, se vuoi",
             "Da 0,5× a 3× senza voce da cartone animato, con le pause accorciate a ogni "
             "punto, se preferisci."),
            ("Per quando sei in giro",
             "Continua a leggere a schermo bloccato, con i comandi nella schermata di blocco "
             "e sugli AirPods, e un timer di stop che abbassa piano il volume."),
            ("Su ogni dispositivo",
             "La sincronizzazione con iCloud è facoltativa e salva il tuo scaffale come "
             "semplici file di testo nel tuo iCloud Drive."),
        ],
        "privacy_title": "I tuoi documenti restano con te.",
        "privacy": [
            "La voce viene creata sul tuo iPhone. I tuoi documenti non vengono mai caricati.",
            "Le voci si scaricano una volta da un server pubblico. Gli articoli che "
            "condividi vengono presi dal loro sito, come farebbe un browser.",
            "Nessun account, nessuna statistica, nessuna pubblicità, nessun tracciamento.",
        ],
        "note": "",
        "reviews": [],
        "why": (
            "Senza server e senza abbonamento.",
            "Molte app di sintesi vocale famose creano le voci sui propri server, quindi gli "
            "articoli e i documenti che ascolti vengono prima caricati lì, e i loro piani "
            "premium possono costare 139 $ l'anno, oppure 29 $ al mese, quasi 350 $ l'anno. "
            "Aloud crea ogni voce direttamente sul tuo iPhone, quindi ciò che leggi non "
            "viene mai inviato da nessuna parte per essere letto. E non c'è abbonamento: un "
            "solo acquisto facoltativo, tuo per sempre.",
        ),
        "shots": [
            "Tutto ciò che puoi leggere, lo legge per te. Articoli, PDF, appunti, letti da una voce naturale, frase per frase.",
            "Arriva in fondo alla lista di lettura. Ascolta nel tragitto, a passeggio, mentre lavi i piatti.",
            "Funziona offline. Ovunque. La voce si scarica una sola volta.",
            "Nessun abbonamento. Nessuna pubblicità. Nessun tracciamento.",
            "Voci naturali. In ogni lingua. Dieci voci per l'inglese, quattro che leggono altre trenta lingue, create sul tuo iPhone.",
            "Modalità lettura: leggi a modo tuo.",
            "Il doppio della velocità. La metà del tempo. Da 0,5× a 3×, con meno silenzio tra le frasi.",
            "Il tuo scaffale, su ogni dispositivo, come file di testo su iCloud Drive.",
            "Leggilo nella tua lingua: qualsiasi testo tradotto sul dispositivo, frase accanto a frase.",
        ],
        "duo": {
            "title": "Su iPhone Duo",
            "sub": "Chiuso, ascolti. Aperto, leggi.",
            "items": [
                ("cover", "cover", "Chiuso", "La voce continua sullo schermo esterno.",
                 "Aloud sullo schermo esterno di iPhone Duo: la voce continua a leggere, con i comandi di riproduzione."),
                ("book", "spread", "Semiaperto", "Due pagine affiancate, a qualsiasi angolo.",
                 "Aloud su iPhone Duo semiaperto: due pagine affiancate."),
                ("flat", "spread", "Aperto", "Stai traducendo? L'originale e la traduzione, fianco a fianco.",
                 "Aloud su iPhone Duo aperto: l'originale spagnolo nella pagina di sinistra, la "
                 "traduzione inglese in quella di destra, riga per riga."),
            ],
        },
    },
    "guide_link": "Come ascoltare articoli, PDF e libri EPUB su iPhone",
    "faq": [
        ("Quale app di sintesi vocale per iPhone non ha abbonamento?", [
            "Aloud legge ad alta voce articoli, PDF, libri EPUB e qualsiasi testo con una "
            "voce naturale. Si scarica gratis, e un solo acquisto in-app toglie il limite per "
            "sempre. Non c'è abbonamento e niente si rinnova.",
            "Le voci vengono create sul tuo iPhone o iPad, quindi ciò che leggi non viene mai "
            "caricato per essere letto, e Aloud continua a leggere senza connessione. Nessun "
            "account, nessuna pubblicità, nessun tracciamento.",
        ]),
        ("Come ascolto un articolo su iPhone?", [
            [
                "Apri l'articolo in Safari o in un'altra app.",
                "Tocca **Condividi**, poi **Aloud**.",
                "Apri Aloud e premi play. La frase che viene letta è evidenziata nella "
                "pagina.",
            ],
            "Quando condividi da Safari, Aloud legge la pagina come la mostra Safari, quindi "
            "funzionano anche gli articoli dei siti in cui hai effettuato l'accesso. Anche i "
            "link condivisi dalle app Facebook, Messenger e Instagram funzionano. [Guida "
            "passo per passo](guide).",
        ]),
        ("Aloud può trasformare un EPUB in un audiolibro?", [
            "Sì. Apri un file EPUB dall'app File, oppure tocca **+** › **Importa un file**. "
            "Aloud conserva la copertina e i capitoli del libro. L'elenco **Capitoli** "
            "mostra quanto dura l'ascolto di ogni capitolo, e puoi partire da qualsiasi "
            "capitolo. Aloud ricorda dove eri arrivato, così un libro lungo si ascolta come "
            "un audiolibro.",
            "I libri acquistati con protezione dalla copia non si aprono in nessun'altra "
            "app, nemmeno in Aloud. Gli EPUB senza DRM, come quelli di Project Gutenberg o "
            "Standard Ebooks, funzionano.",
        ]),
        ("Legge i PDF, anche scansionati?", [
            "Sì. Apri un PDF da File o condividilo con Aloud. Aloud legge il testo in ordine, "
            "e in un PDF scansionato riconosce prima il testo sul dispositivo.",
        ]),
        ("Aloud funziona offline?", [
            "Sì. Ogni voce si scarica una volta, la prima volta che la usi. Poi la voce viene "
            "creata sul tuo iPhone, quindi Aloud legge in modalità aereo, in metropolitana o "
            "in volo. Per prendere un nuovo articolo serve internet; per ciò che è già sullo "
            "scaffale, no.",
        ]),
        ("Quali lingue sa leggere?", [
            "Dieci voci naturali leggono l'inglese, e altre quattro leggono più di trenta "
            "lingue, tra cui italiano, tedesco, spagnolo, francese e portoghese. L'app è in "
            "italiano, inglese, tedesco, spagnolo, francese e portoghese.",
        ]),
        ("Può tradurre quello che sto leggendo?", [
            "Sì, da iOS 18. Tocca il pulsante di traduzione nel lettore e scegli una lingua "
            "in **Tradurre in**. Il traduttore di Apple lavora sul tuo iPhone, quindi non "
            "viene inviato nulla. La pagina mostra ogni frase con la sua traduzione, e "
            "**Leggi ad alta voce la traduzione** fa leggere alla voce l'altra lingua.",
        ]),
        ("Quanto veloce può leggere?", [
            "Da 0,5× a 3×, senza voce da cartone animato. **Accorcia le pause** taglia il "
            "silenzio tra le frasi, così un articolo da 30 minuti entra in una passeggiata "
            "da 15.",
        ]),
        ("Aloud è gratis?", [
            "Aloud si scarica gratis, con tutte le voci e le funzioni. Lo scaffale gratuito "
            "contiene tre testi alla volta. Un acquisto una tantum, **Sblocca Aloud**, toglie "
            "il limite. Non c'è abbonamento. [Vedi su App Store](store).",
        ]),
        ("Posso portare la mia lista di lettura da Pocket o Instapaper?", [
            "Sì. Esporta i tuoi link da Pocket, Instapaper, Raindrop o i segnalibri del "
            "browser, poi in Aloud apri **Impostazioni** › **Importare da un file**. Ogni "
            "link arriva sullo scaffale, e Aloud scarica gli articoli in background.",
        ]),
        ("Aloud carica i miei documenti?", [
            "No. La voce viene creata sul tuo iPhone. Aloud scarica ogni voce una volta da un "
            "server pubblico e prende gli articoli che condividi dal loro sito, come un "
            "browser. **Sincronizza con iCloud** è facoltativo e salva lo scaffale come "
            "semplici file di testo nel tuo iCloud Drive. [Informativa sulla "
            "privacy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "ascoltare-articoli-e-libri",
        "title": "Come ascoltare articoli, PDF e libri EPUB su iPhone",
        "description": "Passo per passo: condividi un articolo da Safari, apri un PDF o un "
                       "EPUB, incolla un testo qualsiasi e fattelo leggere da Aloud con una "
                       "voce naturale creata sul tuo iPhone, alla tua velocità, offline.",
        "lead": "Aloud legge tutto ciò che puoi leggere: un articolo, un PDF, un libro EPUB o "
                "un testo che incolli. La voce viene creata sul tuo iPhone, quindi funziona "
                "offline e nulla di ciò che leggi viene caricato. Ecco come aggiungere ogni "
                "tipo di testo e come ascoltarlo.",
        "choose": [
            ("Articoli", "Condividili da Safari o da un'app"),
            ("PDF ed EPUB", "Aprili da File"),
            ("Qualsiasi testo", "Incollalo"),
        ],
        "steps": [
            ("Installa Aloud",
             "Scarica [Aloud da App Store](store). Funziona su iPhone e iPad con iOS 17 o "
             "successivo. La prima volta che premi play, la voce si scarica una volta. Poi "
             "funziona offline."),
            ("Condividi un articolo",
             "Apri l'articolo in Safari o in un'altra app, tocca **Condividi**, poi "
             "**Aloud**. L'articolo arriva sullo scaffale senza menu, pubblicità o commenti. "
             "Da Safari, Aloud legge la pagina come la vedi, quindi funzionano anche gli "
             "articoli dei siti in cui hai effettuato l'accesso."),
            ("Apri un PDF o un EPUB",
             "In Aloud, tocca **+** › **Importa un file** e scegli il file, oppure "
             "condividilo con Aloud dall'app File. I PDF scansionati vengono riconosciuti sul "
             "dispositivo. I libri EPUB conservano copertina e capitoli."),
            ("Incolla un testo qualsiasi",
             "Tocca **+** › **Incolla testo** per appunti, email o qualsiasi cosa tu abbia "
             "copiato. **Incolla un link** accetta un indirizzo web."),
            ("Premi play",
             "Apri un testo e premi play. La frase letta è evidenziata e il resto rimane "
             "attenuato. Tieni premuta la barra sul margine per scorrere tutto il testo. In "
             "un libro, tocca **Capitoli** nel menu ••• per partire da qualsiasi capitolo."),
            ("Scegli la velocità",
             "Tocca il pulsante della velocità e scegli tra 0,5× e 3×. Attiva **Accorcia le "
             "pause** per ridurre il silenzio tra le frasi."),
            ("Blocca l'iPhone",
             "Aloud continua a leggere a schermo bloccato. Usa i comandi della schermata di "
             "blocco o degli AirPods, e imposta il **Timer di stop** se ascolti a letto: alla "
             "fine la voce si abbassa piano."),
            ("Traducilo, se vuoi",
             "Da iOS 18, tocca il pulsante di traduzione e scegli una lingua in **Tradurre "
             "in**. Ogni frase appare con la sua traduzione, e **Leggi ad alta voce la "
             "traduzione** passa la voce all'altra lingua."),
        ],
        "tips": [
            ("Ricorda dove eri arrivato",
             "Ogni testo ricorda dove ti sei fermato, così puoi passare da un articolo a un "
             "libro e tornare alla stessa frase."),
            ("Modalità lettura",
             "Tocca il pulsante degli occhiali per nascondere il lettore audio e leggere da "
             "solo, con carattere, dimensione e carta a scelta in **Aspetto**."),
            ("La tua lista di lettura",
             "I link di Pocket, Instapaper, Raindrop o i segnalibri del browser entrano da "
             "**Impostazioni** › **Importare da un file**."),
            ("Prova gratis",
             "Lo scaffale gratuito contiene tre testi. Un solo acquisto toglie il limite, e "
             "non c'è abbonamento."),
        ],
        "updated": "Scritto per Aloud 3.2, ottobre 2026.",
        "cta_title": "Ascolta la tua lista di lettura",
        "cta_text": "Aloud legge articoli, PDF e libri EPUB con una voce naturale creata sul "
                    "tuo iPhone. Funziona offline. Paghi una volta, senza abbonamento.",
    },
}
