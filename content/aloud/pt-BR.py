# Aloud in Brazilian Portuguese ("você", as in the app). Keys are explained in
# content/unfollowers/en.py; facts to keep true are in en.py. Button names are
# the app's pt-BR strings (Aloud/Localizable.xcstrings).
import runpy
from pathlib import Path

_ui = runpy.run_path(str(Path(__file__).parents[1] / "unfollowers" / "pt-BR.py"))["L"]["ui"]

L = {
    "name": "Português",
    "path": "pt-br/",
    "og_locale": "pt_BR",
    "ui": {
        **_ui,
        "summary": "O que o Aloud lê",
        "tips": "Bom saber",
        "appearance": "Aparência das capturas",
        "light": "Claro",
        "dark": "Escuro",
        "what_people_say": "O que as pessoas dizem.",
    },
    "page": {
        "shots_dir": "pt-BR",
        "tagline": "Tudo o que você pode ler, lido em voz alta.",
        "pricing": "Teste grátis · Desbloqueio único",
        "platform": "iPhone e iPad · iOS 17 ou posterior",
        "intro": (
            "Compartilhe um artigo, abra um PDF ou cole qualquer texto.",
            "O Aloud lê para você com uma voz natural criada no seu iPhone, frase a frase, "
            "e sempre guarda onde você parou.",
        ),
        "features": [
            ("Vozes naturais, no aparelho",
             "Dez vozes para o inglês e quatro que leem mais trinta idiomas, entre eles o "
             "português. Nenhum servidor fala por você, então o Aloud continua lendo no modo "
             "avião."),
            ("Artigos, PDFs, livros",
             "Compartilhe de qualquer navegador, abra PDFs e livros EPUB pelo app Arquivos, "
             "até PDFs escaneados, ou cole o seu próprio texto."),
            ("Para acompanhar a leitura",
             "A frase que está sendo lida fica em destaque. Segure a barra da margem para "
             "percorrer o documento inteiro."),
            ("Mais rápido, se você quiser",
             "De 0,5× a 3× sem voz de esquilo, com as pausas encurtadas a cada ponto final, "
             "se preferir."),
            ("Para levar junto",
             "Continua lendo com a tela bloqueada, com controles na tela de bloqueio e nos "
             "AirPods, e um timer para dormir que abaixa o som aos poucos."),
            ("Em todos os aparelhos",
             "A sincronização com o iCloud é opcional e guarda sua estante como arquivos de "
             "texto comuns no seu próprio iCloud Drive."),
        ],
        "privacy_title": "Privado por construção.",
        "privacy": [
            "A voz é criada no seu iPhone. Seus documentos nunca são enviados.",
            "As vozes são baixadas uma vez de um servidor público. Os artigos que você "
            "compartilha são buscados no próprio site, como um navegador faria.",
            "Sem conta, sem análises, sem anúncios, sem rastreamento.",
        ],
        "note": "",
        "reviews": [],
        "why": (
            "Sem nuvem. Sem assinatura.",
            "Muitos apps famosos de texto para fala criam as vozes nos próprios servidores, "
            "então os artigos e documentos que você ouve são enviados para lá antes, e os "
            "planos premium podem custar US$ 139 por ano, ou US$ 29 por mês, quase US$ 350 "
            "por ano. O Aloud cria cada voz direto no seu iPhone, então o que você lê nunca "
            "é enviado a lugar nenhum para ser falado. E não há assinatura: uma única compra "
            "opcional, sua para sempre.",
        ),
        "shots": [
            "Tudo o que você lê, ele lê para você. Artigos, PDFs, notas, falados por uma voz natural, frase a frase.",
            "Dê conta da lista de leitura. Ouça no trajeto, na caminhada, lavando a louça.",
            "Funciona offline. Em qualquer lugar. Baixe a voz uma única vez.",
            "Sem assinatura. Sem anúncios. Sem rastreamento.",
            "Vozes naturais. Todos os idiomas. Dez vozes para o inglês, quatro que leem mais trinta idiomas, criadas no seu iPhone.",
            "Modo leitura: leia do seu jeito.",
            "O dobro da velocidade. Metade do tempo. De 0,5× a 3×, com menos silêncio entre as frases.",
            "Sua estante, em todos os aparelhos, como arquivos de texto no iCloud Drive.",
            "Leia no seu idioma: qualquer texto traduzido no aparelho, frase ao lado de frase.",
        ],
        "duo": {
            "title": "No iPhone Duo",
            "sub": "Fechado, você ouve. Aberto, você lê.",
            "items": [
                ("cover", "cover", "Fechado", "A voz continua na tela externa.",
                 "Aloud na tela externa do iPhone Duo: a voz continua lendo, com controles de reprodução."),
                ("book", "spread", "Meio aberto", "Duas páginas lado a lado, em qualquer ângulo.",
                 "Aloud no iPhone Duo meio aberto: duas páginas lado a lado."),
                ("flat", "spread", "Aberto", "Traduzindo? O original e a tradução, lado a lado.",
                 "Aloud no iPhone Duo aberto: o original em espanhol na página da esquerda e a "
                 "tradução em inglês na da direita, linha por linha."),
            ],
        },
    },
    "guide_link": "Como ouvir artigos, PDFs e livros EPUB no iPhone",
    "faq": [
        ("Qual app de texto para fala no iPhone não tem assinatura?", [
            "O Aloud lê em voz alta artigos, PDFs, livros EPUB e qualquer texto com uma voz "
            "natural. Ele é grátis para baixar, e uma única compra dentro do app tira o "
            "limite para sempre. Não há assinatura e nada se renova.",
            "As vozes são criadas no seu iPhone ou iPad, então o que você lê nunca é "
            "enviado para virar voz, e o Aloud continua lendo sem internet. Sem conta, sem "
            "anúncios e sem rastreamento.",
        ]),
        ("Como ouço um artigo no iPhone?", [
            [
                "Abra o artigo no Safari ou em qualquer outro app.",
                "Toque em **Compartilhar** e depois em **Aloud**.",
                "Abra o Aloud e toque em reproduzir. A frase que está sendo lida fica em "
                "destaque na página.",
            ],
            "Quando você compartilha pelo Safari, o Aloud lê a página como o Safari mostra, "
            "então artigos de sites em que você está logado também funcionam. Links "
            "compartilhados pelos apps Facebook, Messenger e Instagram também funcionam. "
            "[Guia passo a passo](guide).",
        ]),
        ("O Aloud transforma um EPUB em audiolivro?", [
            "Sim. Abra um arquivo EPUB pelo app Arquivos ou toque em **+** › **Importar um "
            "arquivo**. O Aloud mantém a capa e os capítulos do livro. A lista "
            "**Capítulos** mostra quanto tempo leva para ouvir cada um, e você pode começar "
            "de qualquer capítulo. O Aloud guarda onde você parou, então um livro longo toca "
            "como um audiolivro.",
            "Livros comprados com proteção contra cópia não abrem em nenhum outro app, "
            "nem no Aloud. EPUBs sem DRM, como os do Project Gutenberg ou do Standard "
            "Ebooks, funcionam.",
        ]),
        ("Ele lê PDFs, até escaneados?", [
            "Sim. Abra um PDF pelo app Arquivos ou compartilhe com o Aloud. O Aloud lê o "
            "texto na ordem, e num PDF escaneado reconhece o texto no próprio aparelho "
            "antes.",
        ]),
        ("O Aloud funciona offline?", [
            "Sim. Cada voz é baixada uma vez, na primeira vez que você a usa. Depois disso a "
            "voz é criada no seu iPhone, então o Aloud lê no modo avião, no metrô ou num voo. "
            "Buscar um artigo novo precisa de internet; o que já está na sua estante, não.",
        ]),
        ("Quais idiomas ele lê?", [
            "Dez vozes naturais leem inglês, e outras quatro leem mais de trinta idiomas, "
            "entre eles português, alemão, espanhol, francês e italiano. O app está em "
            "português, inglês, alemão, espanhol, francês e italiano.",
        ]),
        ("Ele traduz o que estou lendo?", [
            "Sim, no iOS 18 ou posterior. Toque no botão de tradução no leitor e escolha um "
            "idioma em **Traduzir para**. O tradutor da Apple trabalha no seu iPhone, então "
            "nada é enviado. A página mostra cada frase com a tradução, e **Ler a tradução "
            "em voz alta** faz a voz ler o outro idioma.",
        ]),
        ("Qual a velocidade máxima de leitura?", [
            "De 0,5× a 3×, sem voz de esquilo. **Encurtar pausas** corta o silêncio entre as "
            "frases, então um artigo de 30 minutos cabe numa caminhada de 15.",
        ]),
        ("O Aloud é grátis?", [
            "O Aloud é grátis para baixar, com todas as vozes e funções. A estante grátis "
            "guarda três textos por vez. Uma compra única, **Desbloquear o Aloud**, tira o "
            "limite. Não há assinatura. [Ver na App Store](store).",
        ]),
        ("Posso trazer minha lista de leitura do Pocket ou do Instapaper?", [
            "Sim. Exporte seus links salvos do Pocket, do Instapaper, do Raindrop ou os "
            "favoritos do navegador, e no Aloud abra **Ajustes** › **Importar de um "
            "arquivo**. Cada link chega à sua estante, e o Aloud busca os artigos em segundo "
            "plano.",
        ]),
        ("O Aloud envia meus documentos?", [
            "Não. A voz é criada no seu iPhone. O Aloud baixa cada voz uma vez de um servidor "
            "público e busca os artigos que você compartilha no próprio site, como um "
            "navegador. **Sincronizar com o iCloud** é opcional e guarda sua estante como "
            "arquivos de texto comuns no seu próprio iCloud Drive. [Política de "
            "privacidade](privacy).",
        ]),
    ],
    "guide": {
        "slug": "ouvir-artigos-e-livros",
        "title": "Como ouvir artigos, PDFs e livros EPUB no iPhone",
        "description": "Passo a passo: compartilhe um artigo pelo Safari, abra um PDF ou um "
                       "EPUB, cole qualquer texto e deixe o Aloud ler em voz alta com uma voz "
                       "natural criada no seu iPhone, na sua velocidade, offline.",
        "lead": "O Aloud lê tudo o que você pode ler: um artigo, um PDF, um livro EPUB ou um "
                "texto que você cola. A voz é criada no seu iPhone, então funciona offline e "
                "nada do que você lê é enviado. Veja como colocar cada tipo de texto no app "
                "e como ouvir.",
        "choose": [
            ("Artigos", "Compartilhe pelo Safari ou outro app"),
            ("PDFs e EPUBs", "Abra pelo app Arquivos"),
            ("Qualquer texto", "Cole"),
        ],
        "steps": [
            ("Instale o Aloud",
             "Baixe o [Aloud na App Store](store). Ele funciona no iPhone e no iPad com iOS "
             "17 ou posterior. Na primeira vez que você toca em reproduzir, a voz é baixada "
             "uma vez. Depois disso, funciona offline."),
            ("Compartilhe um artigo",
             "Abra o artigo no Safari ou em outro app, toque em **Compartilhar** e depois em "
             "**Aloud**. O artigo chega à sua estante sem menus, anúncios nem comentários. "
             "Pelo Safari, o Aloud lê a página como você a vê, então artigos de sites em que "
             "você está logado funcionam."),
            ("Abra um PDF ou um EPUB",
             "No Aloud, toque em **+** › **Importar um arquivo** e escolha o arquivo, ou "
             "compartilhe com o Aloud pelo app Arquivos. PDFs escaneados são reconhecidos no "
             "aparelho. Livros EPUB mantêm a capa e os capítulos."),
            ("Cole qualquer texto",
             "Toque em **+** › **Colar texto** para notas, e-mails ou qualquer coisa que você "
             "copiou. **Colar um link** aceita um endereço da web."),
            ("Toque em reproduzir",
             "Abra um texto e toque em reproduzir. A frase lida fica em destaque e o resto "
             "fica apagado. Segure a barra da margem para percorrer o texto inteiro. Num "
             "livro, toque em **Capítulos** no menu ••• para começar de qualquer capítulo."),
            ("Escolha a velocidade",
             "Toque no botão de velocidade e escolha entre 0,5× e 3×. Ative **Encurtar "
             "pausas** para cortar o silêncio entre as frases."),
            ("Bloqueie o iPhone",
             "O Aloud continua lendo com a tela bloqueada. Use os controles da tela de "
             "bloqueio ou dos AirPods, e ajuste o **Timer para dormir** se você ouve na cama: "
             "no fim, a voz abaixa aos poucos."),
            ("Traduza, se quiser",
             "No iOS 18 ou posterior, toque no botão de tradução e escolha um idioma em "
             "**Traduzir para**. Cada frase aparece com a tradução, e **Ler a tradução em voz "
             "alta** muda a voz para o outro idioma."),
        ],
        "tips": [
            ("Ele guarda onde você parou",
             "Cada texto guarda onde você parou, então dá para trocar de um artigo para um "
             "livro e voltar à mesma frase."),
            ("Modo leitura",
             "Toque no botão dos óculos para esconder o player e ler você mesmo, com a fonte, "
             "o tamanho e o papel que quiser em **Aparência**."),
            ("Sua lista de leitura",
             "Links do Pocket, do Instapaper, do Raindrop ou favoritos do navegador entram "
             "por **Ajustes** › **Importar de um arquivo**."),
            ("Teste grátis",
             "A estante grátis guarda três textos. Uma única compra tira o limite, e não há "
             "assinatura."),
        ],
        "updated": "Escrito para o Aloud 3.2, outubro de 2026.",
        "cta_title": "Ouça sua lista de leitura",
        "cta_text": "O Aloud lê artigos, PDFs e livros EPUB com uma voz natural criada no seu "
                    "iPhone. Funciona offline. Pague uma vez, sem assinatura.",
    },
}
