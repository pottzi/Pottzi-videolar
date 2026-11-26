import json, subprocess, glob, os, numpy as np
from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
out = {}
for src in sorted(glob.glob("../ham2/IMG_79*")):
    n = os.path.basename(src).split('.')[0][4:]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
    segs, _ = model.transcribe(np.frombuffer(raw, np.float32), language="tr", word_timestamps=True,
        initial_prompt="Uzun yaşamanın sırrı insanlarda. Harvard, Okinawa, moai, yalnızlık, Amerika, salgın, Dünya Sağlık Örgütü.")
    words = [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]
    out[n] = words
    print(n, " ".join(w["w"] for w in words), flush=True)
json.dump(out, open("kelimeler.json", "w"), ensure_ascii=False, indent=0)
