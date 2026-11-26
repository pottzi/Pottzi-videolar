# Oturum devir notları (son güncelleme: 2026-11-26)

Yeni oturumda önce bu dosyayı, sonra `CLAUDE.md`, `REKLAM-SONUCLARI.md` ve `araclar/README.md`'yi oku. Kullanıcıyla Türkçe konuş; teknik olmayan, iPad'den çalışan bir kurucu.

## Kullanıcı ve çalışma şekli
- Pottzi'nin kurucusu; uygulamayı kendisi geliştirmiyor, reklam ve içerik işlerini yürütüyor. **iPad'den çalışıyor, Mac almama kararı verdi** (bulut yeterli; ağır efektler sadece yavaş). Mac mini seçeneği ileride düşünülebilir.
- Aynı zamanda **spor hocası**; kişisel Instagram hesabı için "insan odaklı" sağlık/uzun yaşam/felsefe/sosyallik videoları çekiyor. Tarzı: "Ne anlatırsam anlatayım sonunda insan var; daha iyi yaşam."
- Videoları **Google Drive klasör bağlantısıyla** gönderir (sohbet yüklemesi 30 MB sınırı). İndirme: `python3 -m gdown --folder "<bağlantı>" -O kisisel/ham`. Bağlantı "herkes görüntüleyebilir" olmalı.
- Meta reklam hesabında **onayı olmadan hiçbir şey değiştirme** (salt okunur analiz serbest).

## Pottzi (şirket) içerikleri: durum
- Format: yalnızca **4:5 (1080×1350)**, faststart, tam kalite.
- Ana sorun: **kadın kullanıcı az.** Kadınlar reklamı izliyor ama tıklamıyor/indirmiyor (ayrıntı `REKLAM-SONUCLARI.md`). Kadın 18–30 kampanyaları PAUSED.
- Bu oturumda yapılanlar (`videolar/`):
  - `2026-11-25_meta-reklam-itiraf-odasi-4x5.mp4`: Talk to Many "Aldatılan var mı, benim gibi?" (açık tema, kartlar sağlı sollu, en yeni üstte).
  - `2026-11-25_meta-reklam-aldatilan-var-mi-4x5.mp4`: kullanıcının ekran kaydı (2x) + kadın sesi (Gözde) + boş oda + tek tek gelen cevaplar. Proje `reels-itiraf2/`.
  - `2026-11-25_3d-icinde-ne-var-4x5.mp4`: 3D "Pottzi'nin içinde ne var?" denemesi (breakdown skill'i, `reels-3d/`).
- Talk to Many gerçeği: oda = konu başlığı; kartlar = yorumlar, **sağlı sollu dizilir, en yeni en üste gelir**.
- Fikir listesi (henüz yapılmadı): "Konu aç'a bastım, karşıma bu çıktı" (B), POV mizah (C), mağaza ekran görüntülerini kadınlara göre yenileme, Nostaljik tarzı resimli animasyon (resimleri kullanıcı Gemini'de üretir, biz canlandırırız), kendi karakter/maskot.
- Kullanıcı ileride cartoon-3d-short ya da stick-figure ile bir Pottzi videosu isteyecek.

## Kişisel hesap videoları
- **Depoya girmez** (`kisisel/` ve `videolar/*kisisel*` .gitignore'da; yüzlü video commit'i güvenlik kontrolünce engellendi). Bitmiş videoyu kullanıcıya gönder, telefona kaydetsin.
- Format: **dik 9:16 (1080×1920)**. Stil: **tam ekran** (bölünmüş ekranı denedik, kullanıcı tam ekranı daha samimi buldu).
  - Kelime kelime altyazı, konuşulan kelime sarı (#FFD93D), Montserrat 900.
  - Başın üstündeki boş duvarda kartlar/rakamlar (koyu hap + sarı vurgu); damga efekti; kesim yerlerinde 1.0/1.1 yakınlaştırma.
  - Kapanışta koyu kart.
- Kullanıcı **rakamları ezbere okumak istemiyor**: kendi cümleleriyle konuşur, doğru rakamları ekrana biz yazarız. Yuvarladığı/yanlış söylediği bilgiyi ekranda doğru göster ve kullanıcıya söyle.
- **HDR kuralı:** iPhone HDR (HLG) gelirse HDR kalır (bkz. `CLAUDE.md` §6). Kullanıcı HDR'yi kapattığını söyledi; yeni çekimler büyük ihtimalle SDR.
- Şablonlar (kod, yüzsüz): `araclar/kisisel-sablon/`
  - `yazi.py`: Whisper large-v3-turbo ile kelime zamanları
  - `kes-hdr.py`: sessizlik kesme, HDR parçalar
  - `ed-hdr.tpl.html`: tam ekran kurgu; maskeli "yazı arkanda" açılışı
  - `ed-sdr-uyku.tpl.html`: SDR tam ekran
  - `ed-bolunmus-ekran.tpl.html`: bölünmüş ekran
- Süreç: Drive'dan indir → `yazi.py` → parçaları seç (tekrar çekimler, yarım kalanlar) → kes → sesi `denoise.sh` (DeepFilterNet) + loudnorm → kesilmiş sesi yeniden Whisper'la (kesin zamanlar) → kartları kelime zamanlarına göre yerleştir → render → faststart.
- "Yazı arkanda" efekti: `matte.py --model birefnet-general-lite --backend torch --infer-size 768x768 --stride 2` (büyük model belleğe sığmıyor; kare başı ~6 sn, sadece 2–3 sn'lik anlarda).
- Yapılan videolar:
  1. **Uyku ve kilo** (tam ekran + bölünmüş ekran versiyonu).
  2. **Uzun yaşamın sırrı insanlarda** (yeşil kapüşonlu; SDR ve HDR versiyonu).
  - Kullanıcıya önerilen ek çekim: kapanış cümlesi ("Spor kasını çalıştırır, sohbet kalbini. Uzun yaşamak istiyorsan yalnız yaşama.") ve "trende yabancıyla konuşmak" parçası. Gelirse eklenir.
- Sıradaki konu fikirleri:
  - "Uzun yaşamak, sağlıklı yaşamak mı?" (kondisyon, kavrama gücü, yerden kalkma testi, kas, sosyallik)
  - Kızlar ağırlık kaldırmak sizi iri yapmaz
  - Stres (Pottzi köprüsü)
  - Giyim psikolojisi
  - Stoacılık
- Çekim önerileri:
  - Telefon göz hizasında, 4K 30 fps, HDR kapalı, yüz pencereye dönük.
  - Parça parça çek; takılınca cümleyi tekrar et.
- Önerilen kapanış imzası: "Ben Mert. Daha uzun değil, daha iyi yaşamak için. Birlikte."

## Kişisel video 3: "İnsan ve odaklanma" (devam ediyor, 2026-11-26)
- Konuşma kartları PDF: `kisisel/odaklanma/insan-ve-odaklanma-konusma.pdf` (Kart A–D açılış, Kart 1–8 devam).
- Açılış bitti: `videolar/2026-11-26_kisisel-odaklanma-goril-C.mp4` (34 sn, HDR). Kullanıcı onayladı.
  - Akış: 0–3 sn "👀 TOPU KAÇ KERE ATTIĞIMI SAYIN!" → konuşma (IMG_7995, küçük "SAYMAYA DEVAM" kafanın solunda) →
    IMG_7996 "Doğru bildiyseniz tebrikler, gorili gördünüz mü?" → ⏪ → 3x sayım, goril anında 1x + yakınlaşma + daire → "25 ATIŞ ✓ · 🦍 1 GORİL".
  - Goril: Noto 🦍 siluet, koyu gri, 50 px, üst raf sağ köşe, 1,5 sn (kaynak 7.5–9.0). `goril2.py`.
  - Kod: `kisisel/odaklanma/` (`goril2.py`, `parca5.py`, `index4.tpl.html`, `kur.py`, HyperFrames projesi `hf/`).
- Devam kısmı çekildi (IMG_7997–8012) ve eklendi: `videolar/2026-11-26_kisisel-odaklanma-tam.mp4` (1:30, HDR). Kod: `kes2.py`, `kurB.py`, `indexB.tpl.html`, `hf2/`.
  - "Gidip gelmeler"de kenarlardan sekmeler (Mail, Instagram…) gelip aralarında gidip gelinir, sonra uçup gider. %2 → ekranda doğrusu %2,5 (kullanıcıya söylendi, gerekirse yeniden çekilecek).
  - Uzun HyperFrames render'ı (45 sn+) ~10 dakika sürer: arka planda çalıştır.
  - Son hâl 1:22: 7998 eklendi (sekmeler "sekmeler"de gelir, "bedeli var"da gider), 8002 + 8004 + "sırrını açıklayacağım" kesildi, kapanış kartı 2 sn. Kod: `kes3.py`.
  - Reels açıklamaları (kısa) bu video ve "uzun yaşam" videosu için yazıldı.
- Ders: ffmpeg ses karışımında `apad,atrim` sonsuz döngüye girdi; `amix=...:duration=longest,loudnorm,apad=whole_dur=` kullan. ffmpeg'i `-nostdin` ile çalıştır.

## Kurulu araçlar (yeni oturumda yeniden kur)
- `bash araclar/kurulum.sh --tam`: Whisper, ghost-editor efekt/müzik kütüphanesi, film LUT'ları, DeepFilterNet (model seyrek klonla), kişi maskesi, yüz takibi, gdown, three.js kiti.
- Fluent hareketli emoji indirilemedi (GitHub raw erişimi kapalı); sistemdeki Noto emoji kullanılıyor.
- Disk sınırı dar (~1–2 GB boş): HDR render ~1,1 GB geçici alan ister. Ara dosyaları (parça klasörleri, wav'lar, npm önbelleği) silerek yer aç.
- HDR render ipucu: HDR video katmanının `z-index: -1` olması ve sahne kökünün arka planının şeffaf olması gerekir; yoksa video yazıların üstüne çizilir.
