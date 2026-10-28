# Pedometer in French ("vous", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# App words from Shared/Localizable.xcstrings (Connecter, Marche, Course, Marches
# et courses, Objectifs quotidiens, Soutenir Pedometer); iOS words are Apple's.
# French spacing: a no-break space before ":" and a narrow one before "?" and "!".
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "fr.py"))["L"]["ui"]

L = {
    "name": "Français",
    "path": "fr/",
    "og_locale": "fr_FR",
    "ui": {**_ui, "summary": "Widgets de l'écran verrouillé", "cta_more": "À propos de {name}"},
    "page": {
        "shots_dir": "fr",
        "tagline": "Vos pas sur l'écran verrouillé.",
        "pricing": "Gratuit",
        "intro": (
            "Les pas, la distance et les étages montés, en chiffres et en graphiques clairs.",
            "Pedometer lit Apple Santé et affiche le compte du jour sur votre écran "
            "verrouillé et votre écran d'accueil. Votre iPhone compte vos pas tout seul, et "
            "les pas de l'Apple Watch sont inclus si vous en portez une.",
        ),
        "features": [
            ("Aujourd'hui",
             "Vos pas face à votre objectif, avec ce qu'il reste à faire. La distance et les "
             "étages face à leurs objectifs, avec l'énergie en activité et la vitesse de "
             "marche."),
            ("Marche et course",
             "Enregistrez une marche ou une course en GPS : votre parcours sur la carte, "
             "avec la vitesse ou l'allure, l'altitude, le dénivelé et les calories. Chaque "
             "sortie est enregistrée dans Apple Santé avec son parcours."),
            ("Fréquence cardiaque en direct",
             "Avec des AirPods Pro 3, des Powerbeats Pro 2 ou une ceinture cardio "
             "Bluetooth, votre fréquence cardiaque s'affiche en direct (iOS 26)."),
            ("Sur l'écran verrouillé",
             "En chemin, la durée, la distance, la vitesse, le pouls et les calories "
             "restent sur l'écran verrouillé, avec un bouton pause."),
            ("Partager une sortie",
             "Une image de chaque marche ou course, avec la carte et vos chiffres, pour "
             "l'app de votre choix."),
            ("Vos objectifs",
             "Fixez un objectif quotidien pour les pas, la distance et les étages. Ils "
             "commencent à 10 000 pas, 8 km et 10 étages."),
            ("Historique",
             "Un graphique par chiffre, pour la dernière semaine, le dernier mois ou la "
             "dernière année, avec la moyenne par jour et l'écart avec la période précédente."),
            ("Widgets de l'écran verrouillé",
             "Les pas et la distance, chacun dans un anneau qui se ferme à votre objectif, "
             "et les étages, avec un personnage qui monte un escalier."),
            ("Widget de l'écran d'accueil",
             "La même carte que dans l'app, petite, moyenne ou grande. En clair, en sombre "
             "ou automatique, et avec les pas seuls si vous préférez."),
            ("Par heure",
             "Les pas du jour heure par heure, à côté de votre journée habituelle des "
             "quatre dernières semaines."),
            ("Records",
             "Les totaux de chaque mois et de chaque année, et vos meilleurs jour, semaine "
             "et mois pour les pas, les étages et la vitesse de marche."),
            ("Votre couleur",
             "Graphite, bleu, vert, orange, rose ou violet pour les barres d'objectif, les "
             "graphiques et le widget."),
        ],
        "privacy_title": "Rien ne quitte votre iPhone.",
        "privacy": [
            "Lit Apple Santé et n'y écrit que les marches et courses que vous enregistrez.",
            "Votre position n'est utilisée que pendant un enregistrement et reste sur "
            "votre iPhone.",
            "Tout est compté et stocké sur votre iPhone. Rien n'est envoyé.",
            "Sans compte, sans analyse, sans suivi.",
        ],
        "note": "Pedometer n'est pas un dispositif médical et ne donne pas de conseils médicaux.",
        "shots": [
            "Vos pas sur l'écran verrouillé : un widget podomètre, avec la distance et les étages à côté.",
            "Chaque pas compte : lit Apple Santé, pas de l'Apple Watch inclus.",
            "Marche et course sur la carte : vitesse, altitude, calories et fréquence cardiaque.",
            "En direct, puis à partager : l'écran verrouillé en chemin, une image après.",
            "Aussi sur votre écran d'accueil : la même carte, petite ou moyenne.",
            "Votre journée, heure par heure : les pas du jour à côté d'une journée habituelle.",
            "Vos records : meilleurs jour, semaine et mois, et les totaux.",
            "Choisissez votre couleur : six couleurs pour les barres, les graphiques et le widget.",
            "Votre semaine en un coup d'œil : les barres du jour, la moyenne et l'évolution.",
            "Rien ne quitte votre iPhone : sans compte, sans suivi.",
        ],
    },
    "guide_link": "Comment afficher un podomètre sur l'écran verrouillé de l'iPhone",
    "faq": [
        ("Existe-t-il un podomètre gratuit pour iPhone, sans abonnement ?", [
            "Pedometer est gratuit, sans abonnement et sans compte. Il affiche vos pas, la "
            "distance et les étages montés en chiffres et en graphiques clairs, et les "
            "place en widgets sur l'écran verrouillé et l'écran d'accueil. Il enregistre "
            "aussi les marches et les courses en GPS. Une cagnotte de pourboires facultative "
            "ne débloque rien. [Voir sur l'App Store](store).",
        ]),
        ("Comment afficher mes pas sur l'écran verrouillé de l'iPhone ?", [
            [
                "Installez Pedometer, ouvrez-le et touchez **Connecter** pour qu'il puisse "
                "lire Apple Santé.",
                "Maintenez le doigt sur l'écran verrouillé, touchez **Personnaliser**, puis "
                "choisissez l'écran verrouillé.",
                "Touchez la zone des widgets sous l'heure, choisissez **Pedometer** et "
                "ajoutez les pas, la distance ou les étages montés.",
                "Touchez **OK**.",
            ],
            "Les widgets des pas et de la distance sont dans un anneau qui se ferme à votre "
            "objectif. [Le guide pas à pas](guide).",
        ]),
        ("Faut-il une Apple Watch ?", [
            "Non. Votre iPhone compte vos pas tout seul quand vous le portez sur vous. Si "
            "vous portez aussi une Apple Watch, Pedometer lit Apple Santé, qui réunit les "
            "pas des deux sans les compter deux fois.",
        ]),
        ("Peut-il enregistrer les marches et les courses en GPS ?", [
            "Oui. Touchez **Marche** ou **Course** sous **Marches et courses**. La carte "
            "trace votre parcours et affiche la durée, la distance, la vitesse ou l'allure, "
            "les calories, l'altitude et le dénivelé. En chemin, les chiffres restent sur "
            "l'écran verrouillé avec un bouton pause. Chaque sortie est enregistrée dans "
            "Apple Santé avec son parcours, et vous pouvez en partager une image.",
        ]),
        ("Peut-il afficher ma fréquence cardiaque sans Apple Watch ?", [
            "Oui, sous iOS 26. Avec des AirPods Pro 3, des Powerbeats Pro 2 ou une ceinture "
            "cardio Bluetooth, votre fréquence cardiaque s'affiche en direct pendant une "
            "marche ou une course.",
        ]),
        ("Puis-je changer mon objectif de pas quotidien ?", [
            "Oui. Sous **Objectifs quotidiens**, fixez un objectif pour les pas, la distance "
            "et les étages. Ils commencent à 10 000 pas, 8 km et 10 étages. Les anneaux des "
            "widgets se ferment à vos objectifs.",
        ]),
        ("Pedometer est-il vraiment gratuit ?", [
            "Oui. Toutes les fonctions sont gratuites et il n'y a pas d'abonnement. Dans "
            "**Réglages** › **Soutenir Pedometer**, vous pouvez laisser un pourboire si vous "
            "le souhaitez. Il est facultatif et ne débloque rien.",
        ]),
        ("Pedometer envoie-t-il mes données de santé ?", [
            "Non. Tout est compté et stocké sur votre iPhone, et rien n'est envoyé. "
            "Pedometer lit Apple Santé et n'y écrit que les marches et courses que vous "
            "enregistrez. Votre position n'est utilisée que pendant un enregistrement. Sans "
            "compte, sans analyse, sans suivi. [Politique de confidentialité (en "
            "anglais)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "podometre-ecran-verrouille",
        "title": "Comment afficher un podomètre sur l'écran verrouillé de l'iPhone",
        "description": "Pas à pas : ajouter un widget podomètre gratuit sur l'écran "
                       "verrouillé et l'écran d'accueil de l'iPhone, avec la distance et "
                       "les étages à côté. Sans Apple Watch ni abonnement.",
        "lead": "Votre iPhone compte déjà vos pas. Pedometer affiche ce chiffre sur l'écran "
                "verrouillé, pour que vous le voyiez chaque fois que vous prenez le "
                "téléphone. Cela prend une minute environ, sans Apple Watch.",
        "choose": [
            ("Pas", "Dans un anneau qui se ferme à l'objectif"),
            ("Distance", "Dans un anneau, en km ou en miles"),
            ("Étages montés", "Un personnage monte un escalier"),
        ],
        "steps": [
            ("Installer Pedometer",
             "Téléchargez [Pedometer sur l'App Store](store). Il est gratuit, sans compte."),
            ("Connecter Apple Santé",
             "Ouvrez Pedometer et touchez **Connecter**. Autorisez la lecture des pas, de la "
             "distance et des étages montés. Votre iPhone les compte depuis toujours, donc "
             "votre historique apparaît tout de suite."),
            ("Fixer vos objectifs",
             "Choisissez un objectif quotidien pour les pas, la distance et les étages sous "
             "**Objectifs quotidiens**. Les anneaux des widgets se ferment quand vous les "
             "atteignez."),
            ("Modifier l'écran verrouillé",
             "Verrouillez votre iPhone, réveillez-le, puis maintenez le doigt sur l'écran "
             "verrouillé. Touchez **Personnaliser** et choisissez l'écran verrouillé."),
            ("Ajouter le widget",
             "Touchez la zone des widgets sous l'heure. Trouvez **Pedometer** dans la liste "
             "et touchez les pas, la distance ou les étages montés. Vous pouvez en ajouter "
             "plusieurs."),
            ("Toucher OK",
             "Vos pas sont maintenant sur l'écran verrouillé et se mettent à jour pendant la "
             "journée."),
            ("Sur l'écran d'accueil aussi",
             "Maintenez le doigt sur un espace libre de l'écran d'accueil, touchez "
             "**Modifier**, puis **Ajouter un widget**. Cherchez Pedometer et choisissez la "
             "taille petite, moyenne ou grande. La grande ajoute la journée heure par heure."),
        ],
        "tips": [
            ("Clair, sombre ou les pas seuls",
             "Maintenez le doigt sur le widget de l'écran d'accueil et choisissez **Modifier "
             "le widget** pour l'afficher en clair ou en sombre, ou n'afficher que les pas."),
            ("Choisir une couleur",
             "Graphite, bleu, vert, orange, rose ou violet, pour les barres d'objectif, les "
             "graphiques et le widget."),
            ("Vous partez marcher ?",
             "Touchez **Marche** ou **Course** dans l'app pour enregistrer votre parcours en "
             "GPS. Les chiffres restent sur l'écran verrouillé en chemin."),
            ("Rien ne quitte votre iPhone",
             "Pedometer n'a pas de compte et n'envoie rien. Il lit Apple Santé sur votre "
             "iPhone."),
        ],
        "updated": "Rédigé pour Pedometer 1.5 sous iOS 26, octobre 2026.",
        "cta_title": "Vos pas, d'un coup d'œil",
        "cta_text": "Un podomètre gratuit pour l'écran verrouillé et l'écran d'accueil, avec "
                    "les marches et les courses sur la carte. Sans compte, sans abonnement.",
    },
}
