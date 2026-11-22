# Koşu sahnesi üreteci: compositions/ks.html dosyasını yazar.
SKIN, SKIN2 = "#f8d9c4", "#efc6ad"
TOP, TOP2 = "#3FB8AF", "#2c9690"
LEG, LEG2 = "#3a3170", "#16112c"

def limb_leg(prefix, col):
    return f'''<g transform="translate(0 0)"><g id="{prefix}-thigh">
      <rect x="-19" y="-8" width="38" height="104" rx="19" fill="{col}" />
      <g transform="translate(0 92)"><g id="{prefix}-shin">
        <rect x="-16" y="0" width="32" height="98" rx="16" fill="{col}" />
        <rect x="-20" y="86" width="62" height="28" rx="13" fill="#f4f1fb" /><rect x="-20" y="104" width="62" height="10" rx="5" fill="#FE6D6A" />
      </g></g>
    </g></g>'''

def limb_arm(prefix, col, hand):
    return f'''<g transform="translate(0 -156)"><g id="{prefix}-arm">
      <rect x="-15" y="-6" width="30" height="84" rx="15" fill="{col}" />
      <g transform="translate(0 72)"><g id="{prefix}-fore">
        <rect x="-13" y="0" width="26" height="74" rx="13" fill="{col}" />
        <circle cx="0" cy="76" r="15" fill="{hand}" />
      </g></g>
    </g></g>'''

RUNNER = f'''<g id="runner"><g id="rn-bob">
  {limb_arm("rb", TOP2, SKIN2)}
  {limb_leg("lb", LEG2)}
  <path d="M-42,12 C-48,-60 -46,-142 -22,-180 C-2,-198 32,-194 42,-172 C54,-122 52,-42 42,12 Z" fill="{TOP}" />
  <rect x="-6" y="-214" width="28" height="44" rx="12" fill="{SKIN2}" />
  <g id="rn-head" transform="translate(8 -256)">
    <g id="rn-hair"><ellipse cx="-52" cy="10" rx="16" ry="15" fill="#c4512a" stroke="#a8401f" stroke-width="2" /><ellipse cx="-62" cy="38" rx="16" ry="15" fill="#c4512a" stroke="#a8401f" stroke-width="2" /><ellipse cx="-72" cy="66" rx="16" ry="15" fill="#c4512a" stroke="#a8401f" stroke-width="2" /><ellipse cx="-82" cy="94" rx="16" ry="15" fill="#c4512a" stroke="#a8401f" stroke-width="2" /><ellipse cx="-92" cy="122" rx="16" ry="15" fill="#c4512a" stroke="#a8401f" stroke-width="2" /><circle cx="-96" cy="148" r="8" fill="#D857AE" /></g>
    <path d="M-50,-28 C-46,-58 -14,-66 14,-62 C42,-56 56,-34 56,-8 C56,6 60,10 62,14 C58,18 54,18 54,22 C54,40 44,58 22,62 C-6,66 -40,56 -50,30 C-56,10 -56,-12 -50,-28 Z" fill="{SKIN}" />
    <ellipse cx="-10" cy="8" rx="10" ry="14" fill="{SKIN2}" />
    <path d="M-58,-8 C-62,-62 -20,-74 12,-70 C42,-66 60,-42 58,-14 C40,-40 6,-48 -24,-44 C-44,-38 -54,-24 -58,-8 Z" fill="#c4512a" />
    <path d="M20,-22 Q30,-31 42,-24" fill="none" stroke="#a8401f" stroke-width="3.5" stroke-linecap="round" />
    <g id="rn-eye"><ellipse cx="32" cy="-2" rx="6" ry="8.5" fill="#2a1a14" /><circle cx="34" cy="-5" r="2" fill="#fff" /></g>
    <path d="M35,-10 l5,-6 M38,-7 l7,-4 M39,-3 l8,-1" stroke="#2a1a14" stroke-width="2.6" stroke-linecap="round" />
    <g fill="#c9784f" opacity="0.7"><circle cx="18" cy="14" r="2.5" /><circle cx="28" cy="18" r="2.5" /><circle cx="36" cy="12" r="2.5" /></g>
    <circle cx="24" cy="20" r="12" fill="#ff8aa6" opacity="0.5" />
    <g id="rn-ms"><path d="M36,32 Q44,39 51,32" fill="#e0607e" stroke="#c94f6d" stroke-width="3" stroke-linecap="round" /></g>
    <g id="rn-mf" opacity="0"><path d="M38,34 L50,34" fill="none" stroke="#c94f6d" stroke-width="4" stroke-linecap="round" /></g>
  </g>
  {limb_leg("lf", LEG)}
  {limb_arm("rf", TOP, SKIN)}
  <g id="rn-phone" opacity="0"><rect x="34" y="-150" width="30" height="52" rx="7" fill="#15131F" /><rect x="38" y="-145" width="22" height="40" rx="4" fill="#9fb6ff" /></g>
</g></g>'''

# arka plan şeritleri (tekrarlı)
def lamps(n, gap, y0):
    out = []
    for i in range(n):
        x = 120 + i * gap
        out.append(f'<rect x="{x}" y="{y0}" width="16" height="430" rx="8" fill="#4a3f78" /><path d="M{x+8},{y0} q40,-30 70,0" fill="none" stroke="#4a3f78" stroke-width="12" stroke-linecap="round" /><circle cx="{x+78}" cy="{y0+6}" r="16" fill="#ffe3a8" /><circle cx="{x+78}" cy="{y0+6}" r="40" fill="rgba(255,227,168,0.25)" />')
        out.append(f'<path d="M{x+gap/2},{y0+430} l0,-210" stroke="#5b4f8a" stroke-width="14" /><ellipse cx="{x+gap/2-30}" cy="{y0+215}" rx="70" ry="18" fill="#5b8f6a" transform="rotate(-25 {x+gap/2-30} {y0+215})" /><ellipse cx="{x+gap/2+30}" cy="{y0+215}" rx="70" ry="18" fill="#4f8060" transform="rotate(25 {x+gap/2+30} {y0+215})" /><ellipse cx="{x+gap/2}" cy="{y0+200}" rx="18" ry="70" fill="#5b8f6a" />')
    return "".join(out)

def tiles(n, gap, y0, h, col):
    return "".join(f'<rect x="{i*gap}" y="{y0}" width="6" height="{h}" fill="{col}" />' for i in range(n))

HTML = r'''<template>
  <style>
    #root { position: absolute; inset: 0; overflow: hidden; font-family: "Poppins", sans-serif; color: #15131F; background: #F3EFFC; }
    #s-svg { position: absolute; left: 0; top: 0; }
    .cap { position: absolute; left: 90px; right: 90px; top: 222px; text-align: center; opacity: 0; }
    .cap span { display: inline-block; padding: 16px 32px; border-radius: 36px; background: rgba(255,255,255,0.94); font-size: 40px; font-weight: 700; line-height: 1.3;
      box-shadow: 0 14px 40px rgba(40,20,80,0.16); }
    #cap1 { opacity: 1; }

    #card { position: absolute; left: 110px; right: 110px; top: 340px; height: 660px; border-radius: 48px; background: #fff; overflow: hidden; opacity: 0;
      box-shadow: 0 30px 80px rgba(40,20,90,0.30); }
    #c-head { position: absolute; left: 0; right: 0; top: 0; height: 250px; background: linear-gradient(180deg, #d97bbb, #cf6aae); }
    #c-pill { position: absolute; left: 50%; top: 30px; margin-left: -140px; width: 280px; height: 56px; border-radius: 28px; background: #7b4aa6; color: #fff;
      display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 600; }
    #c-title { position: absolute; left: 50px; right: 50px; top: 104px; text-align: center; color: #fff; font-size: 36px; font-weight: 800; line-height: 1.25; }
    .rc { position: absolute; width: 470px; border-radius: 32px; background: #fff; border: 2px solid #efe6f6; box-shadow: 0 10px 26px rgba(150,80,190,0.12);
      padding: 18px 22px 18px 80px; opacity: 0; }
    .rc.l { left: 22px; } .rc.r { left: 348px; }
    .rc i { position: absolute; left: 22px; top: 22px; width: 42px; height: 42px; border-radius: 50%; }
    .rc b { display: block; font-size: 26px; }
    .rc b em { font-style: normal; font-weight: 500; font-size: 22px; color: #6F4BF1; margin-left: 10px; }
    .rc div { font-size: 30px; font-weight: 500; line-height: 1.3; margin-top: 2px; }

    #flash { position: absolute; inset: 0; background: #fff; opacity: 0; }
    .lbl { position: absolute; left: 70px; padding: 10px 22px; border-radius: 26px; background: rgba(21,19,31,0.78); color: #fff; font-size: 28px; font-weight: 700; opacity: 0; }
    #lbl1 { top: 320px; } #lbl2 { top: 760px; } #lbl3 { top: 1200px; }
    #lbl1 { background: linear-gradient(90deg, #6F4BF1, #D857AE); }
    #dim { position: absolute; inset: 0; background: rgba(21,19,31,0.62); opacity: 0; }
    #fin { position: absolute; left: 110px; right: 110px; top: 720px; text-align: center; color: #fff; font-size: 92px; font-weight: 800; line-height: 1.12; letter-spacing: -0.02em; opacity: 0; }
    #fin .g { background: linear-gradient(90deg, #FE6D6A, #F4698D 35%, #B655CD 68%, #8f97ff); -webkit-background-clip: text; background-clip: text; color: transparent; }
  </style>
  <div id="root" data-composition-id="ks" data-width="1080" data-height="1920">
    <svg id="s-svg" width="1080" height="1920" viewBox="0 0 1080 1920" data-layout-ignore>
      <defs>
        <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9a7f0" /><stop offset="0.55" stop-color="#ffb8c9" /><stop offset="1" stop-color="#ffd9a8" /></linearGradient>
        <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#93b2f2" /><stop offset="1" stop-color="#6c86dc" /></linearGradient>
        <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff1c9" /><stop offset="0.45" stop-color="#ffd38f" /><stop offset="1" stop-color="rgba(255,211,143,0)" /></radialGradient>
        <linearGradient id="skyB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fd0f5" /><stop offset="1" stop-color="#ffd2c2" /></linearGradient>
        <linearGradient id="skyC" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c7b6f2" /><stop offset="1" stop-color="#ffcf9f" /></linearGradient>
        <clipPath id="b1"><rect x="40" y="300" width="1000" height="420" rx="40" /></clipPath>
        <clipPath id="b2"><rect x="40" y="740" width="1000" height="420" rx="40" /></clipPath>
        <clipPath id="b3"><rect x="40" y="1180" width="1000" height="420" rx="40" /></clipPath>
        __RUNNER__
      </defs>

      <!-- SAHNE A/B: sahil -->
      <g id="sceneA">
        <rect width="1080" height="1920" fill="url(#sky)" />
        <circle id="sunA" cx="780" cy="1050" r="230" fill="url(#sun)" />
        <rect y="1060" width="1080" height="230" fill="url(#sea)" />
        <g id="waves" fill="rgba(255,255,255,0.45)">__WAVES__</g>
        <rect y="1278" width="1080" height="14" fill="#6a5fa0" />
        <g id="mid">__LAMPS__</g>
        <rect y="1290" width="1080" height="630" fill="#efe2ea" />
        <g id="ground">__TILES__</g>
        <rect y="1690" width="1080" height="230" fill="#e2d2df" />
        <use id="hero" href="#runner" transform="translate(430 1420) scale(1.25)" />
      </g>

      <!-- SAHNE C: üç şehir -->
      <g id="sceneC" opacity="0">
        <rect width="1080" height="1920" fill="#F3EFFC" />
        <g clip-path="url(#b1)">
          <rect x="40" y="300" width="1000" height="420" fill="url(#sky)" /><circle cx="820" cy="620" r="150" fill="url(#sun)" />
          <rect x="40" y="600" width="1000" height="60" fill="url(#sea)" /><rect x="40" y="655" width="1000" height="70" fill="#efe2ea" />
          <g id="gC1">__TILESC1__</g>
          <use href="#runner" transform="translate(420 590) scale(0.42)" />
        </g>
        <g clip-path="url(#b2)">
          <rect x="40" y="740" width="1000" height="420" fill="url(#skyB)" /><circle cx="200" cy="1060" r="130" fill="url(#sun)" />
          <rect x="40" y="1040" width="1000" height="60" fill="#5f8fd8" /><rect x="40" y="1095" width="1000" height="70" fill="#e8dce6" />
          <g id="gC2">__TILESC2__</g>
          <use href="#runner" transform="translate(560 1030) scale(0.42)" style="filter: brightness(0.15) saturate(0.4); opacity: 0.9" />
        </g>
        <g clip-path="url(#b3)">
          <rect x="40" y="1180" width="1000" height="420" fill="url(#skyC)" /><circle cx="760" cy="1500" r="140" fill="url(#sun)" />
          <g fill="#8a7bb8">__CITY__</g><rect x="40" y="1535" width="1000" height="70" fill="#e5d8e4" />
          <g id="gC3">__TILESC3__</g>
          <use href="#runner" transform="translate(380 1470) scale(0.42)" style="filter: brightness(0.15) saturate(0.4); opacity: 0.9" />
        </g>
      </g>
    </svg>

    <div id="cap1" class="cap"><span>Her sabah 06:30. Tek başıma.</span></div>
    <div id="cap2" class="cap"><span>Bir gün dayanamadım, Pottzi'ye yazdım.</span></div>
    <div id="card" data-layout-allow-occlusion>
      <div id="c-head"><div id="c-pill">💬 Düşünce odası</div><div id="c-title">Her sabah tek başıma koşuyorum, motivasyonum bitti 😮‍💨</div></div>
      <div id="rc0" class="rc l"><i style="background:radial-gradient(circle at 35% 30%,#a8f0c6,#1f9a5a)"></i><b>P-3390<em>şimdi</em></b><div>Ben de! İzmir'den, 06:30 🏃‍♀️</div></div>
      <div id="rc1" class="rc r"><i style="background:radial-gradient(circle at 35% 30%,#c9a6ff,#7a3cf0)"></i><b>P-5071<em>şimdi</em></b><div>Ankara'dan ben. Yarın aynı saatte?</div></div>
      <div id="rc2" class="rc l"><i style="background:radial-gradient(circle at 35% 30%,#ffc6a8,#f06a3c)"></i><b>P-8212<em>şimdi</em></b><div>Eskişehir de katılıyor! 🙋‍♀️</div></div>
    </div>
    <div id="cap3" class="cap"><span>Ertesi sabah, 06:30</span></div>
    <div id="lbl1" class="lbl">Bursa · sen</div>
    <div id="lbl2" class="lbl">İzmir · P-3390</div>
    <div id="lbl3" class="lbl">Ankara · P-5071</div>
    <div id="flash"></div>
    <div id="dim"></div>
    <div id="fin">Görmeden de<br /><span class="g">birlikte</span><br />koşulur.</div>
  </div>
  <script>
    (function () {
      const tl = gsap.timeline({ paused: true });
      function build() {
        const END = 23.9, STOP = 4.7, C = 15.9, D = 20.6, P = 0.5, H = P / 2;
        // ---- koşu döngüsü ----
        function run(t0, t1) {
          const n = Math.max(1, Math.floor((t1 - t0) / H));
          const o = { yoyo: true, repeat: n - 1, duration: H, ease: "sine.inOut", immediateRender: false };
          const sv = { svgOrigin: "0 0" };
          tl.fromTo("#lf-thigh", { rotation: 32, ...sv }, { rotation: -42, ...sv, ...o }, t0);
          tl.fromTo("#lb-thigh", { rotation: -42, ...sv }, { rotation: 32, ...sv, ...o }, t0);
          tl.fromTo("#lf-shin", { rotation: 95, ...sv }, { rotation: 12, ...sv, ...o }, t0);
          tl.fromTo("#lb-shin", { rotation: 12, ...sv }, { rotation: 95, ...sv, ...o }, t0);
          tl.fromTo("#rf-arm", { rotation: -48, ...sv }, { rotation: 38, ...sv, ...o }, t0);
          tl.fromTo("#rb-arm", { rotation: 38, ...sv }, { rotation: -48, ...sv, ...o }, t0);
          tl.fromTo(["#rf-fore", "#rb-fore"], { rotation: -95, ...sv }, { rotation: -70, ...sv, ...o }, t0);
          tl.fromTo("#rn-bob", { y: 0 }, { y: -12, duration: H / 2, yoyo: true, repeat: n * 2 - 1, ease: "sine.inOut", immediateRender: false }, t0);
          tl.fromTo("#rn-hair", { rotation: -8, svgOrigin: "-10 0" }, { rotation: 8, svgOrigin: "-10 0", ...o }, t0);
        }
        function stand(t) {
          const q = { duration: 0.45, ease: "power2.out", svgOrigin: "0 0" };
          tl.to(["#lf-thigh", "#lb-thigh", "#lf-shin", "#lb-shin"], { rotation: 0, ...q }, t);
          tl.to("#rb-arm", { rotation: 6, ...q }, t); tl.to("#rb-fore", { rotation: -10, ...q }, t);
          tl.to("#rf-arm", { rotation: -28, ...q }, t); tl.to("#rf-fore", { rotation: -120, ...q }, t);
          tl.to("#rn-bob", { y: 0, duration: 0.3 }, t);
          tl.to("#rn-hair", { rotation: 0, svgOrigin: "-10 0", duration: 0.5 }, t);
          tl.to("#rn-phone", { opacity: 1, duration: 0.2 }, t + 0.35);
          tl.to("#rn-head", { rotation: 14, svgOrigin: "0 40", duration: 0.4 }, t + 0.3);
        }
        run(0, STOP);
        stand(STOP);
        // göz kırpma
        [1.4, 3.6, 7.2, 12.4, 17.8, 22.2].forEach((t) => tl.fromTo("#rn-eye", { scaleY: 1 }, { scaleY: 0.1, duration: 0.07, yoyo: true, repeat: 1, transformOrigin: "50% 50%", immediateRender: false }, t));
        tl.set("#rn-ms", { opacity: 0 }, 0.8); tl.set("#rn-mf", { opacity: 1 }, 0.8);
        // ---- arka plan hareketi (sahil) ----
        tl.fromTo("#mid", { x: 0 }, { x: -1500, duration: STOP, ease: "none" }, 0);
        tl.to("#mid", { x: -1620, duration: 0.5, ease: "power2.out" }, STOP);
        tl.fromTo("#ground", { x: 0 }, { x: -3000, duration: STOP, ease: "none" }, 0);
        tl.to("#ground", { x: -3240, duration: 0.5, ease: "power2.out" }, STOP);
        tl.fromTo("#waves", { x: 0 }, { x: -400, duration: END, ease: "none" }, 0);
        tl.fromTo("#sunA", { y: 40 }, { y: -40, duration: C, ease: "none" }, 0);
        // ---- altyazılar ----
        tl.to("#cap1", { opacity: 0, y: -30, duration: 0.3 }, 5.1);
        tl.fromTo("#cap2", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }, 5.35);
        tl.to("#cap2", { opacity: 0, y: -30, duration: 0.3 }, 8.0);
        // ---- düşünce odası kartı ----
        tl.fromTo("#card", { opacity: 0, y: 80, scale: 0.92 }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "back.out(1.5)" }, 6.0);
        const R = [8.25, 10.95, 13.85], y0 = 272, step = 128;
        R.forEach((t, i) => {
          tl.fromTo("#rc" + i, { opacity: 0, y: y0 - 30, scale: 0.9 }, { opacity: 1, y: y0, scale: 1, duration: 0.4, ease: "back.out(1.6)" }, t);
          for (let j = 0; j < i; j++) tl.to("#rc" + j, { y: y0 + (i - j) * step, duration: 0.4, ease: "power2.inOut" }, t);
        });
        tl.set("#rn-mf", { opacity: 0 }, 8.6); tl.set("#rn-ms", { opacity: 1 }, 8.6);
        tl.to("#card", { opacity: 0, y: -60, duration: 0.4, ease: "power2.in" }, C - 0.5);
        // ---- sahne C: üç şehir ----
        tl.fromTo("#flash", { opacity: 0 }, { opacity: 1, duration: 0.25 }, C - 0.25);
        tl.set("#sceneA", { opacity: 0 }, C); tl.set("#sceneC", { opacity: 1 }, C);
        tl.set("#rn-phone", { opacity: 0 }, C); tl.set("#rn-head", { rotation: 0, svgOrigin: "0 40" }, C);
        tl.to("#flash", { opacity: 0, duration: 0.35 }, C);
        run(C, END);
        ["#gC1", "#gC2", "#gC3"].forEach((g) => tl.fromTo(g, { x: 0 }, { x: -1400, duration: END - C, ease: "none" }, C));
        tl.fromTo("#cap3", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.35 }, C + 0.2);
        ["#lbl1", "#lbl2", "#lbl3"].forEach((l, i) => tl.fromTo(l, { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.35, ease: "power3.out" }, C + 0.6 + i * 0.5));
        tl.to("#cap3", { opacity: 0, duration: 0.3 }, D - 0.2);
        // ---- final ----
        tl.fromTo("#dim", { opacity: 0 }, { opacity: 1, duration: 0.5 }, D);
        tl.fromTo("#fin", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, D + 0.1);
        tl.set({}, {}, END);
        window.__timelines["ks"] = tl;
      }
      document.fonts.ready.then(build);
    })();
  </script>
</template>
'''

waves = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2" />' for x, y, w in [(60,1100,120),(300,1140,180),(560,1110,90),(780,1170,160),(980,1120,120),(1180,1150,150),(1400,1100,110)])
city = "".join(f'<rect x="{x}" y="{1535-h}" width="{w}" height="{h}" rx="6" />' for x, w, h in [(60,90,180),(160,70,240),(240,110,150),(360,60,280),(430,120,200),(560,80,260),(650,130,170),(790,70,230),(870,110,190),(990,60,250)])
out = (HTML.replace("__RUNNER__", RUNNER).replace("__WAVES__", waves).replace("__LAMPS__", lamps(9, 420, 860))
       .replace("__TILES__", tiles(40, 120, 1290, 400, "rgba(150,120,160,0.18)"))
       .replace("__TILESC1__", tiles(26, 90, 655, 70, "rgba(150,120,160,0.25)"))
       .replace("__TILESC2__", tiles(26, 90, 1095, 70, "rgba(150,120,160,0.25)"))
       .replace("__TILESC3__", tiles(26, 90, 1535, 70, "rgba(150,120,160,0.25)"))
       .replace("__CITY__", city))
open("compositions/ks.html", "w").write(out)
print("ok")
