# Aloud in Spanish ("tú", neutral, as in the app). Keys are explained in
# content/unfollowers/en.py; facts to keep true are in en.py. Button names are
# the app's Spanish strings (Aloud/Localizable.xcstrings).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "es.py"))["L"]["ui"]

L = {
    "name": "Español",
    "path": "es/",
    "og_locale": "es_ES",
    "ui": {
        **_ui,
        "summary": "Lo que Aloud lee",
        "tips": "Conviene saber",
        "appearance": "Aspecto de las capturas",
        "light": "Claro",
        "dark": "Oscuro",
        "what_people_say": "Lo que dice la gente.",
    },
    "page": {
        "shots_dir": "es",
        "tagline": "Todo lo que puedas leer, leído en voz alta.",
        "pricing": "Prueba gratis · Desbloqueo único",
        "platform": "iPhone y iPad · iOS 17 o posterior",
        "intro": (
            "Comparte un artículo, abre un PDF o pega cualquier texto.",
            "Aloud te lo lee con una voz natural creada en tu iPhone, frase a frase, y "
            "siempre recuerda por dónde ibas.",
        ),
        "features": [
            ("Voces naturales, en el dispositivo",
             "Diez voces para inglés y cuatro que leen treinta idiomas más, entre ellos el "
             "español. Ningún servidor habla por ti, así que Aloud sigue leyendo en modo "
             "avión."),
            ("Artículos, PDF, libros",
             "Comparte desde cualquier navegador, abre PDF y libros EPUB desde Archivos, "
             "incluso PDF escaneados, o pega tu propio texto."),
            ("Para leer mientras escuchas",
             "La frase que se está leyendo se ilumina. Mantén pulsada la barra del margen "
             "para recorrer todo el documento."),
            ("Más rápido, si quieres",
             "De 0,5× a 3× sin voz de ardilla, y con las pausas recortadas al final de cada "
             "frase si lo prefieres."),
            ("Para llevar",
             "Sigue leyendo con la pantalla bloqueada, con controles en la pantalla de "
             "bloqueo y en los AirPods, y un temporizador de reposo que baja el volumen poco "
             "a poco."),
            ("En todos tus dispositivos",
             "La sincronización con iCloud es opcional y guarda tu estantería como archivos "
             "de texto normales en tu propio iCloud Drive."),
        ],
        "privacy_title": "Privado por diseño.",
        "privacy": [
            "La voz se genera en tu iPhone. Tus documentos nunca se suben.",
            "Las voces se descargan una vez desde un servidor público. Los artículos que "
            "compartes se obtienen de su propia web, como haría un navegador.",
            "Sin cuenta, sin analíticas, sin anuncios, sin rastreo.",
        ],
        "note": "",
        "reviews": [],
        "why": (
            "Sin nube. Sin suscripción.",
            "Muchas apps conocidas de texto a voz generan sus voces en sus propios "
            "servidores, así que los artículos y documentos que escuchas se suben allí "
            "primero, y sus planes premium pueden costar 139 $ al año o 29 $ al mes, casi "
            "350 $ al año. Aloud genera cada voz en tu iPhone, así que lo que lees nunca se "
            "envía a ninguna parte para leerlo. Y no hay suscripción: una sola compra "
            "opcional, tuya para siempre.",
        ),
        "shots": [
            "Todo lo que puedas leer, te lo lee en voz alta. Artículos, PDF, notas, leídos con una voz natural, frase a frase.",
            "Termina la lista de lectura. Escucha en el trayecto, en el paseo, mientras lavas los platos.",
            "Funciona sin conexión. En cualquier parte. Descarga la voz una sola vez.",
            "Sin suscripción. Sin anuncios. Sin rastreo.",
            "Voces naturales. En todos los idiomas. Diez voces para inglés y cuatro que leen treinta idiomas más, generadas en tu iPhone.",
            "Modo lectura: léelo a tu manera.",
            "El doble de velocidad. La mitad del tiempo. De 0,5× a 3×, con menos silencio entre frases.",
            "Tu estantería, en todos tus dispositivos, como archivos de texto en iCloud Drive.",
            "Léelo en tu idioma: cualquier texto traducido en el dispositivo, frase junto a frase.",
        ],
        "duo": {
            "title": "En el iPhone Duo",
            "sub": "Cerrado, escuchas. Abierto, lees.",
            "items": [
                ("cover", "cover", "Cerrado", "La voz sigue leyendo en la pantalla exterior.",
                 "Aloud en la pantalla exterior del iPhone Duo: la voz sigue leyendo, con controles de reproducción."),
                ("book", "spread", "Medio abierto", "Dos páginas enfrentadas, en cualquier ángulo.",
                 "Aloud en el iPhone Duo medio abierto: dos páginas enfrentadas."),
                ("flat", "spread", "Abierto", "¿Traduces? El original y la traducción, lado a lado.",
                 "Aloud en el iPhone Duo abierto: el original en español en la página izquierda y "
                 "la traducción al inglés en la derecha, línea por línea."),
            ],
        },
    },
    "guide_link": "Cómo escuchar artículos, PDF y libros EPUB en el iPhone",
    "faq": [
        ("¿Qué app de texto a voz para iPhone no tiene suscripción?", [
            "Aloud lee en voz alta artículos, PDF, libros EPUB y cualquier texto con una voz "
            "natural. Se descarga gratis, y una sola compra dentro de la app quita el límite "
            "para siempre. No hay suscripción y nada se renueva.",
            "Las voces se generan en tu iPhone o iPad, así que lo que lees nunca se sube "
            "para convertirlo en voz, y Aloud sigue leyendo sin conexión a internet. No hay "
            "cuenta, ni anuncios, ni rastreo.",
        ]),
        ("¿Cómo escucho un artículo en el iPhone?", [
            [
                "Abre el artículo en Safari o en cualquier otra app.",
                "Toca **Compartir** y luego **Aloud**.",
                "Abre Aloud y pulsa reproducir. La frase que se está leyendo se ilumina en "
                "la página.",
            ],
            "Cuando compartes desde Safari, Aloud lee la página tal como Safari la muestra, "
            "así que también funcionan los artículos de webs en las que tienes la sesión "
            "iniciada. Los enlaces compartidos desde las apps de Facebook, Messenger e "
            "Instagram también funcionan. [Guía paso a paso](guide).",
        ]),
        ("¿Puede Aloud convertir un EPUB en audiolibro?", [
            "Sí. Abre un archivo EPUB desde la app Archivos o toca **+** › **Importar un "
            "archivo**. Aloud conserva la portada y los capítulos del libro. La lista "
            "**Capítulos** muestra cuánto se tarda en escuchar cada uno, y puedes empezar "
            "por cualquiera. Aloud recuerda por dónde ibas, así que un libro largo se "
            "escucha como un audiolibro.",
            "Los libros comprados con protección anticopia no se pueden abrir en otras apps, "
            "tampoco en Aloud. Los EPUB sin DRM, como los de Project Gutenberg o Standard "
            "Ebooks, funcionan.",
        ]),
        ("¿Lee PDF, también escaneados?", [
            "Sí. Abre un PDF desde Archivos o compártelo con Aloud. Aloud lee el texto en "
            "orden, y en un PDF escaneado reconoce primero el texto en el propio "
            "dispositivo.",
        ]),
        ("¿Aloud funciona sin conexión?", [
            "Sí. Cada voz se descarga una vez, la primera vez que la usas. Después la voz se "
            "genera en tu iPhone, así que Aloud lee en modo avión, en el metro o en un "
            "vuelo. Para traer un artículo nuevo hace falta internet; lo que ya está en tu "
            "estantería, no.",
        ]),
        ("¿Qué idiomas puede leer?", [
            "Diez voces naturales leen inglés, y cuatro más leen más de treinta idiomas, "
            "entre ellos español, alemán, francés, italiano y portugués. La app está en "
            "español, inglés, alemán, francés, italiano y portugués.",
        ]),
        ("¿Puede traducir lo que estoy leyendo?", [
            "Sí, en iOS 18 o posterior. Toca el botón de traducir en el lector y elige un "
            "idioma en **Traducir a**. El traductor de Apple trabaja en tu iPhone, así que no "
            "se envía nada. La página muestra entonces cada frase con su traducción, y "
            "**Leer en voz alta la traducción** hace que la voz lea el otro idioma.",
        ]),
        ("¿A qué velocidad puede leer?", [
            "De 0,5× a 3×, sin voz de ardilla. **Acortar las pausas** recorta el silencio "
            "entre frases, así que un artículo de 30 minutos cabe en un paseo de 15.",
        ]),
        ("¿Aloud es gratis?", [
            "Aloud se descarga gratis, con todas las voces y funciones. La estantería "
            "gratuita guarda tres lecturas a la vez. Una compra única, **Desbloquear "
            "Aloud**, quita el límite. No hay suscripción. [Ver en la App Store](store).",
        ]),
        ("¿Puedo traer mi lista de lectura de Pocket o Instapaper?", [
            "Sí. Exporta tus guardados de Pocket, Instapaper, Raindrop o los marcadores de tu "
            "navegador, y en Aloud abre **Ajustes** › **Importar desde un archivo**. Cada "
            "enlace llega a tu estantería, y Aloud descarga los artículos en segundo plano.",
        ]),
        ("¿Aloud sube mis documentos?", [
            "No. La voz se genera en tu iPhone. Aloud descarga cada voz una vez desde un "
            "servidor público y obtiene los artículos que compartes de su propia web, como "
            "un navegador. **Sincronizar con iCloud** es opcional y guarda tu estantería "
            "como archivos de texto normales en tu propio iCloud Drive. [Política de "
            "privacidad](privacy).",
        ]),
    ],
    "guide": {
        "slug": "escuchar-articulos-y-libros",
        "title": "Cómo escuchar artículos, PDF y libros EPUB en el iPhone",
        "description": "Paso a paso: comparte un artículo desde Safari, abre un PDF o un "
                       "EPUB, pega cualquier texto y deja que Aloud te lo lea con una voz "
                       "natural creada en tu iPhone, a tu velocidad, sin conexión.",
        "lead": "Aloud lee todo lo que puedes leer: un artículo de la web, un PDF, un libro "
                "EPUB o un texto que pegues. La voz se crea en tu iPhone, así que funciona "
                "sin conexión y nada de lo que lees se sube. Así se añade cada tipo de texto "
                "y así se escucha.",
        "choose": [
            ("Artículos", "Compártelos desde Safari o cualquier app"),
            ("PDF y EPUB", "Ábrelos desde Archivos"),
            ("Cualquier texto", "Pégalo"),
        ],
        "steps": [
            ("Instala Aloud",
             "Descarga [Aloud desde la App Store](store). Funciona en iPhone y iPad con iOS "
             "17 o posterior. La primera vez que pulsas reproducir, la voz se descarga una "
             "vez. Después funciona sin conexión."),
            ("Comparte un artículo",
             "Abre el artículo en Safari o en otra app, toca **Compartir** y luego "
             "**Aloud**. El artículo llega a tu estantería sin menús, anuncios ni "
             "comentarios. Desde Safari, Aloud lee la página tal como la ves, así que "
             "funcionan también los artículos de webs en las que tienes la sesión iniciada."),
            ("Abre un PDF o un EPUB",
             "En Aloud, toca **+** › **Importar un archivo** y elige el archivo, o "
             "compártelo con Aloud desde la app Archivos. Los PDF escaneados se reconocen en "
             "el dispositivo. Los libros EPUB conservan su portada y sus capítulos."),
            ("Pega cualquier texto",
             "Toca **+** › **Pegar texto** para notas, correos o cualquier cosa que hayas "
             "copiado. **Pegar un enlace** acepta una dirección web."),
            ("Pulsa reproducir",
             "Abre una lectura y pulsa reproducir. La frase que se lee se ilumina y el resto "
             "queda atenuado. Mantén pulsada la barra del margen para recorrer todo el texto. "
             "En un libro, toca **Capítulos** en el menú ••• para empezar por cualquier "
             "capítulo."),
            ("Elige la velocidad",
             "Toca el botón de velocidad y elige entre 0,5× y 3×. Activa **Acortar las "
             "pausas** para recortar el silencio entre frases."),
            ("Bloquea el iPhone",
             "Aloud sigue leyendo con la pantalla bloqueada. Usa los controles de la "
             "pantalla de bloqueo o de los AirPods, y pon el **Temporizador de reposo** si "
             "escuchas en la cama: al final, la voz baja poco a poco."),
            ("Tradúcelo, si quieres",
             "En iOS 18 o posterior, toca el botón de traducir y elige un idioma en "
             "**Traducir a**. Cada frase aparece con su traducción, y **Leer en voz alta la "
             "traducción** cambia la voz al otro idioma."),
        ],
        "tips": [
            ("Recuerda por dónde ibas",
             "Cada lectura guarda dónde te quedaste, así que puedes pasar de un artículo a "
             "un libro y volver a la misma frase."),
            ("Modo lectura",
             "Toca el botón de las gafas para ocultar el reproductor y leer tú mismo, con la "
             "letra, el tamaño y el papel que elijas en **Aspecto**."),
            ("Tu lista de lectura",
             "Los guardados de Pocket, Instapaper, Raindrop o los marcadores del navegador "
             "entran por **Ajustes** › **Importar desde un archivo**."),
            ("Prueba gratis",
             "La estantería gratuita guarda tres lecturas. Una sola compra quita el límite, "
             "y no hay suscripción."),
        ],
        "updated": "Escrito para Aloud 3.2, octubre de 2026.",
        "cta_title": "Escucha tu lista de lectura",
        "cta_text": "Aloud lee artículos, PDF y libros EPUB con una voz natural creada en tu "
                    "iPhone. Funciona sin conexión. Pagas una vez, sin suscripción.",
    },
}
