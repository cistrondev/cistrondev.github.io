# Timegrapher in Spanish ("tú", as in the app and the App Store text). Keys are
# explained in content/unfollowers/en.py; facts to keep true are in en.py.
# Button names are the app's Spanish strings (Timegrapher Localizable.xcstrings):
# Añadir reloj, Medir, Medir en posiciones, Comprobar magnetismo, Marcha por
# fotos, Ángulo de levantamiento, Identificar por la foto, Guía and Hora (tabs).
# Glossary: Timegrapher/Localization/GLOSSARY.md (cronocomparador, marcha,
# amplitud, error de ritmo, volante, espiral, esfera).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "es.py"))["L"]["ui"]

L = {
    "name": "Español",
    "path": "es/",
    "og_locale": "es_ES",
    "ui": {
        **_ui,
        "summary": "De un vistazo",
        "what_people_say": "Lo que dicen.",
    },
    "page": {
        "shots_dir": "es",
        "tagline": "El cronocomparador del relojero, en tu iPhone.",
        "pricing": "Primer reloj gratis · Pro con un pago único",
        "intro": (
            "Marcha, amplitud y error de ritmo en unos treinta segundos.",
            "Timegrapher escucha tu reloj mecánico con el micrófono del iPhone y reúne en "
            "un solo lugar toda tu colección, cada medición y el valor de cada reloj.",
        ),
        "features": [
            ("Marcha, amplitud, error de ritmo",
             "Los segundos que el reloj adelanta o atrasa al día, cuánto gira el volante y "
             "la simetría entre el tic y el tac. La frecuencia se detecta sola, de 18.000 a "
             "36.000 bph."),
            ("Lecturas estables",
             "La app sigue el nivel de ruido de la habitación e ignora los sonidos sueltos. "
             "La amplitud sale del ángulo de levantamiento de tu calibre, que puedes "
             "ajustar al décimo de grado."),
            ("Medir en posiciones",
             "La app te guía por seis posiciones, o por cuatro para ir más rápido, y "
             "muestra la marcha media y la diferencia entre posiciones, como cuando un "
             "relojero revisa un movimiento."),
            ("Tu colección",
             "Cada reloj con su referencia, su calibre, su ángulo de levantamiento y hasta "
             "13 fotos. Cada medición se guarda y se muestra en un gráfico, y un "
             "recordatorio te avisa de cuándo volver a medir. Identificar por la foto "
             "sugiere la marca y el modelo."),
            ("La marcha en un día de uso",
             "Haz una foto de la esfera hoy y otra mañana. Timegrapher compara las fotos "
             "con el reloj del iPhone y muestra cómo funcionó el reloj en tu muñeca."),
            ("Informe de marcha",
             "Comparte un informe de una página sobre un reloj, en PDF o en imagen, con la "
             "última lectura, las posiciones y la evolución. Tus mediciones se pueden "
             "exportar en CSV."),
            ("Cuánto vale",
             "Los precios actuales de Chrono24 para tu referencia exacta, con la mediana "
             "calculada en tu iPhone."),
            ("Comprobación de magnetismo",
             "Una espiral magnetizada es la causa más común de que un reloj empiece a "
             "adelantar de repente. El magnetómetro del iPhone muestra si hay que "
             "desmagnetizar tu reloj."),
            ("Reloj atómico",
             "La pestaña Hora muestra la hora exacta del servidor de Apple y cuánto se "
             "desvía el reloj de tu iPhone. Unos tonos de cuenta atrás antes de cada minuto "
             "te ayudan a poner tu reloj en hora al segundo."),
        ],
        "privacy_title": "El sonido nunca se graba.",
        "privacy": [
            "El sonido del micrófono se analiza en directo y nunca se graba ni se guarda.",
            "Tu colección y tus mediciones se quedan solo en tu iPhone.",
            "La consulta de precios, opcional, busca la referencia de tu reloj en Chrono24.",
            "Identificar por la foto envía la foto al Private Cloud Compute de Apple solo "
            "cuando lo tocas. Apple no la conserva y el desarrollador nunca la ve.",
            "La pestaña Hora pide la hora al servidor de Apple. La petición no lleva datos "
            "personales.",
        ],
        "note": "",
        "reviews": [],
        "shots": [
            "Tu iPhone es un cronocomparador: marcha, amplitud y error de ritmo en 30 segundos.",
            "Lecturas que no saltan: mide movimientos silenciosos incluso con ruido alrededor.",
            "Toda tu colección de un vistazo: edad, estado y valor de cada reloj.",
            "Ve la desviación antes de que importe: cada medición guardada, en un gráfico.",
            "Descubre cuánto vale tu reloj: la mediana de Chrono24 para tu referencia exacta.",
            "¿Tu reloj está magnetizado? Comprobado en diez segundos.",
            "La marcha en un día de uso: dos fotos, con un día entre ellas.",
        ],
    },
    "guide_link": "Cómo comprobar la precisión de tu reloj mecánico con el iPhone",
    "faq": [
        ("¿Puede un iPhone medir la precisión de mi reloj mecánico?", [
            "Sí. Timegrapher escucha el reloj con el micrófono del propio iPhone y funciona "
            "como el cronocomparador de un relojero. En unos 30 segundos muestra la marcha "
            "(los segundos que adelanta o atrasa al día), la amplitud (cuánto gira el "
            "volante) y el error de ritmo (la diferencia entre el tic y el tac).",
            "Funciona con relojes automáticos y de cuerda manual. El primer reloj es gratis "
            "y no hay suscripción. [Ver en la App Store](store).",
        ]),
        ("¿Cómo mido mi reloj con Timegrapher?", [
            [
                "Da cuerda al reloj y busca un sitio tranquilo.",
                "Toca **Añadir reloj** e introduce el calibre y, si lo conoces, su ángulo de "
                "levantamiento.",
                "Toca **Medir** y apoya con firmeza el borde inferior del iPhone sobre el "
                "reloj, mejor sobre el cristal.",
                "No te muevas. La medición se detiene sola a los 0:30 y muestra la marcha, la "
                "amplitud, el error de ritmo y una valoración.",
            ],
            "[Guía paso a paso](guide).",
        ]),
        ("¿Qué valores son buenos para la marcha, la amplitud y el error de ritmo?", [
            "Estos son los márgenes que usa Timegrapher para su valoración:",
            [
                "**Marcha:** dentro de ±5 segundos al día es nivel de cronómetro. Hasta ±15 "
                "está bien para el uso diario. A partir de ±30 el reloj necesita un reglaje.",
                "**Amplitud:** de 250° a 315° es saludable, con el reloj con cuerda y la "
                "esfera hacia arriba. Por debajo de 220° pronto tocará una revisión, y por "
                "debajo de 200° el aceite probablemente se ha secado. Por encima de 315° el "
                "volante puede llegar a rebotar.",
                "**Error de ritmo:** por debajo de 0,3 ms el tic y el tac están bien "
                "equilibrados. A partir de 0,8 ms conviene un ajuste, y por encima de 1,5 ms "
                "el desequilibrio es claro.",
            ],
            "La marcha cambia con la posición, así que anota si el reloj estaba con la "
            "esfera arriba, con la esfera abajo o con la corona abajo. **Medir en "
            "posiciones** las toma una tras otra.",
        ]),
        ("¿Cómo sé si mi reloj está magnetizado?", [
            "Una espiral magnetizada es la causa más común de que un reloj mecánico empiece "
            "a adelantar de repente, a menudo minutos al día. Timegrapher lo comprueba con "
            "el magnetómetro del iPhone: toca **Comprobar magnetismo**, mide el campo de "
            "fondo y luego acerca el reloj a la parte trasera del iPhone. La diferencia es "
            "la respuesta.",
            "Quita antes cualquier funda, cartera o soporte magnético. Cada comprobación se "
            "guarda, así que una antes y otra después de desmagnetizar muestran si funcionó.",
        ]),
        ("¿Qué ángulo de levantamiento debo usar?", [
            "El ángulo de levantamiento es una característica del movimiento, y Timegrapher "
            "lo usa para calcular la amplitud. Muchos calibres suizos usan 52°, pero "
            "bastantes usan otros valores, así que busca el de tu calibre. Un ángulo "
            "equivocado es la razón habitual de que una app de móvil dé mal la amplitud. La "
            "marcha y el error de ritmo no dependen de él. En Timegrapher puedes ajustarlo "
            "al décimo de grado.",
        ]),
        ("¿Qué precisión tiene un cronocomparador en el móvil frente a uno de taller?", [
            "Timegrapher mide cada tic con una precisión de fracciones de milisegundo y "
            "ajusta miles de ellos al reloj del iPhone, el mismo principio que usa una "
            "máquina de taller. Una habitación tranquila y un contacto firme dan las mejores "
            "lecturas. Los auriculares Bluetooth comprimen el sonido, así que desconéctalos "
            "y deja que escuche el micrófono del iPhone.",
            "Toma los resultados como una guía. Para decidir una revisión, cuentan antes "
            "una máquina de taller y el criterio de un relojero.",
        ]),
        ("¿Puedo ver cómo funciona mi reloj en la muñeca durante un día entero?", [
            "Sí. **Marcha por fotos** compara dos fotos de la esfera hechas con un día de "
            "diferencia. Cada foto guarda la hora exacta en que se hizo, así que la "
            "posición del segundero muestra cuánto adelantó o atrasó el reloj mientras lo "
            "llevabas.",
        ]),
        ("¿Funciona con relojes de cuarzo?", [
            "No. Un reloj de cuarzo marca la hora con un cristal de cuarzo y mueve la aguja "
            "una vez por segundo, así que no hay volante que escuchar. Timegrapher es para "
            "relojes mecánicos automáticos y de cuerda manual.",
        ]),
        ("¿Timegrapher es gratis?", [
            "Tu primer reloj es gratis para siempre, con todas las mediciones. **Timegrapher "
            "Pro** es una compra única que quita el límite de relojes. No hay suscripción, y "
            "las compras se restauran en cualquier dispositivo con la misma cuenta de Apple.",
        ]),
        ("¿Timegrapher graba mi audio?", [
            "No. El sonido se analiza en directo y nunca se graba, se guarda ni se sube. Tu "
            "colección se queda en tu iPhone. La consulta de precios, opcional, busca la "
            "referencia de tu reloj en Chrono24, e **Identificar por la foto** envía esa "
            "foto al Private Cloud Compute de Apple solo cuando lo tocas. "
            "[Política de privacidad (en inglés)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "comprobar-precision-reloj",
        "title": "Cómo comprobar la precisión de tu reloj mecánico con el iPhone",
        "description": "Paso a paso: mide la marcha, la amplitud y el error de ritmo de tu "
                       "reloj automático o de cuerda manual con el micrófono del iPhone, "
                       "interpreta los resultados y comprueba si está magnetizado.",
        "lead": "Un cronocomparador indica cuánto adelanta o atrasa un reloj mecánico y en "
                "qué estado está su movimiento. Timegrapher convierte tu iPhone en uno con "
                "el micrófono. Una habitación tranquila y un contacto firme dan la lectura "
                "más estable.",
        "choose": [
            ("Marcha", "Segundos que adelanta o atrasa al día"),
            ("Amplitud", "Cuánto gira el volante"),
            ("Error de ritmo", "El tic frente al tac, en ms"),
        ],
        "steps": [
            ("Instala Timegrapher",
             "Descarga [Timegrapher en la App Store](store). Tu primer reloj es gratis. "
             "Permite el acceso al micrófono cuando la app lo pida."),
            ("Da cuerda al reloj",
             "Da cuerda completa a un reloj manual, o lleva puesto un automático un rato "
             "antes. Con el reloj casi parado, la amplitud sale más baja."),
            ("Añade el reloj",
             "Toca **Añadir reloj** e introduce la marca, la referencia y el calibre. Ajusta "
             "el **Ángulo de levantamiento** de tu calibre, porque la amplitud depende de él. "
             "**Identificar por la foto** puede sugerir la marca y el modelo."),
            ("Busca un sitio tranquilo",
             "El zumbido de una nevera o el tráfico restan precisión. Desconecta los "
             "auriculares Bluetooth para que escuche el micrófono del iPhone."),
            ("Mide",
             "Toca **Medir** y apoya con firmeza el borde inferior del iPhone sobre el "
             "reloj, mejor sobre el cristal. El contacto directo transmite los tics mucho "
             "mejor que el aire. La medición se detiene sola a los 0:30."),
            ("Lee el resultado",
             "Verás la marcha en segundos al día, la amplitud en grados, el error de ritmo "
             "en milisegundos y la frecuencia, con una valoración de Excelente a Necesita "
             "revisión y sus motivos. La pestaña **Guía** explica cada cifra."),
            ("Prueba otras posiciones",
             "La marcha cambia con la posición. **Medir en posiciones** toma el reloj con la "
             "esfera arriba, con la esfera abajo y de canto, y muestra la diferencia entre "
             "ellas."),
            ("Comprueba el magnetismo",
             "Si el reloj empieza a adelantar mucho de repente, toca **Comprobar "
             "magnetismo**. Usa el magnetómetro del iPhone y te dice si hay que "
             "desmagnetizar el reloj."),
        ],
        "tips": [
            ("Síguelo en el tiempo",
             "Cada lectura se guarda y aparece en un gráfico, así que un movimiento que se "
             "desvía poco a poco se nota antes de que se pare."),
            ("Un día en la muñeca",
             "**Marcha por fotos** compara dos fotos de la esfera hechas con un día de "
             "diferencia y muestra cómo funcionó el reloj mientras lo llevabas."),
            ("Cuánto vale",
             "La consulta de precios obtiene los precios actuales de Chrono24 para tu "
             "referencia exacta y guarda la mediana."),
            ("Paga una vez",
             "El primer reloj es gratis. Timegrapher Pro añade relojes ilimitados con un "
             "solo pago, sin suscripción."),
        ],
        "updated": "Escrita para Timegrapher 2.9, noviembre de 2026.",
        "cta_title": "Mide tu reloj esta noche",
        "cta_text": "Marcha, amplitud y error de ritmo en 30 segundos, con el iPhone que ya "
                    "tienes. Primer reloj gratis, sin suscripción.",
    },
}
