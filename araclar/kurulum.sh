#!/usr/bin/env bash
# Pottzi video araçlarını kurar (Whisper altyazı, arka plan silme, Real-ESRGAN büyütme).
# Her yeni bulut oturumunda bir kez çalıştırılır; ortam kurulum betiği bunu otomatik yapar.
set -e
pip install --break-system-packages -q faster-whisper "rembg[cpu]" spandrel
pip install --break-system-packages -q torch torchvision --index-url https://download.pytorch.org/whl/cpu
mkdir -p /root/modeller
[ -f /root/modeller/RealESRGAN_x2plus.pth ] || curl -sfL -o /root/modeller/RealESRGAN_x2plus.pth \
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth
echo "Pottzi araçları hazır."
