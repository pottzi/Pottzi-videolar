#!/usr/bin/env bash
# Pottzi video araçlarını kurar. Her yeni bulut oturumunda bir kez çalıştırılır.
#   bash araclar/kurulum.sh          -> temel araçlar (Whisper altyazı, arka plan silme, büyütme, yüz takibi, Drive indirme)
#   bash araclar/kurulum.sh --tam    -> + konuşan kişi videosu kurgusu için ekler (ghost-editor efekt/müzik/emoji kütüphanesi,
#                                       film renk tonları, DeepFilterNet ses temizleme, kişi maskesi, three.js animasyon kiti)
set -e
R="$(cd "$(dirname "$0")/.." && pwd)"
pip install --break-system-packages -q faster-whisper "rembg[cpu]" spandrel auto-editor yt-dlp gdown opencv-python-headless pillow uv
pip install --break-system-packages -q torch torchvision --index-url https://download.pytorch.org/whl/cpu
mkdir -p /root/modeller
[ -f /root/modeller/RealESRGAN_x2plus.pth ] || curl -sfL -o /root/modeller/RealESRGAN_x2plus.pth \
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth

if [ "${1:-}" = "--tam" ]; then
  command -v python3.11 >/dev/null || { uv python install 3.11; ln -sf "$(uv python find 3.11)" /usr/local/bin/python3.11; }
  G="$R/.claude/skills/ghost-editor"
  python3 "$G/scripts/library_restore.py" --licensed-only      # Mixkit efekt + müzik, Fluent emoji (telifsiz/lisanslı)
  bash "$G/scripts/setup_looks.sh"                              # film renk tonları (LUT)
  ffmpeg -v error -y -f lavfi -i "sine=frequency=300:duration=1" /tmp/_t.wav && bash "$G/scripts/denoise.sh" /tmp/_t.wav /tmp/_t2.wav >/dev/null
  bash "$G/scripts/setup_matte.sh"                              # kişi maskesi (yazıyı kişinin arkasına koymak için)
  (cd "$R/araclar/claude-animation-skills/kit" && npm install --no-audit --no-fund --ignore-scripts -s)
fi
echo "Pottzi araçları hazır."
