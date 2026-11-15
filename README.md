# Pottzi-videolar

Pottzi için Instagram videoları, [HyperFrames](https://hyperframes.heygen.com) ile HTML'den MP4'e üretilir.

## Yapı

- `pottzi-sohbet/`: 7128 ↔ 1854 sohbet animasyonu (1080×1920, 3 dk, geri sayımlı)
  - `index.html`: kök kompozisyon (renk değişkenleri: turuncu, pembe, mor)
  - `compositions/chat.html`: sohbet ekranı, sayaç, mesajlar ve zamanlamaları
  - `compositions/outro.html`: "Süre doldu" kapanışı
- `videolar/`: render edilmiş MP4'ler
- `.claude/settings.json`: HyperFrames Claude Code eklentisi (yeni oturumlarda otomatik hazır)

## Komutlar

```bash
cd pottzi-sohbet
npm run dev      # tarayıcıda önizleme
npm run check    # kontroller
npx hyperframes render -o ../videolar/<ad>.mp4
```
