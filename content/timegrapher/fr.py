# Timegrapher in French ("vous", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# Button names are the app's French strings (Timegrapher Localizable.xcstrings):
# Ajouter une montre, Mesurer, Mesurer en positions, Contrôler le magnétisme,
# Marche par photo, Angle de levée, Identifier d'après la photo, Guide (tab).
# French spacing: a no-break space before ":" and a narrow one before "?" and "!".
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "fr.py"))["L"]["ui"]

L = {
    "name": "Français",
    "path": "fr/",
    "og_locale": "fr_FR",
    "ui": {
        **_ui,
        "summary": "En bref",
        "cta_more": "À propos de {name}",
        "what_people_say": "Ce qu'on en dit.",
    },
    "page": {
        "shots_dir": "fr",
        "tagline": "Le chronocomparateur de l'horloger, dans votre iPhone.",
        "pricing": "Première montre gratuite · Pro en achat unique",
        "intro": (
            "Marche, amplitude et erreur de repère en une trentaine de secondes.",
            "Timegrapher écoute votre montre mécanique avec le microphone de l'iPhone, "
            "puis réunit votre collection, chaque mesure et la valeur de chaque montre "
            "au même endroit.",
        ),
        "features": [
            ("Les valeurs qui comptent",
             "Les secondes d'avance ou de retard par jour, l'angle parcouru par le "
             "balancier et la symétrie du tic et du tac. Fréquence détectée de 18 000 à "
             "36 000 A/h."),
            ("Des valeurs qui restent stables",
             "L'app suit le bruit de fond de la pièce et rejette les sons parasites. "
             "L'amplitude vient de l'angle de levée de votre calibre."),
            ("Votre collection",
             "Chaque montre avec sa photo, sa référence, son mouvement et son angle de "
             "levée. Chaque mesure est conservée et tracée. « Identifier d'après la "
             "photo » suggère la marque et le modèle."),
            ("La marche sur une journée au poignet",
             "Photographiez le cadran aujourd'hui et demain. Timegrapher compare les "
             "photos avec l'horloge de l'iPhone et montre comment la montre a marché à "
             "votre poignet."),
            ("Savoir ce qu'elle vaut",
             "Les prix demandés sur Chrono24 pour votre référence exacte, avec la "
             "médiane calculée sur votre iPhone."),
            ("Contrôle de magnétisme",
             "Un spiral aimanté est la cause la plus fréquente d'une montre qui se met "
             "soudain à avancer. Le magnétomètre de l'iPhone vous dit s'il faut la "
             "démagnétiser."),
        ],
        "privacy_title": "Rien d'enregistré. Rien de conservé.",
        "privacy": [
            "Le son du microphone est analysé en direct et n'est jamais enregistré ni conservé.",
            "Votre collection et vos mesures restent uniquement sur votre iPhone.",
            "Le contrôle de prix facultatif cherche la référence de votre montre sur Chrono24.",
            "« Identifier d'après la photo » n'envoie la photo au Private Cloud Compute "
            "d'Apple que lorsque vous touchez le bouton. Apple ne la garde pas et le "
            "développeur ne la voit jamais.",
            "L'onglet Horloge demande l'heure au serveur de temps d'Apple. La requête ne "
            "contient aucune donnée personnelle.",
        ],
        "note": "",
        "reviews": [],
        "shots": [
            "Votre iPhone est un chronocomparateur : marche, amplitude et erreur de repère en 30 secondes.",
            "Des valeurs qui restent stables : même les mouvements discrets, même dans le bruit.",
            "Votre collection, un seul établi : âge, état et valeur de chaque montre.",
            "Voir la dérive avant qu'elle compte : chaque mesure conservée et tracée.",
            "Savoir ce qu'elle vaut : la médiane Chrono24 pour votre référence exacte.",
            "Votre montre est-elle aimantée ? Contrôlé en dix secondes.",
            "La marche sur une journée au poignet : deux photos, à un jour d'écart.",
        ],
    },
    "guide_link": "Comment vérifier la précision de votre montre mécanique avec un iPhone",
    "faq": [
        ("Un iPhone peut-il mesurer la précision de ma montre mécanique ?", [
            "Oui. Timegrapher écoute la montre avec le microphone intégré de l'iPhone et "
            "fonctionne comme le chronocomparateur d'un horloger. En une trentaine de "
            "secondes, il affiche la marche (secondes d'avance ou de retard par jour), "
            "l'amplitude (l'angle parcouru par le balancier) et l'erreur de repère "
            "(l'écart entre le tic et le tac).",
            "Il fonctionne avec les montres automatiques et à remontage manuel. La première "
            "montre est gratuite, et il n'y a pas d'abonnement. [Voir sur l'App Store](store).",
        ]),
        ("Comment mesurer ma montre avec Timegrapher ?", [
            [
                "Remontez la montre et installez-vous dans un endroit calme.",
                "Touchez **Ajouter une montre** et indiquez le mouvement et, si vous le "
                "connaissez, son angle de levée.",
                "Touchez **Mesurer** et posez fermement le bas de l'iPhone sur la montre, "
                "de préférence sur le verre.",
                "Ne bougez plus. La mesure s'arrête seule à 0:30 et affiche la marche, "
                "l'amplitude, l'erreur de repère et un verdict.",
            ],
            "[Le guide pas à pas](guide).",
        ]),
        ("Quelles sont de bonnes valeurs de marche, d'amplitude et d'erreur de repère ?", [
            "Voici les seuils que Timegrapher utilise pour son verdict :",
            [
                "**Marche :** à ±5 secondes par jour, on est dans les tolérances "
                "chronomètre. Jusqu'à ±15, c'est correct pour un usage quotidien. À partir "
                "de ±30, la montre doit être réglée.",
                "**Amplitude :** de 250° à 315°, c'est sain, montre remontée et cadran vers "
                "le haut. Sous 220°, une révision approche, et sous 200° les huiles sont "
                "probablement sèches. Au-dessus de 315°, le balancier risque de rebattre.",
                "**Erreur de repère :** sous 0,3 ms, la montre est bien au repère. À partir "
                "de 0,8 ms, un réglage se justifie, et au-delà de 1,5 ms elle est nettement "
                "hors repère.",
            ],
            "La marche change selon la position : notez si la montre était cadran en haut, "
            "cadran en bas ou couronne en bas. **Mesurer en positions** les prend l'une "
            "après l'autre.",
        ]),
        ("Comment savoir si ma montre est aimantée ?", [
            "Un spiral aimanté est la cause la plus fréquente d'une montre mécanique qui se "
            "met soudain à avancer, souvent de plusieurs minutes par jour. Timegrapher le "
            "vérifie avec le magnétomètre de l'iPhone : touchez **Contrôler le magnétisme**, "
            "mesurez le champ ambiant, puis tenez la montre contre le dos de l'iPhone. La "
            "différence donne la réponse.",
            "Retirez d'abord toute coque, porte-cartes ou support magnétique. Chaque contrôle "
            "est conservé : un contrôle avant et après la démagnétisation montre si elle a "
            "fonctionné.",
        ]),
        ("Quel angle de levée indiquer ?", [
            "L'angle de levée est une caractéristique du mouvement, et Timegrapher s'en sert "
            "pour calculer l'amplitude. Beaucoup de mouvements suisses ont 52°, mais "
            "beaucoup d'autres non : cherchez la valeur de votre calibre. Un angle de levée "
            "erroné est la cause habituelle d'une amplitude fausse sur téléphone. La marche "
            "et l'erreur de repère n'en dépendent pas.",
        ]),
        ("Un chronocomparateur sur téléphone est-il aussi précis qu'une machine d'établi ?", [
            "Timegrapher mesure chaque tic à la fraction de milliseconde près et en ajuste "
            "des milliers sur l'horloge de l'iPhone, selon le principe de la machine "
            "d'établi. Une pièce calme et un contact ferme donnent les meilleures valeurs. "
            "Les écouteurs Bluetooth compressent le son : déconnectez-les pour que le "
            "microphone de l'iPhone écoute.",
            "Les résultats sont indicatifs. Pour décider d'une révision, la machine d'établi "
            "et le jugement d'un horloger restent la référence.",
        ]),
        ("Puis-je savoir comment ma montre marche au poignet sur une journée ?", [
            "Oui. **Marche par photo** compare deux photos du cadran prises à un jour "
            "d'écart. Chaque photo enregistre l'heure exacte de la prise : la position de "
            "la trotteuse montre donc l'avance ou le retard pris pendant que vous la "
            "portiez.",
        ]),
        ("Fonctionne-t-il avec les montres à quartz ?", [
            "Non. Une montre à quartz bat au rythme d'un cristal et avance son aiguille une "
            "fois par seconde : il n'y a pas de balancier à écouter. Timegrapher est fait "
            "pour les montres mécaniques automatiques ou à remontage manuel.",
        ]),
        ("Timegrapher est-il gratuit ?", [
            "Votre première montre est gratuite pour toujours, avec toutes les mesures. "
            "**Timegrapher Pro** est un achat unique qui supprime la limite du nombre de "
            "montres. Il n'y a pas d'abonnement, et les achats se restaurent sur tout "
            "appareil connecté au même compte Apple.",
        ]),
        ("Timegrapher enregistre-t-il le son ?", [
            "Non. Le son est analysé en direct et n'est jamais enregistré, conservé ni "
            "envoyé. Votre collection reste sur votre iPhone. Le contrôle de prix "
            "facultatif cherche la référence de votre montre sur Chrono24, et **Identifier "
            "d'après la photo** n'envoie cette photo au Private Cloud Compute d'Apple que "
            "si vous le touchez. [Politique de confidentialité (en anglais)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "mesurer-precision-montre",
        "title": "Comment vérifier la précision de votre montre mécanique avec un iPhone",
        "description": "Pas à pas : mesurer la marche, l'amplitude et l'erreur de repère "
                       "de votre montre automatique ou à remontage manuel avec le "
                       "microphone de l'iPhone, lire les résultats et contrôler le "
                       "magnétisme.",
        "lead": "Un chronocomparateur indique si une montre mécanique avance ou retarde, et "
                "dans quel état est son mouvement. Timegrapher en fait un de votre iPhone, "
                "grâce au microphone. Voici comment obtenir une mesure stable, et ce que "
                "les valeurs veulent dire.",
        "choose": [
            ("Marche", "Secondes d'avance ou de retard par jour"),
            ("Amplitude", "L'angle parcouru par le balancier"),
            ("Erreur de repère", "Le tic face au tac, en ms"),
        ],
        "steps": [
            ("Installer Timegrapher",
             "Téléchargez [Timegrapher sur l'App Store](store). Votre première montre est "
             "gratuite. Autorisez l'accès au microphone quand l'app le demande."),
            ("Remonter la montre",
             "Remontez à fond une montre manuelle, ou portez une automatique un moment "
             "avant. L'amplitude est plus faible sur une montre presque arrêtée."),
            ("Ajouter la montre",
             "Touchez **Ajouter une montre** et indiquez la marque, la référence et le "
             "mouvement. Réglez l'**Angle de levée** de votre calibre, car l'amplitude en "
             "dépend. **Identifier d'après la photo** peut suggérer la marque et le modèle."),
            ("Trouver un endroit calme",
             "Le ronronnement d'un frigo ou la circulation coûtent de la précision. "
             "Déconnectez les écouteurs Bluetooth pour que le microphone de l'iPhone écoute."),
            ("Mesurer",
             "Touchez **Mesurer** et posez fermement le bas de l'iPhone sur la montre, de "
             "préférence sur le verre. Le contact direct transmet les tics bien mieux que "
             "l'air. La mesure s'arrête seule à 0:30."),
            ("Lire le résultat",
             "Vous obtenez la marche en secondes par jour, l'amplitude en degrés, l'erreur "
             "de repère en millisecondes et la fréquence, avec un verdict d'Excellent à "
             "Révision nécessaire et ses raisons. L'onglet **Guide** explique chaque valeur."),
            ("Essayer d'autres positions",
             "La marche change selon la position. **Mesurer en positions** prend la montre "
             "cadran en haut, cadran en bas et sur la tranche, et montre l'écart entre elles."),
            ("Contrôler le magnétisme",
             "Si la montre se met soudain à beaucoup avancer, touchez **Contrôler le "
             "magnétisme**. Le magnétomètre de l'iPhone indique s'il faut la démagnétiser."),
        ],
        "tips": [
            ("Suivre dans le temps",
             "Chaque mesure est conservée et tracée : un mouvement qui dérive lentement se "
             "voit avant qu'il ne s'arrête."),
            ("Une journée au poignet",
             "**Marche par photo** compare deux photos du cadran prises à un jour d'écart "
             "et montre comment la montre a marché pendant que vous la portiez."),
            ("Ce qu'elle vaut",
             "Le contrôle de prix récupère les prix demandés sur Chrono24 pour votre "
             "référence exacte et garde la médiane."),
            ("Un seul paiement",
             "La première montre est gratuite. Timegrapher Pro ajoute un nombre illimité de "
             "montres pour un paiement unique, sans abonnement."),
        ],
        "updated": "Rédigé pour Timegrapher 2.7, octobre 2026.",
        "cta_title": "Mesurez votre montre ce soir",
        "cta_text": "Marche, amplitude et erreur de repère en 30 secondes, avec l'iPhone que "
                    "vous avez déjà. Première montre gratuite, sans abonnement.",
    },
}
