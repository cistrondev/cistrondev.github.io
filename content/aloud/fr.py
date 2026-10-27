# Aloud in French ("vous", as in the app). Keys are explained in
# content/unfollowers/en.py; facts to keep true are in en.py. Button names are
# the app's French strings (Aloud/Localizable.xcstrings).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "fr.py"))["L"]["ui"]

L = {
    "name": "Français",
    "path": "fr/",
    "og_locale": "fr_FR",
    "ui": {
        **_ui,
        "summary": "Ce qu'Aloud lit",
        "tips": "Bon à savoir",
        "appearance": "Apparence des captures",
        "light": "Clair",
        "dark": "Sombre",
        "what_people_say": "Ce qu'en disent les gens.",
    },
    "page": {
        "shots_dir": "fr",
        "tagline": "Tout ce qui se lit, lu à voix haute.",
        "pricing": "Essai gratuit · Achat unique",
        "platform": "iPhone et iPad · iOS 17 ou version ultérieure",
        "intro": (
            "Partagez un article, ouvrez un PDF ou collez n'importe quel texte.",
            "Aloud vous le lit d'une voix naturelle créée sur votre iPhone, phrase après "
            "phrase, et retient toujours où vous en êtes.",
        ),
        "features": [
            ("Des voix naturelles, sur l'appareil",
             "Dix voix pour l'anglais et quatre qui lisent trente autres langues, dont le "
             "français. Aucun serveur ne parle à votre place, donc Aloud continue de lire en "
             "mode avion."),
            ("Articles, PDF, livres",
             "Partagez depuis n'importe quel navigateur, ouvrez des PDF et des livres EPUB "
             "depuis Fichiers, même des PDF scannés, ou collez votre propre texte."),
            ("Pour suivre la lecture",
             "La phrase en cours est mise en évidence. Maintenez le doigt sur la barre de la "
             "marge pour parcourir tout le document."),
            ("Plus vite, si vous voulez",
             "De 0,5× à 3× sans voix de dessin animé, avec des pauses raccourcies à chaque "
             "point si vous le souhaitez."),
            ("Pour vos trajets",
             "Continue de lire écran verrouillé, avec les commandes de l'écran verrouillé et "
             "des AirPods, et un minuteur de veille qui baisse doucement le son."),
            ("Sur tous vos appareils",
             "La synchronisation iCloud est facultative et range votre étagère en simples "
             "fichiers texte dans votre propre iCloud Drive."),
        ],
        "privacy_title": "Privé par conception.",
        "privacy": [
            "La voix est créée sur votre iPhone. Vos documents ne sont jamais envoyés.",
            "Les voix se téléchargent une fois depuis un serveur public. Les articles que "
            "vous partagez sont récupérés sur leur propre site, comme le ferait un "
            "navigateur.",
            "Aucun compte, aucune statistique, aucune pub, aucun pistage.",
        ],
        "note": "",
        "reviews": [],
        "why": (
            "Pas de cloud. Pas d'abonnement.",
            "Beaucoup d'apps de synthèse vocale connues créent leurs voix sur leurs propres "
            "serveurs : les articles et documents que vous écoutez y sont donc envoyés "
            "d'abord, et leurs formules premium peuvent coûter 139 $ par an, ou 29 $ par "
            "mois, soit près de 350 $ par an. Aloud crée chaque voix directement sur votre "
            "iPhone : ce que vous lisez n'est jamais envoyé nulle part pour être lu. Et il "
            "n'y a pas d'abonnement : un seul achat facultatif, à vous pour toujours.",
        ),
        "shots": [
            "Tout ce qui se lit, Aloud vous le lit. Articles, PDF, notes, lus d'une voix naturelle, phrase après phrase.",
            "Venez à bout de la liste de lecture. Écoutez dans le métro, en marchant, en faisant la vaisselle.",
            "Fonctionne hors ligne. Partout. La voix se télécharge une seule fois.",
            "Sans abonnement. Sans pub. Sans pistage.",
            "Des voix naturelles. Toutes les langues. Dix voix pour l'anglais, quatre qui lisent trente autres langues, créées sur votre iPhone.",
            "Mode lecteur : lisez à votre façon.",
            "Deux fois plus vite. Moitié moins de temps. De 0,5× à 3×, avec moins de silence entre les phrases.",
            "Votre étagère, sur tous vos appareils, en fichiers texte dans iCloud Drive.",
            "Lisez-le dans votre langue : n'importe quel texte traduit sur l'appareil, phrase à côté de phrase.",
        ],
        "duo": {
            "title": "Sur iPhone Duo",
            "sub": "Fermé, vous écoutez. Ouvert, vous lisez.",
            "items": [
                ("cover", "cover", "Fermé", "La voix continue sur l'écran extérieur.",
                 "Aloud sur l'écran extérieur de l'iPhone Duo : la voix continue de lire, avec les commandes de lecture."),
                ("book", "spread", "À demi ouvert", "Deux pages face à face, à n'importe quel angle.",
                 "Aloud sur l'iPhone Duo à demi ouvert : deux pages face à face."),
                ("flat", "spread", "Ouvert", "Une traduction ? L'original et la traduction côte à côte.",
                 "Aloud sur l'iPhone Duo ouvert : l'original espagnol sur la page de gauche, la "
                 "traduction anglaise sur celle de droite, ligne à ligne."),
            ],
        },
    },
    "guide_link": "Comment écouter des articles, des PDF et des livres EPUB sur iPhone",
    "faq": [
        ("Quelle app de synthèse vocale pour iPhone sans abonnement ?", [
            "Aloud lit à voix haute les articles, les PDF, les livres EPUB et n'importe quel "
            "texte, d'une voix naturelle. L'app est gratuite, et un seul achat intégré lève "
            "la limite pour toujours. Il n'y a pas d'abonnement et rien ne se renouvelle.",
            "Les voix sont créées sur votre iPhone ou iPad : ce que vous lisez n'est jamais "
            "envoyé pour être lu, et Aloud continue de lire sans connexion. Aucun compte, "
            "aucune pub, aucun pistage.",
        ]),
        ("Comment écouter un article sur iPhone ?", [
            [
                "Ouvrez l'article dans Safari ou dans une autre app.",
                "Touchez **Partager**, puis **Aloud**.",
                "Ouvrez Aloud et lancez la lecture. La phrase en cours est mise en évidence "
                "sur la page.",
            ],
            "Quand vous partagez depuis Safari, Aloud lit la page telle que Safari "
            "l'affiche : les articles des sites où vous êtes connecté passent aussi. Les "
            "liens partagés depuis les apps Facebook, Messenger et Instagram fonctionnent "
            "également. [Guide pas à pas](guide).",
        ]),
        ("Aloud peut-il transformer un EPUB en livre audio ?", [
            "Oui. Ouvrez un fichier EPUB depuis l'app Fichiers, ou touchez **+** › "
            "**Importer un fichier**. Aloud garde la couverture et les chapitres du livre. "
            "La liste **Chapitres** indique la durée d'écoute de chaque chapitre, et vous "
            "pouvez commencer par n'importe lequel. Votre position est retenue : un long "
            "livre s'écoute comme un livre audio.",
            "Les livres achetés avec une protection contre la copie ne s'ouvrent dans "
            "aucune autre app, Aloud compris. Les EPUB sans DRM, comme ceux de Project "
            "Gutenberg ou de Standard Ebooks, fonctionnent.",
        ]),
        ("Lit-il les PDF, même scannés ?", [
            "Oui. Ouvrez un PDF depuis Fichiers ou partagez-le avec Aloud. Aloud lit le "
            "texte dans l'ordre, et pour un PDF scanné il reconnaît d'abord le texte sur "
            "l'appareil.",
        ]),
        ("Aloud fonctionne-t-il hors ligne ?", [
            "Oui. Chaque voix se télécharge une fois, à sa première utilisation. Ensuite la "
            "voix est créée sur votre iPhone : Aloud lit en mode avion, dans le métro ou en "
            "vol. Récupérer un nouvel article demande internet ; ce qui est déjà sur votre "
            "étagère, non.",
        ]),
        ("Quelles langues peut-il lire ?", [
            "Dix voix naturelles lisent l'anglais, et quatre autres lisent plus de trente "
            "langues, dont le français, l'allemand, l'espagnol, l'italien et le portugais. "
            "L'app est en français, anglais, allemand, espagnol, italien et portugais.",
        ]),
        ("Peut-il traduire ce que je lis ?", [
            "Oui, à partir d'iOS 18. Touchez le bouton de traduction dans le lecteur et "
            "choisissez une langue sous **Traduire en**. Le traducteur d'Apple travaille sur "
            "votre iPhone : rien n'est envoyé. La page montre alors chaque phrase avec sa "
            "traduction, et **Lire la traduction à voix haute** fait lire l'autre langue.",
        ]),
        ("À quelle vitesse peut-il lire ?", [
            "De 0,5× à 3×, sans voix de dessin animé. **Raccourcir les pauses** coupe le "
            "silence entre les phrases : un article de 30 minutes tient dans une marche de "
            "15 minutes.",
        ]),
        ("Aloud est-il gratuit ?", [
            "Aloud est gratuit, avec toutes les voix et toutes les fonctions. L'étagère "
            "gratuite contient trois textes à la fois. Un achat unique, **Déverrouiller "
            "Aloud**, lève la limite. Il n'y a pas d'abonnement. [Voir sur l'App "
            "Store](store).",
        ]),
        ("Puis-je importer ma liste de lecture depuis Pocket ou Instapaper ?", [
            "Oui. Exportez vos liens depuis Pocket, Instapaper, Raindrop ou les favoris de "
            "votre navigateur, puis dans Aloud ouvrez **Réglages** › **Importer depuis un "
            "fichier**. Chaque lien arrive sur votre étagère, et Aloud récupère les articles "
            "en arrière-plan.",
        ]),
        ("Aloud envoie-t-il mes documents ?", [
            "Non. La voix est créée sur votre iPhone. Aloud télécharge chaque voix une fois "
            "depuis un serveur public et récupère les articles que vous partagez sur leur "
            "propre site, comme un navigateur. **Synchroniser avec iCloud** est facultatif "
            "et range votre étagère en simples fichiers texte dans votre propre iCloud "
            "Drive. [Politique de confidentialité](privacy).",
        ]),
    ],
    "guide": {
        "slug": "ecouter-articles-et-livres",
        "title": "Comment écouter des articles, des PDF et des livres EPUB sur iPhone",
        "description": "Pas à pas : partagez un article depuis Safari, ouvrez un PDF ou un "
                       "EPUB, collez n'importe quel texte, et laissez Aloud vous le lire "
                       "d'une voix naturelle créée sur votre iPhone, à votre vitesse, hors "
                       "ligne.",
        "lead": "Aloud lit tout ce qui se lit : un article web, un PDF, un livre EPUB ou un "
                "texte que vous collez. La voix est créée sur votre iPhone : elle fonctionne "
                "hors ligne et rien de ce que vous lisez n'est envoyé. Voici comment ajouter "
                "chaque type de texte et comment l'écouter.",
        "choose": [
            ("Articles", "À partager depuis Safari ou une app"),
            ("PDF et EPUB", "À ouvrir depuis Fichiers"),
            ("Tout texte", "À coller"),
        ],
        "steps": [
            ("Installez Aloud",
             "Téléchargez [Aloud sur l'App Store](store). L'app fonctionne sur iPhone et "
             "iPad avec iOS 17 ou version ultérieure. À la première lecture, la voix se "
             "télécharge une fois. Ensuite, elle fonctionne hors ligne."),
            ("Partagez un article",
             "Ouvrez l'article dans Safari ou une autre app, touchez **Partager**, puis "
             "**Aloud**. L'article arrive sur votre étagère sans menus, pubs ni "
             "commentaires. Depuis Safari, Aloud lit la page telle que vous la voyez : les "
             "articles des sites où vous êtes connecté fonctionnent."),
            ("Ouvrez un PDF ou un EPUB",
             "Dans Aloud, touchez **+** › **Importer un fichier** et choisissez le fichier, "
             "ou partagez-le avec Aloud depuis l'app Fichiers. Les PDF scannés sont reconnus "
             "sur l'appareil. Les livres EPUB gardent leur couverture et leurs chapitres."),
            ("Collez n'importe quel texte",
             "Touchez **+** › **Coller du texte** pour des notes, des e-mails ou tout ce que "
             "vous avez copié. **Coller un lien** accepte une adresse web."),
            ("Lancez la lecture",
             "Ouvrez un texte et lancez la lecture. La phrase lue est mise en évidence, le "
             "reste reste estompé. Maintenez le doigt sur la barre de la marge pour "
             "parcourir tout le texte. Dans un livre, touchez **Chapitres** dans le menu ••• "
             "pour commencer à n'importe quel chapitre."),
            ("Réglez la vitesse",
             "Touchez le bouton de vitesse et choisissez entre 0,5× et 3×. Activez "
             "**Raccourcir les pauses** pour réduire le silence entre les phrases."),
            ("Verrouillez votre iPhone",
             "Aloud continue de lire écran verrouillé. Utilisez les commandes de l'écran "
             "verrouillé ou des AirPods, et réglez le **Minuteur de veille** si vous écoutez "
             "au lit : à la fin, la voix baisse doucement."),
            ("Traduisez, si vous voulez",
             "À partir d'iOS 18, touchez le bouton de traduction et choisissez une langue "
             "sous **Traduire en**. Chaque phrase apparaît avec sa traduction, et **Lire la "
             "traduction à voix haute** fait passer la voix à l'autre langue."),
        ],
        "tips": [
            ("Votre position est retenue",
             "Chaque texte retient où vous vous êtes arrêté : passez d'un article à un livre "
             "et revenez à la même phrase."),
            ("Mode lecteur",
             "Touchez le bouton des lunettes pour masquer le lecteur audio et lire vous-même, "
             "avec la police, la taille et le papier de votre choix dans **Apparence**."),
            ("Votre liste de lecture",
             "Les liens de Pocket, Instapaper, Raindrop ou des favoris du navigateur arrivent "
             "par **Réglages** › **Importer depuis un fichier**."),
            ("Essai gratuit",
             "L'étagère gratuite contient trois textes. Un seul achat lève la limite, et il "
             "n'y a pas d'abonnement."),
        ],
        "updated": "Rédigé pour Aloud 3.2, octobre 2026.",
        "cta_title": "Écoutez votre liste de lecture",
        "cta_text": "Aloud lit les articles, les PDF et les livres EPUB d'une voix naturelle "
                    "créée sur votre iPhone. Hors ligne. Un seul paiement, sans abonnement.",
    },
}
