# Unfollowers in Polish ("ty", as on the Polish App Store page). Keys are
# explained in en.py. The app itself is in English for Polish speakers, so the
# page says so and shows the English screenshots. Instagram's button names come
# from help.instagram.com/181231772500920 in Polish (checked November 2026);
# names the help page doesn't show are written as plain words.

L = {
    "name": "Polski",
    "path": "pl/",
    "og_locale": "pl_PL",
    "ui": {
        "nav_apps": "Aplikacje",
        "nav_privacy": "Prywatność",
        "nav_about": "",   # no room on phones
        "nav_contact": "Kontakt",
        "trademark": "Instagram i Facebook są znakami towarowymi Meta Platforms, Inc. "
                     "Unfollowers i Unfriended to niezależne aplikacje, niepowiązane z Meta, "
                     "nieautoryzowane ani niesponsorowane przez nią.",
        "rights": "Wszelkie prawa zastrzeżone.",
        "overview": "Przegląd",
        "privacy": "Prywatność",
        "view_on_store": "Zobacz w App Store",
        "platform": "iPhone · iOS 17 lub nowszy",
        "screenshots": "Zrzuty ekranu",
        "prev": "Poprzednie zrzuty ekranu",
        "next": "Następne zrzuty ekranu",
        "privacy_eyebrow": "Prywatność",
        "read_policy": "Przeczytaj politykę prywatności (po angielsku)",
        "more_apps": "Więcej aplikacji",
        "languages": "Języki",
        "faq": "Pytania i odpowiedzi",
        "summary": "Co wybrać",
        "tips": "Warto wiedzieć",
        "cta_more": "O aplikacji {name}",
        "out_of_5": " na 5",
        "decimal": ",",
    },
    "page": {
        "tagline": "Zobacz, kto przestał cię obserwować na Instagramie, bez logowania.",
        "pricing": "Za darmo · Jednorazowy zakup",
        "intro": (
            "Instagram nie pokazuje, kto przestał cię obserwować. Pokazuje to plik z danymi, "
            "który pobierasz z Instagrama.",
            "Unfollowers odczytuje oficjalny eksport, który sam pobierasz z Instagrama, i "
            "pokazuje, co się zmieniło. Aplikacja nigdy nie prosi o hasło. Aplikacja jest w "
            "języku angielskim.",
        ),
        "features": [
            ("Kto przestał cię obserwować",
             "Od jednego importu do drugiego, z datą, kiedy znaleziono każdą zmianę."),
            ("Prawdopodobnie cię zablokował",
             "Konta, które w tym samym momencie zniknęły z twoich obserwujących i "
             "obserwowanych. Aplikacja oznacza je jako prawdopodobne blokady."),
            ("Kto nie obserwuje cię nawzajem",
             "Znana lista, a do tego wzajemne obserwowanie i prośby o obserwowanie, których "
             "nikt nie zaakceptował."),
            ("Z kim masz najwięcej interakcji",
             "Twoje polubienia, komentarze i reakcje na relacje, policzone z twojego eksportu."),
            ("Twoja historia na wykresach",
             "Wykresy wzrostu i wzajemnych obserwacji z każdego eksportu, który importujesz. "
             "Swój rok możesz udostępnić w relacji jako karty."),
            ("Bez logowania",
             "Aplikacja nie ma ekranu logowania. Twoje hasło zostaje przy tobie."),
        ],
        "privacy_title": "Twój eksport zostaje na iPhonie.",
        "privacy": [
            "Eksport z Instagrama jest odczytywany i przechowywany tylko na twoim iPhonie.",
            "Bez rejestracji, analityki, reklam i śledzenia.",
            "Aby sprawdzić, czy konto nadal istnieje, aplikacja wysyła do Instagrama tylko "
            "tę nazwę użytkownika, bez logowania.",
        ],
        "note": "Unfollowers to niezależna aplikacja, niepowiązana z Instagramem ani z Meta.",
        "stats": [],
        "reviews": [],
        "why": (
            "Twoje hasło zostaje przy tobie.",
            "Większość aplikacji do śledzenia obserwujących prosi o hasło do Instagrama, a "
            "potem korzysta z twojego konta w tle. Instagram ostrzega, że dawanie dostępu "
            "nieautoryzowanym aplikacjom naraża konto. Osoby, które regularnie z nich "
            "korzystają, piszą o zablokowanych, zawieszonych i ograniczonych kontach. "
            "Unfollowers nigdy nie prosi o hasło i nie loguje się na twoje konto. Odczytuje "
            "eksport danych, który Instagram daje tobie. Nie ma subskrypcji: jeden "
            "opcjonalny zakup odblokowuje wszystko.",
        ),
        "shots": [
            "Każda osoba, która przestała cię obserwować: kto odszedł i kiedy, z twojego "
            "eksportu z Instagrama.",
            "Prawdopodobnie cię zablokowali: konta, które w tym samym momencie zniknęły z "
            "obserwujących i obserwowanych.",
            "Nie obserwują cię nawzajem: szukaj, sortuj i otwieraj dowolny profil.",
            "Kogo wspierasz najbardziej: twoje polubienia, komentarze i reakcje na relacje, "
            "policzone.",
            "Twoje statystyki na wykresach: wzrost i wzajemne obserwacje z twojej historii.",
            "Udostępnij swój rok: twój rok w obserwujących, twoja pierwsza ekipa i osoby, "
            "które wspierasz najbardziej, jako karty do relacji.",
        ],
    },
    "guide_link": "Jak pobrać swoje dane z Instagrama",
    "faq": [
        ("Jak sprawdzić, kto przestał mnie obserwować na Instagramie?", [
            "Instagram nie pokazuje, kto przestał cię obserwować. Eksport danych z "
            "Instagrama zawiera wszystkich, którzy obserwują cię w dniu pobrania. "
            "Unfollowers porównuje dwa takie eksporty i pokazuje, kto odszedł.",
            [
                "Pobierz eksport danych z Instagrama z obserwującymi i obserwowanymi w "
                "formacie JSON. [Jak to zrobić](guide).",
                "Zaimportuj plik ZIP do Unfollowers. Od razu zobaczysz, kto nie obserwuje "
                "cię nawzajem.",
                "Po kilku tygodniach pobierz nowy eksport i też go zaimportuj. Unfollowers "
                "pokaże, kto przestał cię obserwować od pierwszego eksportu, z datą każdej "
                "zmiany.",
            ],
            "Każdy nowy eksport poszerza twoją historię.",
        ]),
        ("Czy jest bezpieczna aplikacja do sprawdzania obserwujących bez logowania?", [
            "Unfollowers działa bez logowania. Nigdy nie prosi o hasło do Instagrama i nie "
            "loguje się na twoje konto. Odczytuje eksport danych, który sam pobierasz z "
            "Instagrama.",
            "Wiele aplikacji do śledzenia obserwujących prosi o hasło do Instagrama, a potem "
            "korzysta z konta w tle. Instagram ostrzega, że dawanie dostępu "
            "nieautoryzowanym aplikacjom naraża konto. Z Unfollowers hasło zostaje przy "
            "tobie, a aplikacja nie wykonuje żadnych działań na twoim koncie.",
            "Plik eksportu jest odczytywany i przechowywany na twoim iPhonie. Bez "
            "rejestracji, reklam i śledzenia.",
        ]),
        ("Jak pobrać eksport danych z Instagrama?", [
            "W aplikacji Instagram otwórz swój profil i dotknij menu. Następnie przejdź do "
            "Centrum kont › Twoje informacje i uprawnienia › Wyeksportuj swoje informacje › "
            "Wyeksportuj dane. Na niektórych kontach Centrum kont nazywa się Konto Meta. "
            "Wybierz Eksportuj na urządzenie, zaznacz obserwujących i obserwowanych, cały "
            "okres i format JSON, a potem dotknij Rozpocznij eksport. Instagram da znać, gdy "
            "plik będzie gotowy, zwykle po kilku minutach.",
            "[Instrukcja krok po kroku](guide).",
        ]),
        ("Czy mogę sprawdzić, kto zablokował mnie na Instagramie?", [
            "Instagram nie informuje o blokadach, więc żadna aplikacja nie wie tego na "
            "pewno. Gdy ktoś cię zablokuje, znika w tym samym momencie z twoich "
            "obserwujących i obserwowanych. Unfollowers oznacza takie konta jako "
            "prawdopodobne blokady. Działa to tylko dla osób, które cię obserwowały i które "
            "ty obserwowałeś.",
            "Konto usunięte, dezaktywowane lub ze zmienioną nazwą znika w ten sam sposób. "
            "Sprawdzanie profili (vibe check) pyta instagram.com, czy każda nazwa "
            "użytkownika nadal istnieje, i przenosi znikające konta na osobną listę.",
        ]),
        ("Czy Unfollowers jest za darmo?", [
            "Unfollowers można pobrać za darmo. Wersja darmowa pokazuje, kto nie obserwuje "
            "cię nawzajem, kogo ty nie obserwujesz nawzajem i wzajemne obserwowanie. "
            "Jednorazowy zakup odblokowuje całą resztę, w tym listy osób, które przestały "
            "cię obserwować i które prawdopodobnie cię zablokowały. Nie ma subskrypcji. "
            "Aplikacja działa na iPhonie z iOS 17 lub nowszym i jest w języku angielskim.",
        ]),
        ("Czy coś opuszcza mojego iPhone'a?", [
            "Plik eksportu zostaje na twoim iPhonie. Aplikacja tam go odczytuje i "
            "przechowuje, a twórca nie ma żadnych serwerów. Z internetu korzysta tylko "
            "sprawdzanie profili. Pyta instagram.com, czy konto nadal istnieje, i wysyła "
            "tylko tę nazwę użytkownika, bez logowania. Działa, gdy dotkniesz vibe check, a "
            "po odblokowaniu dla maksymalnie 30 nowych kont po każdym imporcie. [Polityka "
            "prywatności (po angielsku)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "pobierz-dane-instagrama",
        "title": "Jak pobrać eksport danych z Instagrama (JSON)",
        "description": "Krok po kroku na iPhonie: wyeksportuj obserwujących i obserwowanych "
                       "z Instagrama w formacie JSON za cały okres i zapisz plik ZIP. Potem "
                       "sprawdź w Unfollowers, kto przestał cię obserwować.",
        "lead": "Instagram pozwala pobrać kopię danych konta. Eksport zawiera pełne listy "
                "twoich obserwujących i kont, które obserwujesz. Unfollowers odczytuje ten "
                "plik, aby pokazać, kto przestał cię obserwować. Poniższe kroki dotyczą "
                "aplikacji Instagram na iPhonie.",
        "choose": [
            ("Informacje", "Obserwujący i obserwowani"),
            ("Zakres dat", "Cały okres"),
            ("Format", "JSON"),
        ],
        "steps": [
            ("Otwórz menu",
             "W aplikacji Instagram dotknij zdjęcia profilowego w prawym dolnym rogu. Potem "
             "dotknij **Menu** (☰) w prawym górnym rogu."),
            ("Centrum kont",
             "Dotknij **Centrum kont**. Na niektórych kontach nazywa się ono Konto Meta."),
            ("Twoje informacje",
             "Dotknij **Twoje informacje i uprawnienia**, a potem **Wyeksportuj swoje "
             "informacje**."),
            ("Wyeksportuj dane",
             "Dotknij **Wyeksportuj dane**. Wybierz swój profil na Instagramie i dotknij "
             "**Dalej**."),
            ("Eksportuj na urządzenie",
             "Wybierz **Eksportuj na urządzenie**. Plik zapisze się na twoim iPhonie."),
            ("Wybierz dane",
             "Na następnym ekranie wybierz informacje do eksportu. W sekcji kontaktów "
             "zaznacz obserwujących i obserwowanych. Aby zobaczyć, z kim masz najwięcej "
             "interakcji, zaznacz też polubienia, komentarze i interakcje z relacjami. Resztę "
             "możesz odznaczyć, żeby plik był mniejszy."),
            ("Cały okres, JSON",
             "W zakresie dat wybierz cały okres. W formacie wybierz **JSON**. Unfollowers "
             "nie odczytuje formatu HTML."),
            ("Rozpocznij eksport",
             "Dotknij **Rozpocznij eksport**. Instagram przygotuje plik. Zwykle trwa to kilka "
             "minut."),
            ("Pobierz ZIP",
             "Gdy plik będzie gotowy, Instagram wyśle powiadomienie. Wróć do **Wyeksportuj "
             "swoje informacje** i pobierz plik. Instagram może poprosić o hasło. Wpisujesz "
             "je w samym Instagramie. Zapisz plik ZIP w aplikacji Pliki."),
            ("Zaimportuj do Unfollowers",
             "Otwórz Unfollowers, dotknij przycisku importu (+ IMPORT) i wybierz plik ZIP. "
             "Nie musisz go rozpakowywać."),
        ],
        "tips": [
            ("Dwa eksporty pokazują, kto odszedł",
             "Jeden eksport zawiera obserwujących z jednego dnia. Importuj nowy eksport co "
             "kilka tygodni. Unfollowers je porówna i pokaże, kto odszedł od ostatniego razu."),
            ("Plik jest dostępny przez cztery dni",
             "Instagram przechowuje gotowy eksport przez cztery dni. Potem utwórz nowy."),
            ("„No follower lists found”",
             "Unfollowers pokazuje ten komunikat, gdy eksport jest w formacie HTML albo gdy "
             "nie zaznaczono obserwujących i obserwowanych. Utwórz nowy eksport w formacie "
             "JSON z obserwującymi i obserwowanymi."),
            ("Może to potrwać dłużej",
             "Większość eksportów jest gotowa w kilka minut. Czasem trwa to dłużej. Instagram "
             "da znać w aplikacji i e-mailem, gdy twój będzie gotowy."),
        ],
        "updated": "Kroki sprawdzone w Centrum pomocy Instagrama w listopadzie 2026 r.",
        "cta_title": "Zobacz, kto przestał cię obserwować",
        "cta_text": "Unfollowers odczytuje ten plik na twoim iPhonie. Pokazuje, kto przestał "
                    "cię obserwować, kto prawdopodobnie cię zablokował i kto nie obserwuje cię "
                    "nawzajem. Bez logowania i bez hasła. Aplikacja jest w języku angielskim.",
    },
}
