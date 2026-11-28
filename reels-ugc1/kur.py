import json, subprocess
W = json.load(open('kelimeler2.json')); Z0 = json.load(open('zaman.json'))
FIX = {}
for w in W: w['w'] = FIX.get(w['w'], w['w'])
def f(word):
    return next(w['s'] for w in W if w['w'].rstrip('.,?!') in (word, word.capitalize()))
VD = Z0['dur']; TOT = round(VD + 3.6, 3)
B = [[round(f('fotoğraf') - 0.1, 2), round(f('İki') - 0.15, 2)],
     [round(f('sohbet') - 0.1, 2), round(f('kimseye') - 0.1, 2)],
     [round(f('istemediğim') - 0.1, 2), round(f('Bence') - 0.12, 2)]]
L1 = B[0][1] - B[0][0]
S1 = {'topic': 0.25, 'ty1': 0.6, 'm1': 1.2, 'type2': 1.45, 'm2': 2.2, 'ty3': 2.45, 'm3': 3.0, 'type4': 3.2, 'm4': 3.8}
Z = {'words': W, 'dur': VD, 'cuts': Z0['cuts'], 'broll': B, 'TOT': TOT, 't': {}, 's1': S1}
h = open('index.tpl.html').read().replace('__Z__', json.dumps(Z, ensure_ascii=False)).replace('__TOT__', str(TOT)).replace('__VD__', str(VD))
open('index.html', 'w').write(h)
L = '../.claude/skills/ghost-editor/library/'
inp = ['-i', 'assets/ses.wav', '-i', L + 'music/lo-fi-02.mp3']
fil = ['[0:a]aresample=48000[v]',
       f'[1:a]aresample=48000,atrim=0:{TOT},volume=0.07,afade=t=in:d=0.6,volume=enable=\'gte(t,{VD})\':volume=2.2,afade=t=out:st={TOT - 1.0}:d=1.0[mu]']
mix = ['[v]', '[mu]']; k = 1
def add(name, at, vol):
    global k
    inp.extend(['-i', L + 'sfx/' + name + '.wav']); k += 1
    fil.append(f"[{k}:a]aresample=48000,volume={vol},adelay={int(at * 1000)}:all=1[s{k}]"); mix.append(f'[s{k}]')
for b in B: add('whoosh-2', b[0] - 0.05, 0.3)
for key, nm in (('m1', 'mesaj-gelen'), ('m2', 'mesaj-giden'), ('m3', 'mesaj-gelen'), ('m4', 'mesaj-giden')):
    inp.extend(['-i', '../reels-meta-3/assets/audio/' + nm + '.mp3']); k += 1
    fil.append(f"[{k}:a]aresample=48000,volume=0.55,adelay={int((B[0][0] + S1[key]) * 1000)}:all=1[s{k}]"); mix.append(f'[s{k}]')
add('ding-1', B[1][1] - 0.6, 0.35)
add('pop-2', B[2][0] + 1.4, 0.4)
add('whoosh-cine', VD - 0.1, 0.3)
fil.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=longest,atrim=0:{TOT},loudnorm=I=-16:TP=-1.5,apad=whole_dur={TOT}[out]")
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y'] + inp + ['-filter_complex', ';'.join(fil), '-map', '[out]', '-ar', '48000', '-t', str(TOT), 'assets/mix.wav'], check=True, stdin=subprocess.DEVNULL)
print('TOT', TOT, 'B', B)
