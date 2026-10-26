# Jobsite Calc in Spanish (Mexico), "tú", with the jobsite words the app itself
# uses (contrahuella, huella, zanca, limatesa, limahoya, bulto, pies tabla).
# Keys are explained in en.py.

L = {
    "name": "Español",
    "path": "es/",
    "og_locale": "es_MX",
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
        "coming_soon": "Pronto en la App Store",
        "soon": "Próximamente",
        "platform": "iPhone y iPad · iOS 17 o posterior",
        "screenshots": "Capturas de pantalla",
        "prev": "Capturas anteriores",
        "next": "Capturas siguientes",
        "privacy_eyebrow": "Privacidad",
        "read_policy": "Leer la política de privacidad (en inglés)",
        "more_apps": "Más apps",
        "languages": "Idiomas",
        "faq": "Preguntas frecuentes",
        "summary": "Los límites que revisa la app",
        "tips": "Conviene saber",
        "cta_more": "Sobre {name}",
    },
    "page": {
        "shots_dir": "es",
        "tagline": "Pies, pulgadas y fracciones. Pagas una vez.",
        "pricing": "Gratis · Desbloqueo único",
        "platform": "iPhone y iPad · iOS 17 o posterior",
        "intro": (
            "Una calculadora de pies, pulgadas y fracciones para carpinteros, armadores y "
            "contratistas.",
            "Escribe la medida como la lees en la cinta, mira toda la operación en pantalla "
            "y saca de ahí escaleras, vigas y concreto. Una sola compra desbloquea todas las "
            "herramientas, para siempre. Sin suscripción, sin cuenta, sin internet.",
        ),
        "features": [
            ("Pies, pulgadas y fracciones",
             "Escribe 12' 3-1/2\" con las teclas Pies, Pulg y /. Suma, resta, multiplica y "
             "divide, y obtén el resultado al 1/16 más cercano, o a la fracción que elijas. "
             "Toda la operación queda en pantalla, con paréntesis."),
            ("Convierte con un toque",
             "Toca la unidad del resultado para pasar de pies y pulgadas a pulgadas, pies "
             "decimales, yardas, metros, centímetros y milímetros. Las áreas, los volúmenes "
             "y los ángulos también se convierten."),
            ("Escaleras con revisión de código",
             "Escribe la altura total y obtén contrahuellas, huellas, largo de zanca, ángulo "
             "y hueco de escalera, con el dibujo de la zanca. Una revisión en verde o rojo "
             "contra los límites de 7-3/4 pulgadas de contrahuella, 10 pulgadas de huella y "
             "6' 8\" de altura libre, que puedes cambiar."),
            ("Vigas y techos",
             "Vigas comunes, limatesas, limahoyas y vigas cortas a partir de la pendiente y "
             "el desarrollo, con los cortes a plomo y a nivel y la lista de cortas. "
             "Limatesas irregulares. Cuadros, paquetes y hojas de techo."),
            ("Concreto y materiales",
             "Losas, zapatas, columnas y pilares en yardas cúbicas y bultos. Hojas de "
             "tablaroca y triplay, block, ladrillo, postes y soleras, pies tabla y costo de "
             "la madera."),
            ("Ángulos y una cinta",
             "Molduras e ingletes compuestos, polígonos, círculos y arcos. Cada resultado "
             "queda en una cinta que puedes reutilizar, copiar o compartir."),
        ],
        "privacy_title": "Nada sale de tu teléfono.",
        "privacy": [
            "La app no tiene código de red. No sube nada.",
            "Sin cuenta, sin analíticas, sin rastreo, sin anuncios.",
            "Tus ajustes y tu cinta se quedan en tu iPhone.",
            "La única compra pasa por Apple y el precio nunca se renueva.",
        ],
        "note": "Pantalla oscura, teclas grandes y clics al teclear, para guantes y sol. "
                "Funciona sin señal.",
        "shots": [
            "Pies, pulgadas y fracciones, con toda la operación en pantalla.",
            "Escaleras a partir de la altura total: contrahuellas, huellas, zanca y revisión de código.",
            "Vigas a partir de la pendiente y el desarrollo, con los cortes a plomo y a nivel.",
            "Losas, zapatas y pilares de concreto en yardas cúbicas y bultos.",
            "Molduras e ingletes compuestos, con los ángulos de inglete y bisel.",
            "Una sola compra desbloquea todas las herramientas, para siempre. Sin suscripción.",
        ],
    },
    "guide_link": "Cómo trazar una escalera con Jobsite Calc",
    "faq": [
        ("¿Jobsite Calc es una compra única?", [
            "Sí. La app es gratis: la calculadora, las conversiones y la cinta no cuestan "
            "nada. Una sola compra dentro de la app desbloquea las herramientas: escaleras, "
            "vigas, techo, concreto, materiales y ángulos. No hay suscripción y nada se "
            "renueva. La compra se comparte con tu familia con Compartir en familia.",
        ]),
        ("¿Cómo escribo pies, pulgadas y fracciones?", [
            "Teclea 12, Pies, 3, Pulg, 1, /, 2 y la pantalla muestra 12' 3-1/2\". Un número "
            "solo se toma como pulgadas; en Ajustes puedes cambiarlo a pies, milímetros o "
            "centímetros. Con las teclas métricas activadas puedes mezclar metros y "
            "pulgadas en la misma operación, y el resultado sale en la unidad que elijas.",
            "Toda la operación queda en pantalla mientras escribes, con paréntesis, para "
            "que veas lo que metiste antes de tocar igual.",
        ]),
        ("¿Cómo calcula la escalera?", [
            "Escribe la altura total, de piso a piso. La app la divide en el menor número "
            "de contrahuellas que quepan bajo el límite, 7-3/4 pulgadas por defecto, y te "
            "da la altura de contrahuella, las huellas, el desarrollo total, el largo de la "
            "zanca, el ángulo y el hueco de escalera. Una línea se pone en verde cuando la "
            "escalera cumple los límites de contrahuella, huella y altura libre, y en rojo "
            "cuando no. Los límites se cambian en Ajustes.",
            "[Paso a paso](guide).",
        ]),
        ("¿Qué vigas calcula?", [
            "Vigas comunes a partir de la pendiente y el desarrollo, limatesas y limahoyas "
            "regulares e irregulares, y las vigas cortas a tu separación, cada una con sus "
            "cortes a plomo y a nivel. La pendiente puede ser 7/12, grados o porcentaje. La "
            "herramienta de techo convierte un área en planta y una pendiente en cuadros, "
            "paquetes y hojas, y las filas de muro inclinado dan el largo de los postes a "
            "lo largo de un hastial.",
        ]),
        ("¿Funciona en sistema métrico?", [
            "Sí. Activa las teclas métricas en Ajustes para m, cm y mm, mezcla unidades en "
            "una misma operación y toca la unidad del resultado para convertirlo. El "
            "concreto se puede mostrar en metros cúbicos y bultos de 25 kg, y las "
            "herramientas de escaleras y vigas también aceptan medidas métricas.",
        ]),
        ("¿Algo sale de mi iPhone?", [
            "No. La app no tiene código de red y no hace ninguna conexión. No hay cuenta, "
            "ni analíticas, ni anuncios. La única compra pasa por la App Store y la maneja "
            "Apple. [Política de privacidad](privacy), en inglés.",
        ]),
    ],
    "guide": {
        "slug": "trazar-escalera",
        "title": "Cómo trazar una zanca de escalera: contrahuellas, huellas y la revisión de código",
        "description": "Paso a paso: mide la altura total, escríbela en Jobsite Calc, lee "
                       "las contrahuellas, las huellas, el largo de la zanca y el hueco de "
                       "escalera, revisa la escalera contra el código y marca la zanca.",
        "lead": "Una escalera empieza con una sola medida, la altura total. A partir de ella "
                "la app da el número de contrahuellas, su altura, las huellas, el desarrollo "
                "total, el largo de la zanca, el ángulo y el hueco de escalera, y los revisa "
                "contra los límites del código. Así se usa.",
        "choose": [
            ("Contrahuella", "7-3/4 pulg como máximo"),
            ("Huella", "10 pulg como mínimo"),
            ("Altura libre", "6 pies 8 pulg como mínimo"),
        ],
        "steps": [
            ("Mide la altura total",
             "Mide en vertical desde el piso terminado de abajo hasta el piso terminado de "
             "arriba. Cuenta el acabado que llevará cada nivel: la escalera se traza a las "
             "superficies terminadas, no al contrapiso."),
            ("Abre Escaleras",
             "En Jobsite Calc toca Herramientas y luego **Escaleras**. La contrahuella "
             "máxima, el fondo de huella y la altura libre vienen con los límites "
             "habituales del código. Puedes cambiarlos en Ajustes."),
            ("Escribe la altura total",
             "Escríbela como la lees en la cinta, por ejemplo 9' 1\". La app calcula la "
             "escalera mientras escribes."),
            ("Lee las contrahuellas",
             "La app usa el menor número de contrahuellas que mantenga cada una bajo el "
             "límite, todas de la misma altura. Para 9' 1\" son 15 contrahuellas de 7-1/4\"."),
            ("Huellas y desarrollo total",
             "Hay una huella menos que contrahuellas. 14 huellas de 10\" dan un desarrollo "
             "total de 11' 8\". Si tienes menos espacio, escribe el desarrollo total que "
             "tienes: la app acorta las huellas para que quepan, y la revisión de código te "
             "avisa si quedan demasiado cortas."),
            ("Revisa la línea del código",
             "Verde significa que cada contrahuella mide como máximo 7-3/4\", cada huella "
             "como mínimo 10\" y la altura libre como mínimo 6' 8\". Rojo nombra el límite "
             "que falla. Los códigos locales varían, así que pon tus propios límites en "
             "Ajustes."),
            ("Hueco de escalera",
             "La app también da el largo del hueco en el piso que conserva la altura libre, "
             "usando el espesor de piso de Ajustes. Compáralo con la estructura antes de "
             "cortar."),
            ("Marca y corta la zanca",
             "Pon una escuadra de armador en la altura de contrahuella y el fondo de huella "
             "y repítela a lo largo de la zanca, una vez por contrahuella. El largo de zanca "
             "en pantalla va de la primera contrahuella a la última, así que compra madera "
             "más larga. Rebaja la base de la zanca el espesor de una huella, para que el "
             "primer y el último escalón queden parejos una vez puestas las huellas."),
        ],
        "tips": [
            ("Todas las contrahuellas iguales",
             "Los códigos permiten solo 3/8\" entre la contrahuella más alta y la más baja "
             "de un tramo. La app da una sola altura; respétala en cada escalón."),
            ("El desarrollo sale de las huellas",
             "El desarrollo total es huellas por fondo de huella. La nariz sobresale de "
             "cada contrahuella pero no cambia el desarrollo."),
            ("Elige tu fracción",
             "La app redondea a 1/16\" por defecto. Elige 1/8\" o 1/32\" en Ajustes, o "
             "decimales si lo prefieres."),
            ("Los límites son los habituales en vivienda",
             "Contrahuella de 7-3/4\", huella de 10\" y 6' 8\" de altura libre son los "
             "límites que usan la mayoría de los códigos residenciales de Estados Unidos. "
             "Las escaleras comerciales y otros países varían. Cambia los límites en "
             "Ajustes y la revisión los sigue."),
        ],
        "updated": "Escrito para Jobsite Calc 1.0, octubre de 2026.",
        "cta_title": "Traza la siguiente escalera en segundos",
        "cta_text": "Jobsite Calc calcula contrahuellas, huellas, zanca y revisión de código "
                    "a partir de la altura total, en tu iPhone, sin internet. Pagas una vez, "
                    "sin suscripción.",
    },
}
