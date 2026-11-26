import json, subprocess, re
K = json.load(open('kelimeler.json'))
# (klip, başlangıç, bitiş): seçilen aralıklar
SEC = [("7976",0.0,2.30),("7974",0.0,7.25),("7975",0.0,2.30),("7977",3.50,7.45),("7980",0.0,12.80),("7983",0.0,18.35),("7984",0.0,9.15),("7986",0.0,11.15)]
VF = "scale=1080:1920:flags=lanczos,fps=30,setsar=1"
def src(n):
    import glob; return glob.glob(f"../ham2/IMG_{n}.*")[0]
def silences(f):
    r = subprocess.run(["ffmpeg","-i",f,"-af","silencedetect=noise=-33dB:d=0.32","-f","null","-"],capture_output=True,text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    return list(zip(st, en + [1e9]*(len(st)-len(en))))
segs = []
for n, a, b in SEC:
    f = src(n); keep = [[a, b]]
    for s, e in silences(f):
        s2, e2 = s + 0.12, e - 0.10           # sessizliğin kenarlarında biraz pay bırak
        if e2 - s2 < 0.15: continue
        nk = []
        for x, y in keep:
            if e2 <= x or s2 >= y: nk.append([x, y]); continue
            if s2 > x: nk.append([x, s2])
            if e2 < y: nk.append([e2, y])
        keep = nk
    for x, y in keep:
        if y - x > 0.12: segs.append((n, round(x, 3), round(y, 3)))
words = []; t = 0; cuts = []
lst = open('parca-hdr/liste.txt', 'w')
for i, (n, x, y) in enumerate(segs):
    o = f'parca-hdr/p{i:02d}.mov'; d = y - x
    subprocess.run(['ffmpeg','-v','error','-y','-threads','2','-ss',f'{x:.3f}','-i',src(n),'-t',f'{d:.3f}','-vf',VF,
        '-af',f'aresample=48000,afade=t=in:d=0.012,afade=t=out:st={max(0,d-0.02):.3f}:d=0.02','-c:v','libx265','-crf','16','-preset','medium','-x265-params','log-level=error:colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc','-tag:v','hvc1',
        '-pix_fmt','yuv420p10le','-color_primaries','bt2020','-color_trc','arib-std-b67','-colorspace','bt2020nc','-c:a','pcm_s16le',o], check=True)
    real = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',o],capture_output=True,text=True).stdout)
    for w in K[n]:
        mid = (w['s'] + w['e']) / 2
        if x - 0.05 <= w['s'] and w['e'] <= y + 0.05 or (x <= mid <= y and w['e'] - w['s'] < 0.6):
            words.append({'w': w['w'], 's': round(max(w['s'], x) - x + t, 2), 'e': round(min(w['e'], y) - x + t, 2), 'clip': n})
    cuts.append(round(t, 3)); t += real
    lst.write(f"file 'p{i:02d}.mov'\n")
lst.close()
# aynı kelime iki parçaya bölünmüşse tekrarı at
ded = []
for w in words:
    if ded and ded[-1]['w'] == w['w'] and ded[-1]['clip'] == w['clip'] and w['s'] - ded[-1]['e'] < 0.05: ded[-1]['e'] = w['e']; continue
    ded.append(w)
json.dump({'cuts': cuts, 'dur': round(t, 3)}, open('zaman-hdr.json', 'w'))
print('parça', len(segs), 'süre', round(t, 2))
print(' '.join(f"{w['w']}@{w['s']}" for w in ded))
