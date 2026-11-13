#!/usr/bin/env python3
"""Generates the static FoodGauge landing pages (en, tr, ru, ar) into the repo dir given as argv[1]."""
import html, json, sys, os

OUT = sys.argv[1]
BASE = "https://teach-bot-sys.github.io/foodgauge-site/"
APPSTORE = "https://apps.apple.com/us/app/id6802302665"
IG = "https://www.instagram.com/food.gauge/"
MAIL = "mrfatihkrkmz@gmail.com"
PAGES = {"en": "", "tr": "tr.html", "ru": "ru.html", "ar": "ar.html"}
LANG_NAMES = {"en": "English", "tr": "Türkçe", "ru": "Русский", "ar": "العربية"}
OG_LOCALE = {"en": "en_US", "tr": "tr_TR", "ru": "ru_RU", "ar": "ar_AR"}

e = lambda s: html.escape(s, quote=True)

T = {}

T["en"] = dict(
    title="FoodGauge: Food Label Scanner for Allergens, Additives & E Codes",
    desc="Scan a barcode or photograph a food label to check ingredients, allergens, additives and E codes, with the source of each fact. Free on iPhone. No account.",
    keywords="food label scanner, barcode scanner food, ingredient scanner, allergen scanner, food additives, E numbers, E codes, halal scanner, vegan scanner, nutrition label reader",
    tagline="Know what you eat.",
    nav=("How it works", "FAQ", "Privacy"),
    kicker="Now on the App Store",
    h1="Scan the barcode. Read the label.",
    lead="Scan a barcode to see a product’s ingredients, allergens and additives, with the source of each fact. No record for it? Photograph the ingredient label and FoodGauge reads it.",
    chips=("Barcode or label", "Your allergens highlighted", "E-code catalog offline", "No account"),
    cta="Download on the App Store",
    android="Android: closed testing on Google Play",
    card_kicker="Example · At a glance",
    card_product="Hazelnut granola",
    card_rows=(("Your allergens", "Milk · Hazelnut"), ("May contain", "Peanut"), ("Additives", "2"), ("Sugar", "24 g / 100 g"), ("Saturated fat", "3.1 g / 100 g"), ("Salt", "0.2 g / 100 g")),
    card_note="Sample product for illustration.",
    gap_kicker="When the barcode comes up empty",
    gap_h="No record? Read the label instead.",
    gap_p="Barcode lookups depend on someone having added the product to a database. FoodGauge tries that first, and when it finds nothing, it reads the label you are holding.",
    gap_rows=("A local brand nobody has added yet", "A small producer", "An import that never made the catalogue", "A smudged or torn barcode", "A product with no barcode at all"),
    gap_status="Read the label",
    gap_end="Use the camera or a photo from your gallery, check the extracted ingredient text, correct it if needed, and continue.",
    how_kicker="How it works",
    how_h="Scan, read, check.",
    steps=(("Scan the barcode", "Or type it in. FoodGauge shows the ingredients and nutrition information it can find, and where each fact came from. Barcode lookups need a connection."),
           ("No record? Read the label", "Photograph the ingredient list or pick an image. The text is read on your phone, and you can correct it before it is used."),
           ("Check what matters to you", "Allergens you flag in Settings are highlighted. Additives are matched by E code or by name. Contains and may-contain declarations are listed separately.")),
    ev_kicker="Evidence first",
    ev_h="No score without evidence.",
    ev_p="Most products open with an At a glance card instead of an overall health score. When the information needed for a score is missing, FoodGauge withholds the score and shows what is missing or conflicting.",
    ev_items=(("At a glance", "Your allergens, the number of additives, and sugar, saturated fat and salt amounts."),
              ("Contains and may contain", "Declared allergens and precautionary warnings are kept apart, so a trace warning is not confused with an ingredient."),
              ("Halal, vegan and vegetarian clues", "Status from community records for barcodes, plus the words found in the ingredient list. These are clues, not certifications."),
              ("E codes, offline", "A local catalog with a short explanation for each code. Basic Mode works without internet.")),
    ev_warn_k="Always check the package",
    ev_warn="Source records do not replace the current package. Check the label itself when making allergy-related decisions.",
    faq_kicker="Questions",
    faq_h="Straight answers.",
    faq=(("What is FoodGauge?", "FoodGauge is a food label scanner for iPhone, with an Android version in testing. Scan a barcode or photograph the ingredient label to see ingredients, allergens, additives, E codes and available nutrition information, with the source of each fact."),
         ("Do I need a barcode?", "No. A barcode lookup is the quickest route, but when a product has no record, or no barcode at all, you can photograph the ingredient label or choose an image from your gallery, then review and correct the extracted text."),
         ("Does FoodGauge give a health score?", "Most products show an At a glance card without an overall health score. A score is withheld when the required evidence is unavailable, and missing or conflicting information stays visible."),
         ("Can it tell me if a product is halal or vegan?", "For barcodes it shows halal, vegan and vegetarian status from community databases, and it checks the ingredient list on your phone for related words. Both are clues, not certifications."),
         ("Does it work offline?", "Basic Mode reads labels on your phone and includes the local E-code catalog, so it works without internet. New barcode lookups need a connection."),
         ("Are my photos uploaded?", "No. Label text is read on your phone. In AI mode, only the extracted text is sent for analysis, not the photo."),
         ("Is FoodGauge medical advice?", "No. FoodGauge provides general label information, not medical advice or a personalised nutrition plan. For allergy-related decisions, always check the current package."),
         ("Do I need an account?", "No. There is no login or registration. Saved products and recent inspections are available without an account."),
         ("Which languages does the app support?", "English, Turkish, Spanish, French, Russian and Arabic."),
         ("How do I get it?", "FoodGauge is free on the App Store and contains ads. The Android version is in closed testing on Google Play.")),
    pr_kicker="Privacy",
    pr_h="What the app does with your data.",
    sup_h="Support",
    sup_p="Questions, a label that scanned badly, or a bug to report? Write to us and include the product name.",
    privacy=("No account, no registration, no personal profile is created.",
             "The camera is used only after you choose to take a photo, and the photo picker only receives the image you select.",
             "Label text is read on your phone. In AI mode, only the extracted text is sent for analysis. The photo itself is not uploaded.",
             "A barcode lookup sends the barcode number to fetch the product record.",
             "Scan history is stored on your device. You can delete a single record or clear the whole history at any time.",
             "The app shows ads. Ad personalisation follows the consent choice you make on first launch, which you can revisit from the privacy screen.",
             "No medical profile, diet profile or health record is created or requested."),
    end_kicker="Free on iPhone",
    end_h="Try it on the next packaged product you pick up.",
    end_p="Android is in closed testing. Follow @food.gauge on Instagram for the Google Play launch.",
    foot1="Not medical advice. Label-based general information only.",
    foot2="FoodGauge does not use Nutri-Score branding and is not affiliated with any food authority. Product records come from community databases.",
    lang_label="Language",
    card_aria="Example result card",
)

T["tr"] = dict(
    title="FoodGauge: Gıda Etiketi ve Barkod Tarayıcı | Alerjen, Katkı, E Kodu",
    desc="Barkodu tarayın ya da etiketin fotoğrafını çekin; içindekileri, alerjenleri, katkı maddelerini ve E kodlarını kaynağıyla görün. iPhone'da ücretsiz, hesap gerekmez.",
    keywords="gıda etiketi tarayıcı, barkod okuyucu gıda, içindekiler analizi, alerjen tarayıcı, katkı maddesi, E kodları, helal kontrol, vegan kontrol",
    tagline="Ne yediğini bil.",
    nav=("Nasıl çalışır", "SSS", "Gizlilik"),
    kicker="App Store’da",
    h1="Barkodu tara. Etiketi oku.",
    lead="Barkodu tarayın; ürünün içindekilerini, alerjenlerini ve katkı maddelerini her bilginin kaynağıyla görün. Ürün kaydı yoksa içindekiler etiketinin fotoğrafını çekin, FoodGauge etiketi okusun.",
    chips=("Barkod ya da etiket", "Alerjenleriniz vurgulanır", "Çevrimdışı E kodu kataloğu", "Hesap yok"),
    cta="App Store’dan indirin",
    android="Android: Google Play’de kapalı test",
    card_kicker="Örnek · Bir bakışta",
    card_product="Fındıklı granola",
    card_rows=(("Alerjenleriniz", "Süt · Fındık"), ("İz miktarda içerebilir", "Yer fıstığı"), ("Katkı maddesi", "2"), ("Şeker", "24 g / 100 g"), ("Doymuş yağ", "3,1 g / 100 g"), ("Tuz", "0,2 g / 100 g")),
    card_note="Gösterim amaçlı örnek ürün.",
    gap_kicker="Barkod sonuç vermediğinde",
    gap_h="Kayıt yoksa etiketi okuyun.",
    gap_p="Barkod sorgusu, ürünün daha önce bir veritabanına eklenmiş olmasına bağlıdır. FoodGauge önce bunu dener, bir şey bulamazsa elinizdeki etiketi okur.",
    gap_rows=("Henüz kimsenin eklemediği yerel bir marka", "Küçük bir üretici", "Kataloğa hiç girmemiş ithal bir ürün", "Silik ya da yırtık bir barkod", "Barkodu olmayan bir ürün"),
    gap_status="Etiketi oku",
    gap_end="Kamerayı kullanın ya da galeriden bir fotoğraf seçin. Çıkan içindekiler metnini kontrol edin, gerekirse düzeltin ve devam edin.",
    how_kicker="Nasıl çalışır",
    how_h="Tara, oku, kontrol et.",
    steps=(("Barkodu tarayın", "Ya da numarayı elle girin. FoodGauge bulabildiği içindekiler ve besin bilgilerini, her bilginin nereden geldiğiyle birlikte gösterir. Barkod sorgusu internet ister."),
           ("Kayıt yok mu? Etiketi okutun", "İçindekiler listesinin fotoğrafını çekin ya da bir görsel seçin. Metin telefonunuzda okunur ve kullanılmadan önce düzeltebilirsiniz."),
           ("Size önemli olanı kontrol edin", "Ayarlarda işaretlediğiniz alerjenler vurgulanır. Katkı maddeleri E koduyla ya da adıyla eşleşir. “İçerir” ve “iz miktarda içerebilir” bildirimleri ayrı listelenir.")),
    ev_kicker="Önce kanıt",
    ev_h="Kanıt yoksa puan da yok.",
    ev_p="Çoğu üründe genel bir sağlık puanı yerine “Bir bakışta” kartı açılır. Puan için gereken bilgi eksikse FoodGauge puan vermez; neyin eksik ya da çelişkili olduğunu gösterir.",
    ev_items=(("Bir bakışta", "Alerjenleriniz, katkı maddesi sayısı ve şeker, doymuş yağ, tuz miktarları."),
              ("İçerir ve iz miktarda içerebilir", "Bildirilen alerjenler ile uyarı ifadeleri ayrı tutulur; iz uyarısı bir içerikle karıştırılmaz."),
              ("Helal, vegan ve vejetaryen ipuçları", "Barkodlu ürünlerde topluluk kayıtlarındaki durum ve içindekiler listesinde bulunan kelimeler. Bunlar ipucudur, sertifika değildir."),
              ("Çevrimdışı E kodları", "Her kod için kısa açıklama içeren yerel katalog. Temel Mod internetsiz çalışır.")),
    ev_warn_k="Paketi mutlaka kontrol edin",
    ev_warn="Kaynak kayıtlar güncel paketin yerini tutmaz. Alerjiyle ilgili kararlarda etiketin kendisine bakın.",
    faq_kicker="Sorular",
    faq_h="Net cevaplar.",
    faq=(("FoodGauge nedir?", "FoodGauge, iPhone için bir gıda etiketi tarayıcısıdır; Android sürümü testte. Barkodu tarayarak ya da içindekiler etiketinin fotoğrafını çekerek içindekileri, alerjenleri, katkı maddelerini, E kodlarını ve mevcut besin bilgisini her bilginin kaynağıyla görürsünüz."),
         ("Barkod gerekli mi?", "Hayır. Barkod sorgusu en hızlı yoldur. Ürünün kaydı ya da hiç barkodu yoksa içindekiler etiketinin fotoğrafını çekebilir veya galeriden bir görsel seçip çıkan metni kontrol edip düzeltebilirsiniz."),
         ("FoodGauge sağlık puanı veriyor mu?", "Çoğu üründe genel sağlık puanı olmadan “Bir bakışta” kartı gösterilir. Gerekli kanıt yoksa puan verilmez; eksik ya da çelişkili bilgi görünür kalır."),
         ("Ürünün helal ya da vegan olup olmadığını söyler mi?", "Barkodlu ürünlerde topluluk veritabanlarındaki helal, vegan ve vejetaryen durumunu gösterir; ayrıca içindekiler listesini telefonunuzda ilgili kelimeler için tarar. İkisi de ipucudur, sertifika değildir."),
         ("İnternetsiz çalışır mı?", "Temel Mod etiketleri telefonunuzda okur ve yerel E kodu kataloğunu içerir, bu yüzden internetsiz çalışır. Yeni barkod sorguları için bağlantı gerekir."),
         ("Fotoğraflarım yükleniyor mu?", "Hayır. Etiket metni telefonunuzda okunur. AI modunda analiz için fotoğraf değil, yalnızca çıkarılan metin gönderilir."),
         ("FoodGauge tıbbi tavsiye mi?", "Hayır. FoodGauge genel etiket bilgisi sunar; tıbbi tavsiye ya da kişisel beslenme planı değildir. Alerjiyle ilgili kararlarda her zaman güncel paketi kontrol edin."),
         ("Hesap açmam gerekiyor mu?", "Hayır. Giriş ya da kayıt yok. Kaydettiğiniz ürünler ve son incelemeler hesapsız kullanılabilir."),
         ("Uygulama hangi dilleri destekliyor?", "Türkçe, İngilizce, İspanyolca, Fransızca, Rusça ve Arapça."),
         ("Nasıl indiririm?", "FoodGauge App Store’da ücretsizdir ve reklam içerir. Android sürümü Google Play’de kapalı testte.")),
    pr_kicker="Gizlilik",
    pr_h="Uygulama verilerinizle ne yapıyor?",
    sup_h="Destek",
    sup_p="Sorunuz mu var, bir etiket kötü mü okundu, ya da bir hata mı buldunuz? Ürün adını da ekleyerek bize yazın.",
    privacy=("Hesap, kayıt ya da kişisel profil oluşturulmaz.",
             "Kamera yalnızca siz fotoğraf çekmeyi seçtiğinizde kullanılır; fotoğraf seçici yalnızca seçtiğiniz görsele erişir.",
             "Etiket metni telefonunuzda okunur. AI modunda analiz için yalnızca çıkarılan metin gönderilir; fotoğrafın kendisi yüklenmez.",
             "Barkod sorgusu, ürün kaydını getirmek için barkod numarasını gönderir.",
             "Tarama geçmişi cihazınızda saklanır. Tek bir kaydı silebilir ya da geçmişin tamamını istediğiniz zaman temizleyebilirsiniz.",
             "Uygulamada reklam gösterilir. Reklam kişiselleştirme, ilk açılışta verdiğiniz izin tercihine göre yapılır; bu tercihi gizlilik ekranından değiştirebilirsiniz.",
             "Tıbbi profil, diyet profili ya da sağlık kaydı oluşturulmaz, istenmez."),
    end_kicker="iPhone’da ücretsiz",
    end_h="Elinize aldığınız bir sonraki paketli üründe deneyin.",
    end_p="Android sürümü kapalı testte. Google Play çıkışı için Instagram’da @food.gauge hesabını takip edin.",
    foot1="Tıbbi tavsiye değildir. Yalnızca etikete dayalı genel bilgi sunar.",
    foot2="FoodGauge, Nutri-Score markasını kullanmaz ve hiçbir gıda otoritesiyle bağlantılı değildir. Ürün kayıtları topluluk veritabanlarından gelir.",
    lang_label="Dil",
    card_aria="Örnek sonuç kartı",
)

T["ru"] = dict(
    title="FoodGauge: сканер этикеток и штрихкодов — аллергены, добавки, E-коды",
    desc="Отсканируйте штрихкод или сфотографируйте этикетку: состав, аллергены, добавки и E-коды с источником каждого факта. Бесплатно на iPhone, без аккаунта.",
    keywords="сканер этикеток, сканер штрихкодов продуктов, состав продуктов, аллергены, пищевые добавки, E-коды, халяль, веган",
    tagline="Знай, что ешь.",
    nav=("Как это работает", "Вопросы", "Конфиденциальность"),
    kicker="Уже в App Store",
    h1="Сканируйте штрихкод. Читайте этикетку.",
    lead="Отсканируйте штрихкод, чтобы увидеть состав, аллергены и добавки продукта с источником каждого факта. Записи нет? Сфотографируйте список ингредиентов, и FoodGauge прочитает этикетку.",
    chips=("Штрихкод или этикетка", "Ваши аллергены выделены", "Каталог E-кодов офлайн", "Без аккаунта"),
    cta="Загрузить в App Store",
    android="Android: закрытое тестирование в Google Play",
    card_kicker="Пример · Кратко",
    card_product="Гранола с фундуком",
    card_rows=(("Ваши аллергены", "Молоко · Фундук"), ("Может содержать", "Арахис"), ("Добавки", "2"), ("Сахар", "24 г / 100 г"), ("Насыщенные жиры", "3,1 г / 100 г"), ("Соль", "0,2 г / 100 г")),
    card_note="Условный продукт для примера.",
    gap_kicker="Когда штрихкод ничего не нашёл",
    gap_h="Записи нет? Прочитайте этикетку.",
    gap_p="Поиск по штрихкоду работает, только если кто-то уже добавил продукт в базу. FoodGauge сначала пробует его, а если ничего не находит, читает этикетку у вас в руках.",
    gap_rows=("Местный бренд, который ещё никто не добавил", "Небольшой производитель", "Импорт, не попавший в каталог", "Смазанный или порванный штрихкод", "Продукт совсем без штрихкода"),
    gap_status="Прочитать этикетку",
    gap_end="Используйте камеру или фото из галереи, проверьте распознанный текст состава, при необходимости исправьте его и продолжайте.",
    how_kicker="Как это работает",
    how_h="Сканируйте, читайте, проверяйте.",
    steps=(("Отсканируйте штрихкод", "Или введите его вручную. FoodGauge покажет найденный состав и пищевую ценность и укажет источник каждого факта. Для поиска по штрихкоду нужен интернет."),
           ("Записи нет? Прочитайте этикетку", "Сфотографируйте список ингредиентов или выберите изображение. Текст распознаётся на телефоне, и его можно исправить до использования."),
           ("Проверьте то, что важно вам", "Аллергены, отмеченные в настройках, выделяются. Добавки распознаются по E-коду или названию. «Содержит» и «может содержать» показаны отдельно.")),
    ev_kicker="Сначала факты",
    ev_h="Нет данных — нет оценки.",
    ev_p="Для большинства продуктов вместо общей оценки полезности открывается карточка «Кратко». Если данных для оценки не хватает, FoodGauge не выставляет её и показывает, чего не хватает или что противоречит друг другу.",
    ev_items=(("Кратко", "Ваши аллергены, количество добавок, содержание сахара, насыщенных жиров и соли."),
              ("Содержит и может содержать", "Заявленные аллергены и предупреждения о следах показаны раздельно, чтобы одно не путалось с другим."),
              ("Подсказки: халяль, веган, вегетарианское", "Статус из общественных баз для штрихкодов и слова, найденные в составе. Это подсказки, а не сертификация."),
              ("E-коды офлайн", "Локальный каталог с кратким описанием каждого кода. Базовый режим работает без интернета.")),
    ev_warn_k="Всегда проверяйте упаковку",
    ev_warn="Записи из источников не заменяют текущую упаковку. Принимая решения, связанные с аллергией, сверяйтесь с самой этикеткой.",
    faq_kicker="Вопросы",
    faq_h="Прямые ответы.",
    faq=(("Что такое FoodGauge?", "FoodGauge — сканер этикеток продуктов для iPhone; версия для Android проходит тестирование. Отсканируйте штрихкод или сфотографируйте состав, чтобы увидеть ингредиенты, аллергены, добавки, E-коды и доступную пищевую ценность с источником каждого факта."),
         ("Нужен ли штрихкод?", "Нет. Поиск по штрихкоду — самый быстрый путь, но если записи о продукте нет или штрихкода нет вовсе, можно сфотографировать состав или выбрать изображение из галереи, а затем проверить и исправить распознанный текст."),
         ("Ставит ли FoodGauge оценку полезности?", "Для большинства продуктов показывается карточка «Кратко» без общей оценки. Если нужных данных нет, оценка не выставляется, а недостающая или противоречивая информация остаётся на виду."),
         ("Покажет ли он, халяль продукт или веган?", "Для штрихкодов показывается статус халяль, веган и вегетарианский из общественных баз, а состав дополнительно проверяется на телефоне на соответствующие слова. И то и другое — подсказки, а не сертификация."),
         ("Работает ли без интернета?", "Базовый режим распознаёт этикетки на телефоне и включает локальный каталог E-кодов, поэтому работает без интернета. Для нового поиска по штрихкоду нужно подключение."),
         ("Загружаются ли мои фото?", "Нет. Текст этикетки распознаётся на телефоне. В режиме ИИ на анализ отправляется только распознанный текст, а не фото."),
         ("Это медицинская рекомендация?", "Нет. FoodGauge даёт общую информацию с этикетки, а не медицинские советы или персональный план питания. В вопросах аллергии всегда проверяйте текущую упаковку."),
         ("Нужен ли аккаунт?", "Нет. Входа и регистрации нет. Сохранённые продукты и недавние проверки доступны без аккаунта."),
         ("Какие языки поддерживает приложение?", "Английский, турецкий, испанский, французский, русский и арабский."),
         ("Как установить?", "FoodGauge бесплатен в App Store и содержит рекламу. Версия для Android проходит закрытое тестирование в Google Play.")),
    pr_kicker="Конфиденциальность",
    pr_h="Что приложение делает с вашими данными.",
    sup_h="Поддержка",
    sup_p="Есть вопрос, этикетка распозналась плохо или нашлась ошибка? Напишите нам и укажите название продукта.",
    privacy=("Аккаунт, регистрация и личный профиль не создаются.",
             "Камера используется только после того, как вы решили сделать снимок; средство выбора фото получает только выбранное изображение.",
             "Текст этикетки распознаётся на телефоне. В режиме ИИ на анализ отправляется только распознанный текст. Само фото не загружается.",
             "При поиске по штрихкоду отправляется номер штрихкода, чтобы получить запись о продукте.",
             "История сканирований хранится на устройстве. Можно удалить отдельную запись или очистить всю историю в любой момент.",
             "В приложении показывается реклама. Персонализация рекламы зависит от выбора согласия при первом запуске; его можно изменить на экране конфиденциальности.",
             "Медицинский профиль, профиль питания или медицинские записи не создаются и не запрашиваются."),
    end_kicker="Бесплатно на iPhone",
    end_h="Попробуйте на следующем упакованном продукте.",
    end_p="Версия для Android на закрытом тестировании. Следите за запуском в Google Play в Instagram @food.gauge.",
    foot1="Не является медицинской рекомендацией. Только общая информация с этикетки.",
    foot2="FoodGauge не использует бренд Nutri-Score и не связан ни с одним органом по безопасности пищевых продуктов. Записи о продуктах берутся из общественных баз данных.",
    lang_label="Язык",
    card_aria="Пример карточки результата",
)

T["ar"] = dict(
    title="FoodGauge: ماسح ملصقات الأغذية والباركود — مسببات الحساسية والمضافات ورموز E",
    desc="امسح الباركود أو صوّر ملصق المنتج لترى المكونات ومسببات الحساسية والمضافات ورموز E مع مصدر كل معلومة. مجاني على iPhone ودون حساب.",
    keywords="ماسح ملصقات الأغذية, ماسح باركود الطعام, المكونات, مسببات الحساسية, المضافات الغذائية, رموز E, حلال, نباتي",
    tagline="اعرف ماذا تأكل.",
    nav=("كيف يعمل", "الأسئلة", "الخصوصية"),
    kicker="متوفر الآن على App Store",
    h1="امسح الباركود. اقرأ الملصق.",
    lead="امسح الباركود لترى مكونات المنتج ومسببات الحساسية والمضافات مع مصدر كل معلومة. لا يوجد سجل للمنتج؟ صوّر قائمة المكونات وسيقرأ FoodGauge الملصق.",
    chips=("باركود أو ملصق", "إبراز مسببات الحساسية لديك", "دليل رموز E دون إنترنت", "دون حساب"),
    cta="حمّله من App Store",
    android="Android: اختبار مغلق على Google Play",
    card_kicker="مثال · نظرة سريعة",
    card_product="غرانولا بالبندق",
    card_rows=(("مسببات الحساسية لديك", "حليب · بندق"), ("قد يحتوي على", "فول سوداني"), ("المضافات", "2"), ("السكر", "24 غ / 100 غ"), ("الدهون المشبعة", "3.1 غ / 100 غ"), ("الملح", "0.2 غ / 100 غ")),
    card_note="منتج افتراضي للتوضيح.",
    gap_kicker="عندما لا يجد الباركود شيئًا",
    gap_h="لا يوجد سجل؟ اقرأ الملصق.",
    gap_p="يعتمد البحث بالباركود على أن يكون أحدهم قد أضاف المنتج إلى قاعدة بيانات. يجرب FoodGauge ذلك أولًا، وإذا لم يجد شيئًا يقرأ الملصق الذي بين يديك.",
    gap_rows=("علامة محلية لم يضفها أحد بعد", "منتج صغير", "منتج مستورد لم يدخل الفهرس", "باركود ممسوح أو ممزق", "منتج بلا باركود أصلًا"),
    gap_status="اقرأ الملصق",
    gap_end="استخدم الكاميرا أو صورة من المعرض، وراجع نص المكونات المستخرج وصحّحه عند الحاجة، ثم تابع.",
    how_kicker="كيف يعمل",
    how_h="امسح، اقرأ، تحقق.",
    steps=(("امسح الباركود", "أو أدخله يدويًا. يعرض FoodGauge المكونات والقيم الغذائية المتوفرة ومصدر كل معلومة. يحتاج البحث بالباركود إلى اتصال."),
           ("لا يوجد سجل؟ اقرأ الملصق", "صوّر قائمة المكونات أو اختر صورة. تُقرأ النصوص على هاتفك، ويمكنك تصحيحها قبل استخدامها."),
           ("تحقق مما يهمك", "تُبرَز مسببات الحساسية التي تحددها في الإعدادات. تُعرَّف المضافات برمز E أو بالاسم. ويُعرض «يحتوي على» و«قد يحتوي على» بشكل منفصل.")),
    ev_kicker="الدليل أولًا",
    ev_h="لا تقييم دون دليل.",
    ev_p="تُفتح معظم المنتجات ببطاقة «نظرة سريعة» بدل تقييم صحي عام. وإذا نقصت المعلومات اللازمة للتقييم، يحجبه FoodGauge ويعرض ما هو ناقص أو متعارض.",
    ev_items=(("نظرة سريعة", "مسببات الحساسية لديك، وعدد المضافات، وكميات السكر والدهون المشبعة والملح."),
              ("يحتوي على وقد يحتوي على", "تبقى مسببات الحساسية المعلنة منفصلة عن التحذيرات الاحترازية، فلا يُخلط تحذير الآثار بمكوّن فعلي."),
              ("مؤشرات الحلال والنباتي", "الحالة من سجلات مجتمعية للمنتجات ذات الباركود، والكلمات الموجودة في قائمة المكونات. هذه مؤشرات وليست شهادات."),
              ("رموز E دون إنترنت", "دليل محلي مع شرح مختصر لكل رمز. يعمل الوضع الأساسي دون إنترنت.")),
    ev_warn_k="تحقق دائمًا من العبوة",
    ev_warn="لا تغني السجلات عن العبوة الحالية. راجع الملصق نفسه عند اتخاذ قرارات تتعلق بالحساسية.",
    faq_kicker="أسئلة",
    faq_h="إجابات مباشرة.",
    faq=(("ما هو FoodGauge؟", "FoodGauge ماسح لملصقات الأغذية على iPhone، ونسخة Android قيد الاختبار. امسح الباركود أو صوّر ملصق المكونات لترى المكونات ومسببات الحساسية والمضافات ورموز E والقيم الغذائية المتوفرة مع مصدر كل معلومة."),
         ("هل أحتاج إلى باركود؟", "لا. البحث بالباركود هو الطريق الأسرع، لكن إذا لم يكن للمنتج سجل أو لم يكن له باركود أصلًا، يمكنك تصوير ملصق المكونات أو اختيار صورة من المعرض ثم مراجعة النص المستخرج وتصحيحه."),
         ("هل يعطي FoodGauge تقييمًا صحيًا؟", "تعرض معظم المنتجات بطاقة «نظرة سريعة» دون تقييم صحي عام. يُحجب التقييم عندما لا تتوفر الأدلة اللازمة، وتبقى المعلومات الناقصة أو المتعارضة ظاهرة."),
         ("هل يخبرني إن كان المنتج حلالًا أو نباتيًا؟", "للمنتجات ذات الباركود يعرض حالة الحلال والنباتي الصرف والنباتي من قواعد بيانات مجتمعية، ويفحص قائمة المكونات على هاتفك بحثًا عن كلمات ذات صلة. كلاهما مؤشرات وليس شهادات."),
         ("هل يعمل دون إنترنت؟", "يقرأ الوضع الأساسي الملصقات على هاتفك ويتضمن دليل رموز E المحلي، لذا يعمل دون إنترنت. يحتاج البحث الجديد بالباركود إلى اتصال."),
         ("هل تُرفع صوري؟", "لا. يُقرأ نص الملصق على هاتفك. في وضع الذكاء الاصطناعي يُرسل النص المستخرج فقط للتحليل، وليس الصورة."),
         ("هل FoodGauge نصيحة طبية؟", "لا. يقدم FoodGauge معلومات عامة من الملصق، وليس نصيحة طبية أو خطة غذائية شخصية. في القرارات المتعلقة بالحساسية تحقق دائمًا من العبوة الحالية."),
         ("هل أحتاج إلى حساب؟", "لا. لا يوجد تسجيل دخول أو تسجيل. المنتجات المحفوظة وعمليات الفحص الأخيرة متاحة دون حساب."),
         ("ما اللغات التي يدعمها التطبيق؟", "الإنجليزية والتركية والإسبانية والفرنسية والروسية والعربية."),
         ("كيف أحصل عليه؟", "FoodGauge مجاني على App Store ويحتوي على إعلانات. نسخة Android في اختبار مغلق على Google Play.")),
    pr_kicker="الخصوصية",
    pr_h="ماذا يفعل التطبيق ببياناتك.",
    sup_h="الدعم",
    sup_p="لديك سؤال، أو قُرئ ملصق بشكل سيئ، أو وجدت خطأ؟ راسلنا واذكر اسم المنتج.",
    privacy=("لا يُنشأ حساب أو تسجيل أو ملف شخصي.",
             "تُستخدم الكاميرا فقط بعد أن تختار التقاط صورة، ولا يصل منتقي الصور إلا إلى الصورة التي تختارها.",
             "يُقرأ نص الملصق على هاتفك. في وضع الذكاء الاصطناعي يُرسل النص المستخرج فقط للتحليل، ولا تُرفع الصورة نفسها.",
             "يرسل البحث بالباركود رقم الباركود لجلب سجل المنتج.",
             "يُحفظ سجل الفحص على جهازك. يمكنك حذف سجل واحد أو مسح السجل كله في أي وقت.",
             "يعرض التطبيق إعلانات. يتبع تخصيص الإعلانات خيار الموافقة الذي تحدده عند أول تشغيل، ويمكنك تغييره من شاشة الخصوصية.",
             "لا يُنشأ ولا يُطلب ملف طبي أو غذائي أو سجل صحي."),
    end_kicker="مجاني على iPhone",
    end_h="جرّبه على المنتج المعبأ التالي الذي تلتقطه.",
    end_p="نسخة Android في اختبار مغلق. تابع ‎@food.gauge على Instagram لموعد الإطلاق على Google Play.",
    foot1="ليس نصيحة طبية. معلومات عامة مبنية على الملصق فقط.",
    foot2="لا يستخدم FoodGauge علامة Nutri-Score وليس تابعًا لأي جهة رقابية على الغذاء. تأتي سجلات المنتجات من قواعد بيانات مجتمعية.",
    lang_label="اللغة",
    card_aria="بطاقة نتيجة توضيحية",
)

KICK = '<p class="kicker {cls}"><span class="inline-block h-2 w-2" style="background:{c}"></span>{t}</p>'
H2 = '<h2 class="mt-5 text-[clamp(1.75rem,3.4vw,2.6rem)] font-bold leading-[1.06] tracking-tight">{t}</h2>'


def url(lang):
    return BASE + PAGES[lang]


def page(lang):
    t = T[lang]
    rtl = lang == "ar"
    d = "rtl" if rtl else "ltr"
    out = []
    # ---------- head ----------
    alt = "".join(f'    <link rel="alternate" hreflang="{l}" href="{url(l)}" />\n' for l in PAGES)
    sw = {
        "@context": "https://schema.org", "@type": "MobileApplication", "name": "FoodGauge",
        "alternateName": "FoodGauge: Food Label Scanner", "applicationCategory": "LifestyleApplication",
        "applicationSubCategory": "Food label scanner", "operatingSystem": "iOS",
        "description": t["desc"], "url": url(lang), "inLanguage": lang,
        "image": BASE + "og.png", "installUrl": APPSTORE, "downloadUrl": APPSTORE, "sameAs": [APPSTORE, IG],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "availableLanguage": ["en", "tr", "es", "fr", "ru", "ar"],
        "publisher": {"@type": "Organization", "name": "Kaira Labs"},
    }
    fq = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    ws = {"@context": "https://schema.org", "@type": "WebSite", "name": "FoodGauge", "url": BASE,
          "inLanguage": list(PAGES), "publisher": {"@type": "Organization", "name": "Kaira Labs", "sameAs": [IG]}}
    jd = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out.append(f'''<!doctype html>
<html lang="{lang}" dir="{d}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/foodgauge-site/favicon.svg" />
    <link rel="apple-touch-icon" href="/foodgauge-site/icon-512.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet" />
    <title>{e(t["title"])}</title>
    <meta name="description" content="{e(t["desc"])}" />
    <link rel="canonical" href="{url(lang)}" />
{alt}    <link rel="alternate" hreflang="x-default" href="{BASE}" />
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
    <meta name="theme-color" content="#0A1C05" />
    <meta name="author" content="Kaira Labs" />
    <meta name="keywords" content="{e(t["keywords"])}" />
    <meta name="apple-itunes-app" content="app-id=6802302665" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="FoodGauge" />
    <meta property="og:locale" content="{OG_LOCALE[lang]}" />
    <meta property="og:title" content="{e(t["title"])}" />
    <meta property="og:description" content="{e(t["desc"])}" />
    <meta property="og:url" content="{url(lang)}" />
    <meta property="og:image" content="{BASE}og.png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{e(t["title"])}" />
    <meta name="twitter:description" content="{e(t["desc"])}" />
    <meta name="twitter:image" content="{BASE}og.png" />
    <script type="application/ld+json">{jd(sw)}</script>
    <script type="application/ld+json">{jd(fq)}</script>
    <script type="application/ld+json">{jd(ws)}</script>
    <link rel="stylesheet" crossorigin href="/foodgauge-site/app.css">
  </head>
  <body>
    <div id="root"><div dir="{d}" class="min-h-screen bg-paper">''')
    # ---------- header ----------
    langs = "".join(
        f'<a href="/foodgauge-site/{PAGES[l]}" hrefLang="{l}"' + (' aria-current="true" class="px-2 py-1 tracking-widest transition-colors bg-lime text-ink"' if l == lang else ' class="px-2 py-1 tracking-widest transition-colors text-paper/55 hover:text-paper"') + f'>{l.upper()}</a>'
        for l in PAGES)
    chips = "".join(f'<li class="flex items-center gap-2"><span class="text-lime">/</span>{e(c)}</li>' for c in t["chips"])
    rows = "".join(
        f'<div class="flex items-center justify-between gap-6 border-t border-paper/12 py-4"><span class="text-[15px] text-paper/70">{e(k)}</span><span class="font-mono text-[13px] text-paper">{e(v)}</span></div>'
        for k, v in t["card_rows"])
    out.append(f'''<header class="relative overflow-hidden bg-ink text-paper"><div aria-hidden="true" class="pointer-events-none absolute inset-0 opacity-[0.16]" style="background-image:linear-gradient(to right, #A8F03D 1px, transparent 1px), linear-gradient(to bottom, #A8F03D 1px, transparent 1px);background-size:72px 72px;mask-image:radial-gradient(120% 80% at 70% 0%, black, transparent 70%);-webkit-mask-image:radial-gradient(120% 80% at 70% 0%, black, transparent 70%)"></div><div class="wrap relative"><div class="flex items-center justify-between py-6"><a href="#top" class="flex items-baseline gap-2.5"><span class="text-[19px] font-bold tracking-tight">FoodGauge</span><span class="hidden font-mono text-[11px] text-lime sm:inline">{e(t["tagline"])}</span></a><div class="flex items-center gap-5"><div class="hidden items-center gap-5 font-mono text-[11px] uppercase tracking-[0.14em] text-paper/60 md:flex"><a class="hover:text-paper" href="#how">{e(t["nav"][0])}</a><a class="hover:text-paper" href="#faq">{e(t["nav"][1])}</a><a class="hover:text-paper" href="#privacy">{e(t["nav"][2])}</a></div><nav aria-label="{e(t["lang_label"])}" class="flex items-center gap-1 font-mono text-[11px]">{langs}</nav></div></div><div class="grid grid-cols-1 items-end gap-12 pb-16 pt-10 md:pb-24 md:pt-16 lg:grid-cols-12 lg:gap-8"><div class="lg:col-span-7">{KICK.format(cls="text-lime", c="#A8F03D", t=e(t["kicker"]))}<h1 class="mt-6 text-[clamp(2.5rem,6.2vw,4.6rem)] font-bold leading-[0.95] tracking-tightest">{e(t["h1"])}</h1><p class="mt-7 max-w-[46ch] text-[17px] leading-relaxed text-paper/70">{e(t["lead"])}</p><ul class="mt-9 flex flex-wrap gap-x-6 gap-y-2 font-mono text-[12px] text-paper/60">{chips}</ul><div class="mt-10 flex flex-wrap items-center gap-4"><a href="{APPSTORE}" target="_blank" rel="noopener" class="bg-lime px-6 py-3.5 text-[14px] font-bold text-ink transition-transform hover:-translate-y-0.5">{e(t["cta"])}</a><span class="font-mono text-[12px] text-paper/45">{e(t["android"])}</span></div></div><div class="lg:col-span-5"><figure class="border border-paper/15 bg-forest/40 p-8" aria-label="{e(t["card_aria"])}"><p class="kicker text-lime"><span class="inline-block h-2 w-2" style="background:#A8F03D"></span>{e(t["card_kicker"])}</p><p class="mt-5 text-[19px] font-bold leading-snug">{e(t["card_product"])}</p><div class="mt-5">{rows}</div><figcaption class="mt-4 border-t border-paper/12 pt-4 font-mono text-[11px] text-paper/45">{e(t["card_note"])}</figcaption></figure></div></div></div></header><main id="top">''')
    # ---------- gap ----------
    grows = "".join(
        f'<div class="flex items-center justify-between gap-6 border-b border-ink/8 px-5 py-4 last:border-0"><span class="text-[15px] text-ink/80">{e(r)}</span><span class="flex shrink-0 items-center gap-2 font-mono text-[11px] uppercase tracking-wider text-brand"><span class="h-1.5 w-1.5 rounded-full bg-brand"></span>{e(t["gap_status"])}</span></div>'
        for r in t["gap_rows"])
    out.append(f'''<section class="border-b border-ink/10 bg-paper py-20 md:py-28"><div class="wrap grid grid-cols-1 gap-12 lg:grid-cols-12"><div class="lg:col-span-5">{KICK.format(cls="text-ink/50", c="#F59E0B", t=e(t["gap_kicker"]))}{H2.format(t=e(t["gap_h"]))}<p class="mt-6 max-w-[42ch] text-[16px] leading-relaxed text-ink/65">{e(t["gap_p"])}</p></div><div class="lg:col-span-7"><div class="border border-ink/12 bg-white">{grows}</div><p class="mt-6 border-s-2 border-lime ps-5 text-[16px] font-medium leading-relaxed">{e(t["gap_end"])}</p></div></div></section>''')
    # ---------- how ----------
    steps = "".join(
        f'<li class="bg-white p-7"><span class="font-mono text-[13px] text-lime [text-shadow:0_0_0_#1B5E0F]"><span class="text-brand">0{i+1}</span></span><h3 class="mt-4 text-[19px] font-bold leading-snug">{e(h)}</h3><p class="mt-3 text-[15px] leading-relaxed text-ink/60">{e(p)}</p></li>'
        for i, (h, p) in enumerate(t["steps"]))
    out.append(f'''<section id="how" class="border-b border-ink/10 bg-white py-20 md:py-28"><div class="wrap">{KICK.format(cls="text-ink/50", c="#1B5E0F", t=e(t["how_kicker"]))}<h2 class="mt-5 max-w-[18ch] text-[clamp(1.75rem,3.4vw,2.6rem)] font-bold leading-[1.06] tracking-tight">{e(t["how_h"])}</h2><ol class="mt-14 grid grid-cols-1 gap-px border border-ink/12 bg-ink/12 md:grid-cols-3">{steps}</ol></div></section>''')
    # ---------- evidence ----------
    colors = ("#22C55E", "#F59E0B", "#A8F03D", "#F6F8F2")
    items = "".join(
        f'<div class="grid grid-cols-[auto_1fr] gap-x-5 border-t border-paper/12 py-5"><dt class="col-span-2 flex items-baseline justify-between gap-4"><span class="flex items-center gap-3 text-[17px] font-bold"><span class="h-2.5 w-2.5 shrink-0" style="background:{colors[i]}"></span>{e(h)}</span></dt><dd class="col-span-2 mt-2 max-w-[52ch] text-[14px] leading-relaxed text-paper/55 ms-[22px]">{e(p)}</dd></div>'
        for i, (h, p) in enumerate(t["ev_items"]))
    out.append(f'''<section id="evidence" class="border-b border-ink/10 bg-ink py-20 text-paper md:py-28"><div class="wrap"><div class="grid grid-cols-1 gap-12 lg:grid-cols-12"><div class="lg:col-span-5">{KICK.format(cls="text-lime", c="#A8F03D", t=e(t["ev_kicker"]))}{H2.format(t=e(t["ev_h"]))}<p class="mt-6 max-w-[42ch] text-[16px] leading-relaxed text-paper/65">{e(t["ev_p"])}</p></div><div class="lg:col-span-7"><dl class="mt-8">{items}</dl><div class="mt-6 border border-rag-red/45 bg-rag-red/[0.07] p-5"><p class="kicker text-rag-red"><span class="inline-block h-2 w-2 bg-rag-red"></span>{e(t["ev_warn_k"])}</p><p class="mt-3 text-[15px] leading-relaxed text-paper/80">{e(t["ev_warn"])}</p></div></div></div></div></section>''')
    # ---------- faq ----------
    faqs = "".join(
        f'''<details class="group border-t border-ink/12 py-5 last:border-b"><summary class="flex cursor-pointer list-none items-start justify-between gap-6 text-[17px] font-bold leading-snug marker:content-[&#x27;&#x27;]"><span>{e(q)}</span><span class="mt-1 shrink-0 font-mono text-[18px] leading-none text-brand transition-transform group-open:rotate-45">+</span></summary><p class="mt-4 max-w-[62ch] text-[15px] leading-relaxed text-ink/65">{e(a)}</p></details>'''
        for q, a in t["faq"])
    out.append(f'''<section id="faq" class="border-b border-ink/10 bg-white py-20 md:py-28"><div class="wrap grid grid-cols-1 gap-12 lg:grid-cols-12"><div class="lg:col-span-4">{KICK.format(cls="text-ink/50", c="#1B5E0F", t=e(t["faq_kicker"]))}{H2.format(t=e(t["faq_h"]))}</div><div class="lg:col-span-8">{faqs}</div></div></section>''')
    # ---------- privacy ----------
    pr = "".join(
        f'<li class="flex gap-4 border-t border-ink/12 py-4 first:border-t-0 first:pt-0"><span class="mt-2 h-1.5 w-1.5 shrink-0 bg-brand"></span><span class="text-[15px] leading-relaxed text-ink/75">{e(x)}</span></li>'
        for x in t["privacy"])
    out.append(f'''<section id="privacy" class="border-b border-ink/10 bg-paper py-20 md:py-28"><div class="wrap grid grid-cols-1 gap-12 lg:grid-cols-12"><div class="lg:col-span-5">{KICK.format(cls="text-ink/50", c="#1B5E0F", t=e(t["pr_kicker"]))}{H2.format(t=e(t["pr_h"]))}<div class="mt-10 border border-ink/12 bg-white p-6"><h3 class="text-[17px] font-bold">{e(t["sup_h"])}</h3><p class="mt-3 text-[15px] leading-relaxed text-ink/65">{e(t["sup_p"])}</p><a href="mailto:{MAIL}" class="mt-4 inline-block border-b-2 border-lime pb-0.5 font-mono text-[13px] hover:bg-lime/30">{MAIL}</a></div></div><ul class="lg:col-span-7">{pr}</ul></div></section>''')
    # ---------- end cta ----------
    out.append(f'''<section class="bg-brand py-20 text-paper md:py-24"><div class="wrap flex flex-col items-start justify-between gap-8 md:flex-row md:items-end"><div>{KICK.format(cls="text-lime", c="#A8F03D", t=e(t["end_kicker"]))}<h2 class="mt-5 max-w-[20ch] text-[clamp(1.6rem,3vw,2.3rem)] font-bold leading-[1.08] tracking-tight">{e(t["end_h"])}</h2><p class="mt-4 max-w-[46ch] text-[16px] text-paper/70">{e(t["end_p"])} <a href="{IG}" target="_blank" rel="noopener" class="border-b-2 border-lime pb-0.5 hover:text-paper">@food.gauge</a></p></div><a href="{APPSTORE}" target="_blank" rel="noopener" class="shrink-0 bg-lime px-7 py-4 text-[14px] font-bold text-ink transition-transform hover:-translate-y-0.5">{e(t["cta"])}</a></div></section></main>''')
    # ---------- footer ----------
    fl = "".join(f'<a href="/foodgauge-site/{PAGES[l]}" hrefLang="{l}" class="hover:text-paper">{LANG_NAMES[l]}</a>' for l in PAGES)
    out.append(f'''<footer class="bg-ink py-14 text-paper/45"><div class="wrap"><div class="flex flex-col gap-8 md:flex-row md:items-start md:justify-between"><div><p class="text-[17px] font-bold text-paper">FoodGauge</p><p class="mt-1 font-mono text-[12px] text-lime">{e(t["tagline"])}</p></div><div class="flex flex-wrap gap-x-8 gap-y-2 font-mono text-[12px]">{fl}<a href="{APPSTORE}" target="_blank" rel="noopener" class="hover:text-paper">App Store</a><a href="{IG}" target="_blank" rel="noopener" class="hover:text-paper">Instagram</a></div></div><div class="mt-10 border-t border-paper/12 pt-6 text-[13px] leading-relaxed"><p class="text-paper/60">{e(t["foot1"])}</p><p class="mt-2 max-w-[70ch]">{e(t["foot2"])}</p><p class="mt-4 font-mono text-[11px] text-paper/30">© 2026 FoodGauge · Kaira Labs</p></div></div></footer></div></div>
  </body>
</html>
''')
    return "".join(out)


for lang, fn in PAGES.items():
    with open(os.path.join(OUT, fn or "index.html"), "w", encoding="utf-8") as f:
        f.write(page(lang))
print("ok")
