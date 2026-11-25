#!/usr/bin/env python3
"""Pottzi 3D 'içinde ne var' klibi: breakdown skill'inin kit'iyle, ekran görüntüsünü de çalışma klasörüne koyarak render eder.
    python3 build3d.py [--snap 1.0,4.0]
"""
import shutil, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
KIT = HERE.parents[1] / 'araclar' / 'claude-animation-skills' / 'kit'
sys.path.insert(0, str(KIT)); import anim  # noqa
spec_path = HERE / 'pottzi.breakdown.json'
spec = anim.load_spec(spec_path, {'title': '', 'subtitle': '', 'labels': [], 'accent': '#F4698D'})
dur = 4.2 + float(spec.get('hold', 0))
work = HERE / '.work' / '3d'
anim.prepare(HERE / spec['template'], spec, dur, work, three=True)
shutil.copy(HERE / 'ekran.png', work / 'ekran.png')
if '--snap' in sys.argv:
    anim.snapshots(work, [float(x) for x in sys.argv[sys.argv.index('--snap') + 1].split(',')], HERE / 'snaps')
else:
    print('render: cd ' + str(work) + ' && npx --yes hyperframes@0.9.52 render -o ' + str(HERE.parent / 'assets/video/3d.mp4'))
