# Unfollowers in Italian ("tu", as in the App Store text). Keys are explained in en.py.

L = {
    "name": "Italiano",
    "path": "it/",
    "og_locale": "it_IT",
    "ui": {
        "nav_apps": "App",
        "nav_privacy": "Privacy",
        "nav_about": "Info",
        "nav_contact": "Contatti",
        "trademark": "Instagram e Facebook sono marchi di Meta Platforms, Inc. Unfollowers e "
                     "Unfriended sono app indipendenti, non affiliate, approvate o "
                     "sponsorizzate da Meta.",
        "rights": "Tutti i diritti riservati.",
        "overview": "Panoramica",
        "privacy": "Privacy",
        "view_on_store": "Vedi su App Store",
        "platform": "iPhone · iOS 17 o versioni successive",
        "screenshots": "Screenshot",
        "prev": "Screenshot precedenti",
        "next": "Screenshot successivi",
        "privacy_eyebrow": "Privacy",
        "read_policy": "Leggi l'informativa sulla privacy (in inglese)",
        "more_apps": "Altre app",
        "languages": "Lingue",
        "faq": "Domande frequenti",
        "summary": "Cosa scegliere",
        "tips": "Da sapere",
        "cta_more": "Scopri {name}",
    },
    "page": {
        "shots_dir": "it",
        "tagline": "Scopri chi ha smesso di seguirti su Instagram. Senza login.",
        "pricing": "Gratis · Sblocco una tantum",
        "intro": (
            "Instagram non ti dice chi ha smesso di seguirti. Il tuo export di dati sì.",
            "Unfollowers legge l'export ufficiale che scarichi tu stesso da Instagram e ti "
            "mostra cosa è cambiato. Non ti chiede mai la password.",
        ),
        "features": [
            ("Chi ha smesso di seguirti",
             "Seguito da un'importazione all'altra, con la data in cui è stato trovato ogni "
             "cambiamento."),
            ("Probabilmente ti ha bloccato",
             "Account spariti nello stesso momento dai tuoi follower e dai tuoi seguiti. "
             "L'app li segna come probabili blocchi."),
            ("Chi non ricambia il follow",
             "La lista classica, più i mutuals e le richieste di follow mai accettate."),
            ("Con chi interagisci di più",
             "I tuoi like, commenti e reazioni alle storie, contati dal tuo export."),
            ("La tua storia in grafici",
             "Grafici di crescita e di follow-back creati da ogni export che importi."),
            ("Niente login",
             "Nell'app non c'è nessuna schermata di accesso. La tua password resta tua."),
        ],
        "privacy_title": "Il tuo export resta sul tuo iPhone.",
        "privacy": [
            "Il tuo export di Instagram viene letto e salvato solo sul tuo iPhone.",
            "Niente account, niente analytics, niente pubblicità, niente tracciamento.",
            "Per controllare se un account esiste ancora, l'app invia a Instagram solo quel "
            "nome utente, senza fare login.",
        ],
        "note": "Unfollowers è un'app indipendente, non affiliata a Instagram o a Meta.",
        "stats": [],
        "reviews": [],
        "why": (
            "La tua password resta tua.",
            "La maggior parte delle app per i follower ti chiede la password di Instagram e "
            "poi usa il tuo account in background. Instagram avverte che far entrare app non "
            "autorizzate nel tuo account lo mette a rischio. Chi le usa spesso racconta di "
            "account bloccati, sospesi o con azioni bloccate. Unfollowers non ti chiede mai "
            "la password e non accede mai al tuo account. Legge l'export di dati che ti dà "
            "Instagram stesso. E non c'è abbonamento: un solo acquisto facoltativo sblocca "
            "tutto.",
        ),
        "shots": [
            "Vedi ogni unfollower: chi se n'è andato e quando, letto dal tuo export dei dati "
            "di Instagram.",
            "Probabilmente ti ha bloccato: account spariti nello stesso momento dai tuoi "
            "follower e dai tuoi seguiti.",
            "Non ricambiano il segui: cerca, ordina e apri qualsiasi profilo.",
            "A chi dai più hype: i tuoi like, commenti e reazioni alle storie, contati.",
            "Le tue stats in grafici: crescita e follow-back dalla tua cronologia.",
        ],
    },
    "guide_link": "Come scaricare i tuoi dati di Instagram",
    "faq": [
        ("Come vedere chi ha smesso di seguirmi su Instagram?", [
            "Instagram non mostra chi ha smesso di seguirti. Il tuo export di dati di "
            "Instagram contiene tutte le persone che ti seguono il giorno in cui lo scarichi. "
            "Unfollowers confronta due di questi export e ti mostra chi se n'è andato.",
            [
                "Scarica il tuo export di dati da Instagram, con Follower e persone seguite "
                "in formato JSON. [Ecco i passaggi](guide).",
                "Importa il file ZIP in Unfollowers. Vedi subito chi non ricambia il follow.",
                "Qualche settimana dopo, scarica un nuovo export e importa anche quello. "
                "Unfollowers ti mostra chi ha smesso di seguirti dal primo export, con la "
                "data in cui è stato trovato ogni cambiamento.",
            ],
            "Ogni nuovo export che importi allunga la tua cronologia.",
        ]),
        ("Esiste un'app sicura per vedere chi ha smesso di seguirmi senza login?", [
            "Unfollowers funziona senza login. Non ti chiede mai la password di Instagram e "
            "non accede mai al tuo account. Legge l'export di dati che scarichi tu stesso da "
            "Instagram.",
            "Molte app per i follower ti chiedono la password di Instagram e poi usano il tuo "
            "account in background. Instagram avverte che far entrare app non autorizzate "
            "nel tuo account lo mette a rischio. Con Unfollowers la tua password resta tua, e "
            "l'app non compie mai azioni sul tuo account.",
            "Il file viene letto e salvato sul tuo iPhone. Niente account, niente pubblicità, "
            "niente tracciamento.",
        ]),
        ("Come si scaricano i dati di Instagram?", [
            "Nell'app di Instagram apri il tuo profilo e tocca il menu. Poi vai su Centro "
            "gestione account › Le tue informazioni e autorizzazioni › Esporta le tue "
            "informazioni › Crea esportazione. In alcuni account il Centro gestione account "
            "si chiama Account Meta. Scegli Esporta sul dispositivo. Seleziona Follower e "
            "persone seguite, tutto il periodo e il formato JSON, poi tocca Avvia "
            "esportazione. Instagram ti avvisa quando il file è pronto, di solito in pochi "
            "minuti.",
            "[Guida passo passo](guide).",
        ]),
        ("Posso vedere chi mi ha bloccato su Instagram?", [
            "Instagram non segnala i blocchi, quindi nessuna app può saperlo con certezza. "
            "Quando qualcuno ti blocca, sparisce nello stesso momento dai tuoi follower e dai "
            "tuoi seguiti. Unfollowers segna questi account come probabili blocchi. Funziona "
            "solo con persone che ti seguivano e che seguivi anche tu.",
            "Un account eliminato, disattivato o che ha cambiato nome sparisce allo stesso "
            "modo. Il controllo dei profili (il vibe check) chiede a instagram.com se ogni "
            "nome utente esiste ancora e sposta gli account spariti in una lista a parte.",
        ]),
        ("Unfollowers è gratis?", [
            "Scaricare Unfollowers è gratis. La versione gratuita mostra chi non ricambia il "
            "follow, chi non ricambi tu e i tuoi mutuals. Un solo acquisto sblocca tutto il "
            "resto, comprese le liste di chi ha smesso di seguirti e di chi probabilmente ti "
            "ha bloccato. Non c'è abbonamento. L'app funziona su iPhone con iOS 17 o versioni "
            "successive.",
        ]),
        ("Esce qualcosa dal mio iPhone?", [
            "Il file del tuo export resta sul tuo iPhone. L'app lo legge e lo salva lì, e lo "
            "sviluppatore non ha server. L'unica funzione che usa internet è il controllo dei "
            "profili. Chiede a instagram.com se un account esiste ancora e invia solo quel "
            "nome utente, senza fare login. Parte quando tocchi il vibe check e, con l'app "
            "sbloccata, per un massimo di 30 nuovi account dopo ogni importazione. "
            "[Informativa sulla privacy (in inglese)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "scaricare-dati-instagram",
        "title": "Come scaricare i tuoi dati di Instagram (export in JSON)",
        "description": "Passo passo su iPhone: esporta i tuoi follower e le persone che "
                       "segui su Instagram in formato JSON, dall'inizio, e salva il file ZIP. "
                       "Poi scopri chi ha smesso di seguirti con Unfollowers.",
        "lead": "Instagram ti permette di scaricare una copia dei dati del tuo account. "
                "L'export contiene la lista completa dei tuoi follower e degli account che "
                "segui. Unfollowers legge questo file per mostrarti chi ha smesso di seguirti. "
                "Ecco come ottenerlo nell'app di Instagram su iPhone.",
        "choose": [
            ("Informazioni", "Follower e persone seguite"),
            ("Intervallo di date", "Dall'inizio"),
            ("Formato", "JSON"),
        ],
        "steps": [
            ("Apri il menu",
             "Nell'app di Instagram, tocca la tua immagine del profilo in basso a destra. Poi "
             "tocca il menu (☰) in alto a destra."),
            ("Centro gestione account",
             "Tocca **Centro gestione account**. In alcuni account si chiama **Account Meta**."),
            ("Le tue informazioni",
             "Tocca **Le tue informazioni e autorizzazioni**, poi **Esporta le tue "
             "informazioni**."),
            ("Crea l'esportazione",
             "Tocca **Crea esportazione**. Scegli il tuo profilo Instagram e tocca **Avanti**."),
            ("Esporta sul dispositivo",
             "Scegli **Esporta sul dispositivo**. Così il file viene salvato sul tuo iPhone."),
            ("Scegli i dati",
             "Nella schermata successiva scegli le informazioni da esportare. Seleziona "
             "**Follower e persone seguite**, nella parte dei collegamenti. Per vedere con chi "
             "interagisci di più, seleziona anche i Mi piace, i commenti e le interazioni con "
             "le storie. Puoi togliere il resto per avere un file più piccolo."),
            ("Dall'inizio, in JSON",
             "Nell'intervallo di date scegli tutto il periodo, dall'inizio. Nel formato "
             "scegli **JSON**. Unfollowers non legge il formato HTML."),
            ("Avvia l'esportazione",
             "Tocca **Avvia esportazione**. Instagram prepara il file. Di solito ci vogliono "
             "pochi minuti."),
            ("Scarica lo ZIP",
             "Instagram ti avvisa quando il file è pronto. Torna su **Esporta le tue "
             "informazioni** e scarica il file. Instagram può chiederti la password. La "
             "inserisci in Instagram stesso. Salva il file ZIP nell'app File."),
            ("Importalo in Unfollowers",
             "Apri Unfollowers, tocca il pulsante per importare e scegli il file ZIP. Non "
             "serve decomprimerlo."),
        ],
        "tips": [
            ("Due export mostrano chi se n'è andato",
             "Un export contiene i tuoi follower di un solo giorno. Importa un nuovo export "
             "ogni qualche settimana. Unfollowers li confronta e ti mostra chi se n'è andato "
             "dall'ultimo."),
            ("Il file resta disponibile quattro giorni",
             "Instagram conserva un export pronto per quattro giorni. Dopo, creane uno nuovo."),
            ("“Nessuna lista di follower trovata”",
             "Unfollowers mostra questo messaggio quando l'export è in formato HTML o quando "
             "non hai selezionato Follower e persone seguite. Crea un nuovo export in JSON con "
             "Follower e persone seguite."),
            ("Può volerci di più",
             "La maggior parte degli export è pronta in pochi minuti. A volte ci vuole di "
             "più. Instagram ti avvisa nell'app e via e-mail quando il tuo è pronto."),
        ],
        "updated": "Passaggi verificati sul Centro assistenza di Instagram a ottobre 2026.",
        "cta_title": "Scopri chi ha smesso di seguirti",
        "cta_text": "Unfollowers legge questo file sul tuo iPhone. Ti mostra chi ha smesso di "
                    "seguirti, chi probabilmente ti ha bloccato e chi non ricambia il follow. "
                    "Senza login e senza password.",
    },
}
