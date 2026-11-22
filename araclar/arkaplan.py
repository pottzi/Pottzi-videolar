#!/usr/bin/env python3
"""Görselden arka planı siler (şeffaf PNG). Kullanım: python3 araclar/arkaplan.py girdi.png cikti.png
Video için: npx hyperframes remove-background girdi.mp4"""
import sys
from rembg import remove
from PIL import Image
remove(Image.open(sys.argv[1])).save(sys.argv[2])
