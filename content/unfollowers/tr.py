# Unfollowers in Turkish ("sen", as in the app). Keys are explained in en.py.
# Instagram's button names come from help.instagram.com/181231772500920 in
# Turkish (checked November 2026). The data checkboxes aren't named there, so
# they are written as plain words.

L = {
    "name": "Türkçe",
    "path": "tr/",
    "og_locale": "tr_TR",
    "ui": {
        "nav_apps": "Uygulamalar",
        "nav_privacy": "Gizlilik",
        "nav_about": "",   # no room on phones
        "nav_contact": "İletişim",
        "trademark": "Instagram ve Facebook, Meta Platforms, Inc.'in ticari markalarıdır. "
                     "Unfollowers ve Unfriended bağımsız uygulamalardır; Meta ile bağlantılı "
                     "değildir, Meta tarafından onaylanmaz veya desteklenmez.",
        "rights": "Tüm hakları saklıdır.",
        "overview": "Genel bakış",
        "privacy": "Gizlilik",
        "view_on_store": "App Store'da gör",
        "platform": "iPhone · iOS 17 veya üzeri",
        "screenshots": "Ekran görüntüleri",
        "prev": "Önceki ekran görüntüleri",
        "next": "Sonraki ekran görüntüleri",
        "privacy_eyebrow": "Gizlilik",
        "read_policy": "Gizlilik politikasını oku (İngilizce)",
        "more_apps": "Diğer uygulamalar",
        "languages": "Diller",
        "faq": "Sorular ve cevaplar",
        "summary": "Ne seçmeli",
        "tips": "Bilmekte fayda var",
        "cta_more": "{name} hakkında",
        "out_of_5": " / 5",
        "decimal": ",",
    },
    "page": {
        "shots_dir": "tr",
        "tagline": "Instagram'da seni kimin takipten çıktığını gör, giriş yapmadan.",
        "pricing": "Ücretsiz · Tek seferlik kilit açma",
        "intro": (
            "Instagram, seni kimin takipten çıktığını göstermez. Instagram'dan indirdiğin "
            "veri dosyası gösterir.",
            "Unfollowers, Instagram'dan kendin indirdiğin resmi dışa aktarımı okur ve neyin "
            "değiştiğini gösterir. Uygulama şifreni asla istemez.",
        ),
        "features": [
            ("Seni takipten çıkanlar",
             "Bir içe aktarmadan diğerine, her değişikliğin bulunduğu tarihle."),
            ("Muhtemelen seni engelleyenler",
             "Takipçilerinden ve takip ettiklerinden aynı anda çıkan hesaplar. Uygulama "
             "bunları olası engel olarak işaretler."),
            ("Seni geri takip etmeyenler",
             "Bilinen liste; ayrıca karşılıklı takipler ve hiç kabul edilmeyen takip "
             "istekleri."),
            ("En çok etkileşim kurduğun hesaplar",
             "Beğenilerin, yorumların ve hikaye tepkilerin, kendi dışa aktarımından sayılır."),
            ("Geçmişin grafiklerde",
             "İçe aktardığın her dosyadan büyüme ve geri takip grafikleri. Yılını hikayende "
             "kartlarla paylaş."),
            ("Giriş yok",
             "Uygulamanın giriş ekranı yok. Şifren sende kalır."),
        ],
        "privacy_title": "Dışa aktarımın iPhone'unda kalır.",
        "privacy": [
            "Instagram dışa aktarımın yalnızca iPhone'unda okunur ve saklanır.",
            "Hesap yok, analitik yok, reklam yok, izleme yok.",
            "Bir hesabın hâlâ var olup olmadığını kontrol etmek için uygulama, giriş "
            "yapmadan Instagram'a yalnızca o kullanıcı adını gönderir.",
        ],
        "note": "Unfollowers bağımsız bir uygulamadır; Instagram veya Meta ile bağlantılı "
                "değildir.",
        "stats": [],
        "reviews": [],
        "why": (
            "Şifren sende kalır.",
            "Takipçi uygulamalarının çoğu Instagram şifreni ister, sonra hesabını arka "
            "planda kullanır. Instagram, yetkisiz uygulamalara hesabına erişim vermenin "
            "hesabını riske attığı konusunda uyarır. Bu uygulamaları düzenli kullananlar "
            "kilitlenen, askıya alınan ya da işlem engeli alan hesaplardan bahsediyor. "
            "Unfollowers şifreni asla istemez ve hesabına asla giriş yapmaz. Instagram'ın "
            "sana verdiği veri dışa aktarımını okur. Abonelik yoktur: isteğe bağlı tek bir "
            "satın alma her şeyin kilidini açar.",
        ),
        "shots": [
            "Takipten çıkan herkes: kim, ne zaman gitti; kendi Instagram dışa aktarımından "
            "okunur.",
            "Muhtemelen seni engelleyenler: takipçilerinden ve takip ettiklerinden aynı anda "
            "çıkan hesaplar.",
            "Seni geri takip etmeyenler: ara, sırala ve istediğin profili aç.",
            "En çok gaz verdiklerin: beğenilerin, yorumların ve hikaye tepkilerin, sayılmış "
            "halde.",
            "İstatistiklerin grafiklerle: kendi geçmişinden büyüme ve geri takip grafikleri.",
            "Yılını paylaş: takipçilerle yılın, ilk ekibin ve en çok gaz verdiklerin, "
            "hikayen için kartlar halinde.",
        ],
    },
    "guide_link": "Instagram verilerini nasıl indirirsin",
    "faq": [
        ("Instagram'da beni kimin takipten çıktığını nasıl görürüm?", [
            "Instagram, seni kimin takipten çıktığını göstermez. Instagram veri dışa "
            "aktarımı, dosyayı indirdiğin gün seni takip eden herkesi listeler. Unfollowers "
            "bu dışa aktarımlardan ikisini karşılaştırır ve kimin gittiğini gösterir.",
            [
                "Instagram'dan, takipçiler ve takip edilenler JSON formatında olacak şekilde "
                "veri dışa aktarımını indir. [Nasıl yapılacağı burada](guide).",
                "ZIP dosyasını Unfollowers'a aktar. Seni geri takip etmeyenleri hemen "
                "görürsün.",
                "Birkaç hafta sonra yeni bir dışa aktarım indir ve onu da aktar. Unfollowers, "
                "ilkinden bu yana seni takipten çıkanları, her değişikliğin bulunduğu tarihle "
                "listeler.",
            ],
            "Aktardığın her yeni dosya geçmişini büyütür.",
        ]),
        ("Giriş yapmadan güvenli bir takipten çıkanlar uygulaması var mı?", [
            "Unfollowers giriş yapmadan çalışır. Instagram şifreni asla istemez ve hesabına "
            "asla giriş yapmaz. Instagram'dan kendin indirdiğin veri dışa aktarımını okur.",
            "Pek çok takipçi uygulaması Instagram şifreni ister, sonra hesabını arka planda "
            "kullanır. Instagram, yetkisiz uygulamalara hesabına erişim vermenin hesabını "
            "riske attığı konusunda uyarır. Unfollowers ile şifren sende kalır ve uygulama "
            "hesabında hiçbir işlem yapmaz.",
            "Dışa aktarım dosyan iPhone'unda okunur ve saklanır. Hesap yok, reklam yok, "
            "izleme yok.",
        ]),
        ("Instagram veri dışa aktarımımı nasıl indiririm?", [
            "Instagram uygulamasında profilini aç ve menüye dokun. Sonra Hesaplar Merkezi › "
            "Bilgilerin ve izinlerin › Bilgilerini dışa aktar › Dışa aktarım oluştur yolunu "
            "izle. Bazı hesaplarda Hesaplar Merkezi'nin adı Meta Hesabı'dır. Cihaza aktar'ı "
            "seç. Takipçiler ve takip edilenleri, tüm zamanları ve JSON formatını seç, sonra "
            "Dışa aktarımı başlat'a dokun. Instagram, dosya hazır olduğunda genelde birkaç "
            "dakika içinde haber verir.",
            "[Adım adım rehber](guide).",
        ]),
        ("Instagram'da beni kimin engellediğini görebilir miyim?", [
            "Instagram engellemeleri bildirmez, bu yüzden hiçbir uygulama bunu kesin olarak "
            "bilemez. Biri seni engellediğinde, takipçilerinden ve takip ettiklerinden aynı "
            "anda kaybolur. Unfollowers bu hesapları muhtemelen seni engelleyenler olarak "
            "işaretler. Bu yalnızca seni takip eden ve senin de takip ettiğin kişiler için "
            "çalışır.",
            "Silinen, devre dışı bırakılan ya da adı değişen bir hesap da aynı şekilde "
            "kaybolur. Profil kontrolü (vibe check), her kullanıcı adının hâlâ var olup "
            "olmadığını instagram.com'a sorar ve kaybolan hesapları ayrı bir listeye taşır.",
        ]),
        ("Unfollowers ücretsiz mi?", [
            "Unfollowers'ı indirmek ücretsizdir. Ücretsiz sürüm, seni geri takip "
            "etmeyenleri, senin geri takip etmediklerini ve karşılıklı takipleri gösterir. "
            "Tek seferlik bir satın alma, seni takipten çıkanlar ve muhtemelen seni "
            "engelleyenler listeleri dahil geri kalan her şeyin kilidini açar. Abonelik "
            "yoktur. Uygulama, iOS 17 veya üzeri yüklü iPhone'da çalışır.",
        ]),
        ("iPhone'umdan bir şey çıkıyor mu?", [
            "Dışa aktarım dosyan iPhone'unda kalır. Uygulama onu orada okur ve saklar; "
            "geliştiricinin sunucusu yoktur. İnternet kullanan tek özellik profil "
            "kontrolüdür. Bir hesabın hâlâ var olup olmadığını instagram.com'a sorar ve "
            "giriş yapmadan yalnızca o kullanıcı adını gönderir. Vibe check'e dokunduğunda "
            "ve kilit açıldıktan sonra her içe aktarmanın ardından en fazla 30 yeni hesap "
            "için çalışır. [Gizlilik politikası (İngilizce)](privacy).",
        ]),
    ],
    "guide": {
        "slug": "instagram-verilerini-indir",
        "title": "Instagram veri dışa aktarımı nasıl indirilir (JSON)",
        "description": "iPhone'da adım adım: Instagram takipçilerini ve takip ettiklerini "
                       "JSON formatında, tüm zamanlar için dışa aktar ve ZIP dosyasını "
                       "kaydet. Sonra Unfollowers ile seni kimin takipten çıktığını gör.",
        "lead": "Instagram, hesap verilerinin bir kopyasını indirmene izin verir. Dışa "
                "aktarım, takipçilerinin ve takip ettiğin hesapların tam listesini içerir. "
                "Unfollowers, seni kimin takipten çıktığını göstermek için bu dosyayı okur. "
                "Aşağıdaki adımlar iPhone'daki Instagram uygulaması içindir.",
        "choose": [
            ("Bilgiler", "Takipçiler ve takip edilenler"),
            ("Tarih aralığı", "Tüm zamanlar"),
            ("Format", "JSON"),
        ],
        "steps": [
            ("Menüyü aç",
             "Instagram uygulamasında sağ alttaki profil fotoğrafına dokun. Sonra sağ "
             "üstteki menüye (☰) dokun."),
            ("Hesaplar Merkezi",
             "**Hesaplar Merkezi**'ne dokun. Bazı hesaplarda adı **Meta Hesabı**'dır."),
            ("Bilgilerin",
             "**Bilgilerin ve izinlerin**'e, sonra **Bilgilerini dışa aktar**'a dokun."),
            ("Dışa aktarım oluştur",
             "**Dışa aktarım oluştur**'a dokun. Instagram profilini seç ve **İleri**'ye "
             "dokun."),
            ("Cihaza aktar",
             "**Cihaza aktar**'ı seç. Böylece dosya iPhone'una kaydedilir."),
            ("Verileri seç",
             "Sonraki ekranda dışa aktarılacak bilgileri seç. Bağlantılar bölümünde "
             "takipçiler ve takip edilenleri işaretle. En çok kiminle etkileşim kurduğunu "
             "görmek için beğenileri, yorumları ve hikaye etkileşimlerini de işaretle. "
             "Dosya küçük kalsın diye geri kalanın işaretini kaldırabilirsin."),
            ("Tüm zamanlar, JSON",
             "Tarih aralığı olarak tüm zamanları seç. Format olarak **JSON**'u seç. "
             "Unfollowers HTML formatını okuyamaz."),
            ("Dışa aktarımı başlat",
             "**Dışa aktarımı başlat**'a dokun. Instagram dosyayı hazırlar. Bu genelde "
             "birkaç dakika sürer."),
            ("ZIP'i indir",
             "Dosya hazır olduğunda Instagram sana bildirim gönderir. **Bilgilerini dışa "
             "aktar**'a geri dön ve dosyayı indir. Instagram şifreni sorabilir. Şifreni "
             "Instagram'ın kendisine yazarsın. ZIP dosyasını Dosyalar uygulamasına kaydet."),
            ("Unfollowers'a aktar",
             "Unfollowers'ı aç, içe aktar düğmesine dokun ve ZIP dosyasını seç. Dosyayı "
             "açmana gerek yok."),
        ],
        "tips": [
            ("İki dışa aktarım, kimin gittiğini gösterir",
             "Bir dışa aktarım, takipçilerini tek bir gün için listeler. Birkaç haftada bir "
             "yeni bir dışa aktarım aktar. Unfollowers ikisini karşılaştırır ve son "
             "seferden beri kimin gittiğini gösterir."),
            ("Dosya dört gün indirilebilir",
             "Instagram hazır bir dışa aktarımı dört gün tutar. Sonrasında yeni bir tane "
             "oluştur."),
            ("“Takipçi listesi bulunamadı”",
             "Unfollowers bu mesajı, dışa aktarım HTML formatında olduğunda ya da "
             "takipçiler ve takip edilenler işaretlenmediğinde gösterir. Takipçiler ve takip "
             "edilenlerle JSON formatında yeni bir dışa aktarım oluştur."),
            ("Daha uzun sürebilir",
             "Çoğu dışa aktarım birkaç dakikada hazır olur. Bazen daha uzun sürer. "
             "Instagram, seninki hazır olduğunda uygulamada ve e-postayla haber verir."),
        ],
        "updated": "Adımlar Kasım 2026'da Instagram Yardım Merkezi ile karşılaştırıldı.",
        "cta_title": "Seni kimin takipten çıktığını gör",
        "cta_text": "Unfollowers bu dosyayı iPhone'unda okur. Seni takipten çıkanları, "
                    "muhtemelen seni engelleyenleri ve seni geri takip etmeyenleri gösterir. "
                    "Giriş yok, şifre yok.",
    },
}
