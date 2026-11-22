#!/usr/bin/env python3
"""Türkçe ses/video -> kelime zamanlı altyazı (JSON). Kullanım: python3 araclar/altyazi.py ses.mp3 [cikti.json]"""
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else None
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
model = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = model.transcribe(audio, language="tr", word_timestamps=True)
words = [{"text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)} for s in segs for w in s.words]
txt = json.dumps(words, ensure_ascii=False, indent=1)
open(out, "w").write(txt) if out else print(txt)
