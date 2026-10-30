# Unfollowers in French ("tu", as in the App Store text). Keys are explained in en.py.
# French puts a no-break space before ? ! : ; (written here as  ).

L = {
    "name": "Français",
    "path": "fr/",
    "og_locale": "fr_FR",
    "ui": {
        "nav_apps": "Apps",
        "nav_privacy": "Vie privée",
        "nav_about": "",   # no room on phones
        "nav_contact": "Contact",
        "trademark": "Instagram et Facebook sont des marques de Meta Platforms, Inc. "
                     "Unfollowers et Unfriended sont des apps indépendantes. Elles ne sont ni "
                     "affiliées à Meta, ni approuvées ou sponsorisées par Meta.",
        "rights": "Tous droits réservés.",
        "overview": "Aperçu",
        "privacy": "Vie privée",
        "view_on_store": "Voir sur l'App Store",
        "platform": "iPhone · iOS 17 ou version ultérieure",
        "screenshots": "Captures d'écran",
        "prev": "Captures précédentes",
        "next": "Captures suivantes",
        "privacy_eyebrow": "Confidentialité",
        "read_policy": "Lire la politique de confidentialité (en anglais)",
        "more_apps": "Autres apps",
        "languages": "Langues",
        "faq": "Questions fréquentes",
        "summary": "Quoi choisir",
        "tips": "Bon à savoir",
        "cta_more": "À propos d'{name}",
        "out_of_5": " sur 5",
        "decimal": ",",
    },
    "page": {
        "shots_dir": "fr",
        "tagline": "Découvre qui a arrêté de te suivre sur Instagram. Sans login.",
        "pricing": "Gratuit · Déblocage unique",
        "intro": (
            "Instagram ne te dit pas qui a arrêté de te suivre. Ton propre export de "
            "données, si.",
            "Unfollowers lit l'export officiel que tu télécharges toi-même depuis Instagram "
            "et te montre ce qui a changé. L'app ne te demande jamais ton mot de passe.",
        ),
        "features": [
            ("Qui a arrêté de te suivre",
             "Suivi d'un import à l'autre, avec la date à laquelle chaque changement a été "
             "repéré."),
            ("T'a probablement bloqué",
             "Les comptes qui ont quitté en même temps tes abonnés et tes abonnements. L'app "
             "les signale comme des blocages probables."),
            ("Qui ne te suit pas en retour",
             "La liste classique, plus tes mutuals et les demandes d'abonnement jamais "
             "acceptées."),
            ("Avec qui tu interagis le plus",
             "Tes j'aime, commentaires et réactions aux stories, comptés à partir de ton "
             "propre export."),
            ("Ton historique en graphiques",
             "Des graphiques de croissance et de follow-back créés à partir de chaque export "
             "que tu importes."),
            ("Sans login",
             "L'app n'a aucun écran de connexion. Ton mot de passe reste à toi."),
        ],
        "privacy_title": "Ton export reste sur ton iPhone.",
        "privacy": [
            "Ton export Instagram est lu et enregistré uniquement sur ton iPhone.",
            "Pas de compte, pas d'analytics, pas de pub, pas de tracking.",
            "Pour vérifier qu'un compte existe encore, l'app envoie à Instagram uniquement "
            "ce nom d'utilisateur, sans se connecter.",
        ],
        "note": "Unfollowers est une app indépendante, sans lien avec Instagram ou Meta.",
        "stats": [],
        "reviews": [],
        "why": (
            "Ton mot de passe reste à toi.",
            "La plupart des apps de suivi d'abonnés te demandent ton mot de passe Instagram, "
            "puis utilisent ton compte en arrière-plan. Instagram prévient que laisser des "
            "apps non autorisées accéder à ton compte le met en danger. Les personnes qui les "
            "utilisent souvent parlent de comptes verrouillés, suspendus ou avec des actions "
            "bloquées. Unfollowers ne te demande jamais ton mot de passe et ne se connecte "
            "jamais à ton compte. L'app lit l'export de données qu'Instagram te donne "
            "lui-même. Et il n'y a pas d'abonnement : un seul achat facultatif débloque "
            "tout.",
        ),
        "shots": [
            "Chaque unfollower : qui est parti et quand, lu depuis ton propre export de "
            "données Instagram.",
            "T'ont probablement bloqué : les comptes qui ont quitté en même temps tes "
            "abonnés et tes abonnements.",
            "Ils ne te suivent pas en retour : cherche, trie et ouvre n'importe quel "
            "profil.",
            "Qui tu hypes le plus : tes j'aime, commentaires et réactions aux stories, "
            "comptés.",
            "Tes stats en courbes : croissance et follow-back depuis ton historique.",
        ],
    },
    "guide_link": "Comment télécharger tes données Instagram",
    "faq": [
        ("Comment voir qui ne me suit plus sur Instagram ?", [
            "Instagram ne montre pas qui a arrêté de te suivre. Ton export de données "
            "Instagram contient toutes les personnes qui te suivent le jour où tu le "
            "télécharges. Unfollowers compare deux de ces exports et te montre qui est parti.",
            [
                "Télécharge ton export de données depuis Instagram, avec Abonnés et "
                "abonnements au format JSON. [Voici les étapes](guide).",
                "Importe le fichier ZIP dans Unfollowers. Tu vois tout de suite qui ne te "
                "suit pas en retour.",
                "Quelques semaines plus tard, télécharge un nouvel export et importe-le "
                "aussi. Unfollowers te montre qui a arrêté de te suivre depuis le premier, "
                "avec la date à laquelle chaque changement a été repéré.",
            ],
            "Chaque nouvel export que tu importes complète ton historique.",
        ]),
        ("Existe-t-il une app sûre pour voir qui s'est désabonné, sans login ?", [
            "Unfollowers fonctionne sans login. L'app ne te demande jamais ton mot de passe "
            "Instagram et ne se connecte jamais à ton compte. Elle lit l'export de données "
            "que tu télécharges toi-même depuis Instagram.",
            "Beaucoup d'apps de suivi d'abonnés te demandent ton mot de passe Instagram, puis "
            "utilisent ton compte en arrière-plan. Instagram prévient que laisser des apps "
            "non autorisées accéder à ton compte le met en danger. Avec Unfollowers, ton mot "
            "de passe reste à toi, et l'app n'agit jamais sur ton compte.",
            "Le fichier est lu et enregistré sur ton iPhone. Pas de compte, pas de pub, pas "
            "de tracking.",
        ]),
        ("Comment télécharger mes données Instagram ?", [
            "Dans l'app Instagram, ouvre ton profil et touche le menu. Va ensuite dans Espace "
            "Comptes › Vos informations et autorisations › Exporter vos informations › Créer "
            "une exportation. Sur certains comptes, l'Espace Comptes s'appelle Compte Meta. "
            "Choisis Exporter vers l'appareil. Coche Abonnés et abonnements, choisis toute la "
            "période et le format JSON, puis touche Démarrer l'exportation. Instagram te "
            "prévient quand le fichier est prêt, en général en quelques minutes.",
            "[Le guide étape par étape](guide).",
        ]),
        ("Puis-je voir qui m'a bloqué sur Instagram ?", [
            "Instagram ne signale pas les blocages, donc aucune app ne peut le savoir avec "
            "certitude. Quand quelqu'un te bloque, il disparaît en même temps de tes abonnés "
            "et de tes abonnements. Unfollowers signale ces comptes comme des blocages "
            "probables. Cela ne marche qu'avec les personnes qui te suivaient et que tu "
            "suivais aussi.",
            "Un compte supprimé, désactivé ou renommé disparaît de la même façon. La "
            "vérification des profils (le vibe check) demande à instagram.com si chaque nom "
            "d'utilisateur existe encore, et range les comptes disparus dans une liste à part.",
        ]),
        ("Unfollowers est-il gratuit ?", [
            "Le téléchargement d'Unfollowers est gratuit. La version gratuite montre qui ne "
            "te suit pas en retour, qui tu ne suis pas en retour et tes mutuals. Un achat "
            "unique débloque tout le reste, dont les listes de qui a arrêté de te suivre et "
            "de qui t'a probablement bloqué. Il n'y a pas d'abonnement. L'app fonctionne sur "
            "iPhone avec iOS 17 ou version ultérieure.",
        ]),
        ("Est-ce que quelque chose quitte mon iPhone ?", [
            "Ton fichier d'export reste sur ton iPhone. L'app le lit et l'enregistre là, et "
            "le développeur n'a pas de serveur. La seule fonction qui utilise internet est la "
            "vérification des profils. Elle demande à instagram.com si un compte existe "
            "encore et envoie uniquement ce nom d'utilisateur, sans se connecter. Elle se "
            "lance quand tu touches le vibe check et, une fois l'app débloquée, pour 30 "
            "nouveaux comptes au maximum après chaque import. [Politique de confidentialité "
            "(en anglais)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "telecharger-donnees-instagram",
        "title": "Comment télécharger tes données Instagram (export JSON)",
        "description": "Étape par étape sur iPhone : exporte tes abonnés et tes "
                       "abonnements Instagram au format JSON, depuis le début, et enregistre "
                       "le fichier ZIP. Ensuite, découvre qui a arrêté de te suivre avec "
                       "Unfollowers.",
        "lead": "Instagram te permet de télécharger une copie des données de ton compte. "
                "L'export contient la liste complète de tes abonnés et des comptes que tu "
                "suis. Unfollowers lit ce fichier pour te montrer qui a arrêté de te suivre. "
                "Voici comment l'obtenir dans l'app Instagram sur iPhone.",
        "choose": [
            ("Informations", "Abonnés et abonnements"),
            ("Plage de dates", "Depuis le début"),
            ("Format", "JSON"),
        ],
        "steps": [
            ("Ouvre le menu",
             "Dans l'app Instagram, touche ta photo de profil en bas à droite. Touche ensuite "
             "le menu (☰) en haut à droite."),
            ("Espace Comptes",
             "Touche **Espace Comptes**. Sur certains comptes, il s'appelle **Compte Meta**."),
            ("Tes informations",
             "Touche **Vos informations et autorisations**, puis **Exporter vos "
             "informations**."),
            ("Crée l'exportation",
             "Touche **Créer une exportation**. Choisis ton profil Instagram et touche "
             "**Suivant**."),
            ("Exporter vers l'appareil",
             "Choisis **Exporter vers l'appareil**. Le fichier est alors enregistré sur ton "
             "iPhone."),
            ("Choisis les données",
             "Sur l'écran suivant, choisis les informations à exporter. Coche **Abonnés et "
             "abonnements**, dans la partie connexions. Pour voir avec qui tu interagis le "
             "plus, coche aussi les j'aime, les commentaires et les interactions avec les "
             "stories. Tu peux décocher le reste pour un fichier plus léger."),
            ("Depuis le début, en JSON",
             "Dans la plage de dates, choisis toute la période, depuis le début. Dans le "
             "format, choisis **JSON**. Unfollowers ne lit pas le format HTML."),
            ("Lance l'exportation",
             "Touche **Démarrer l'exportation**. Instagram prépare le fichier. Cela prend en "
             "général quelques minutes."),
            ("Télécharge le ZIP",
             "Instagram te prévient quand le fichier est prêt. Retourne dans **Exporter vos "
             "informations** et télécharge le fichier. Instagram peut te demander ton mot de "
             "passe. Tu le saisis dans Instagram même. Enregistre le fichier ZIP dans l'app "
             "Fichiers."),
            ("Importe-le dans Unfollowers",
             "Ouvre Unfollowers, touche le bouton d'import et choisis le fichier ZIP. Pas "
             "besoin de le décompresser."),
        ],
        "tips": [
            ("Deux exports montrent qui est parti",
             "Un export contient tes abonnés à une seule date. Importe un nouvel export "
             "toutes les quelques semaines. Unfollowers les compare et te montre qui est "
             "parti depuis le dernier."),
            ("Le fichier reste disponible quatre jours",
             "Instagram garde un export terminé pendant quatre jours. Ensuite, crée-en un "
             "nouveau."),
            ("« Aucune liste d'abonnés trouvée »",
             "Unfollowers affiche ce message quand l'export est au format HTML, ou quand la "
             "catégorie Abonnés et abonnements n'était pas cochée. Crée un nouvel export en "
             "JSON avec Abonnés et abonnements."),
            ("Ça peut prendre plus longtemps",
             "La plupart des exports sont prêts en quelques minutes. Parfois, c'est plus "
             "long. Instagram te prévient dans l'app et par e-mail quand le tien est prêt."),
        ],
        "updated": "Étapes vérifiées dans les pages d'aide d'Instagram en octobre 2026.",
        "cta_title": "Découvre qui a arrêté de te suivre",
        "cta_text": "Unfollowers lit ce fichier sur ton iPhone. L'app te montre qui a arrêté "
                    "de te suivre, qui t'a probablement bloqué et qui ne te suit pas en "
                    "retour. Sans login, sans mot de passe.",
    },
}
