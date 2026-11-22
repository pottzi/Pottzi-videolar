# Pottzi video araçları

Kurulum (yeni oturumda): `bash araclar/kurulum.sh`

| Araç | Ne yapar | Kullanım |
|---|---|---|
| `altyazi.py` | Türkçe sesi kelime kelime zamanlı altyazıya çevirir (Whisper) | `python3 araclar/altyazi.py ses.mp3 cikti.json` |
| `efekt.sh` | ElevenLabs ile ses efekti üretir | `araclar/efekt.sh "soft pop" cikti.mp3 0.6` |
| `arkaplan.py` | Görselden arka planı siler (şeffaf PNG) | `python3 araclar/arkaplan.py girdi.png cikti.png` |
| `buyut.py` | Görseli 2 kat büyütür (Real-ESRGAN, kare başı ~1,5 dk, sadece tek görseller için) | `python3 araclar/buyut.py girdi.png cikti.png` |

Video arka planı silme: `npx hyperframes remove-background girdi.mp4`

## Hazır ses efektleri — `assets/efektler/`
mesaj-gelen, mesaj-giden, yaziyor, whoosh, baglanti-kuruldu, buton, saat-tik, gece-ambiyans

## HyperFrames şablonları — `sablonlar/`
Kataloğun tamamı (geçişler, altyazı stilleri, sohbet/arayüz kartları, yazı efektleri, dokular, kamera hareketleri)
`sablonlar/compositions/` (bloklar) ve `sablonlar/compositions/components/` (bileşenler) içinde.
Bir projeye almak için: ilgili dosyayı projenin `compositions/` klasörüne kopyala ya da proje içinde `npx hyperframes add <isim>`.
Arama: `npx hyperframes catalog --query "<ingilizce tarif>"`
