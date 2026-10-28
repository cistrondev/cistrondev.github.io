# Pedometer in Spanish ("tú", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# App words from Shared/Localizable.xcstrings (Conectar, Caminata, Carrera,
# Caminatas y carreras, Objetivos diarios, Apoyar a Pedometer, Ajustes); iOS
# words are Apple's Spanish (Spain). Screenshots are the es-ES set.
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "es.py"))["L"]["ui"]

L = {
    "name": "Español",
    "path": "es/",
    "og_locale": "es_ES",
    "ui": {**_ui, "summary": "Widgets de la pantalla de bloqueo"},
    "page": {
        "shots_dir": "es",
        "tagline": "Tus pasos en la pantalla de bloqueo.",
        "pricing": "Gratis",
        "intro": (
            "Pasos, distancia y pisos subidos, en números y gráficos claros.",
            "Pedometer lee Apple Salud y muestra el recuento de hoy en tu pantalla de "
            "bloqueo y tu pantalla de inicio. Tu iPhone cuenta tus pasos por sí solo, y si "
            "llevas un Apple Watch, sus pasos también cuentan.",
        ),
        "features": [
            ("Hoy",
             "Tus pasos frente a tu objetivo, con lo que te falta. La distancia y los pisos "
             "frente a sus objetivos, con la energía activa y la velocidad al caminar."),
            ("Caminar y correr",
             "Registra una caminata o una carrera con GPS: tu ruta en el mapa, con "
             "velocidad o ritmo, altitud, desnivel y calorías. Cada una se guarda en Apple "
             "Salud con su ruta."),
            ("Frecuencia cardiaca en directo",
             "Con AirPods Pro 3, Powerbeats Pro 2 o una banda de frecuencia cardiaca "
             "Bluetooth, ves tu frecuencia cardiaca en directo (iOS 26)."),
            ("En la pantalla de bloqueo",
             "Mientras andas, el tiempo, la distancia, la velocidad, el pulso y las "
             "calorías siguen en la pantalla de bloqueo, con un botón de pausa."),
            ("Comparte una caminata",
             "Una imagen de cada caminata o carrera, con el mapa y tus datos, para "
             "cualquier app."),
            ("Tus objetivos",
             "Fija un objetivo diario de pasos, distancia y pisos. Empiezan en 10.000 "
             "pasos, 8 km y 10 pisos."),
            ("Historial",
             "Un gráfico por dato para la última semana, el último mes o el último año, con "
             "la media diaria y el cambio respecto al periodo anterior."),
            ("Widgets de la pantalla de bloqueo",
             "Los pasos y la distancia, cada uno dentro de un anillo que se cierra al llegar "
             "a tu objetivo, y los pisos, con una figura que sube una escalera."),
            ("Widget de la pantalla de inicio",
             "La misma tarjeta que en la app, pequeña, mediana o grande. Clara, oscura o "
             "automática, y solo con los pasos si quieres."),
            ("Por horas",
             "Los pasos de hoy hora a hora, junto a tu día habitual de las últimas cuatro "
             "semanas."),
            ("Récords",
             "Totales de cada mes y año, y tu mejor día, semana y mes en pasos, pisos y "
             "velocidad al caminar."),
            ("Tu color",
             "Grafito, azul, verde, naranja, rosa o morado para las barras de objetivo, los "
             "gráficos y el widget."),
        ],
        "privacy_title": "Nada sale de tu iPhone.",
        "privacy": [
            "Lee Apple Salud y solo escribe en ella las caminatas y carreras que registras.",
            "Tu ubicación solo se usa mientras registras y se queda en tu iPhone.",
            "Todo se cuenta y se guarda en tu iPhone. No se sube nada.",
            "Sin cuenta, sin analíticas, sin rastreo.",
        ],
        "note": "Pedometer no es un dispositivo médico y no da consejos médicos.",
        "shots": [
            "Tus pasos en la pantalla de bloqueo: un widget contador de pasos, con la distancia y los pisos al lado.",
            "Cada paso cuenta: lee Apple Salud e incluye los pasos del Apple Watch.",
            "Caminar y correr, en el mapa: velocidad, altitud, calorías y frecuencia cardiaca.",
            "En tiempo real y luego a compartir: la pantalla de bloqueo mientras andas, una imagen después.",
            "También en tu pantalla de inicio: la misma tarjeta, pequeña o mediana.",
            "Tu día, hora a hora: los pasos de hoy junto a un día habitual.",
            "Tu mejor día, semana y mes: totales de cada mes y año, y de siempre.",
            "Elige tu color: seis colores para las barras, los gráficos y el widget.",
            "Tu semana de un vistazo: barras diarias, la media y el cambio.",
            "Nada sale de tu iPhone: sin cuenta, sin rastreo.",
        ],
    },
    "guide_link": "Cómo poner un contador de pasos en la pantalla de bloqueo del iPhone",
    "faq": [
        ("¿Hay un contador de pasos gratis para iPhone sin suscripción?", [
            "Pedometer es gratis, sin suscripción y sin cuenta. Muestra tus pasos, la "
            "distancia y los pisos subidos en números y gráficos claros, y los pone como "
            "widgets en la pantalla de bloqueo y la pantalla de inicio. También registra "
            "caminatas y carreras con GPS. Un bote de propinas opcional no desbloquea nada. "
            "[Ver en el App Store](store).",
        ]),
        ("¿Cómo muestro mis pasos en la pantalla de bloqueo del iPhone?", [
            [
                "Instala Pedometer, ábrelo y toca **Conectar** para que pueda leer Apple Salud.",
                "Mantén pulsada la pantalla de bloqueo, toca **Personalizar** y elige la "
                "pantalla de bloqueo.",
                "Toca la zona de widgets bajo la hora, elige **Pedometer** y añade los pasos, "
                "la distancia o los pisos subidos.",
                "Toca **OK**.",
            ],
            "Los widgets de pasos y distancia van dentro de un anillo que se cierra al llegar "
            "a tu objetivo. [Guía paso a paso](guide).",
        ]),
        ("¿Necesito un Apple Watch?", [
            "No. Tu iPhone cuenta tus pasos por sí solo cuando lo llevas encima. Si además "
            "llevas un Apple Watch, Pedometer lee Apple Salud, que junta los pasos de los dos "
            "sin contarlos dos veces.",
        ]),
        ("¿Puede registrar caminatas y carreras con GPS?", [
            "Sí. Toca **Caminata** o **Carrera** en **Caminatas y carreras**. El mapa dibuja "
            "tu ruta y muestra el tiempo, la distancia, la velocidad o el ritmo, las "
            "calorías, la altitud y el desnivel. Mientras andas, los datos siguen en la "
            "pantalla de bloqueo con un botón de pausa. Cada una se guarda en Apple Salud con "
            "su ruta, y puedes compartir una imagen.",
        ]),
        ("¿Puede mostrar mi frecuencia cardiaca sin Apple Watch?", [
            "Sí, con iOS 26. Con AirPods Pro 3, Powerbeats Pro 2 o una banda de frecuencia "
            "cardiaca Bluetooth, ves tu frecuencia cardiaca en directo durante una caminata "
            "o una carrera.",
        ]),
        ("¿Puedo cambiar mi objetivo diario de pasos?", [
            "Sí. En **Objetivos diarios** fijas un objetivo de pasos, distancia y pisos. "
            "Empiezan en 10.000 pasos, 8 km y 10 pisos. Los anillos de los widgets se cierran "
            "al llegar a tus objetivos.",
        ]),
        ("¿Pedometer es gratis de verdad?", [
            "Sí. Todas las funciones son gratis y no hay suscripción. En **Ajustes** › "
            "**Apoyar a Pedometer** puedes dejar una propina si quieres. Es opcional y no "
            "desbloquea nada.",
        ]),
        ("¿Pedometer sube mis datos de salud?", [
            "No. Todo se cuenta y se guarda en tu iPhone, y no se sube nada. Pedometer lee "
            "Apple Salud y solo escribe en ella las caminatas y carreras que registras. Tu "
            "ubicación solo se usa mientras registras. Sin cuenta, sin analíticas, sin "
            "rastreo. [Política de privacidad (en inglés)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "contador-pasos-pantalla-bloqueo",
        "title": "Cómo poner un contador de pasos en la pantalla de bloqueo del iPhone",
        "description": "Paso a paso: añade un widget contador de pasos gratis a la pantalla "
                       "de bloqueo y a la pantalla de inicio del iPhone, con la distancia y "
                       "los pisos al lado. Sin Apple Watch ni suscripción.",
        "lead": "Tu iPhone ya cuenta tus pasos. Pedometer pone esa cifra en la pantalla de "
                "bloqueo, para que la veas cada vez que coges el móvil. Lleva un minuto, y no "
                "necesitas un Apple Watch.",
        "choose": [
            ("Pasos", "En un anillo que se cierra en tu objetivo"),
            ("Distancia", "En un anillo, en km o millas"),
            ("Pisos subidos", "Una figura sube una escalera"),
        ],
        "steps": [
            ("Instala Pedometer",
             "Descarga [Pedometer del App Store](store). Es gratis y no pide cuenta."),
            ("Conecta Apple Salud",
             "Abre Pedometer y toca **Conectar**. Permite leer los pasos, la distancia y los "
             "pisos subidos. Tu iPhone los ha contado siempre, así que tu historial aparece "
             "enseguida."),
            ("Fija tus objetivos",
             "Elige un objetivo diario de pasos, distancia y pisos en **Objetivos diarios**. "
             "Los anillos de los widgets se cierran al alcanzarlos."),
            ("Edita la pantalla de bloqueo",
             "Bloquea el iPhone, actívalo y mantén pulsada la pantalla de bloqueo. Toca "
             "**Personalizar** y elige la pantalla de bloqueo."),
            ("Añade el widget",
             "Toca la zona de widgets bajo la hora. Busca **Pedometer** en la lista y toca "
             "pasos, distancia o pisos subidos. Puedes añadir más de uno."),
            ("Toca OK",
             "Tus pasos ya están en la pantalla de bloqueo y se actualizan durante el día."),
            ("Ponlo también en la pantalla de inicio",
             "Mantén pulsada una zona vacía de la pantalla de inicio, toca **Editar** y "
             "luego **Añadir widget**. Busca Pedometer y elige el tamaño pequeño, mediano o "
             "grande. El grande añade el día hora a hora."),
        ],
        "tips": [
            ("Claro, oscuro o solo pasos",
             "Mantén pulsado el widget de la pantalla de inicio y elige **Editar widget** "
             "para ponerlo claro u oscuro, o mostrar solo los pasos."),
            ("Elige un color",
             "Grafito, azul, verde, naranja, rosa o morado, para las barras de objetivo, los "
             "gráficos y el widget."),
            ("¿Sales a caminar?",
             "Toca **Caminata** o **Carrera** en la app para registrar tu ruta con GPS. Los "
             "datos siguen en la pantalla de bloqueo mientras andas."),
            ("Nada sale de tu iPhone",
             "Pedometer no tiene cuenta y no sube nada. Lee Apple Salud en tu iPhone."),
        ],
        "updated": "Escrito para Pedometer 1.5 en iOS 26, octubre de 2026.",
        "cta_title": "Tus pasos, de un vistazo",
        "cta_text": "Un contador de pasos gratis para la pantalla de bloqueo y la de inicio, "
                    "con caminatas y carreras en el mapa. Sin cuenta, sin suscripción.",
    },
}
