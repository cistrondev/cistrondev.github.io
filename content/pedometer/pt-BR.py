# Pedometer in Brazilian Portuguese ("você", as in the app and the App Store
# text). Keys are explained in content/unfollowers/en.py; facts to keep true are
# in en.py. App words from Shared/Localizable.xcstrings (Conectar, Caminhada,
# Corrida, Caminhadas e corridas, Metas diárias, Apoiar o Pedometer, Ajustes);
# iOS words are Apple's Brazilian Portuguese (Tela Bloqueada, Tela de Início).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "pt-BR.py"))["L"]["ui"]

L = {
    "name": "Português (Brasil)",
    "path": "pt-br/",
    "og_locale": "pt_BR",
    "also": ["pt"],
    "ui": {**_ui, "summary": "Widgets da Tela Bloqueada"},
    "page": {
        "shots_dir": "pt-BR",
        "tagline": "Seus passos na Tela Bloqueada.",
        "pricing": "Grátis",
        "intro": (
            "Passos, distância e andares subidos, em números e gráficos claros.",
            "O Pedometer lê o Apple Saúde e coloca a contagem de hoje na sua Tela Bloqueada "
            "e na Tela de Início. Seu iPhone conta seus passos sozinho, e se você usa um "
            "Apple Watch, os passos dele também contam.",
        ),
        "features": [
            ("Hoje",
             "Seus passos ao lado da sua meta, com quanto falta. Distância e andares ao lado "
             "das metas deles, com energia ativa e velocidade de caminhada."),
            ("Caminhadas e corridas",
             "Registre uma caminhada ou corrida com GPS: seu trajeto no mapa, com velocidade "
             "ou ritmo, altitude, subida e calorias. Cada uma é salva no Apple Saúde com o "
             "trajeto."),
            ("Frequência cardíaca ao vivo",
             "Com AirPods Pro 3, Powerbeats Pro 2 ou uma cinta cardíaca Bluetooth, você vê "
             "sua frequência cardíaca ao vivo (iOS 26)."),
            ("Na Tela Bloqueada",
             "Durante o percurso, tempo, distância, velocidade, batimentos e calorias "
             "ficam na Tela Bloqueada, com um botão de pausa."),
            ("Compartilhe uma caminhada",
             "Uma imagem de cada caminhada ou corrida, com o mapa e seus números, para "
             "qualquer app."),
            ("Suas metas",
             "Defina uma meta diária de passos, distância e andares. Elas começam em 10.000 "
             "passos, 8 km e 10 andares."),
            ("Histórico",
             "Um gráfico por número para a última semana, mês ou ano, com a média diária e "
             "a variação em relação ao período anterior."),
            ("Widgets da Tela Bloqueada",
             "Passos e distância, cada um num anel que se fecha na sua meta, e andares, com "
             "um bonequinho que sobe uma escada."),
            ("Widget da Tela de Início",
             "O mesmo cartão do app, pequeno, médio ou grande. Claro, escuro ou automático, "
             "e só com os passos, se preferir."),
            ("Por hora",
             "Os passos de hoje hora a hora, ao lado do seu dia típico das últimas quatro "
             "semanas."),
            ("Recordes",
             "Totais de cada mês e ano, e seu melhor dia, semana e mês em passos, andares e "
             "velocidade de caminhada."),
            ("Sua cor",
             "Grafite, azul, verde, laranja, rosa ou roxo para as barras de meta, os "
             "gráficos e o widget."),
        ],
        "privacy_title": "Nada sai do seu iPhone.",
        "privacy": [
            "Lê o Apple Saúde e grava nele só as caminhadas e corridas que você registra.",
            "Sua localização só é usada enquanto você registra e fica no seu iPhone.",
            "Tudo é contado e guardado no seu iPhone. Nada é enviado.",
            "Sem conta, sem análise, sem rastreamento.",
        ],
        "note": "O Pedometer não é um dispositivo médico e não dá conselhos médicos.",
        "shots": [
            "Seus passos na Tela Bloqueada: um widget contador de passos, com distância e andares ao lado.",
            "Cada passo conta: lê o Apple Saúde e inclui os passos do Apple Watch.",
            "Caminhe e corra com o mapa: velocidade, altitude, calorias e frequência cardíaca.",
            "Ao vivo, e depois compartilhe: a Tela Bloqueada no percurso, uma imagem depois.",
            "Também na sua Tela de Início: o mesmo cartão, pequeno ou médio.",
            "Seu dia, hora a hora: os passos de hoje ao lado de um dia típico.",
            "Seu melhor dia, semana e mês: totais de cada mês e ano, e de todos os tempos.",
            "Escolha a sua cor: seis cores para as barras, os gráficos e o widget.",
            "Sua semana em um relance: barras diárias, a média e a variação.",
            "Nada sai do seu iPhone: sem conta, sem rastreamento.",
        ],
    },
    "guide_link": "Como colocar um contador de passos na Tela Bloqueada do iPhone",
    "faq": [
        ("Existe um contador de passos grátis para iPhone sem assinatura?", [
            "O Pedometer é grátis, sem assinatura e sem conta. Ele mostra seus passos, a "
            "distância e os andares subidos em números e gráficos claros, e os coloca como "
            "widgets na Tela Bloqueada e na Tela de Início. Também registra caminhadas e "
            "corridas com GPS. Uma gorjeta opcional não desbloqueia nada. [Ver na App "
            "Store](store).",
        ]),
        ("Como mostro meus passos na Tela Bloqueada do iPhone?", [
            [
                "Instale o Pedometer, abra e toque em **Conectar** para ele poder ler o "
                "Apple Saúde.",
                "Toque e segure a Tela Bloqueada, toque em **Personalizar** e escolha a Tela "
                "Bloqueada.",
                "Toque na área de widgets abaixo do relógio, escolha **Pedometer** e "
                "adicione passos, distância ou andares subidos.",
                "Toque em **OK**.",
            ],
            "Os widgets de passos e distância ficam num anel que se fecha na sua meta. "
            "[Guia passo a passo](guide).",
        ]),
        ("Preciso de um Apple Watch?", [
            "Não. Seu iPhone conta seus passos sozinho quando você o leva com você. Se você "
            "também usa um Apple Watch, o Pedometer lê o Apple Saúde, que junta os passos dos "
            "dois sem contar duas vezes.",
        ]),
        ("Ele registra caminhadas e corridas com GPS?", [
            "Sim. Toque em **Caminhada** ou **Corrida** em **Caminhadas e corridas**. O mapa "
            "desenha seu trajeto e mostra tempo, distância, velocidade ou ritmo, calorias, "
            "altitude e subida. Durante o percurso, os números ficam na Tela Bloqueada com um "
            "botão de pausa. Cada uma é salva no Apple Saúde com o trajeto, e você pode "
            "compartilhar uma imagem.",
        ]),
        ("Ele mostra minha frequência cardíaca sem Apple Watch?", [
            "Sim, no iOS 26. Com AirPods Pro 3, Powerbeats Pro 2 ou uma cinta cardíaca "
            "Bluetooth, você vê sua frequência cardíaca ao vivo durante uma caminhada ou "
            "corrida.",
        ]),
        ("Posso mudar minha meta diária de passos?", [
            "Sim. Em **Metas diárias** você define metas de passos, distância e andares. "
            "Elas começam em 10.000 passos, 8 km e 10 andares. Os anéis dos widgets se fecham "
            "nas suas metas.",
        ]),
        ("O Pedometer é grátis mesmo?", [
            "Sim. Todos os recursos são grátis e não há assinatura. Em **Ajustes** › "
            "**Apoiar o Pedometer** você pode deixar uma gorjeta, se quiser. Ela é opcional "
            "e não desbloqueia nada.",
        ]),
        ("O Pedometer envia meus dados de saúde?", [
            "Não. Tudo é contado e guardado no seu iPhone, e nada é enviado. O Pedometer lê "
            "o Apple Saúde e grava nele só as caminhadas e corridas que você registra. Sua "
            "localização só é usada enquanto você registra. Sem conta, sem análise, sem "
            "rastreamento. [Política de privacidade (em inglês)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "contador-de-passos-tela-bloqueada",
        "title": "Como colocar um contador de passos na Tela Bloqueada do iPhone",
        "description": "Passo a passo: adicione um widget contador de passos grátis à Tela "
                       "Bloqueada e à Tela de Início do iPhone, com distância e andares ao "
                       "lado. Sem Apple Watch e sem assinatura.",
        "lead": "Seu iPhone já conta seus passos. O Pedometer coloca esse número na Tela "
                "Bloqueada, para você ver toda vez que pega o celular. Leva cerca de um "
                "minuto, e você não precisa de um Apple Watch.",
        "choose": [
            ("Passos", "Num anel que se fecha na sua meta"),
            ("Distância", "Num anel, em km ou milhas"),
            ("Andares subidos", "Um bonequinho sobe uma escada"),
        ],
        "steps": [
            ("Instale o Pedometer",
             "Baixe o [Pedometer na App Store](store). É grátis e não pede conta."),
            ("Conecte o Apple Saúde",
             "Abra o Pedometer e toque em **Conectar**. Permita a leitura de passos, "
             "distância e andares subidos. Seu iPhone sempre contou esses dados, então seu "
             "histórico aparece na hora."),
            ("Defina suas metas",
             "Escolha uma meta diária de passos, distância e andares em **Metas diárias**. "
             "Os anéis dos widgets se fecham quando você chega lá."),
            ("Edite a Tela Bloqueada",
             "Bloqueie o iPhone, desperte-o e toque e segure a Tela Bloqueada. Toque em "
             "**Personalizar** e escolha a Tela Bloqueada."),
            ("Adicione o widget",
             "Toque na área de widgets abaixo do relógio. Encontre **Pedometer** na lista e "
             "toque em passos, distância ou andares subidos. Você pode adicionar mais de um."),
            ("Toque em OK",
             "Seus passos agora estão na Tela Bloqueada e se atualizam ao longo do dia."),
            ("Coloque também na Tela de Início",
             "Toque e segure uma área vazia da Tela de Início, toque em **Editar** e depois "
             "em **Adicionar Widget**. Busque Pedometer e escolha pequeno, médio ou grande. O "
             "grande mostra também o dia hora a hora."),
        ],
        "tips": [
            ("Claro, escuro ou só passos",
             "Toque e segure o widget da Tela de Início e escolha **Editar Widget** para "
             "deixá-lo claro ou escuro, ou mostrar só os passos."),
            ("Escolha uma cor",
             "Grafite, azul, verde, laranja, rosa ou roxo, para as barras de meta, os "
             "gráficos e o widget."),
            ("Vai caminhar?",
             "Toque em **Caminhada** ou **Corrida** no app para registrar seu trajeto com "
             "GPS. Os números ficam na Tela Bloqueada durante o percurso."),
            ("Nada sai do seu iPhone",
             "O Pedometer não tem conta e não envia nada. Ele lê o Apple Saúde no seu iPhone."),
        ],
        "updated": "Escrito para o Pedometer 1.5 no iOS 26, outubro de 2026.",
        "cta_title": "Seus passos num relance",
        "cta_text": "Um contador de passos grátis para a Tela Bloqueada e a Tela de Início, "
                    "com caminhadas e corridas no mapa. Sem conta, sem assinatura.",
    },
}
