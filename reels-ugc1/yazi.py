import json, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", "assets/ses.wav", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
segs, _ = m.transcribe(np.frombuffer(raw, np.float32), language="tr", word_timestamps=True, initial_prompt="Kızlar, bu uygulamada beni rahat ettiren üç şey var. Fotoğraf yok. Sohbet üç dakika. Engelliyorum. Flört uygulaması mı? Konu aç.")
w = [{"w": x.word.strip(), "s": round(x.start, 2), "e": round(x.end, 2)} for s in segs for x in s.words]
json.dump(w, open("kelimeler2.json", "w"), ensure_ascii=False)
print(" ".join(f"{x['w']}@{x['s']}" for x in w))
