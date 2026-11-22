#!/usr/bin/env python3
"""Real-ESRGAN x2 ile görsel büyütme (CPU). Kullanım: python3 araclar/buyut.py girdi.png cikti.png
Model: /root/modeller/RealESRGAN_x2plus.pth (yoksa araclar/kurulum.sh indirir)."""
import sys, torch, numpy as np
from PIL import Image
from spandrel import ModelLoader
m = ModelLoader().load_from_file("/root/modeller/RealESRGAN_x2plus.pth").eval()
img = np.asarray(Image.open(sys.argv[1]).convert("RGB")).astype(np.float32) / 255
t = torch.from_numpy(img).permute(2, 0, 1)[None]
torch.set_num_threads(4)
T = 256; _, _, H, W = t.shape; out = torch.zeros(1, 3, H * 2, W * 2)
with torch.no_grad():
    for y in range(0, H, T):
        for x in range(0, W, T):
            y0, x0 = max(0, y - 8), max(0, x - 8); y1, x1 = min(H, y + T + 8), min(W, x + T + 8)
            r = m(t[:, :, y0:y1, x0:x1])
            out[:, :, y*2:min(H, y+T)*2, x*2:min(W, x+T)*2] = r[:, :, (y-y0)*2:(y-y0+min(H, y+T)-y)*2, (x-x0)*2:(x-x0+min(W, x+T)-x)*2]
Image.fromarray((out[0].permute(1, 2, 0).clamp(0, 1).numpy() * 255).round().astype(np.uint8)).save(sys.argv[2])
