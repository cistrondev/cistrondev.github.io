# Timegrapher in Brazilian Portuguese ("você", as in the app and the App Store
# text). Keys are explained in content/unfollowers/en.py; facts to keep true are
# in en.py. Button names are the app's pt-BR strings (Timegrapher
# Localizable.xcstrings): Adicionar relógio, Medir, Medir em posições, Verificar
# magnetismo, Marcha por fotos, Ângulo de levantamento, Identificar pela foto,
# Guia and Hora (tabs). Glossary: Timegrapher/Localization/GLOSSARY.md
# (cronocomparador, marcha, amplitude, erro de batida, balanço, mostrador).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "pt-BR.py"))["L"]["ui"]

L = {
    "name": "Português (Brasil)",
    "path": "pt-br/",
    "og_locale": "pt_BR",
    "also": ["pt"],
    "ui": {
        **_ui,
        "summary": "Em resumo",
        "what_people_say": "O que dizem.",
    },
    "page": {
        "shots_dir": "pt-BR",
        "tagline": "O cronocomparador do relojoeiro, no seu iPhone.",
        "pricing": "Primeiro relógio grátis · Pro com pagamento único",
        "intro": (
            "Marcha, amplitude e erro de batida em cerca de trinta segundos.",
            "O Timegrapher ouve o seu relógio mecânico pelo microfone do iPhone e reúne em "
            "um só lugar toda a sua coleção, cada medição e o valor de cada relógio.",
        ),
        "features": [
            ("Marcha, amplitude, erro de batida",
             "Os segundos que o relógio adianta ou atrasa por dia, quanto o balanço gira e "
             "a simetria entre o tique e o taque. A frequência é detectada sozinha, de "
             "18.000 a 36.000 bph."),
            ("Leituras estáveis",
             "O app acompanha o nível de ruído do ambiente e ignora sons soltos. A "
             "amplitude vem do ângulo de levantamento do seu calibre, que você ajusta com "
             "precisão de um décimo de grau."),
            ("Medir em posições",
             "O app guia você pelas seis posições, ou por quatro para ser mais rápido, e "
             "mostra a marcha média e a diferença entre as posições, como um relojoeiro faz "
             "ao revisar um movimento."),
            ("Sua coleção",
             "Cada relógio com referência, calibre, ângulo de levantamento e até 13 fotos. "
             "Cada medição fica salva e aparece em um gráfico, e um lembrete avisa quando "
             "medir de novo. Identificar pela foto sugere a marca e o modelo."),
            ("A marcha em um dia de uso",
             "Tire uma foto do mostrador hoje e outra amanhã. O Timegrapher compara as fotos "
             "com o relógio do iPhone e mostra como o relógio funcionou no seu pulso."),
            ("Relatório de marcha",
             "Compartilhe um relatório de uma página sobre um relógio, em PDF ou imagem, com "
             "a última leitura, as posições e a evolução. Suas medições podem ser exportadas "
             "em CSV."),
            ("Quanto vale",
             "Os preços atuais do Chrono24 para a sua referência exata, com a mediana "
             "calculada no seu iPhone."),
            ("Verificação de magnetismo",
             "Uma espiral magnetizada é o motivo mais comum para um relógio começar a "
             "adiantar de repente. O magnetômetro do iPhone mostra se o seu relógio precisa "
             "ser desmagnetizado."),
            ("Relógio atômico",
             "A aba Hora mostra a hora exata do servidor da Apple e quanto o relógio do seu "
             "iPhone está desviado. Bipes de contagem regressiva antes de cada minuto ajudam "
             "a acertar o seu relógio no segundo."),
        ],
        "privacy_title": "O som nunca é gravado.",
        "privacy": [
            "O som do microfone é analisado ao vivo e nunca é gravado nem salvo.",
            "Sua coleção e suas medições ficam só no seu iPhone.",
            "A consulta de preços, opcional, busca a referência do seu relógio no Chrono24.",
            "Identificar pela foto envia a foto ao Private Cloud Compute da Apple só quando "
            "você toca. A Apple não a guarda, e o desenvolvedor nunca a vê.",
            "A aba Hora pede a hora ao servidor da Apple. O pedido não leva dados pessoais.",
        ],
        "note": "",
        "reviews": [],
        "shots": [
            "Seu iPhone é um cronocomparador: marcha, amplitude e erro de batida em 30 segundos.",
            "Leituras que não pulam: mede movimentos silenciosos mesmo com barulho em volta.",
            "Toda a sua coleção num relance: idade, estado e valor de cada relógio.",
            "Veja o desvio antes que importe: cada medição salva, em um gráfico.",
            "Saiba quanto vale seu relógio: a mediana do Chrono24 para a sua referência exata.",
            "Seu relógio está magnetizado? Verificado em dez segundos.",
            "A marcha em um dia de uso: duas fotos, com um dia de intervalo.",
        ],
    },
    "guide_link": "Como verificar a precisão do seu relógio mecânico com o iPhone",
    "faq": [
        ("Um iPhone consegue medir a precisão do meu relógio mecânico?", [
            "Sim. O Timegrapher ouve o relógio pelo microfone do próprio iPhone e funciona "
            "como o cronocomparador de um relojoeiro. Em cerca de 30 segundos, ele mostra a "
            "marcha (os segundos que o relógio adianta ou atrasa por dia), a amplitude "
            "(quanto o balanço gira) e o erro de batida (a diferença entre o tique e o "
            "taque).",
            "Funciona com relógios automáticos e de corda manual. O primeiro relógio é "
            "grátis, e não há assinatura. [Ver na App Store](store).",
        ]),
        ("Como medir meu relógio com o Timegrapher?", [
            [
                "Dê corda no relógio e procure um lugar silencioso.",
                "Toque em **Adicionar relógio** e informe o calibre e, se souber, o ângulo "
                "de levantamento.",
                "Toque em **Medir** e apoie com firmeza a borda inferior do iPhone no "
                "relógio, de preferência no vidro.",
                "Fique parado. A medição para sozinha em 0:30 e mostra a marcha, a "
                "amplitude, o erro de batida e uma avaliação.",
            ],
            "[Guia passo a passo](guide).",
        ]),
        ("Quais são bons valores de marcha, amplitude e erro de batida?", [
            "Estas são as faixas que o Timegrapher usa na avaliação:",
            [
                "**Marcha:** dentro de ±5 segundos por dia é nível de cronômetro. Até ±15 "
                "está bom para o uso diário. A partir de ±30 o relógio precisa de regulagem.",
                "**Amplitude:** de 250° a 315° é saudável, com o relógio com corda e o "
                "mostrador para cima. Abaixo de 220° uma revisão está próxima, e abaixo de "
                "200° o óleo provavelmente secou. Acima de 315° o balanço corre o risco de "
                "bater.",
                "**Erro de batida:** abaixo de 0,3 ms o tique e o taque estão bem "
                "equilibrados. A partir de 0,8 ms vale a pena um ajuste, e acima de 1,5 ms o "
                "desequilíbrio é claro.",
            ],
            "A marcha muda com a posição, então anote se o relógio estava com o mostrador "
            "para cima, para baixo ou com a coroa para baixo. **Medir em posições** mede "
            "cada uma por vez.",
        ]),
        ("Como saber se meu relógio está magnetizado?", [
            "Uma espiral magnetizada é o motivo mais comum para um relógio mecânico começar "
            "a adiantar de repente, muitas vezes minutos por dia. O Timegrapher verifica "
            "isso com o magnetômetro do iPhone: toque em **Verificar magnetismo**, meça o "
            "campo de fundo e depois aproxime o relógio da parte de trás do iPhone. A "
            "diferença é a resposta.",
            "Antes, tire capas, carteiras ou suportes magnéticos. Cada verificação fica "
            "salva, então uma antes e outra depois de desmagnetizar mostram se funcionou.",
        ]),
        ("Qual ângulo de levantamento devo usar?", [
            "O ângulo de levantamento é uma característica do movimento, e o Timegrapher o "
            "usa para calcular a amplitude. Muitos calibres suíços usam 52°, mas vários usam "
            "outros valores, então procure o do seu calibre. Um ângulo errado é o motivo "
            "comum de um app de celular mostrar a amplitude errada. A marcha e o erro de "
            "batida não dependem dele. No Timegrapher você o ajusta com precisão de um "
            "décimo de grau.",
        ]),
        ("Qual a precisão de um cronocomparador no celular comparado a um de bancada?", [
            "O Timegrapher mede cada tique com precisão de frações de milissegundo e ajusta "
            "milhares deles ao relógio do iPhone, o mesmo princípio de uma máquina de "
            "bancada. Um lugar silencioso e um contato firme dão as melhores leituras. Fones "
            "Bluetooth comprimem o som, então desconecte-os e deixe o microfone do iPhone "
            "ouvir.",
            "Use os resultados como referência. Para decidir uma revisão, valem antes uma "
            "máquina de bancada e a avaliação de um relojoeiro.",
        ]),
        ("Posso ver como meu relógio funciona no pulso durante um dia inteiro?", [
            "Sim. **Marcha por fotos** compara duas fotos do mostrador tiradas com um dia de "
            "intervalo. Cada foto registra a hora exata em que foi tirada, então a posição "
            "do ponteiro dos segundos mostra quanto o relógio adiantou ou atrasou enquanto "
            "você o usava.",
        ]),
        ("Funciona com relógios de quartzo?", [
            "Não. Um relógio de quartzo marca o tempo com um cristal de quartzo e move o "
            "ponteiro uma vez por segundo, então não há balanço para ouvir. O Timegrapher é "
            "para relógios mecânicos automáticos e de corda manual.",
        ]),
        ("O Timegrapher é grátis?", [
            "Seu primeiro relógio é grátis para sempre, com todas as medições. O "
            "**Timegrapher Pro** é uma compra única que remove o limite de relógios. Não há "
            "assinatura, e as compras são restauradas em qualquer aparelho com a mesma Conta "
            "Apple.",
        ]),
        ("O Timegrapher grava meu áudio?", [
            "Não. O som é analisado ao vivo e nunca é gravado, salvo ou enviado. Sua coleção "
            "fica no seu iPhone. A consulta de preços, opcional, busca a referência do seu "
            "relógio no Chrono24, e **Identificar pela foto** envia essa foto ao Private "
            "Cloud Compute da Apple só quando você toca. "
            "[Política de privacidade (em inglês)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "verificar-precisao-relogio",
        "title": "Como verificar a precisão do seu relógio mecânico com o iPhone",
        "description": "Passo a passo: meça a marcha, a amplitude e o erro de batida do seu "
                       "relógio automático ou de corda manual com o microfone do iPhone, "
                       "entenda os resultados e verifique se ele está magnetizado.",
        "lead": "Um cronocomparador mostra quanto um relógio mecânico adianta ou atrasa e "
                "como está o movimento. O Timegrapher transforma o seu iPhone em um, usando "
                "o microfone. Um lugar silencioso e um contato firme dão a leitura mais "
                "estável.",
        "choose": [
            ("Marcha", "Segundos que adianta ou atrasa por dia"),
            ("Amplitude", "Quanto o balanço gira"),
            ("Erro de batida", "Tique contra taque, em ms"),
        ],
        "steps": [
            ("Instale o Timegrapher",
             "Baixe o [Timegrapher na App Store](store). Seu primeiro relógio é grátis. "
             "Permita o acesso ao microfone quando o app pedir."),
            ("Dê corda no relógio",
             "Dê corda completa em um relógio manual, ou use um automático no pulso por um "
             "tempo antes. Com o relógio quase parando, a amplitude fica mais baixa."),
            ("Adicione o relógio",
             "Toque em **Adicionar relógio** e informe a marca, a referência e o calibre. "
             "Ajuste o **Ângulo de levantamento** do seu calibre, porque a amplitude depende "
             "dele. **Identificar pela foto** pode sugerir a marca e o modelo."),
            ("Procure um lugar silencioso",
             "O zumbido de uma geladeira ou o trânsito tiram precisão. Desconecte os fones "
             "Bluetooth para que o microfone do iPhone ouça."),
            ("Meça",
             "Toque em **Medir** e apoie com firmeza a borda inferior do iPhone no relógio, "
             "de preferência no vidro. O contato direto transmite os tiques muito melhor que "
             "o ar. A medição para sozinha em 0:30."),
            ("Leia o resultado",
             "Você vê a marcha em segundos por dia, a amplitude em graus, o erro de batida em "
             "milissegundos e a frequência, com uma avaliação de Excelente a Precisa de "
             "revisão e os motivos. A aba **Guia** explica cada número."),
            ("Teste outras posições",
             "A marcha muda com a posição. **Medir em posições** mede o relógio com o "
             "mostrador para cima, para baixo e de lado, e mostra a diferença entre elas."),
            ("Verifique o magnetismo",
             "Se o relógio começar a adiantar muito de repente, toque em **Verificar "
             "magnetismo**. Ele usa o magnetômetro do iPhone e diz se o relógio precisa ser "
             "desmagnetizado."),
        ],
        "tips": [
            ("Acompanhe com o tempo",
             "Cada leitura fica salva e aparece em um gráfico, então um movimento que vai se "
             "desviando aos poucos aparece antes de parar."),
            ("Um dia no pulso",
             "**Marcha por fotos** compara duas fotos do mostrador tiradas com um dia de "
             "intervalo e mostra como o relógio funcionou enquanto você o usava."),
            ("Quanto vale",
             "A consulta de preços busca os preços atuais do Chrono24 para a sua referência "
             "exata e salva a mediana."),
            ("Pague uma vez",
             "O primeiro relógio é grátis. O Timegrapher Pro libera relógios ilimitados com "
             "um único pagamento, sem assinatura."),
        ],
        "updated": "Escrito para o Timegrapher 2.9, novembro de 2026.",
        "cta_title": "Meça seu relógio hoje à noite",
        "cta_text": "Marcha, amplitude e erro de batida em 30 segundos, com o iPhone que você "
                    "já tem. Primeiro relógio grátis, sem assinatura.",
    },
}
