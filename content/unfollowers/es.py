# Unfollowers in Spanish ("tú", as in the App Store text). Keys are explained in en.py.

L = {
    "name": "Español",
    "path": "es/",
    "og_locale": "es_ES",
    "ui": {
        "nav_apps": "Apps",
        "nav_privacy": "Privacidad",
        "nav_about": "",   # no room on phones
        "nav_contact": "Contacto",
        "trademark": "Instagram y Facebook son marcas comerciales de Meta Platforms, Inc. "
                     "Unfollowers y Unfriended son apps independientes. No están afiliadas a "
                     "Meta ni cuentan con su respaldo o patrocinio.",
        "rights": "Todos los derechos reservados.",
        "overview": "Resumen",
        "privacy": "Privacidad",
        "view_on_store": "Ver en la App Store",
        "platform": "iPhone · iOS 17 o posterior",
        "screenshots": "Capturas de pantalla",
        "prev": "Capturas anteriores",
        "next": "Capturas siguientes",
        "privacy_eyebrow": "Privacidad",
        "read_policy": "Leer la política de privacidad (en inglés)",
        "more_apps": "Más apps",
        "languages": "Idiomas",
        "faq": "Preguntas frecuentes",
        "summary": "Qué elegir",
        "tips": "Conviene saber",
        "cta_more": "Sobre {name}",
    },
    "page": {
        "shots_dir": "es",
        "tagline": "Mira quién dejó de seguirte en Instagram. Sin login.",
        "pricing": "Gratis · Desbloqueo único",
        "intro": (
            "Instagram no te dice quién dejó de seguirte. Tu propio export de datos sí.",
            "Unfollowers lee el export oficial que tú mismo descargas de Instagram y te "
            "muestra qué cambió. Nunca te pide la contraseña.",
        ),
        "features": [
            ("Quién dejó de seguirte",
             "Se sigue de una importación a otra, con la fecha en que se detectó cada "
             "cambio."),
            ("Probablemente te bloqueó",
             "Cuentas que salieron a la vez de tus seguidores y de tus seguidos. La app las "
             "marca como probables bloqueos."),
            ("Quién no te sigue de vuelta",
             "La lista clásica, más tus mutuos y las solicitudes de seguimiento que nunca se "
             "aceptaron."),
            ("Con quién más interactúas",
             "Tus me gusta, comentarios y reacciones a historias, contados desde tu propio "
             "export."),
            ("Tu historial en gráficos",
             "Gráficos de crecimiento y de follow-back creados con cada export que importas."),
            ("Sin login",
             "La app no tiene ninguna pantalla de inicio de sesión. Tu contraseña es solo "
             "tuya."),
        ],
        "privacy_title": "Tu export se queda en tu iPhone.",
        "privacy": [
            "Tu export de Instagram se lee y se guarda solo en tu iPhone.",
            "Sin cuenta, sin analíticas, sin anuncios y sin rastreo.",
            "Para comprobar si una cuenta sigue existiendo, la app envía a Instagram solo ese "
            "nombre de usuario, sin iniciar sesión.",
        ],
        "note": "Unfollowers es una app independiente, sin afiliación con Instagram ni con Meta.",
        "stats": [],
        "reviews": [],
        "why": (
            "Tu contraseña es solo tuya.",
            "La mayoría de las apps de seguidores te piden la contraseña de Instagram y "
            "luego usan tu cuenta en segundo plano. Instagram advierte que dejar entrar apps "
            "no autorizadas en tu cuenta la pone en riesgo. Quienes las usan a menudo cuentan "
            "que su cuenta acabó bloqueada, suspendida o con acciones bloqueadas. Unfollowers "
            "nunca te pide la contraseña y nunca inicia sesión en tu cuenta. Lee el export de "
            "datos que te da el propio Instagram. Y no hay suscripción: una única compra "
            "opcional lo desbloquea todo.",
        ),
        "shots": [
            "Mira cada unfollower: quién se fue y cuándo, leído de tu propio export de datos "
            "de Instagram.",
            "Probablemente te bloquearon: cuentas que salieron a la vez de tus seguidores y "
            "de tus seguidos.",
            "No te siguen de vuelta: busca, ordena y abre cualquier perfil.",
            "A quién das más bombo: tus likes, comentarios y reacciones a historias, "
            "contados desde tu export.",
            "Tus stats en gráficas: crecimiento y follow-back con tu propio historial.",
        ],
    },
    "guide_link": "Cómo descargar tus datos de Instagram",
    "faq": [
        ("¿Cómo puedo ver quién me dejó de seguir en Instagram?", [
            "Instagram no muestra quién dejó de seguirte. Tu export de datos de Instagram "
            "contiene la lista de todas las personas que te siguen el día que lo descargas. "
            "Unfollowers compara dos de estos exports y te muestra quién se fue.",
            [
                "Descarga tu export de datos de Instagram, con Seguidores y seguidos en "
                "formato JSON. [Aquí tienes los pasos](guide).",
                "Importa el archivo ZIP en Unfollowers. Al momento ves quién no te sigue de "
                "vuelta.",
                "Unas semanas después, descarga un export nuevo e impórtalo también. "
                "Unfollowers te muestra quién dejó de seguirte desde el primero, con la "
                "fecha en que se detectó cada cambio.",
            ],
            "Cada export nuevo que importas amplía tu historial.",
        ]),
        ("¿Hay alguna app segura para ver quién me dejó de seguir sin login?", [
            "Unfollowers funciona sin login. Nunca te pide la contraseña de Instagram y "
            "nunca inicia sesión en tu cuenta. Lee el export de datos que tú mismo descargas "
            "de Instagram.",
            "Muchas apps de seguidores te piden la contraseña de Instagram y luego usan tu "
            "cuenta en segundo plano. Instagram advierte que dejar entrar apps no autorizadas "
            "en tu cuenta la pone en riesgo. Con Unfollowers, tu contraseña es solo tuya y "
            "la app nunca hace nada en tu cuenta.",
            "El archivo se lee y se guarda en tu iPhone. No hay cuenta, ni anuncios, ni "
            "rastreo.",
        ]),
        ("¿Cómo descargo mi export de datos de Instagram?", [
            "En la app de Instagram, abre tu perfil y toca el menú. Luego ve a Centro de "
            "cuentas › Tu información y tus permisos › Exportar tu información › Crear "
            "exportación. En algunas cuentas, el Centro de cuentas se llama Cuenta de Meta. "
            "Elige Exportar al dispositivo. Marca Seguidores y seguidos, elige todo el "
            "periodo y el formato JSON, y toca Iniciar exportación. Instagram te avisa "
            "cuando el archivo está listo, normalmente en pocos minutos.",
            "[Guía paso a paso](guide).",
        ]),
        ("¿Puedo ver quién me bloqueó en Instagram?", [
            "Instagram no informa de los bloqueos, así que ninguna app puede saberlo con "
            "seguridad. Cuando alguien te bloquea, desaparece a la vez de tus seguidores y "
            "de tus seguidos. Unfollowers marca esas cuentas como probables bloqueos. Esto "
            "solo funciona con personas que te seguían y a las que tú seguías.",
            "Una cuenta eliminada, desactivada o que cambió de nombre desaparece de la misma "
            "forma. La comprobación de perfiles (el vibe check) pregunta a instagram.com si "
            "cada nombre de usuario sigue existiendo y pasa las cuentas desaparecidas a una "
            "lista aparte.",
        ]),
        ("¿Unfollowers es gratis?", [
            "Descargar Unfollowers es gratis. La versión gratuita muestra quién no te sigue "
            "de vuelta, a quién no sigues tú de vuelta y tus mutuos. Una única compra "
            "desbloquea todo lo demás, incluidas las listas de quién dejó de seguirte y de "
            "quién probablemente te bloqueó. No hay suscripción. La app funciona en iPhone "
            "con iOS 17 o posterior.",
        ]),
        ("¿Sale algo de mi iPhone?", [
            "Tu archivo de export se queda en tu iPhone. La app lo lee y lo guarda ahí, y el "
            "desarrollador no tiene servidores. La única función que usa internet es la "
            "comprobación de perfiles. Pregunta a instagram.com si una cuenta sigue "
            "existiendo y envía solo ese nombre de usuario, sin iniciar sesión. Se ejecuta "
            "cuando tocas el vibe check y, con la app desbloqueada, para un máximo de 30 "
            "cuentas nuevas después de cada importación. [Política de privacidad (en "
            "inglés)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "descargar-datos-instagram",
        "title": "Cómo descargar tus datos de Instagram (export en JSON)",
        "description": "Paso a paso en iPhone: exporta tus seguidores y seguidos de "
                       "Instagram en formato JSON, desde el principio, y guarda el archivo "
                       "ZIP. Luego mira quién dejó de seguirte con Unfollowers.",
        "lead": "Instagram te deja descargar una copia de los datos de tu cuenta. El export "
                "incluye la lista completa de tus seguidores y de las cuentas que sigues. "
                "Unfollowers lee este archivo para mostrarte quién dejó de seguirte. Así se "
                "consigue en la app de Instagram para iPhone.",
        "choose": [
            ("Información", "Seguidores y seguidos"),
            ("Intervalo de fechas", "Desde el principio"),
            ("Formato", "JSON"),
        ],
        "steps": [
            ("Abre el menú",
             "En la app de Instagram, toca tu foto de perfil abajo a la derecha. Luego toca "
             "el menú (☰) arriba a la derecha."),
            ("Centro de cuentas",
             "Toca **Centro de cuentas**. En algunas cuentas se llama **Cuenta de Meta**."),
            ("Tu información",
             "Toca **Tu información y tus permisos** y luego **Exportar tu información**."),
            ("Crea la exportación",
             "Toca **Crear exportación**. Elige tu perfil de Instagram y toca **Siguiente**."),
            ("Exportar al dispositivo",
             "Elige **Exportar al dispositivo**. Así el archivo se guarda en tu iPhone."),
            ("Elige los datos",
             "En la pantalla siguiente, elige la información que quieres exportar. Marca "
             "**Seguidores y seguidos**, en la parte de conexiones. Para ver con quién más "
             "interactúas, marca también los me gusta, los comentarios y las interacciones "
             "con historias. Puedes desmarcar el resto para que el archivo sea más pequeño."),
            ("Desde el principio, en JSON",
             "En el intervalo de fechas, elige todo el periodo, desde el principio. En el "
             "formato, elige **JSON**. Unfollowers no puede leer el formato HTML."),
            ("Inicia la exportación",
             "Toca **Iniciar exportación**. Instagram prepara el archivo. Normalmente tarda "
             "unos minutos."),
            ("Descarga el ZIP",
             "Instagram te avisa cuando el archivo está listo. Vuelve a **Exportar tu "
             "información** y descarga el archivo. Puede que Instagram te pida la "
             "contraseña. La escribes en el propio Instagram. Guarda el archivo ZIP en la "
             "app Archivos."),
            ("Impórtalo en Unfollowers",
             "Abre Unfollowers, toca el botón de importar y elige el archivo ZIP. No hace "
             "falta descomprimirlo."),
        ],
        "tips": [
            ("Dos exports muestran quién se fue",
             "Un export contiene tus seguidores de un solo día. Importa un export nuevo cada "
             "pocas semanas. Unfollowers los compara y te muestra quién se fue desde el "
             "último."),
            ("El archivo está disponible cuatro días",
             "Instagram guarda un export terminado durante cuatro días. Después, crea uno "
             "nuevo."),
            ("“No se encontraron listas de seguidores”",
             "Unfollowers muestra este mensaje cuando el export está en formato HTML o "
             "cuando no marcaste Seguidores y seguidos. Crea un export nuevo en JSON con "
             "Seguidores y seguidos."),
            ("Puede tardar más",
             "La mayoría de los exports están listos en pocos minutos. A veces tardan más. "
             "Instagram te avisa en la app y por correo cuando el tuyo está listo."),
        ],
        "updated": "Pasos revisados en el servicio de ayuda de Instagram en octubre de 2026.",
        "cta_title": "Mira quién dejó de seguirte",
        "cta_text": "Unfollowers lee este archivo en tu iPhone. Te muestra quién dejó de "
                    "seguirte, quién probablemente te bloqueó y quién no te sigue de vuelta. "
                    "Sin login y sin contraseña.",
    },
}
