# Pottzi video araçları

Kurulum (yeni oturumda): `bash araclar/kurulum.sh`

| Araç | Ne yapar | Kullanım |
|---|---|---|
| `altyazi.py` | Türkçe sesi kelime kelime zamanlı altyazıya çevirir (Whisper) | `python3 araclar/altyazi.py ses.mp3 cikti.json` |
| `efekt.sh` | ElevenLabs ile ses efekti üretir | `araclar/efekt.sh "soft pop" cikti.mp3 0.6` |
| `arkaplan.py` | Görselden arka planı siler (şeffaf PNG) | `python3 araclar/arkaplan.py girdi.png cikti.png` |
| `auto-editor` | Videodaki sessiz yerleri/duraksamaları otomatik keser (gerçek çekim UGC'lerde ölü anlar için). Bitiş gülümsemesi gibi istenen sessiz kısımları da kesebilir, `--margin` ile ayarla | `auto-editor girdi.mp4 --margin 0.25s --no-open -o cikti.mp4` |
| `yt-dlp` | Bağlantıdan video indirir (kendi paylaşımlarımız, referans videolar). Başkasının içeriği sadece inceleme amaçlı, reklamda kullanılmaz | `yt-dlp -o cikti.mp4 <link>` |
| `buyut.py` | Görseli 2 kat büyütür (Real-ESRGAN, kare başı ~1,5 dk, sadece tek görseller için) | `python3 araclar/buyut.py girdi.png cikti.png` |

Video arka planı silme: `npx hyperframes remove-background girdi.mp4`

## Hazır ses efektleri — `assets/efektler/`
mesaj-gelen, mesaj-giden, yaziyor, whoosh, baglanti-kuruldu, buton, saat-tik, gece-ambiyans

## HyperFrames şablonları — `sablonlar/`
Kataloğun tamamı (geçişler, altyazı stilleri, sohbet/arayüz kartları, yazı efektleri, dokular, kamera hareketleri)
`sablonlar/compositions/` (bloklar) ve `sablonlar/compositions/components/` (bileşenler) içinde.
Bir projeye almak için: ilgili dosyayı projenin `compositions/` klasörüne kopyala ya da proje içinde `npx hyperframes add <isim>`.
Arama: `npx hyperframes catalog --query "<ingilizce tarif>"`

## Ek Claude skill'leri — `.claude/skills/` (2026-11-25)
Yeni oturumda kendiliğinden yüklenir. Hepsi MIT lisanslı, GitHub'dan alındı, kurulmadan önce içerikleri incelendi.

| Skill | Kaynak | Ne işe yarar | Not |
|---|---|---|---|
| `ghost-editor` | kurbaitaev/ghost-editor | Ham konuşan-kafa çekimini (tekrarlar, duraksamalar) 19 stilden biriyle bitmiş reels'e çevirir | Mac için yazılmış, Linux'ta denenmedi; çıktısı 9:16, bizde 4:5'e uyarlanmalı. İlk kullanımda `scripts/doctor.sh` ve `scripts/library_restore.py` (~60 MB efekt/müzik) çalıştırılmalı (kullanıcı onayıyla) |
| `cartoon-3d-short` | mromidev/claude-animated-shorts | three.js + Remotion ile "Pixar benzeri" 3D dünyada 2D karakterli hikâye animasyonu | Remotion + `@remotion/three` kurulumu gerekir |
| `motion-broll`, `explainer-high-energy`, `explainer-default`, `explainer-engaging`, `sound-effects`, `object-separation` | Barty-Bart/motion-graphics | Konuşmaya denk motion grafik, 12–20 sn hızlı tanıtım, uygulama arayüzünü yeniden çizen demo, ölçülü ses efekti, nesne/kişi ayırma | |
| `zach-d-films`, `zach-3d-films`, `stick-figure`, `low-poly`, `minecraft`, `kurzgesagt`, `dan-koe`, `map-route`, `breakdown`, `graph`, `minimalistic-graphics` | artemnovitckii/claude-animation-skills (`araclar/claude-animation-skills/`, skill'ler link) | three.js ile 3D çizgi film açıklayıcı, çöp adam, low-poly, voxel, sayaç/grafik animasyonları | İlk kullanımda `bash araclar/claude-animation-skills/kit/setup.sh`; Playwright sürümü buradaki Chromium ile uyuşmayabilir, `executablePath: /opt/pw-browsers/chromium` ile çalıştır |

- Liste: `araclar/awesome-claude-video-skills.md` (180 video skill reposunun kataloğu; ihtiyaç olunca buradan seçilir).
- Kurulmayanlar: **MotionClone** (GPU isteyen araştırma modeli, burada çalışmaz), **claude-shorts** (uzun videodan kısa kesit çıkarır; bizde uzun video yok), **yt-dlp** zaten kurulu.

## Konuşan kişi videosu kurgusu için ekler (2026-11-25)
`bash araclar/kurulum.sh --tam` ile kurulur (Mac gerekmez, hepsi bulut ortamında çalışır):
- **ghost-editor kütüphanesi** (`scripts/library_restore.py --licensed-only`): Mixkit ses efektleri ve müzik, Microsoft Fluent hareketli emoji. Telifli YouTube/meme sesleri bilerek indirilmez.
- **Yüz takibi** (`.claude/skills/ghost-editor/scripts/face_track.py`, OpenCV YuNet): yakınlaştırmalar ve altyazı yüze göre yerleşir.
- **Ses temizleme** (`scripts/denoise.sh`, DeepFilterNet3): telefon kaydındaki uğultu/oda sesini alır.
- **Film renk tonları** (`scripts/setup_looks.sh` → `scripts/film_look.py`): sinematik renk.
- **Kişi maskesi** (`scripts/setup_matte.sh`, BiRefNet): yazıyı konuşan kişinin arkasına koyma efekti.
- **Drive'dan indirme**: `gdown --folder <paylaşım bağlantısı>` (bağlantı "herkes görüntüleyebilir" olmalı).
- Kişisel hesap videoları `kisisel/` altında çalışılır ve depoya girmez. Varsayılan stil: tam ekran, kelime kelime sarı vurgulu altyazı, başın üstünde kartlar.
