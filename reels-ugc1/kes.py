import subprocess, json
SEG = [(0.85, 4.42), (5.02, 7.78), (10.74, 13.16), (14.22, 18.12), (20.74, 24.62), (26.74, 27.98)]
VF = "crop=720:900:0:110,scale=1080:1350:flags=lanczos,unsharp=5:5:0.6,fps=30,setsar=1"
t = 0; cuts = []; lst = open('parca/liste.txt', 'w')
for i, (a, b) in enumerate(SEG):
    d = b - a; o = f'parca/p{i}.mp4'
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', f'{a}', '-t', f'{d}', '-i', 'ham/veo.mp4', '-vf', VF,
        '-af', f'aresample=48000,afade=t=in:d=0.025,afade=t=out:st={d - 0.04:.3f}:d=0.04', '-c:v', 'libx264', '-crf', '15', '-preset', 'medium',
        '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', o.replace('.mp4', '.mov')], check=True)
    real = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', o.replace('.mp4', '.mov')], capture_output=True, text=True).stdout)
    cuts.append(round(t, 3)); t += real; lst.write(f"file 'p{i}.mov'\n")
lst.close()
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'parca/liste.txt', '-c:v', 'copy', '-an', 'assets/kadin.mp4'], check=True)
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'parca/liste.txt', '-vn', '-af', 'loudnorm=I=-16:TP=-1.5', '-ar', '48000', 'assets/ses.wav'], check=True)
json.dump({'cuts': cuts, 'dur': round(t, 3)}, open('zaman.json', 'w'))
print(cuts, round(t, 3))
