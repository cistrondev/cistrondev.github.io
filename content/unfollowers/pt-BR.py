# Unfollowers in Brazilian Portuguese ("você"). Keys are explained in en.py.
# The Portuguese App Store screenshots use European "tu" forms, so this page
# shows the English screenshots.

L = {
    "name": "Português (Brasil)",
    "path": "pt-br/",
    "og_locale": "pt_BR",
    "ui": {
        "nav_apps": "Apps",
        "nav_privacy": "Privacidade",
        "nav_about": "",   # no room on phones
        "nav_contact": "Contato",
        "trademark": "Instagram e Facebook são marcas da Meta Platforms, Inc. Unfollowers e "
                     "Unfriended são apps independentes, sem afiliação, endosso ou patrocínio "
                     "da Meta.",
        "rights": "Todos os direitos reservados.",
        "overview": "Início",
        "privacy": "Privacidade",
        "view_on_store": "Ver na App Store",
        "platform": "iPhone · iOS 17 ou posterior",
        "screenshots": "Capturas de tela",
        "prev": "Capturas anteriores",
        "next": "Próximas capturas",
        "privacy_eyebrow": "Privacidade",
        "read_policy": "Ler a política de privacidade (em inglês)",
        "more_apps": "Mais apps",
        "languages": "Idiomas",
        "faq": "Perguntas e respostas",
        "summary": "O que escolher",
        "tips": "Bom saber",
        "cta_more": "Sobre o {name}",
    },
    "page": {
        "tagline": "Veja quem parou de seguir você no Instagram. Sem login.",
        "pricing": "Grátis · Desbloqueio único",
        "intro": (
            "O Instagram não mostra quem parou de seguir você. O arquivo de dados que você "
            "baixa do Instagram mostra.",
            "O Unfollowers lê a exportação oficial que você mesmo baixa do Instagram e "
            "mostra o que mudou. O app nunca pede a sua senha.",
        ),
        "features": [
            ("Quem parou de seguir você",
             "Acompanhado de uma importação para a outra, com a data em que cada mudança "
             "foi encontrada."),
            ("Provavelmente bloqueou você",
             "Contas que saíram ao mesmo tempo dos seus seguidores e da sua lista de "
             "seguindo. O app marca essas contas como prováveis bloqueios."),
            ("Quem não segue você de volta",
             "A lista clássica, mais os mútuos e as solicitações para seguir que nunca "
             "foram aceitas."),
            ("Com quem você mais interage",
             "Suas curtidas, comentários e reações a stories, contados a partir da sua "
             "própria exportação."),
            ("Seu histórico em gráficos",
             "Gráficos de crescimento e de follow-back feitos com cada exportação que você "
             "importa."),
            ("Sem login",
             "O app não tem nenhuma tela de login. A sua senha fica com você."),
        ],
        "privacy_title": "A sua exportação fica no seu iPhone.",
        "privacy": [
            "A sua exportação do Instagram é lida e guardada apenas no seu iPhone.",
            "Sem cadastro, sem analytics, sem anúncios e sem rastreamento.",
            "Para conferir se uma conta ainda existe, o app envia ao Instagram apenas esse "
            "nome de usuário, sem fazer login.",
        ],
        "note": "O Unfollowers é um app independente, sem afiliação com o Instagram ou a Meta.",
        "stats": [],
        "reviews": [],
        "why": (
            "A sua senha fica com você.",
            "A maioria dos apps de seguidores pede a sua senha do Instagram e depois usa a "
            "sua conta em segundo plano. O Instagram avisa que deixar apps não autorizados "
            "entrar na sua conta coloca a conta em risco. Quem usa esses apps com frequência "
            "relata contas travadas, suspensas ou com ações bloqueadas. O Unfollowers nunca "
            "pede a sua senha e nunca entra na sua conta. Ele lê a exportação de dados que o "
            "próprio Instagram dá a você. E não tem assinatura: uma compra única e opcional "
            "desbloqueia tudo.",
        ),
        "shots": [
            "Veja cada unfollower: quem saiu e quando, lido da sua própria exportação do "
            "Instagram.",
            "Provavelmente bloqueou você: contas que saíram ao mesmo tempo dos seus "
            "seguidores e da sua lista de seguindo.",
            "Não seguem você de volta: pesquise, ordene e abra qualquer perfil.",
            "Com quem você mais interage: suas curtidas, comentários e reações a stories, "
            "contados.",
            "Suas estatísticas em gráficos: crescimento e follow-back a partir do seu "
            "próprio histórico.",
        ],
    },
    "guide_link": "Como baixar os seus dados do Instagram",
    "faq": [
        ("Como ver quem parou de me seguir no Instagram?", [
            "O Instagram não mostra quem parou de seguir você. A exportação de dados do "
            "Instagram lista todo mundo que segue você no dia em que você baixa o arquivo. "
            "O Unfollowers compara duas dessas exportações e mostra quem saiu.",
            [
                "Baixe a sua exportação de dados do Instagram, com Seguidores e seguindo em "
                "formato JSON. [Veja o passo a passo](guide).",
                "Importe o arquivo ZIP no Unfollowers. Você já vê na hora quem não segue "
                "você de volta.",
                "Algumas semanas depois, baixe uma nova exportação e importe também. O "
                "Unfollowers mostra quem parou de seguir você desde a primeira, com a data "
                "em que cada mudança foi encontrada.",
            ],
            "Cada nova exportação que você importa aumenta o seu histórico.",
        ]),
        ("Existe um app seguro para ver quem parou de seguir sem login?", [
            "O Unfollowers funciona sem login. Ele nunca pede a sua senha do Instagram e "
            "nunca entra na sua conta. Ele lê a exportação de dados que você mesmo baixa "
            "do Instagram.",
            "Muitos apps de seguidores pedem a sua senha do Instagram e depois usam a sua "
            "conta em segundo plano. O Instagram avisa que deixar apps não autorizados "
            "entrar na sua conta coloca a conta em risco. Com o Unfollowers, a sua senha "
            "fica com você, e o app nunca faz nenhuma ação na sua conta.",
            "O arquivo da exportação é lido e guardado no seu iPhone. Não tem cadastro, "
            "nem anúncios, nem rastreamento.",
        ]),
        ("Como baixar a exportação de dados do Instagram?", [
            "No app do Instagram, abra o seu perfil e toque no menu. Depois vá em Central "
            "de Contas › Suas informações e permissões › Exportar suas informações › Criar "
            "exportação. Em algumas contas, a Central de Contas se chama Conta Meta. "
            "Escolha Exportar para o dispositivo. Marque Seguidores e seguindo, escolha "
            "todo o período e o formato JSON, e toque em Iniciar a exportação. O Instagram "
            "avisa quando o arquivo fica pronto, normalmente em poucos minutos.",
            "[Passo a passo completo](guide).",
        ]),
        ("Dá para ver quem me bloqueou no Instagram?", [
            "O Instagram não informa bloqueios, então nenhum app consegue saber com "
            "certeza. Quando alguém bloqueia você, a pessoa some ao mesmo tempo dos seus "
            "seguidores e da sua lista de seguindo. O Unfollowers marca essas contas como "
            "prováveis bloqueios. Isso só funciona com quem seguia você e era seguido por "
            "você.",
            "Uma conta excluída, desativada ou que mudou de nome some do mesmo jeito. A "
            "verificação de perfis (o vibe check) pergunta ao instagram.com se cada nome de "
            "usuário ainda existe e coloca as contas que sumiram numa lista separada.",
        ]),
        ("O Unfollowers é grátis?", [
            "O download do Unfollowers é grátis. A versão grátis mostra quem não segue você "
            "de volta, quem você não segue de volta e os seus mútuos. Uma compra única "
            "desbloqueia todo o resto, incluindo as listas de quem parou de seguir você e "
            "de quem provavelmente bloqueou você. Não tem assinatura. O app funciona no "
            "iPhone com iOS 17 ou posterior.",
        ]),
        ("Alguma coisa sai do meu iPhone?", [
            "O arquivo da sua exportação fica no seu iPhone. O app lê e guarda o arquivo "
            "ali, e o desenvolvedor não tem servidores. O único recurso que usa a internet "
            "é a verificação de perfis. Ela pergunta ao instagram.com se uma conta ainda "
            "existe e envia apenas esse nome de usuário, sem fazer login. Ela roda quando "
            "você toca no vibe check e, depois do desbloqueio, para até 30 contas novas "
            "após cada importação. [Política de privacidade (em inglês)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "baixar-dados-instagram",
        "title": "Como baixar os seus dados do Instagram (exportação em JSON)",
        "description": "Passo a passo no iPhone: exporte os seus seguidores e quem você "
                       "segue no Instagram em formato JSON, de todo o período, e salve o "
                       "arquivo ZIP. Depois veja quem parou de seguir você com o Unfollowers.",
        "lead": "O Instagram permite baixar uma cópia dos dados da sua conta. A exportação "
                "traz a lista completa dos seus seguidores e das contas que você segue. O "
                "Unfollowers lê esse arquivo para mostrar quem parou de seguir você. Veja "
                "como baixar o arquivo no app do Instagram no iPhone.",
        "choose": [
            ("Informações", "Seguidores e seguindo"),
            ("Intervalo de datas", "Todo o período"),
            ("Formato", "JSON"),
        ],
        "steps": [
            ("Abra o menu",
             "No app do Instagram, toque na sua foto de perfil no canto inferior direito. "
             "Depois toque no menu (☰) no canto superior direito."),
            ("Central de Contas",
             "Toque em **Central de Contas**. Em algumas contas, ela se chama **Conta Meta**."),
            ("Suas informações",
             "Toque em **Suas informações e permissões** e depois em **Exportar suas "
             "informações**."),
            ("Crie a exportação",
             "Toque em **Criar exportação**. Escolha o seu perfil do Instagram e toque em "
             "**Avançar**."),
            ("Exportar para o dispositivo",
             "Escolha **Exportar para o dispositivo**. Assim o arquivo fica salvo no seu "
             "iPhone."),
            ("Escolha os dados",
             "Na tela seguinte, escolha as informações que vão na exportação. Marque "
             "**Seguidores e seguindo**, na parte de conexões. Para ver com quem você mais "
             "interage, marque também curtidas, comentários e interações com stories. Você "
             "pode desmarcar o resto para o arquivo ficar menor."),
            ("Todo o período, JSON",
             "No intervalo de datas, escolha todo o período, desde o início. No formato, "
             "escolha **JSON**. O Unfollowers não lê o formato HTML."),
            ("Inicie a exportação",
             "Toque em **Iniciar a exportação**. O Instagram prepara o arquivo. Isso "
             "normalmente leva alguns minutos."),
            ("Baixe o ZIP",
             "O Instagram avisa quando o arquivo fica pronto. Volte em **Exportar suas "
             "informações** e baixe o arquivo. O Instagram pode pedir a sua senha. Você "
             "digita a senha no próprio Instagram. Salve o arquivo ZIP no app Arquivos."),
            ("Importe no Unfollowers",
             "Abra o Unfollowers, toque no botão de importar e escolha o arquivo ZIP. Não "
             "precisa descompactar."),
        ],
        "tips": [
            ("Duas exportações mostram quem saiu",
             "Uma exportação lista os seus seguidores em um único dia. Importe uma nova "
             "exportação a cada poucas semanas. O Unfollowers compara as duas e mostra quem "
             "saiu desde a última."),
            ("O arquivo fica disponível por quatro dias",
             "O Instagram guarda uma exportação pronta por quatro dias. Depois disso, crie "
             "uma nova."),
            ("“Não foram encontradas listas de seguidores”",
             "O Unfollowers mostra essa mensagem quando a exportação está em formato HTML "
             "ou quando Seguidores e seguindo não foi marcado. Crie uma nova exportação em "
             "JSON com Seguidores e seguindo."),
            ("Pode demorar mais",
             "A maioria das exportações fica pronta em poucos minutos. Às vezes demora "
             "mais. O Instagram avisa no app e por email quando a sua estiver pronta."),
        ],
        "updated": "Passos conferidos na Central de Ajuda do Instagram em outubro de 2026.",
        "cta_title": "Veja quem parou de seguir você",
        "cta_text": "O Unfollowers lê esse arquivo no seu iPhone. Ele mostra quem parou de "
                    "seguir você, quem provavelmente bloqueou você e quem não segue você de "
                    "volta. Sem login e sem senha.",
    },
}
