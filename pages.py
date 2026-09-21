# pages.py  —  ORA v11.4 · Dark Edition
# v11.4: مودال «همه‌ی لینک‌ها» برای کانفیگ‌های مولتی + کپی/QR تک‌تک واریانت‌ها
#        + بنر هشدار بک‌اند قدیمی + فیلد Clean IP تایپ‌پذیر با datalist

# ─────────────────────────── لوگوی ORA (اسکلت + آتش) ───────────────────────────
LOGO_SVG = """<svg class="ora-logo" viewBox="0 0 140 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ora">
<defs>
<linearGradient id="fireG" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#7A0D0D"/><stop offset=".45" stop-color="#E63B12"/><stop offset="1" stop-color="#FFC93C"/></linearGradient>
<linearGradient id="fireG2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6A00"/><stop offset="1" stop-color="#B31212"/></linearGradient>
<radialGradient id="emberG"><stop offset="0" stop-color="#FFD24A"/><stop offset=".55" stop-color="#FF6A00"/><stop offset="1" stop-color="#FF6A00" stop-opacity="0"/></radialGradient>
<radialGradient id="haloG" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FF5A1F" stop-opacity=".28"/><stop offset="1" stop-color="#FF5A1F" stop-opacity="0"/></radialGradient>
<linearGradient id="boneG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F2E7D3"/><stop offset=".55" stop-color="#D3C3A6"/><stop offset="1" stop-color="#8F7E63"/></linearGradient>
</defs>
<circle cx="70" cy="70" r="66" fill="url(#haloG)"/>
<g class="ring r1"><circle cx="70" cy="70" r="63" fill="none" stroke="url(#fireG)" stroke-width="2.6" stroke-dasharray="34 12 7 12" stroke-linecap="round"/></g>
<g class="ring r2"><circle cx="70" cy="70" r="55" fill="none" stroke="url(#fireG2)" stroke-width="1.6" stroke-dasharray="2 8" stroke-linecap="round" opacity=".9"/></g>
<g class="ring r3"><circle cx="70" cy="70" r="47" fill="none" stroke="#FF4500" stroke-width="1" stroke-dasharray="70 46" opacity=".4"/></g>
<circle cx="70" cy="70" r="39" fill="#0A0504" stroke="url(#fireG)" stroke-width="1.3"/>
<path class="flame k1" d="M60 37c-3.2-2.8-3.4-6.2-.6-9.6.7 3 2.1 4.8 4.2 6-.5 1.7-1.7 2.9-3.6 3.6z" fill="url(#fireG)"/>
<path class="flame k2" d="M70 33.5c-3.6-3.4-3.8-7.2-.4-11 .7 3.4 2.3 5.4 4.6 6.7-.6 1.9-1.9 3.3-4.2 4.3z" fill="url(#fireG)"/>
<path class="flame k3" d="M80 37c-3.2-2.8-3.4-6.2-.6-9.6.7 3 2.1 4.8 4.2 6-.5 1.7-1.7 2.9-3.6 3.6z" fill="url(#fireG)"/>
<path d="M70 42c-11.8 0-20.3 8.5-20.3 19.7 0 6.7 2.8 10.8 6.1 13.6 1.5 1.3 2.4 3.1 2.4 5v3.9c0 1.8 1.3 3.1 3 3.1h17.6c1.7 0 3-1.3 3-3.1v-3.9c0-1.9.9-3.7 2.4-5 3.3-2.8 6.1-6.9 6.1-13.6C90.3 50.5 81.8 42 70 42z" fill="url(#boneG)"/>
<path d="M70 42c-11.8 0-20.3 8.5-20.3 19.7 0 6.7 2.8 10.8 6.1 13.6l2.1-1.9c-2.9-2.6-4.9-6.1-4.9-11.7C53 52 60.5 45.3 70 45.3z" fill="#0A0504" opacity=".16"/>
<ellipse cx="62.4" cy="63.2" rx="4.8" ry="5.8" fill="#070302"/>
<ellipse cx="77.6" cy="63.2" rx="4.8" ry="5.8" fill="#070302"/>
<circle class="pupil p1" cx="62.4" cy="63.6" r="2.5" fill="url(#emberG)"/>
<circle class="pupil p2" cx="77.6" cy="63.6" r="2.5" fill="url(#emberG)"/>
<path d="M70 69.6l-3.6 6.6a.9.9 0 0 0 .8 1.3h5.6a.9.9 0 0 0 .8-1.3z" fill="#070302"/>
<path d="M60.6 84.2h18.8v3.4c0 1.1-.9 2-2 2H62.6c-1.1 0-2-.9-2-2z" fill="url(#boneG)"/>
<path d="M66.2 84.4v5.2M70 84.4v5.2M73.8 84.4v5.2" stroke="#0A0504" stroke-width="1.2"/>
<path class="flame f1" d="M70 91.5c-5 3.6-7.6 6.9-7.6 10.4 0 4.4 3.3 7.3 7.6 7.3s7.6-2.9 7.6-7.3c0-3.5-2.6-6.8-7.6-10.4z" fill="url(#fireG)" opacity=".95"/>
<path class="flame f2" d="M70 96.5c-2.9 2.4-4.4 4.7-4.4 6.9 0 2.8 2 4.7 4.4 4.7s4.4-1.9 4.4-4.7c0-2.2-1.5-4.5-4.4-6.9z" fill="#FFD24A"/>
<circle class="spark s1" cx="64" cy="94" r="1.3" fill="#FFB347"/>
<circle class="spark s2" cx="76" cy="96" r="1.1" fill="#FF8A3C"/>
<circle class="spark s3" cx="70" cy="90" r="1" fill="#FFD24A"/>
</svg>"""

# ─────────────────────────── انیمیشن خون ───────────────────────────
BLOOD_HTML = """<div class="bl-wrap" aria-hidden="true">
<div class="bl-drips">
<i style="left:9%;--h:26px;animation-delay:.2s"></i>
<i style="left:21%;--h:17px;animation-delay:1.5s"></i>
<i style="left:33%;--h:30px;animation-delay:.8s"></i>
<i style="left:47%;--h:21px;animation-delay:2.4s"></i>
<i style="left:60%;--h:28px;animation-delay:1.1s"></i>
<i style="left:73%;--h:19px;animation-delay:3.1s"></i>
<i style="left:86%;--h:25px;animation-delay:1.9s"></i>
</div>
<svg class="bl-wave" viewBox="0 0 1200 70" preserveAspectRatio="none">
<defs><linearGradient id="blGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C01818"/><stop offset="1" stop-color="#4A0808"/></linearGradient></defs>
<g class="bwg b-slow"><path fill="#5C0A0A" d="M0 30 q37.5 -13 75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 V70 H0 Z"/><path fill="#5C0A0A" transform="translate(1200,0)" d="M0 30 q37.5 -13 75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 V70 H0 Z"/></g>
<g class="bwg"><path fill="url(#blGrad)" d="M0 44 q37.5 12 75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 V70 H0 Z"/><path fill="url(#blGrad)" transform="translate(1200,0)" d="M0 44 q37.5 12 75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 t75 0 V70 H0 Z"/></g>
</svg>
<div class="bl-cap">ORA</div>
</div>"""

# CSS مشترک لوگو + خون
_ORA_CSS = """
.ora-logo{display:block;filter:drop-shadow(0 0 10px rgba(255,90,20,.28))}
.ora-logo .ring{transform-box:fill-box;transform-origin:center}
.ora-logo .r1{animation:oraCW 14s linear infinite}
.ora-logo .r2{animation:oraCCW 9s linear infinite}
.ora-logo .r3{animation:oraCW 24s linear infinite}
@keyframes oraCW{to{transform:rotate(360deg)}}
@keyframes oraCCW{to{transform:rotate(-360deg)}}
.ora-logo .pupil{transform-box:fill-box;transform-origin:center;animation:oraFlick 1.9s ease-in-out infinite}
.ora-logo .p2{animation-delay:.35s}
@keyframes oraFlick{0%,100%{opacity:.7;transform:scale(1)}18%{opacity:1;transform:scale(1.3)}46%{opacity:.55}72%{opacity:.95;transform:scale(1.12)}}
.ora-logo .flame{transform-box:fill-box;transform-origin:50% 100%;animation:oraFlame 1.7s ease-in-out infinite}
.ora-logo .k2{animation-delay:.25s}.ora-logo .k3{animation-delay:.5s}.ora-logo .f2{animation-delay:.15s}
@keyframes oraFlame{0%,100%{transform:scale(1,1);opacity:.95}32%{transform:scale(.93,1.16)}58%{transform:scale(1.05,.9);opacity:.8}}
.ora-logo .spark{opacity:0;animation:oraSpark 2.6s linear infinite}
.ora-logo .s2{animation-delay:.9s}.ora-logo .s3{animation-delay:1.7s}
@keyframes oraSpark{0%{opacity:0;transform:translateY(2px)}14%{opacity:1}100%{opacity:0;transform:translateY(-16px)}}
.bl-wrap{display:flex;flex-direction:column;align-items:center;pointer-events:none;user-select:none}
.bl-drips{position:relative;width:100%;height:0}
.bl-drips i{position:absolute;top:0;width:3px;height:0;border-radius:0 0 3px 3px;background:linear-gradient(180deg,rgba(139,16,16,0),#8B1010 35%,#A11212);animation:blGrow 4.6s ease-in infinite}
.bl-drips i::after{content:'';position:absolute;left:50%;bottom:-8px;width:9px;height:12px;transform:translateX(-50%);background:radial-gradient(circle at 35% 28%,#D02525,#7A0D0D 70%);border-radius:50% 50% 58% 58%/62% 62% 44% 44%;box-shadow:0 0 10px rgba(179,18,18,.8),inset 0 -2px 3px rgba(0,0,0,.4);opacity:0;animation:blFall 4.6s ease-in infinite}
@keyframes blGrow{0%{height:0}36%{height:var(--h,24px)}100%{height:var(--h,24px)}}
@keyframes blFall{0%,38%{opacity:0;transform:translate(-50%,0)}46%{opacity:1}88%{opacity:1}100%{opacity:0;transform:translate(-50%,54px)}}
.bl-wave{width:100%;height:56px;display:block;filter:drop-shadow(0 -3px 16px rgba(179,18,18,.35))}
.bwg{animation:blFlow 15s linear infinite}
.bwg.b-slow{animation-duration:27s;opacity:.55}
@keyframes blFlow{to{transform:translateX(-1200px)}}
.bl-cap{font-family:'Cinzel',serif;font-size:9px;letter-spacing:.55em;text-indent:.55em;color:rgba(179,18,18,.55);text-shadow:0 0 10px rgba(179,18,18,.4);margin-top:2px}
"""

# ═══════════════════════════════ صفحه ورود (LOGIN) ═══════════════════════════════
_LOGIN_TPL = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · ORA</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050303;--fire:#FF5A1F;--fire2:#FF8A3C;--fire3:#FFC93C;--blood:#A11212;--card:rgba(18,9,7,.72);--bord:rgba(255,90,20,.16);--bordH:rgba(255,90,20,.45);--gd:rgba(255,80,20,.08);--t1:#EFE2D0;--t2:#C4AE97;--t3:#8A7462;--red:#FF7B72}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px}
.bg{position:fixed;inset:0;background:radial-gradient(900px 500px at 50% -10%,rgba(255,90,20,.1),transparent 60%),radial-gradient(700px 500px at 88% 112%,rgba(179,18,18,.07),transparent 60%),var(--bg);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(255,90,20,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,90,20,.05) 1px,transparent 1px);background-size:44px 44px;-webkit-mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,#000 30%,transparent 75%);mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,#000 30%,transparent 75%);z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(90px);z-index:0;animation:fl 9s ease-in-out infinite}
.o1{width:380px;height:380px;background:rgba(255,90,20,.08);top:-100px;right:-80px}
.o2{width:280px;height:280px;background:rgba(179,18,18,.07);bottom:-60px;left:-60px;animation-delay:4s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
.wrap{position:relative;z-index:10;width:100%;max-width:410px}
.card{background:linear-gradient(165deg,rgba(28,13,9,.85),rgba(9,4,3,.94));border:1px solid var(--bord);border-radius:26px;padding:36px 32px 30px;backdrop-filter:blur(22px);box-shadow:0 30px 90px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,138,60,.08);position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:62%;height:1px;background:linear-gradient(90deg,transparent,rgba(255,138,60,.75),transparent)}
.brand{text-align:center;margin-bottom:22px}
.brand .ora-logo{width:112px;height:112px;margin:0 auto 12px}
.brand-name{font-family:'Cinzel',serif;font-size:26px;font-weight:900;letter-spacing:.32em;text-indent:.32em;background:linear-gradient(135deg,#FFD9A0,#FF7A2E 45%,#B31212);-webkit-background-clip:text;background-clip:text;color:transparent}
.brand-sub{font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:.42em;text-indent:.42em;color:var(--t3);margin-top:6px}
h1{font-size:18px;font-weight:700;color:var(--t1);text-align:center;margin-bottom:5px}
.sub{font-size:12px;color:var(--t2);text-align:center;margin-bottom:22px;line-height:1.7}
.hint{display:flex;align-items:center;gap:10px;background:var(--gd);border:1px solid var(--bord);border-radius:12px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--t3);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--fire2);background:rgba(255,90,20,.1);border:1px solid rgba(255,90,20,.3);padding:3px 12px;border-radius:8px;cursor:pointer;transition:.15s;letter-spacing:.12em;direction:ltr}
.hint-val:hover{background:rgba(255,90,20,.22)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--t3);margin-bottom:7px;letter-spacing:.08em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 16px;border-radius:12px;border:1px solid var(--bord);background:rgba(0,0,0,.4);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:.2s}
input[type=password]:focus{border-color:rgba(255,106,0,.55);box-shadow:0 0 0 3px rgba(255,90,20,.13)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:18px;pointer-events:none;transition:.2s}
input:focus+.ic{color:var(--fire2)}
.err{display:none;background:rgba(229,72,77,.08);border:1px solid rgba(229,72,77,.25);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:var(--red);align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:13px;border-radius:12px;border:none;cursor:pointer;background:linear-gradient(135deg,#FFC93C,#FF6A00 55%,#B31212);color:#1A0703;font-family:inherit;font-size:14px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 6px 24px rgba(255,90,20,.3),inset 0 1px 0 rgba(255,255,255,.35);transition:.2s;position:relative}
.btn:hover{filter:brightness(1.08)}
.btn:disabled{opacity:.55;cursor:not-allowed}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--bord);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--t3)}
.footer a{color:var(--fire2);font-weight:700;text-decoration:none;display:flex;align-items:center;gap:4px}
@keyframes spin{to{transform:rotate(360deg)}}
.bl-wrap{position:fixed;left:0;right:0;bottom:0;z-index:5;padding:34px 0 0;background:linear-gradient(180deg,transparent,rgba(6,3,2,.95) 45%)}
__ORA_CSS__
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="orb o1"></div><div class="orb o2"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">__LOGO_SVG__<div class="brand-name">ORA</div><div class="brand-sub">DARK EDITION · VIP PANEL</div></div>
    <h1>ورود به پنل</h1>
    <p class="sub">برای دسترسی به داشبورد، رمز عبور را وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">رمز پیش‌فرض سیستم</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='OMID';document.getElementById('pw').focus()">OMID</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-flame ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer">پشتیبانی <a href="https://t.me/omiddemon" target="_blank"><i class="ti ti-brand-telegram"></i>@omiddemon</a></div>
  </div>
</div>
__BLOOD__
<script>
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""

# ═══════════════════════════════ داشبورد (DASHBOARD) ═══════════════════════════════
_DASH_TPL = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ORA · پنل مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&family=Cinzel:wght@700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050303;--bg2:#0A0505;--bg3:#130705;--card:rgba(20,10,8,.72);--card2:rgba(28,13,9,.85);--bord:rgba(255,90,20,.16);--bordH:rgba(255,90,20,.42);--gd:rgba(255,80,20,.08);--fire:#FF5A1F;--fire2:#FF8A3C;--fire3:#FFC93C;--blood:#A11212;--t1:#EFE2D0;--t2:#C4AE97;--t3:#8A7462;--green-t:#7DDFA8;--red-t:#FF7B72;--amber-t:#FFB35C;--sb-w:250px;--rad:16px;--sh:0 10px 40px rgba(0,0,0,.5)}
[data-theme="light"]{--bg:#E9E1D4;--bg2:#E1D8C8;--bg3:#D8CCB8;--card:rgba(252,248,240,.88);--card2:#FFFDF7;--bord:rgba(140,60,20,.28);--bordH:rgba(140,60,20,.55);--gd:rgba(140,60,20,.09);--t1:#241610;--t2:#6B5443;--t3:#9A8570;--green-t:#1E7A4F;--red-t:#A32020;--amber-t:#8A5E0F;--sh:0 8px 30px rgba(90,40,10,.12)}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:radial-gradient(900px 500px at 80% -10%,rgba(255,90,20,.06),transparent 60%),var(--bg);color:var(--t1);min-height:100vh;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:rgba(255,90,20,.25);border-radius:3px}
a{color:inherit;text-decoration:none}
.bgfix{position:fixed;inset:0;pointer-events:none;background-image:linear-gradient(rgba(255,90,20,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,90,20,.035) 1px,transparent 1px);background-size:44px 44px;z-index:0}
.sidebar{width:var(--sb-w);min-height:100vh;background:linear-gradient(180deg,var(--bg2),var(--bg));border-left:1px solid var(--bord);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s}
.logo{display:flex;align-items:center;gap:11px;padding:18px 16px 14px;border-bottom:1px solid var(--bord);position:relative}
.logo .ora-logo{width:42px;height:42px;flex-shrink:0}
.logo-name{font-family:'Cinzel',serif;font-size:15px;font-weight:900;letter-spacing:.26em;background:linear-gradient(135deg,#FFD9A0,#FF7A2E 45%,#B31212);-webkit-background-clip:text;background-clip:text;color:transparent}
.logo-sub{font-size:9px;color:var(--t3);letter-spacing:.2em;margin-top:2px;font-family:'Cinzel',serif}
.sb-close{display:none;position:absolute;left:12px;top:18px;background:var(--gd);border:1px solid var(--bord);color:var(--t2);width:28px;height:28px;border-radius:8px;font-size:14px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 16px 4px;font-size:9px;letter-spacing:.16em;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 8px;border-radius:9px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--gd);color:var(--t2)}
.nav-it.on{background:var(--gd);color:var(--fire2);border-right-color:var(--fire);font-weight:700}
.nav-it.on i{color:var(--fire3)}
.nav-badge{margin-right:auto;background:var(--gd);border:1px solid var(--bord);color:var(--fire2);font-size:9px;padding:1px 7px;border-radius:20px;font-weight:700;min-width:20px;text-align:center}
.sb-foot{padding:12px 14px;border-top:1px solid var(--bord)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:54px;background:var(--bg2);border-bottom:1px solid var(--bord);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-top .ora-logo{width:30px;height:30px}
.mob-title{font-family:'Cinzel',serif;font-size:13px;font-weight:900;letter-spacing:.24em;color:var(--fire2)}
.menu-btn{background:var(--gd);border:1px solid var(--bord);color:var(--fire2);width:34px;height:34px;border-radius:9px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sb-w);flex:1;padding:26px 26px 40px;min-width:0;position:relative;z-index:1}
.pg{display:none}.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:800;display:flex;align-items:center;gap:9px}
.tb-title i{color:var(--fire);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10.5px;padding:4px 12px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:6px;border:1px solid var(--bord);background:var(--gd);color:var(--fire2)}
.dot{width:7px;height:7px;border-radius:50%;display:inline-block;flex-shrink:0}
.dg{background:#3ECF8E}.dr{background:#E5484D}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:16px}
.metric{background:var(--card);border:1px solid var(--bord);border-radius:var(--rad);padding:17px;transition:.2s;position:relative;overflow:hidden;backdrop-filter:blur(10px)}
.metric::before{content:'';position:absolute;top:0;right:0;width:100%;height:2px;background:linear-gradient(90deg,var(--fire),transparent 70%);opacity:.55}
.metric:hover{border-color:var(--bordH);transform:translateY(-2px);box-shadow:var(--sh)}
.m-icon{width:36px;height:36px;border-radius:10px;background:var(--gd);display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--fire2);font-size:17px;border:1px solid var(--bord)}
.m-icon.suc{color:var(--green-t);background:rgba(62,207,142,.08);border-color:rgba(62,207,142,.2)}
.m-icon.dan{color:var(--red-t);background:rgba(229,72,77,.08);border-color:rgba(229,72,77,.2)}
.m-icon.amb{color:var(--amber-t);background:rgba(229,168,62,.08);border-color:rgba(229,168,62,.2)}
.m-val{font-size:25px;font-weight:800;line-height:1;background:linear-gradient(135deg,#FFD9A0,#FF7A2E 45%,#B31212);-webkit-background-clip:text;background-clip:text;color:transparent;display:flex;align-items:baseline;gap:5px}
[data-theme="light"] .m-val{background:linear-gradient(135deg,#8a2c0c,#B3400F);-webkit-background-clip:text;background-clip:text}
.m-unit{font-size:11px;font-weight:500;-webkit-text-fill-color:var(--t3);color:var(--t3)}
.m-label{font-size:10.5px;color:var(--t3);margin-top:7px;font-weight:600}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.card{background:var(--card);border:1px solid var(--bord);border-radius:var(--rad);padding:18px 20px;transition:border-color .2s;backdrop-filter:blur(10px)}
.card:hover{border-color:var(--bordH)}
.card-title{font-size:12.5px;font-weight:700;margin-bottom:15px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:16px;color:var(--fire)}
.ml-auto{margin-right:auto}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(255,90,20,.07);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:7px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{font-weight:700;font-size:11.5px;color:var(--t1)}
.mono{font-family:ui-monospace,monospace;direction:ltr}
.ch-lg{position:relative;height:320px}
.ch{position:relative;height:230px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700}
.ec-ok{background:rgba(62,207,142,.1);color:var(--green-t)}
.ec-warn{background:rgba(229,168,62,.1);color:var(--amber-t)}
.ec-exp{background:rgba(229,72,77,.1);color:var(--red-t)}
.btn{font-family:inherit;font-size:12.5px;font-weight:700;border-radius:11px;padding:10px 16px;cursor:pointer;border:none;display:inline-flex;align-items:center;justify-content:center;gap:7px;transition:.18s;white-space:nowrap}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-p{background:linear-gradient(135deg,#FFC93C,#FF6A00 55%,#B31212);color:#1A0703;box-shadow:0 6px 22px rgba(255,90,20,.28),inset 0 1px 0 rgba(255,255,255,.35)}
.btn-p:hover{filter:brightness(1.08);transform:translateY(-1px)}
.btn-o{background:transparent;border:1px solid var(--bord);color:var(--t2)}
.btn-o:hover{border-color:var(--bordH);color:var(--fire2);background:var(--gd)}
.btn-d{background:rgba(229,72,77,.12);border:1px solid rgba(229,72,77,.3);color:var(--red-t)}
.btn-d:hover{background:rgba(229,72,77,.22)}
.btn.tg{background:linear-gradient(135deg,#2AABEE,#1D86C7);color:#fff}
.btn.full{width:100%;margin-top:10px}
.btn-sm{padding:6px 11px;font-size:11px;border-radius:9px}
.btn-icon{width:30px;height:30px;padding:0;border-radius:8px;background:var(--gd);color:var(--fire2);border:1px solid var(--bord);display:inline-flex;align-items:center;justify-content:center;cursor:pointer;font-size:14px;transition:.15s}
.btn-icon:hover{border-color:var(--bordH);color:var(--fire3);background:rgba(255,90,20,.16)}
.btn-icon.danger{color:var(--red-t);border-color:rgba(229,72,77,.25)}
.btn-icon.danger:hover{background:rgba(229,72,77,.14)}
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:16px}
.traf-main{background:linear-gradient(155deg,var(--bg3),var(--card) 70%);border:1px solid var(--bord);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--gd),transparent 70%);pointer-events:none}
.tml{font-size:10.5px;color:var(--t3);font-weight:700;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px}
.tml i{color:var(--fire)}
.tmv{font-size:33px;font-weight:800;background:linear-gradient(135deg,#FFD9A0,#FF7A2E 45%,#B31212);-webkit-background-clip:text;background-clip:text;color:transparent;display:flex;align-items:baseline;gap:6px}
[data-theme="light"] .tmv{background:linear-gradient(135deg,#8a2c0c,#B3400F);-webkit-background-clip:text;background-clip:text}
.tmv span{font-size:14px;font-weight:500;-webkit-text-fill-color:var(--t3);color:var(--t3)}
.trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 11px;border-radius:20px;margin-top:12px;background:rgba(62,207,142,.1);color:var(--green-t)}
.traf-mini{background:var(--card);border:1px solid var(--bord);border-radius:20px;padding:18px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s}
.traf-mini:hover{border-color:var(--bordH);transform:translateY(-2px)}
.tmi-ic{width:32px;height:32px;border-radius:9px;background:var(--gd);color:var(--fire2);display:flex;align-items:center;justify-content:center;font-size:15px;border:1px solid var(--bord);margin-bottom:12px}
.tmv2{font-size:21px;font-weight:800}
.tml2{font-size:9.5px;color:var(--t3);font-weight:700;letter-spacing:.06em;margin-top:4px}
.tcard{margin-bottom:0}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;flex-wrap:wrap;gap:10px}
.ct-title{font-size:14px;font-weight:800;display:flex;align-items:center;gap:8px}
.ct-title i{color:var(--fire)}
.ct-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.rtabs{display:flex;gap:4px;background:var(--gd);padding:3px;border-radius:10px;border:1px solid var(--bord)}
.rtab{padding:6px 14px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.rtab.on{background:linear-gradient(135deg,#FFC93C,#B3400F);color:#1A0703;box-shadow:0 2px 10px rgba(255,90,20,.3)}
.searchrow{display:flex;align-items:center;gap:9px;background:var(--card);border:1px solid var(--bord);border-radius:12px;padding:10px 14px;margin-bottom:14px}
.searchrow input{flex:1;background:none;border:none;outline:none;color:var(--t1);font-family:inherit;font-size:13px}
.searchrow i{color:var(--t3)}
.lclist{display:flex;flex-direction:column;gap:12px}
.lcard{background:var(--card);border:1px solid var(--bord);border-radius:var(--rad);padding:16px 18px;transition:.2s}
.lcard:hover{border-color:var(--bordH)}
.lcard.off{opacity:.55}
.lc-head{display:flex;align-items:center;gap:10px;margin-bottom:11px;flex-wrap:wrap}
.lc-name{font-weight:700;font-size:13.5px;display:flex;align-items:center;gap:8px}
.lc-actions{margin-right:auto;display:flex;gap:6px;flex-wrap:wrap}
.chip{font-size:9.5px;padding:3px 9px;border-radius:20px;background:var(--gd);border:1px solid var(--bord);color:var(--t2);display:inline-flex;align-items:center;gap:4px;font-weight:600;white-space:nowrap}
.chip-gold{color:var(--fire2);border-color:rgba(255,90,20,.4)}
.chip-ok{color:var(--green-t);border-color:rgba(62,207,142,.3)}
.chip-exp{color:var(--red-t);border-color:rgba(229,72,77,.3)}
.lc-badges{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:11px}
.lc-usage{margin-bottom:8px}
.ubar{height:6px;border-radius:6px;background:rgba(0,0,0,.4);overflow:hidden;border:1px solid rgba(255,90,20,.1)}
.ubar i{display:block;height:100%;background:linear-gradient(90deg,#8B1010,#FF6A00,#FFC93C);border-radius:6px;transition:width .4s;box-shadow:0 0 8px rgba(255,106,0,.45)}
.utxt{font-size:10.5px;color:var(--t3);margin-top:6px}
.lc-note{font-size:11px;color:var(--t3);margin-top:8px;padding-top:8px;border-top:1px dashed rgba(255,90,20,.12)}
.sicon{width:34px;height:34px;border-radius:10px;background:var(--gd);border:1px solid var(--bord);color:var(--fire2);display:flex;align-items:center;justify-content:center;font-size:16px}
.gold{color:var(--fire2)}
.urlrow{display:flex;align-items:center;gap:8px;background:rgba(0,0,0,.3);border:1px solid var(--bord);border-radius:10px;padding:8px 12px;margin-top:8px}
[data-theme="light"] .urlrow{background:rgba(140,60,20,.06)}
.urltext{flex:1;font-family:ui-monospace,monospace;font-size:10.5px;color:var(--fire2);direction:ltr;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tscroll{overflow-x:auto}
.tgrid{min-width:680px}
.thead,.trow{display:grid;grid-template-columns:1.2fr 1.4fr .5fr .8fr 1fr 1fr;gap:8px;align-items:center}
.thead{font-size:9.5px;font-weight:700;color:var(--t3);letter-spacing:.06em;padding:0 10px 10px;border-bottom:1px solid var(--bord)}
.trow{padding:11px 10px;border-bottom:1px solid rgba(255,90,20,.06);font-size:11.5px}
.trow:last-child{border-bottom:none}
.cip{font-family:ui-monospace,monospace;direction:ltr;text-align:right;color:var(--fire2);font-weight:600}
.lgrow{display:flex;align-items:center;gap:11px;padding:11px 12px;border-bottom:1px solid rgba(255,90,20,.06);font-size:12px}
.lgrow:last-child{border-bottom:none}
.lgrow>i{width:30px;height:30px;border-radius:9px;background:var(--gd);border:1px solid var(--bord);color:var(--fire2);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lgrow.err>i{color:var(--red-t);border-color:rgba(229,72,77,.3);background:rgba(229,72,77,.08)}
.lgrow.ok>i{color:var(--green-t);border-color:rgba(62,207,142,.3);background:rgba(62,207,142,.08)}
.lgrow.warn>i{color:var(--amber-t);border-color:rgba(229,168,62,.3);background:rgba(229,168,62,.08)}
.lgmsg{flex:1;color:var(--t1)}
.lgtime{font-size:10px;color:var(--t3);font-family:ui-monospace,monospace;direction:ltr}
.modal{position:fixed;inset:0;background:rgba(3,1,1,.75);backdrop-filter:blur(6px);z-index:300;display:none;align-items:center;justify-content:center;padding:18px}
.modal.show{display:flex}
.modal-card{width:100%;max-width:580px;max-height:88vh;overflow-y:auto;background:linear-gradient(165deg,#1A0C07,#0A0403);border:1px solid var(--bordH);border-radius:20px;padding:22px;box-shadow:0 30px 90px rgba(0,0,0,.75)}
[data-theme="light"] .modal-card{background:linear-gradient(165deg,#FFFDF7,#F1E8D8)}
.modal-title{font-size:14px;font-weight:800;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--fire)}
.modal-foot{display:flex;gap:8px;margin-top:18px;justify-content:flex-end}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.fg{display:flex;flex-direction:column;gap:6px}
.fg.full{grid-column:1/-1}
.fg label{font-size:10px;color:var(--t3);font-weight:700;letter-spacing:.05em}
.fg input,.fg select{background:rgba(0,0,0,.38);border:1px solid var(--bord);border-radius:10px;padding:10px 12px;color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;width:100%}
[data-theme="light"] .fg input,[data-theme="light"] .fg select{background:rgba(255,255,255,.75)}
.fg input:focus,.fg select:focus{border-color:rgba(255,106,0,.5)}
.fg input[dir="ltr"]{text-align:left;font-family:ui-monospace,monospace}
select option{background:#130705;color:var(--t1)}
[data-theme="light"] select option{background:#FFFDF7;color:#241610}
.mrow{display:flex;align-items:center;gap:10px;padding:10px 12px;border:1px solid var(--bord);border-radius:10px;margin-bottom:8px;cursor:pointer;font-size:12px}
.mrow input{accent-color:#FF5A1F;width:16px;height:16px}
.qrbox{display:flex;flex-direction:column;align-items:center;gap:12px;padding:10px 0}
.qrbox img{width:260px;height:260px;border-radius:14px;border:1px solid var(--bordH);background:#fff;padding:8px}
#toasts{position:fixed;bottom:18px;left:18px;z-index:400;display:flex;flex-direction:column;gap:8px}
.toast{background:rgba(20,9,6,.96);border:1px solid var(--bordH);color:var(--t1);padding:10px 16px;border-radius:12px;font-size:12px;display:flex;align-items:center;gap:8px;transform:translateY(12px);opacity:0;transition:.25s;box-shadow:0 8px 30px rgba(0,0,0,.55)}
[data-theme="light"] .toast{background:#FFFDF7;border-color:var(--bordH)}
.toast.show{transform:none;opacity:1}
.toast.err{border-color:rgba(229,72,77,.5);color:var(--red-t)}
.toast i{color:var(--fire3)}
.empty{padding:34px;text-align:center;color:var(--t3);font-size:12px}
.main .bl-wrap{position:static;opacity:.5;margin:36px 0 4px;padding:6px 0 0;background:none}
.main .bl-drips{display:none}
/* ── Clean IPs ── */
.cip-add,.cip-bulk{display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap}
.cip-add input{flex:1;min-width:170px;background:rgba(0,0,0,.38);border:1px solid var(--bord);border-radius:10px;padding:10px 12px;color:var(--t1);font-family:inherit;font-size:12.5px;outline:none}
.cip-add input:focus{border-color:rgba(255,106,0,.5)}
.cip-add input[dir="ltr"]{text-align:left;font-family:ui-monospace,monospace}
.cip-bulk{align-items:stretch}
.cip-bulk textarea{flex:1;background:rgba(0,0,0,.38);border:1px solid var(--bord);border-radius:10px;padding:10px 12px;color:var(--t1);font-family:ui-monospace,monospace;font-size:12px;outline:none;resize:vertical;direction:ltr;text-align:left;min-width:200px}
.cip-bulk textarea:focus{border-color:rgba(255,106,0,.5)}
[data-theme="light"] .cip-add input,[data-theme="light"] .cip-bulk textarea{background:rgba(255,255,255,.75)}
.cip-list{display:flex;flex-direction:column;gap:8px;margin-top:6px}
.cip-item{display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.3);border:1px solid var(--bord);border-radius:12px;padding:9px 14px;flex-wrap:wrap}
[data-theme="light"] .cip-item{background:rgba(140,60,20,.06)}
.cip-item .ci-dot{width:8px;height:8px;border-radius:50%;background:var(--fire);box-shadow:0 0 8px rgba(255,90,20,.55);flex-shrink:0}
.cip-item .ci-ip{font-family:ui-monospace,monospace;direction:ltr;font-size:12.5px;color:var(--fire2);font-weight:700}
.cip-item .ci-label{font-size:11px;color:var(--t3)}
.cip-item .ci-ms{font-size:10.5px;font-family:ui-monospace,monospace;direction:ltr;color:var(--t3)}
.cip-item .ci-actions{margin-right:auto;display:flex;gap:6px}
@media(max-width:1080px){.metrics{grid-template-columns:1fr 1fr}.traf-hero{grid-template-columns:1fr 1fr}.g3{grid-template-columns:1fr}}
@media(max-width:860px){
 .sidebar{transform:translateX(100%)}.sidebar.open{transform:none;box-shadow:-20px 0 60px rgba(0,0,0,.6)}
 .sb-close{display:flex}.mob-top{display:flex}
 .main{margin-right:0;padding:70px 14px 30px}.metrics{grid-template-columns:1fr 1fr}.traf-hero{grid-template-columns:1fr}.g2{grid-template-columns:1fr}.fgrid{grid-template-columns:1fr}
}
@media(max-width:520px){.metrics{grid-template-columns:1fr}.ch-lg{height:250px}}
__ORA_CSS__
</style>
</head>
<body>
<div class="bgfix"></div>
<aside class="sidebar" id="sb">
  <div class="logo">__LOGO_SVG__<div><div class="logo-name">ORA</div><div class="logo-sub">DARK PANEL · v11.4</div></div><button class="sb-close" id="sbClose"><i class="ti ti-x"></i></button></div>
  <nav class="nav-wrap">
    <div class="nav-sec">مدیریت</div>
    <a class="nav-it on" data-pg="dash"><i class="ti ti-layout-dashboard"></i>داشبورد</a>
    <a class="nav-it" data-pg="traffic"><i class="ti ti-chart-area-line"></i>ترافیک</a>
    <a class="nav-it" data-pg="links"><i class="ti ti-link"></i>کانفیگ‌ها<span class="nav-badge" id="nbLinks">0</span></a>
    <a class="nav-it" data-pg="subs"><i class="ti ti-users-group"></i>گروه‌های ساب<span class="nav-badge" id="nbSubs">0</span></a>
    <a class="nav-it" data-pg="conns"><i class="ti ti-access-point"></i>اتصالات زنده<span class="nav-badge" id="nbConns">0</span></a>
    <div class="nav-sec">سیستم</div>
    <a class="nav-it" data-pg="logs"><i class="ti ti-history"></i>لاگ فعالیت</a>
    <a class="nav-it" data-pg="settings"><i class="ti ti-settings"></i>تنظیمات</a>
  </nav>
  <div class="sb-foot">
    <a class="btn tg full" style="margin:0 0 8px" href="https://t.me/omiddemon" target="_blank"><i class="ti ti-brand-telegram"></i>کانال پشتیبانی</a>
    <button class="btn btn-d full" style="margin:0" id="btnLogout"><i class="ti ti-logout"></i>خروج</button>
  </div>
</aside>
<div class="overlay" id="ov"></div>
<header class="mob-top">
  <div class="ml">__LOGO_SVG__<span class="mob-title">ORA</span></div>
  <button class="menu-btn" id="sbOpen"><i class="ti ti-menu-2"></i></button>
</header>
<main class="main">

<section class="pg on" id="pg-dash">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-flame"></i>داشبورد</div><div class="tb-sub">نمای کلی سیستم در یک نگاه</div></div>
    <div class="tb-right"><span class="badge"><i class="ti ti-clock"></i><span id="bUptime">--:--:--</span></span><span class="badge" style="color:var(--green-t);border-color:rgba(62,207,142,.3)"><span class="dot dg pulse"></span>آنلاین</span></div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-access-point"></i></div><div class="m-val"><span id="mConns">0</span></div><div class="m-label">اتصالات زنده</div></div>
    <div class="metric"><div class="m-icon suc"><i class="ti ti-arrows-exchange"></i></div><div class="m-val"><span id="mTraffic">0</span><span class="m-unit">MB</span></div><div class="m-label">ترافیک کل</div></div>
    <div class="metric"><div class="m-icon amb"><i class="ti ti-link"></i></div><div class="m-val"><span id="mLinks">0</span></div><div class="m-label">کانفیگ فعال / کل</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-users-group"></i></div><div class="m-val"><span id="mSubs">0</span></div><div class="m-label">گروه‌های ساب</div></div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-bar"></i>ترافیک ساعتی<span class="ml-auto"></span><span class="tb-sub" style="margin:0">MB</span></div><div class="ch-lg"><canvas id="chHourly"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-server"></i>وضعیت سیستم</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-world"></i>میزبان</span><span class="sr-v mono" id="sysHost">--</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-arrows-transfer-up"></i>کل درخواست‌ها</span><span class="sr-v" id="sysReq">0</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-alert-triangle"></i>خطاها</span><span class="sr-v" id="sysErr">0</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-versions"></i>نسخه</span><span class="sr-v">ORA v11.4</span></div>
    </div>
  </div>
  <div class="card"><div class="card-title"><i class="ti ti-history"></i>آخرین رویدادها</div><div id="dashRecent"></div></div>
</section>

<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area-line"></i>ترافیک</div><div class="tb-sub">آمار مصرف و پرفورمنس سیستم</div></div>
    <div class="tb-right"><span class="badge"><i class="ti ti-clock"></i><span id="tUp">--</span></span></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main"><div class="tml"><i class="ti ti-arrows-exchange"></i>کل ترافیک منتقل‌شده</div><div class="tmv"><span id="thTraffic">0</span><span>MB</span></div><div class="trend"><i class="ti ti-trending-up"></i>زنده</div></div>
    <div class="traf-mini"><div class="tmi-ic"><i class="ti ti-access-point"></i></div><div class="tmv2" id="thConns">0</div><div class="tml2">اتصالات زنده</div></div>
    <div class="traf-mini"><div class="tmi-ic"><i class="ti ti-arrows-transfer-up"></i></div><div class="tmv2" id="thReq">0</div><div class="tml2">کل درخواست‌ها</div></div>
    <div class="traf-mini"><div class="tmi-ic"><i class="ti ti-alert-triangle"></i></div><div class="tmv2" id="thErr">0</div><div class="tml2">خطاها</div></div>
  </div>
  <div class="card tcard">
    <div class="traf-chart-head">
      <div><div class="ct-title"><i class="ti ti-chart-line"></i>نمودار ترافیک ساعتی</div><div class="ct-sub">بر اساس ساعت تهران</div></div>
      <div class="rtabs"><button class="rtab" data-r="12">۱۲ ساعت</button><button class="rtab on" data-r="24">۲۴ ساعت</button><button class="rtab" data-r="all">همه</button></div>
    </div>
    <div class="ch-lg"><canvas id="chTraffic"></canvas></div>
  </div>
</section>

<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link"></i>کانفیگ‌ها</div><div class="tb-sub"><span id="linksCount">0</span> کانفیگ ثبت شده</div></div>
    <div class="tb-right"><button class="btn btn-o" id="btnSubAll"><i class="ti ti-stack-2"></i>ساب همه</button><button class="btn btn-p" id="btnNewLink"><i class="ti ti-plus"></i>کانفیگ جدید</button></div>
  </div>
  <div class="searchrow"><i class="ti ti-search"></i><input id="linkSearch" placeholder="جستجو در کانفیگ‌ها..."></div>
  <div id="linksList" class="lclist"></div>
</section>

<section class="pg" id="pg-subs">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-users-group"></i>گروه‌های ساب</div><div class="tb-sub">لینک ساب حرفه‌ای برای مجموعه‌ای از کانفیگ‌ها</div></div>
    <div class="tb-right"><button class="btn btn-p" id="btnNewSub"><i class="ti ti-plus"></i>گروه جدید</button></div>
  </div>
  <div id="subsList" class="lclist"></div>
</section>

<section class="pg" id="pg-conns">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-access-point"></i>اتصالات زنده</div><div class="tb-sub">گروه‌بندی‌شده بر اساس آی‌پی · بروزرسانی خودکار</div></div>
    <div class="tb-right"><span class="badge"><i class="ti ti-world"></i>آی‌پی یکتا: <b id="cCount">0</b></span><span class="badge"><i class="ti ti-plug"></i>اتصال: <b id="cRaw">0</b></span></div>
  </div>
  <div class="card"><div class="tscroll"><div class="tgrid">
    <div class="thead"><div>آی‌پی</div><div>کانفیگ</div><div>سشن</div><div>ترافیک</div><div>آخرین فعالیت</div><div>ترابرد</div></div>
    <div id="connsBody"></div>
  </div></div></div>
</section>

<section class="pg" id="pg-logs">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-history"></i>لاگ فعالیت</div><div class="tb-sub">رویدادهای سیستم، ورودها و تغییرات کانفیگ‌ها</div></div>
  </div>
  <div class="card"><div id="logsList"></div></div>
</section>

<section class="pg" id="pg-settings">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-settings"></i>تنظیمات</div><div class="tb-sub">امنیت، آی‌پی‌های تمیز، پوسته و پشتیبانی</div></div>
  </div>

  <div class="card" style="margin-bottom:13px">
    <div class="card-title"><i class="ti ti-world-wind"></i>آی‌پی‌های تمیز (Clean IPs)<span class="ml-auto"></span><span class="chip chip-gold" id="cipBadge">0 آی‌پی</span><button class="btn-icon danger" title="پاک کردن همه" onclick="clearCips()"><i class="ti ti-trash"></i></button></div>
    <div id="cipWarn" style="display:none;background:rgba(229,72,77,.1);border:1px solid rgba(229,72,77,.4);border-radius:12px;padding:12px 16px;margin-bottom:12px;color:var(--red-t);font-size:12px;line-height:1.9">
      <b>⚠️ بک‌اند قدیمی است!</b> مسیر <span class="mono">/api/clean-ips</span> روی سرور پیدا نشد؛ یعنی فایل <b>main.py</b> جدید هنوز دیپلوی نشده. فایل main.py نسخه 11.4 را کامل جایگزین کن، Deploy بگیر و با Ctrl+Shift+R رفرش کن.
    </div>
    <div class="tb-sub" style="margin:0 0 14px">کلاینت به این آی‌پی وصل می‌شود ولی Host/SNI همان دامنه‌ی اصلی پنل می‌ماند. در حالت «مولتی»، برای هر کانفیگ به‌ازای همه‌ی آی‌پی‌های تمیز یک لینک جدا داخل فایل ساب ساخته می‌شود.</div>
    <div class="cip-add">
      <input id="cipIp" dir="ltr" placeholder="Clean IP — 172.67.1.1 یا [2606:4700::] یا mirror.site.com">
      <input id="cipLabel" placeholder="برچسب (اختیاری)">
      <button class="btn btn-p" id="btnCipAdd"><i class="ti ti-plus"></i>افزودن</button>
    </div>
    <div class="cip-bulk">
      <textarea id="cipBulk" rows="3" dir="ltr" placeholder="ورود گروهی — هر خط یک آی‌پی (اختیاری: با کاما برچسب)&#10;172.67.1.1,Cloudflare&#10;104.16.132.229,CF2"></textarea>
      <button class="btn btn-o" id="btnCipBulk"><i class="ti ti-list-numbers"></i>افزودن گروهی</button>
    </div>
    <div id="cipList" class="cip-list"></div>
  </div>

  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-key"></i>تغییر رمز عبور</div>
      <div class="fg" style="margin-bottom:12px"><label>رمز فعلی</label><input type="password" id="pwCur"></div>
      <div class="fg" style="margin-bottom:12px"><label>رمز جدید</label><input type="password" id="pwNew"></div>
      <div class="fg"><label>تکرار رمز جدید</label><input type="password" id="pwNew2"></div>
      <button class="btn btn-p full" id="btnPw"><i class="ti ti-device-floppy"></i>ذخیره رمز جدید</button>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-palette"></i>پوسته و پشتیبانی</div>
      <button class="btn btn-o full" style="margin:0 0 10px" id="btnTheme"><i class="ti ti-moon"></i>تغییر پوسته (تیره / خاکستر)</button>
      <a class="btn tg full" style="margin:0 0 10px" href="https://t.me/omiddemon" target="_blank"><i class="ti ti-brand-telegram"></i>کانال پشتیبانی @omiddemon</a>
      <button class="btn btn-d full" style="margin:0" id="btnLogout2"><i class="ti ti-logout"></i>خروج از حساب</button>
      <div class="sr" style="margin-top:14px"><span class="sr-k"><i class="ti ti-versions"></i>نسخه</span><span class="sr-v">ORA v11.4 — Dark Edition</span></div>
    </div>
  </div>
</section>

__BLOOD__
</main>

<div class="modal" id="mLink"><div class="modal-card">
  <div class="modal-title"><i class="ti ti-link"></i><span id="mlTitle">کانفیگ جدید</span></div>
  <div class="fgrid">
    <div class="fg full"><label>نام / برچسب</label><input id="fLabel" placeholder="مثلاً کانفیگ تاریکی"></div>
    <div class="fg"><label>پروتکل / ترابرد</label><select id="fProto"><option value="vless-ws">VLESS + WebSocket</option><option value="xhttp-packet-up">XHTTP (packet-up)</option><option value="xhttp-stream-up">XHTTP (stream-up)</option><option value="xhttp-stream-one">XHTTP (stream-one)</option></select></div>
    <div class="fg"><label>Fingerprint (uTLS)</label><select id="fFp"><option>chrome</option><option>firefox</option><option>safari</option><option>ios</option><option>android</option><option>edge</option><option>360</option><option>qq</option><option>random</option><option>randomized</option></select></div>
    <div class="fg"><label>ALPN</label><input id="fAlpn" placeholder="پیش‌فرض پروتکل" dir="ltr"></div>
    <div class="fg"><label>پورت</label><input id="fPort" type="number" value="443" dir="ltr"></div>
    <div class="fg"><label>محدودیت حجم</label><div style="display:flex;gap:6px"><input id="fLimit" type="number" placeholder="∞"><select id="fLimitU" style="width:84px"><option>GB</option><option>MB</option><option>KB</option></select></div></div>
    <div class="fg"><label>محدودیت سرعت (Mbps)</label><input id="fSpeed" type="number" placeholder="∞" dir="ltr"></div>
    <div class="fg"><label>محدودیت آی‌پی هم‌زمان</label><input id="fIps" type="number" placeholder="∞" dir="ltr"></div>
    <div class="fg"><label>انقضا (روز)</label><input id="fDays" type="number" placeholder="بدون انقضا" dir="ltr"></div>
    <div class="fg"><label>آی‌پی تمیز (Clean IP)</label><input id="fCleanIp" list="cipDL" dir="ltr" placeholder="خالی = دامنه اصلی"><datalist id="cipDL"></datalist></div>
    <div class="fg"><label>حالت آدرس</label><select id="fMultiIp"><option value="0">تک — فقط آدرس انتخابی</option><option value="1">مولتی — همه آی‌پی‌های تمیز</option></select></div>
    <div class="fg full"><label>گروه ساب</label><select id="fSub"></select></div>
    <div class="fg full"><label>یادداشت</label><input id="fNote" placeholder="اختیاری"></div>
  </div>
  <div class="modal-foot"><button class="btn btn-o" onclick="closeM('mLink')">انصراف</button><button class="btn btn-p" id="btnSaveLink"><i class="ti ti-device-floppy"></i>ذخیره</button></div>
</div></div>

<div class="modal" id="mVars"><div class="modal-card" style="max-width:640px">
  <div class="modal-title"><i class="ti ti-stack-2"></i><span id="mvTitle"></span></div>
  <div id="mvList" style="display:flex;flex-direction:column;gap:8px"></div>
  <div class="modal-foot"><button class="btn btn-p" onclick="copyAllVars()"><i class="ti ti-copy"></i>کپی همه</button><button class="btn btn-o" onclick="closeM('mVars')">بستن</button></div>
</div></div>

<div class="modal" id="mSub"><div class="modal-card" style="max-width:480px">
  <div class="modal-title"><i class="ti ti-users-group"></i>گروه ساب جدید</div>
  <div class="fg" style="margin-bottom:12px"><label>نام گروه</label><input id="sName" placeholder="مثلاً VIP"></div>
  <div class="fg" style="margin-bottom:12px"><label>توضیحات</label><input id="sDesc" placeholder="اختیاری"></div>
  <div class="fg"><label>رمز عبور گروه (اختیاری)</label><input id="sPw" type="password" placeholder="بدون رمز"></div>
  <div class="modal-foot"><button class="btn btn-o" onclick="closeM('mSub')">انصراف</button><button class="btn btn-p" id="btnSaveSub"><i class="ti ti-device-floppy"></i>ساخت گروه</button></div>
</div></div>

<div class="modal" id="mManage"><div class="modal-card">
  <div class="modal-title"><i class="ti ti-adjustments"></i>مدیریت کانفیگ‌های گروه</div>
  <div id="manageList"></div>
  <div class="modal-foot"><button class="btn btn-p" onclick="closeM('mManage')">اتمام</button></div>
</div></div>

<div class="modal" id="mQr"><div class="modal-card" style="max-width:340px">
  <div class="modal-title"><i class="ti ti-qrcode"></i><span id="qrTitle"></span></div>
  <div class="qrbox"><img id="qrImg" alt="QR"></div>
  <div class="modal-foot"><button class="btn btn-o" onclick="closeM('mQr')">بستن</button></div>
</div></div>

<div class="modal" id="mConfirm"><div class="modal-card" style="max-width:400px">
  <div class="modal-title"><i class="ti ti-alert-triangle" style="color:var(--red-t)"></i><span id="cfTitle"></span></div>
  <p style="font-size:12.5px;color:var(--t2);line-height:1.8" id="cfMsg"></p>
  <div class="modal-foot"><button class="btn btn-o" onclick="closeM('mConfirm')">انصراف</button><button class="btn btn-d" id="cfOk">بله، انجام بده</button></div>
</div></div>

<div id="toasts"></div>
<script>
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
let page='dash',timers=[],chDash=null,chTraf=null,range='24',lastHourly={},links=[],subs=[],cleanIps=[],confirmCb=null,editId=null,manageSid=null,upSec=null,varLinks=[],varLinkId=null;
const setT=(s,v)=>{const el=$(s);if(el)el.textContent=v};
const PROTO={'vless-ws':'VLESS + WS','xhttp-packet-up':'XHTTP · Packet','xhttp-stream-up':'XHTTP · Stream','xhttp-stream-one':'XHTTP · Stream-One'};
function fmtB(b){b=+b||0;if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
async function api(u,o={}){const r=await fetch(u,o);if(r.status===401){location.href='/login';throw new Error('unauthorized')}let d={};try{d=await r.json()}catch(_){ }if(!r.ok)throw new Error(d.detail||'خطا در ارتباط');return d}
function toast(m,t='ok'){const el=document.createElement('div');el.className='toast '+t;el.innerHTML='<i class="ti '+(t==='ok'?'ti-flame':'ti-alert-circle')+'"></i>'+esc(m);$('#toasts').appendChild(el);requestAnimationFrame(()=>el.classList.add('show'));setTimeout(()=>{el.classList.remove('show');setTimeout(()=>el.remove(),300)},2600)}
function copyTxt(s,m){m=m||'کپی شد';navigator.clipboard.writeText(s).then(()=>toast(m)).catch(()=>{const i=document.createElement('textarea');i.value=s;document.body.appendChild(i);i.select();try{document.execCommand('copy');toast(m)}catch(e){}i.remove()})}
function clearTimers(){timers.forEach(clearInterval);timers=[]}
function every(ms,fn){fn();timers.push(setInterval(fn,ms))}
function faTime(iso){try{return new Date(iso).toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit'})}catch(e){return (iso||'').slice(11,16)}}
function timeAgo(iso){if(!iso)return '—';const s=(Date.now()-new Date(iso))/1000;if(s<60)return 'همین حالا';if(s<3600)return Math.floor(s/60)+' دقیقه پیش';if(s<86400)return Math.floor(s/3600)+' ساعت پیش';return Math.floor(s/86400)+' روز پیش'}
function daysLeft(iso){if(!iso)return '';const d=new Date(iso)-Date.now();return d>0?Math.ceil(d/86400000)+' روز':'منقضی'}
function bytesToValUnit(b){b=+b||0;if(!b)return['','GB'];if(b>=1073741824)return[+(b/1073741824).toFixed(2),'GB'];if(b>=1048576)return[+(b/1048576).toFixed(2),'MB'];return[Math.ceil(b/1024),'KB']}
function logRow(l){const cls=l.level==='err'?'err':(l.level==='warn'?'warn':'ok');const ic=l.level==='err'?'ti-alert-triangle':(l.level==='warn'?'ti-alert-circle':'ti-check');return '<div class="lgrow '+cls+'"><i class="ti '+ic+'"></i><span class="lgmsg">'+esc(l.message)+'</span><span class="lgtime">'+faTime(l.time)+'</span></div>'}
function openM(id){const m=$('#'+id);if(m)m.classList.add('show')}
function closeM(id){const m=$('#'+id);if(m)m.classList.remove('show')}
function askConfirm(title,msg,cb){$('#cfTitle').textContent=title;$('#cfMsg').textContent=msg;confirmCb=cb;openM('mConfirm')}
function showQr(title,data){$('#qrTitle').textContent=title;$('#qrImg').src='https://api.qrserver.com/v1/create-qr-code/?size=300x300&margin=10&data='+encodeURIComponent(data);openM('mQr')}
function chartDefaults(){
  const light=document.documentElement.getAttribute('data-theme')==='light';
  Chart.defaults.font.family="'Vazirmatn',sans-serif";
  Chart.defaults.color=light?'#6B5443':'#8A7462';
  Chart.defaults.borderColor=light?'rgba(140,60,20,.12)':'rgba(255,90,20,.09)';
}
function drawHourly(h){
  const cv=$('#chHourly');if(!cv||!window.Chart)return;
  const keys=Object.keys(h||{}).sort().slice(-24);
  const vals=keys.map(k=>+(((h[k]||0)/1048576).toFixed(2)));
  chartDefaults();
  if(chDash)chDash.destroy();
  chDash=new Chart(cv.getContext('2d'),{type:'bar',data:{labels:keys,datasets:[{data:vals,backgroundColor:'rgba(255,106,0,.35)',hoverBackgroundColor:'rgba(255,138,60,.6)',borderColor:'#FF6A00',borderWidth:1.5,borderRadius:6,maxBarThickness:34}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>c.parsed.y+' MB'}}},scales:{x:{grid:{display:false}},y:{beginAtZero:true,ticks:{callback:v=>v+' MB'}}}}});
}
function drawTraffic(){
  const cv=$('#chTraffic');if(!cv||!window.Chart)return;
  let keys=Object.keys(lastHourly||{}).sort();
  if(range!=='all')keys=keys.slice(-parseInt(range||'24'));
  const vals=keys.map(k=>+(((lastHourly[k]||0)/1048576).toFixed(2)));
  chartDefaults();
  if(chTraf)chTraf.destroy();
  chTraf=new Chart(cv.getContext('2d'),{type:'line',data:{labels:keys,datasets:[{data:vals,borderColor:'#FF6A00',backgroundColor:'rgba(255,106,0,.15)',fill:true,tension:.35,pointRadius:2,pointBackgroundColor:'#FFC93C',borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>c.parsed.y+' MB'}}},scales:{x:{grid:{display:false}},y:{beginAtZero:true,ticks:{callback:v=>v+' MB'}}}}});
}
function go(p){
  page=p;
  $$('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===p));
  $$('.pg').forEach(s=>s.classList.toggle('on',s.id==='pg-'+p));
  $('#sb').classList.remove('open');$('#ov').classList.remove('show');
  try{history.replaceState(null,'','#'+p)}catch(e){}
  clearTimers();
  if(p==='dash')loadDash();
  else if(p==='traffic')loadTraffic();
  else if(p==='links')loadLinks();
  else if(p==='subs')loadSubs();
  else if(p==='conns')loadConns();
  else if(p==='logs')loadLogs();
  else if(p==='settings')loadCleanIps();
}
/* ── Dash ── */
async function loadDash(){
  try{
    const s=await api('/stats');
    upSec=(s.uptime||'0:0:0').split(':').reduce((a,v)=>a*60+(+v||0),0);
    setT('#mConns',s.active_connections||0);
    setT('#mTraffic',(+(s.total_traffic_mb||0)).toFixed(1));
    setT('#mLinks',(s.active_links||0)+'/'+(s.links_count||0));
    setT('#mSubs',s.subs_count||0);
    setT('#sysHost',location.hostname||'—');
    setT('#sysReq',(s.total_requests||0).toLocaleString('fa-IR'));
    setT('#sysErr',s.total_errors||0);
    setT('#nbLinks',s.links_count||0);setT('#nbSubs',s.subs_count||0);setT('#nbConns',s.active_connections||0);
    lastHourly=s.hourly||{};
    drawHourly(lastHourly);
    const a=await api('/api/activity');
    const logs=a.logs||[];
    $('#dashRecent').innerHTML=logs.length?logs.slice(-6).reverse().map(logRow).join(''):'<div class="empty">هنوز رویدادی ثبت نشده است</div>';
  }catch(e){}
}
/* ── Traffic ── */
async function loadTraffic(){
  try{
    const s=await api('/stats');
    upSec=(s.uptime||'0:0:0').split(':').reduce((a,v)=>a*60+(+v||0),0);
    setT('#thTraffic',(+(s.total_traffic_mb||0)).toFixed(2));
    setT('#thConns',s.active_connections||0);
    setT('#thReq',(s.total_requests||0).toLocaleString('fa-IR'));
    setT('#thErr',s.total_errors||0);
    lastHourly=s.hourly||{};
    drawTraffic();
  }catch(e){}
}
 $$('.rtab').forEach(b=>b.addEventListener('click',()=>{$$('.rtab').forEach(x=>x.classList.remove('on'));b.classList.add('on');range=b.dataset.r;drawTraffic()}));
/* ── Links ── */
function findLink(id){return links.find(l=>l.uuid===id)}
async function loadLinks(){
  try{
    const d=await api('/api/links');
    links=d.links||[];
    setT('#linksCount',links.length);
    setT('#nbLinks',links.length);
    renderLinks();
  }catch(e){}
}
function expChip(l){
  if(!l.expires_at)return '<span class="exp-chip ec-ok">بدون انقضا</span>';
  const d=new Date(l.expires_at)-Date.now();
  if(d<=0)return '<span class="exp-chip ec-exp">منقضی</span>';
  const days=Math.ceil(d/86400000);
  const cls=days<=3?'ec-exp':(days<=7?'ec-warn':'ec-ok');
  return '<span class="exp-chip '+cls+'">'+days+' روز</span>';
}
function renderLinks(){
  const q=($('#linkSearch').value||'').trim().toLowerCase();
  const list=$('#linksList');
  let items=q?links.filter(l=>((l.label||'')+' '+(l.note||'')+' '+(l.clean_ip||'')).toLowerCase().includes(q)):links;
  if(!items.length){list.innerHTML='<div class="empty">کانفیگی پیدا نشد</div>';return}
  list.innerHTML=items.map(l=>{
    const ok=l.active&&!l.expired;
    const pct=l.limit_bytes?Math.min(100,Math.round(l.used_bytes/l.limit_bytes*100)):0;
    const pctTxt=l.limit_bytes?pct+'% از '+fmtB(l.limit_bytes):'نامحدود';
    const nv=(l.vless_links&&l.vless_links.length)||1;
    return '<div class="lcard'+(ok?'':' off')+'">'
      +'<div class="lc-head">'
      +'<span class="sicon"><i class="ti '+(ok?'ti-link':'ti-link-off')+'"></i></span>'
      +'<span class="lc-name">'+esc(l.label)+(l.is_default?' <span class="chip chip-gold">پیش‌فرض</span>':'')+'</span>'
      +'<span class="lc-actions">'
      +'<button class="btn-icon" title="QR کانفیگ" onclick="showQrLink(\''+l.uuid+'\')"><i class="ti ti-qrcode"></i></button>'
      +'<button class="btn-icon" title="کپی لینک VLESS" onclick="copyLinkVless(\''+l.uuid+'\')"><i class="ti ti-copy"></i></button>'
      +'<button class="btn-icon" title="کپی لینک ساب" onclick="copyLinkSub(\''+l.uuid+'\')"><i class="ti ti-copy"></i></button>'
      +'<button class="btn-icon" title="ویرایش" onclick="editLinkById(\''+l.uuid+'\')"><i class="ti ti-pencil"></i></button>'
      +'<button class="btn-icon '+(ok?'danger':'')+'" title="'+(ok?'غیرفعال‌سازی':'فعال‌سازی')+'" onclick="toggleLinkById(\''+l.uuid+'\')"><i class="ti '+(ok?'ti-player-pause':'ti-player-play')+'"></i></button>'
      +'<button class="btn-icon danger" title="حذف" onclick="delLinkById(\''+l.uuid+'\')"><i class="ti ti-trash"></i></button>'
      +'</span></div>'
      +'<div class="lc-badges">'
      +'<span class="chip '+(ok?'chip-ok':'chip-exp')+'"><span class="dot '+(ok?'dg':'dr')+'"></span>'+(ok?'فعال':'غیرفعال')+'</span>'
      +'<span class="chip"><i class="ti ti-route"></i>'+(PROTO[l.protocol]||esc(l.protocol))+'</span>'
      +expChip(l)
      +'<span class="chip"><i class="ti ti-plug"></i>'+(l.connected_ips||0)+' آی‌پی</span>'
      +(l.ip_limit?'<span class="chip">حد '+l.ip_limit+' آی‌پی</span>':'')
      +(l.speed_limit_bytes?'<span class="chip">⚡ '+(l.speed_limit_bytes*8/1048576).toFixed(1)+' Mbps</span>':'')
      +(l.clean_ip?'<span class="chip chip-gold"><i class="ti ti-world-wind"></i>'+esc(l.clean_ip)+'</span>':'')
      +(l.multi_ip?'<span class="chip '+(cleanIps.length?'chip-ok':'chip-exp')+'" style="cursor:pointer" onclick="showVariants(\''+l.uuid+'\')" title="نمایش همه‌ی لینک‌ها"><i class="ti ti-stack-2"></i>مولتی · '+nv+' لینک'+(cleanIps.length?'':' · بدون آی‌پی تمیز!')+'</span>':'')
      +'</div>'
      +'<div class="lc-usage"><div class="ubar"><i style="width:'+pct+'%"></i></div>'
      +'<div class="utxt">'+fmtB(l.used_bytes)+' — '+pctTxt+'</div></div>'
      +(l.note?'<div class="lc-note">'+esc(l.note)+'</div>':'')
      +'<div class="lc-note" style="display:flex;gap:6px;flex-wrap:wrap">'
      +(l.multi_ip&&nv>1?'<button class="btn btn-sm btn-p" onclick="showVariants(\''+l.uuid+'\')"><i class="ti ti-stack-2"></i>همه‌ی '+nv+' لینک</button>':'')
      +'<button class="btn btn-sm btn-o" onclick="resetUsageById(\''+l.uuid+'\')"><i class="ti ti-rotate"></i>ریست مصرف</button>'
      +'<button class="btn btn-sm btn-o" onclick="copyLinkVless(\''+l.uuid+'\')"><i class="ti ti-copy"></i>کپی VLESS</button>'
      +'<button class="btn btn-sm btn-o" onclick="copyLinkSub(\''+l.uuid+'\')"><i class="ti ti-copy"></i>کپی ساب</button>'
      +'</div></div>';
  }).join('');
}
function linkVariants(l){return(l.vless_links&&l.vless_links.length)?l.vless_links:[l.vless_link]}
function showQrLink(id){const l=findLink(id);if(!l)return;const vs=linkVariants(l);showQr('QR: '+l.label+(vs.length>1?' · لینک ۱ از '+vs.length:''),vs[0])}
function copyLinkVless(id){
  const l=findLink(id);if(!l)return;
  const vs=linkVariants(l);
  if(vs.length>1){copyTxt(vs.join('\n'),vs.length+' لینک کپی شد (هر خط یک آی‌پی تمیز)')}
  else{copyTxt(vs[0],'لینک VLESS کپی شد')}
}
function copyLinkSub(id){const l=findLink(id);if(l)copyTxt(l.sub_url,'لینک ساب کپی شد')}
function showVariants(id){
  const l=findLink(id);if(!l)return;
  varLinks=linkVariants(l);varLinkId=id;
  $('#mvTitle').textContent='لینک‌های «'+l.label+'» — '+varLinks.length+' مورد';
  $('#mvList').innerHTML=varLinks.map((u,j)=>{
    const m=u.match(/@(\[[^\]]+\]|[^:?]+):/);
    const ip=m?m[1].replace(/^\[|\]$/g,''):'؟';
    return '<div class="urlrow" style="margin:0"><span class="ci-ip" style="min-width:120px">'+esc(ip)+'</span>'
      +'<span class="urltext">'+esc(u)+'</span>'
      +'<button class="btn-icon" onclick="copyVar('+j+')"><i class="ti ti-copy"></i></button>'
      +'<button class="btn-icon" onclick="qrVar('+j+')"><i class="ti ti-qrcode"></i></button></div>';
  }).join('');
  openM('mVars');
}
function copyVar(j){copyTxt(varLinks[j],'لینک '+(j+1)+' کپی شد')}
function qrVar(j){showQr('QR لینک '+(j+1),varLinks[j])}
function copyAllVars(){copyTxt(varLinks.join('\n'),'همه‌ی '+varLinks.length+' لینک کپی شد — در اپ «Import از کلیپ‌بورد» بزن')}
async function toggleLinkById(id){const l=findLink(id);if(!l)return;try{await api('/api/links/'+id,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:!l.active})});loadLinks()}catch(e){toast(e.message,'err')}}
function resetUsageById(id){askConfirm('ریست مصرف','مصرف این کانفیگ صفر شود؟',async()=>{try{await api('/api/links/'+id,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});toast('مصرف ریست شد');loadLinks()}catch(e){toast(e.message,'err')}})}
function delLinkById(id){
  const l=findLink(id);if(!l)return;
  askConfirm('حذف کانفیگ','از حذف «'+l.label+'» مطمئنی؟ این عمل برگشت‌ناپذیر است.',async()=>{
    try{await api('/api/links/'+id,{method:'DELETE'});toast('کانفیگ حذف شد');loadLinks()}catch(e){toast(e.message,'err')}
  });
}
async function fillSubSelect(selected){
  let list=[];
  try{const d=await api('/api/subs');list=d.subs||[]}catch(e){}
  subs=list;
  const sel=$('#fSub');
  sel.innerHTML='<option value="">بدون گروه</option>'+subs.map(s=>'<option value="'+s.sub_id+'">'+esc(s.name)+'</option>').join('');
  if(selected!=null&&[...sel.options].some(o=>o.value===selected))sel.value=selected;
}
function fillCleanIpSelects(){
  const dl=$('#cipDL');if(!dl)return;
  dl.innerHTML=cleanIps.map(c=>'<option value="'+esc(c.ip)+'">'+(c.label?esc(c.label):'')+'</option>').join('');
}
 $('#btnNewLink').addEventListener('click',async()=>{
  editId=null;
  $('#mlTitle').textContent='کانفیگ جدید';
  $('#fLabel').value='';$('#fProto').value='vless-ws';$('#fFp').value='chrome';$('#fAlpn').value='';
  $('#fPort').value='443';$('#fLimit').value='';$('#fLimitU').value='GB';$('#fSpeed').value='';
  $('#fIps').value='';$('#fDays').value='';$('#fNote').value='';
  $('#fCleanIp').value='';$('#fMultiIp').value='0';
  await fillSubSelect('');
  fillCleanIpSelects();
  openM('mLink');
});
async function editLinkById(id){
  const l=findLink(id);if(!l)return;
  await fillSubSelect(l.sub_id||'');
  editId=id;
  $('#mlTitle').textContent='ویرایش کانفیگ';
  $('#fLabel').value=l.label||'';
  $('#fProto').value=l.protocol||'vless-ws';
  $('#fFp').value=l.fingerprint||'chrome';
  $('#fAlpn').value=l.alpn||'';
  $('#fPort').value=l.port||443;
  const vu=bytesToValUnit(l.limit_bytes);
  $('#fLimit').value=vu[0];$('#fLimitU').value=vu[1];
  $('#fSpeed').value=l.speed_limit_bytes?(l.speed_limit_bytes*8/1048576).toFixed(1):'';
  $('#fIps').value=l.ip_limit||'';
  $('#fDays').value=l.expires_at?Math.max(0,Math.ceil((new Date(l.expires_at)-Date.now())/86400000)):'';
  $('#fNote').value=l.note||'';
  fillCleanIpSelects();
  $('#fCleanIp').value=l.clean_ip||'';
  $('#fMultiIp').value=l.multi_ip?'1':'0';
  openM('mLink');
}
 $('#btnSaveLink').addEventListener('click',async()=>{
  const body={
    label:$('#fLabel').value.trim()||'کانفیگ جدید',
    protocol:$('#fProto').value,
    fingerprint:$('#fFp').value,
    alpn:$('#fAlpn').value.trim(),
    port:+$('#fPort').value||443,
    limit_value:+$('#fLimit').value||0,
    limit_unit:$('#fLimitU').value,
    speed_limit_value:+$('#fSpeed').value||0,
    speed_limit_unit:'MBIT',
    ip_limit:+$('#fIps').value||0,
    expires_days:+$('#fDays').value||0,
    note:$('#fNote').value.trim(),
    sub_id:$('#fSub').value||null,
    clean_ip:$('#fCleanIp').value.trim()||'',
    multi_ip:$('#fMultiIp').value==='1'
  };
  const btn=$('#btnSaveLink');btn.disabled=true;
  try{
    if(editId){
      await api('/api/links/'+editId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      toast('کانفیگ ویرایش شد');
    }else{
      await api('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      toast('کانفیگ ساخته شد');
    }
    closeM('mLink');editId=null;loadLinks();
  }catch(e){toast(e.message,'err')}
  btn.disabled=false;
});
 $('#btnSubAll').addEventListener('click',()=>copyTxt(location.origin+'/sub-all','لینک ساب همه کپی شد (نیاز به لاگین دارد)'));
 $('#linkSearch').addEventListener('input',renderLinks);
/* ── Subs ── */
function findSub(id){return subs.find(x=>x.sub_id===id)}
async function loadSubs(){
  try{
    const d=await api('/api/subs');
    subs=d.subs||[];
    setT('#nbSubs',subs.length);
    renderSubs();
  }catch(e){}
}
function renderSubs(){
  const list=$('#subsList');
  if(!subs.length){list.innerHTML='<div class="empty">هنوز گروهی ساخته نشده — با دکمه «گروه جدید» شروع کن.</div>';return}
  list.innerHTML=subs.map(s=>
    '<div class="lcard">'
    +'<div class="lc-head">'
    +'<span class="sicon"><i class="ti ti-users-group"></i></span>'
    +'<span class="lc-name">'+esc(s.name)+'</span>'
    +'<span class="lc-actions">'
    +'<button class="btn-icon" title="کپی لینک ساب" onclick="copySubUrl(\''+s.sub_id+'\')"><i class="ti ti-copy"></i></button>'
    +'<button class="btn-icon" title="QR لینک ساب" onclick="qrSubUrl(\''+s.sub_id+'\')"><i class="ti ti-qrcode"></i></button>'
    +'<button class="btn-icon" title="مدیریت کانفیگ‌ها" onclick="openManage(\''+s.sub_id+'\')"><i class="ti ti-adjustments"></i></button>'
    +'<button class="btn-icon danger" title="حذف گروه" onclick="delSub(\''+s.sub_id+'\')"><i class="ti ti-trash"></i></button>'
    +'</span></div>'
    +'<div class="lc-badges">'
    +'<span class="chip"><i class="ti ti-link"></i>'+s.links_count+' کانفیگ</span>'
    +'<span class="chip chip-ok"><i class="ti ti-check"></i>'+s.active_count+' فعال</span>'
    +'<span class="chip"><i class="ti ti-arrows-exchange"></i>'+esc(s.total_used_fmt)+'</span>'
    +(s.has_password?'<span class="chip chip-gold"><i class="ti ti-lock"></i>رمزدار</span>':'')
    +'</div>'
    +'<div class="urlrow"><span class="urltext">'+esc(s.sub_url)+'</span>'
    +'<button class="btn-icon" onclick="copySubUrl(\''+s.sub_id+'\')"><i class="ti ti-copy"></i></button></div>'
    +(s.desc?'<div class="lc-note">'+esc(s.desc)+'</div>':'')
    +'</div>').join('');
}
function copySubUrl(id){const s=findSub(id);if(s)copyTxt(s.sub_url,'لینک ساب کپی شد')}
function qrSubUrl(id){const s=findSub(id);if(s)showQr('QR ساب: '+s.name,s.sub_url)}
function delSub(id){
  const s=findSub(id);if(!s)return;
  askConfirm('حذف گروه','از حذف گروه «'+s.name+'» مطمئنی؟ کانفیگ‌ها حذف نمی‌شوند، فقط از گروه خارج می‌شوند.',async()=>{
    try{await api('/api/subs/'+id,{method:'DELETE'});toast('گروه حذف شد');loadSubs()}catch(e){toast(e.message,'err')}
  });
}
 $('#btnNewSub').addEventListener('click',()=>{$('#sName').value='';$('#sDesc').value='';$('#sPw').value='';openM('mSub')});
 $('#btnSaveSub').addEventListener('click',async()=>{
  const name=$('#sName').value.trim();
  if(!name)return toast('نام گروه را وارد کن','err');
  try{
    await api('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:name,desc:$('#sDesc').value.trim(),password:$('#sPw').value})});
    closeM('mSub');toast('گروه ساخته شد');loadSubs();
  }catch(e){toast(e.message,'err')}
});
async function openManage(sid){
  manageSid=sid;
  try{
    const d=await api('/api/links');
    links=d.links||[];
    renderManage();
    openM('mManage');
  }catch(e){toast(e.message,'err')}
}
function renderManage(){
  const el=$('#manageList');
  el.innerHTML=links.map(l=>{
    const inG=(l.sub_id===manageSid);
    return '<div class="mrow" onclick="toggleAssign(\''+l.uuid+'\')">'
      +'<input type="checkbox" '+(inG?'checked':'')+'>'
      +'<span style="flex:1">'+esc(l.label)+'</span>'
      +'<span class="chip">'+(PROTO[l.protocol]||esc(l.protocol))+'</span>'
      +'</div>';
  }).join('');
}
async function toggleAssign(uid){
  if(!manageSid)return;
  const l=links.find(x=>x.uuid===uid);if(!l)return;
  const action=(l.sub_id===manageSid)?'remove':'add';
  try{
    await api('/api/subs/'+manageSid+'/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_id:uid,action:action})});
    l.sub_id=(action==='add')?manageSid:null;
    renderManage();
  }catch(e){toast(e.message,'err')}
}
/* ── Conns ── */
async function loadConns(){
  try{
    const d=await api('/api/connections');
    setT('#cCount',d.count||0);setT('#cRaw',d.raw_count||0);setT('#nbConns',d.count||0);
    const rows=d.connections||[];
    $('#connsBody').innerHTML=rows.length?rows.map(c=>'<div class="trow"><div class="cip">'+esc(c.ip)+'</div><div>'+esc(c.label)+'</div><div>'+c.sessions+'</div><div>'+fmtB(c.bytes)+'</div><div>'+timeAgo(c.last_connected_at)+'</div><div>'+(c.transports||[]).map(t=>'<span class="chip">'+esc(t)+'</span>').join(' ')+'</div></div>').join(''):'<div class="empty">هیچ اتصال فعالی وجود ندارد</div>';
  }catch(e){}
}
/* ── Logs ── */
async function loadLogs(){
  try{
    const d=await api('/api/activity');
    const logs=(d.logs||[]).slice().reverse();
    $('#logsList').innerHTML=logs.length?logs.map(logRow).join(''):'<div class="empty">لاگی ثبت نشده است</div>';
  }catch(e){}
}
/* ── Clean IPs ── */
async function loadCleanIps(){
  try{
    const r=await fetch('/api/clean-ips');
    if(r.status===404){const w=$('#cipWarn');if(w)w.style.display='block';return}
    if(r.status===401){location.href='/login';return}
    const d=await r.json();
    cleanIps=d.clean_ips||[];
    const w=$('#cipWarn');if(w)w.style.display='none';
    renderCleanIps();fillCleanIpSelects();
  }catch(e){}
}
function renderCleanIps(){
  const list=$('#cipList');if(!list)return;
  const b=$('#cipBadge');if(b)b.textContent=cleanIps.length+' آی‌پی';
  if(!cleanIps.length){list.innerHTML='<div class="empty" style="padding:18px">هنوز آی‌پی تمیزی ثبت نشده — یکی اضافه کن یا گروهی وارد کن.</div>';return}
  list.innerHTML=cleanIps.map(c=>{
    const used=links.filter(l=>(l.clean_ip||'')===c.ip).length;
    return '<div class="cip-item">'
      +'<span class="ci-dot"></span>'
      +'<span class="ci-ip">'+esc(c.ip)+'</span>'
      +(c.label?'<span class="ci-label">'+esc(c.label)+'</span>':'')
      +(used?'<span class="chip chip-ok">'+used+' کانفیگ</span>':'')
      +'<span class="ci-ms" id="cims-'+esc(c.id)+'"></span>'
      +'<span class="ci-actions">'
      +'<button class="btn-icon" title="تست اتصال (TCP 443)" onclick="checkCip(\''+esc(c.id)+'\')"><i class="ti ti-plug-connected"></i></button>'
      +'<button class="btn-icon danger" title="حذف" onclick="delCip(\''+esc(c.id)+'\')"><i class="ti ti-trash"></i></button>'
      +'</span></div>';
  }).join('');
}
async function addCip(){
  const ip=$('#cipIp').value.trim(),label=$('#cipLabel').value.trim();
  if(!ip)return toast('اول آی‌پی تمیز را وارد کن','err');
  try{
    const d=await api('/api/clean-ips',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({ips:ip,label:label})});
    $('#cipIp').value='';$('#cipLabel').value='';
    toast(d.added&&d.added.length?('«'+ip+'» اضافه شد'):'آی‌پی نامعتبر یا تکراری است',d.added&&d.added.length?'ok':'err');
    loadCleanIps();
  }catch(e){toast(e.message,'err')}
}
async function bulkCip(){
  const t=$('#cipBulk').value.trim();
  if(!t)return toast('چیزی برای افزودن نیست','err');
  try{
    const d=await api('/api/clean-ips',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({ips:t})});
    $('#cipBulk').value='';
    const na=(d.added||[]).length,ns=(d.skipped||[]).length;
    toast(na+' آی‌پی اضافه شد'+(ns?(' · '+ns+' رد شد'):''));
    loadCleanIps();
  }catch(e){toast(e.message,'err')}
}
async function delCip(id){
  try{await api('/api/clean-ips/'+id,{method:'DELETE'});toast('آی‌پی تمیز حذف شد');loadCleanIps()}catch(e){toast(e.message,'err')}
}
function clearCips(){
  if(!cleanIps.length)return toast('لیست خالی است','err');
  askConfirm('پاک کردن همه','همه‌ی آی‌پی‌های تمیز حذف شوند؟',async()=>{
    try{await api('/api/clean-ips',{method:'DELETE'});toast('لیست پاک شد');loadCleanIps()}catch(e){toast(e.message,'err')}
  });
}
async function checkCip(id){
  const c=cleanIps.find(x=>x.id===id);if(!c)return;
  const el=document.getElementById('cims-'+id);if(el)el.textContent='در حال تست...';
  try{
    const r=await api('/api/clean-ips/check',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({ip:c.ip})});
    if(el)el.textContent=r.ok?('✔ '+r.ms+' ms'):'✘ بدون پاسخ';
  }catch(e){if(el)el.textContent='✘ خطا'}
}
 $('#btnCipAdd').addEventListener('click',addCip);
 $('#btnCipBulk').addEventListener('click',bulkCip);
 $('#cipIp').addEventListener('keydown',e=>{if(e.key==='Enter')addCip()});
 $('#cipBulk').addEventListener('keydown',e=>{if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))bulkCip()});
/* ── Settings ── */
 $('#btnPw').addEventListener('click',async()=>{
  const cur=$('#pwCur').value,n1=$('#pwNew').value,n2=$('#pwNew2').value;
  if(!cur||!n1)return toast('فیلدها را کامل کن','err');
  if(n1!==n2)return toast('تکرار رمز مطابقت ندارد','err');
  try{
    await api('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:n1})});
    toast('رمز عوض شد');
    $('#pwCur').value='';$('#pwNew').value='';$('#pwNew2').value='';
  }catch(e){toast(e.message,'err')}
});
 $('#btnTheme').addEventListener('click',()=>{
  const el=document.documentElement;
  const next=el.getAttribute('data-theme')==='light'?'':'light';
  if(next)el.setAttribute('data-theme',next);else el.removeAttribute('data-theme');
  try{localStorage.setItem('ora-theme',next)}catch(e){}
  chartDefaults();
  if(page==='dash')drawHourly(lastHourly);
  if(page==='traffic')drawTraffic();
});
async function logout(){try{await api('/api/logout',{method:'POST'})}catch(e){} location.href='/login'}
 $('#btnLogout').addEventListener('click',logout);
 $('#btnLogout2').addEventListener('click',logout);
/* ── Modal overlay close ── */
 $$('.modal').forEach(m=>m.addEventListener('click',e=>{if(e.target===m)m.classList.remove('show')}));
 $('#cfOk').addEventListener('click',async()=>{closeM('mConfirm');const cb=confirmCb;confirmCb=null;if(cb)await cb()});
/* ── Sidebar (mobile) ── */
 $('#sbOpen').addEventListener('click',()=>{$('#sb').classList.add('open');$('#ov').classList.add('show')});
 $('#sbClose').addEventListener('click',()=>{$('#sb').classList.remove('open');$('#ov').classList.remove('show')});
 $('#ov').addEventListener('click',()=>{$('#sb').classList.remove('open');$('#ov').classList.remove('show')});
/* ── Uptime tick + conns auto-refresh ── */
setInterval(()=>{
  if(upSec==null)return;
  upSec++;
  const h=String(Math.floor(upSec/3600)).padStart(2,'0'),m=String(Math.floor(upSec%3600/60)).padStart(2,'0'),s=String(upSec%60).padStart(2,'0');
  setT('#bUptime',h+':'+m+':'+s);setT('#tUp',h+':'+m+':'+s);
},1000);
setInterval(()=>{if(page==='conns')loadConns()},5000);
/* ── Boot ── */
(async function boot(){
  try{const t=localStorage.getItem('ora-theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}
  try{const me=await api('/api/me');if(!me.authenticated){location.href='/login';return}}catch(e){return}
  $$('.nav-it').forEach(n=>n.addEventListener('click',e=>{e.preventDefault();go(n.dataset.pg)}));
  const hash=(location.hash||'').replace('#','');
  go(['dash','traffic','links','subs','conns','logs','settings'].indexOf(hash)>=0?hash:'dash');
  loadLinks();
  loadCleanIps();
})();
</script>
</body></html>"""

# ═══════════════════════════════ صفحه عمومی ساب (PUBLIC) ═══════════════════════════════
_PUB_TPL = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ORA · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050303;--bord:rgba(255,90,20,.16);--gd:rgba(255,80,20,.08);--fire2:#FF8A3C;--fire3:#FFC93C;--t1:#EFE2D0;--t2:#C4AE97;--t3:#8A7462;--green-t:#7DDFA8;--red-t:#FF7B72}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px 14px}
.bg{position:fixed;inset:0;background:radial-gradient(900px 500px at 50% -10%,rgba(255,90,20,.1),transparent 60%),var(--bg);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(255,90,20,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,90,20,.05) 1px,transparent 1px);background-size:44px 44px;-webkit-mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,#000 30%,transparent 75%);mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,#000 30%,transparent 75%);z-index:0}
.wrap{position:relative;z-index:10;width:100%;max-width:560px}
.card{background:linear-gradient(165deg,rgba(28,13,9,.85),rgba(9,4,3,.94));border:1px solid var(--bord);border-radius:26px;padding:30px 24px 24px;backdrop-filter:blur(22px);box-shadow:0 30px 90px rgba(0,0,0,.7);position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:62%;height:1px;background:linear-gradient(90deg,transparent,rgba(255,138,60,.75),transparent)}
.brand{text-align:center;margin-bottom:16px}
.brand .ora-logo{width:88px;height:88px;margin:0 auto 8px}
.brand-name{font-family:'Cinzel',serif;font-size:22px;font-weight:900;letter-spacing:.32em;text-indent:.32em;background:linear-gradient(135deg,#FFD9A0,#FF7A2E 45%,#B31212);-webkit-background-clip:text;background-clip:text;color:transparent}
h1{font-size:18px;font-weight:800;text-align:center;margin-bottom:4px}
.sub{font-size:12px;color:var(--t2);text-align:center;margin-bottom:18px;line-height:1.8}
.mrow2{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px}
.stat{background:var(--gd);border:1px solid var(--bord);border-radius:14px;padding:12px;text-align:center}
.stat b{display:block;font-size:17px;color:var(--fire2)}
.stat span{font-size:10px;color:var(--t3)}
.urlrow{display:flex;align-items:center;gap:8px;background:rgba(0,0,0,.3);border:1px solid var(--bord);border-radius:12px;padding:8px 12px;margin-bottom:16px}
.urltext{flex:1;font-family:ui-monospace,monospace;font-size:10.5px;color:var(--fire2);direction:ltr;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.btn-icon{width:30px;height:30px;padding:0;border-radius:8px;background:var(--gd);color:var(--fire2);border:1px solid var(--bord);display:inline-flex;align-items:center;justify-content:center;cursor:pointer;font-size:14px;transition:.15s;flex-shrink:0}
.btn-icon:hover{border-color:rgba(255,90,20,.45)}
.btn{font-family:inherit;font-size:13px;font-weight:700;border-radius:12px;padding:11px 16px;cursor:pointer;border:none;display:inline-flex;align-items:center;justify-content:center;gap:7px}
.btn-p{background:linear-gradient(135deg,#FFC93C,#FF6A00 55%,#B31212);color:#1A0703}
.btn.full{width:100%}
.btn-o{background:transparent;border:1px solid var(--bord);color:var(--t2)}
input[type=password]{width:100%;padding:12px 14px;border-radius:12px;border:1px solid var(--bord);background:rgba(0,0,0,.4);color:var(--t1);font-family:inherit;font-size:14px;outline:none;margin-bottom:10px}
input[type=password]:focus{border-color:rgba(255,106,0,.55)}
.lclist{display:flex;flex-direction:column;gap:10px}
.lcard{background:rgba(0,0,0,.28);border:1px solid var(--bord);border-radius:16px;padding:14px 16px}
.lcard.off{opacity:.5}
.lc-head{display:flex;align-items:center;gap:9px;margin-bottom:9px}
.lc-name{font-weight:700;font-size:13px;display:flex;align-items:center;gap:8px;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.lc-actions{display:flex;gap:6px}
.chip{font-size:9.5px;padding:3px 9px;border-radius:20px;background:var(--gd);border:1px solid var(--bord);color:var(--t2);display:inline-flex;align-items:center;gap:4px;font-weight:600}
.chip-ok{color:var(--green-t);border-color:rgba(62,207,142,.3)}
.chip-exp{color:var(--red-t);border-color:rgba(229,72,77,.3)}
.chip-gold{color:var(--fire2)}
.ubar{height:6px;border-radius:6px;background:rgba(0,0,0,.4);overflow:hidden;border:1px solid rgba(255,90,20,.1)}
.ubar i{display:block;height:100%;background:linear-gradient(90deg,#8B1010,#FF6A00,#FFC93C);border-radius:6px;box-shadow:0 0 8px rgba(255,106,0,.45)}
.utxt{font-size:10px;color:var(--t3);margin-top:5px}
.empty{padding:24px;text-align:center;color:var(--t3);font-size:12px}
.qrbox{display:flex;flex-direction:column;align-items:center;gap:12px;padding:8px 0}
.qrbox img{width:250px;height:250px;border-radius:14px;border:1px solid rgba(255,90,20,.45);background:#fff;padding:8px}
.modal{position:fixed;inset:0;background:rgba(3,1,1,.78);backdrop-filter:blur(6px);z-index:300;display:none;align-items:center;justify-content:center;padding:18px}
.modal.show{display:flex}
.modal-card{width:100%;max-width:320px;background:linear-gradient(165deg,#1A0C07,#0A0403);border:1px solid rgba(255,90,20,.45);border-radius:20px;padding:18px}
.modal-title{font-size:13px;font-weight:800;margin-bottom:10px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--fire2)}
.modal-foot{display:flex;gap:8px;margin-top:14px;justify-content:flex-end}
.bl-wrap{position:fixed;left:0;right:0;bottom:0;z-index:5;padding:34px 0 0;background:linear-gradient(180deg,transparent,rgba(6,3,2,.95) 45%);pointer-events:none}
__ORA_CSS__
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">__LOGO_SVG__<div class="brand-name">ORA</div></div>
    <h1 id="gName">در حال بارگذاری…</h1>
    <p class="sub" id="gDesc"></p>
    <div id="lockedBox" style="display:none">
      <input type="password" id="pwInput" placeholder="رمز عبور این اشتراک را وارد کنید">
      <button class="btn btn-p full" id="btnUnlock"><i class="ti ti-lock-open"></i> نمایش کانفیگ‌ها</button>
    </div>
    <div id="content" style="display:none">
      <div class="mrow2">
        <div class="stat"><b id="stUsed">—</b><span>مصرف کل</span></div>
        <div class="stat"><b id="stConns">0</b><span>اتصال فعال</span></div>
      </div>
      <div class="urlrow"><span class="urltext" id="subUrl"></span>
        <button class="btn-icon" onclick="pubCopySub()"><i class="ti ti-copy"></i></button>
        <button class="btn-icon" onclick="pubQrSub()"><i class="ti ti-qrcode"></i></button>
      </div>
      <div id="linksList" class="lclist"></div>
    </div>
  </div>
</div>
<div class="modal" id="mQr"><div class="modal-card">
  <div class="modal-title"><i class="ti ti-qrcode"></i><span id="qrTitle"></span></div>
  <div class="qrbox"><img id="qrImg" alt="QR"></div>
  <div class="modal-foot"><button class="btn btn-o" onclick="document.getElementById('mQr').classList.remove('show')">بستن</button></div>
</div></div>
__BLOOD__
<script>
const KEY='__UUID_KEY__';
const $=s=>document.querySelector(s);
let DATA=null;
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function copyTxt(s,m){m=m||'کپی شد';navigator.clipboard.writeText(s).then(()=>flash(m)).catch(()=>{const i=document.createElement('textarea');i.value=s;document.body.appendChild(i);i.select();try{document.execCommand('copy');flash(m)}catch(e){}i.remove()})}
function flash(m){const t=document.createElement('div');t.textContent=m;t.style.cssText='position:fixed;bottom:18px;left:50%;transform:translateX(-50%);background:rgba(20,9,6,.96);border:1px solid rgba(255,90,20,.45);color:#EFE2D0;padding:9px 16px;border-radius:12px;font-size:12px;z-index:400;font-family:inherit';document.body.appendChild(t);setTimeout(()=>t.remove(),2200)}
function fmtB(b){b=+b||0;if(b<1024)return b+' B';if(b<1048576)return(b/1024).toFixed(1)+' KB';if(b<1073741824)return(b/1048576).toFixed(2)+' MB';return(b/1073741824).toFixed(2)+' GB'}
function qrModal(title,data){
  $('#qrTitle').textContent=title;
  $('#qrImg').src='https://api.qrserver.com/v1/create-qr-code/?size=300x300&margin=10&data='+encodeURIComponent(data);
  $('#mQr').classList.add('show');
}
function variantsOf(i){const l=DATA.links[i];return(l.vless_links&&l.vless_links.length?l.vless_links:[l.vless_link])}
function pubCopySub(){if(DATA)copyTxt(DATA.sub_url,'لینک ساب کپی شد')}
function pubQrSub(){if(DATA)qrModal('QR لینک ساب',DATA.sub_url)}
function pubCopyV(i,j){if(!DATA)return;copyTxt(variantsOf(i)[j],'لینک کانفیگ کپی شد')}
function pubQrV(i,j){if(!DATA)return;const l=DATA.links[i];qrModal('QR: '+l.label+' · '+(j+1),variantsOf(i)[j])}
async function load(pw){
  try{
    const r=await fetch('/api/public/sub/'+KEY+(pw?('?pw='+encodeURIComponent(pw)):''));
    const d=await r.json();
    if(d.locked){
      $('#lockedBox').style.display='block';$('#content').style.display='none';
      $('#gName').textContent=d.name||'اشتراک قفل است';$('#gDesc').textContent='این اشتراک رمزدار است';
      return;
    }
    DATA=d;
    $('#lockedBox').style.display='none';$('#content').style.display='block';
    $('#gName').textContent=d.name||'اشتراک ORA';
    $('#gDesc').textContent=d.desc||'کانفیگ‌های اختصاصی شما';
    $('#stUsed').textContent=d.total_used_fmt||'0 B';
    $('#stConns').textContent=d.active_connections||0;
    $('#subUrl').textContent=d.sub_url||'';
    const ls=d.links||[];
    $('#linksList').innerHTML=ls.length?ls.map((l,i)=>{
      const ok=l.active;
      const pct=l.limit_bytes?Math.min(100,Math.round(l.used_bytes/l.limit_bytes*100)):0;
      let exp='';
      if(l.expires_at){const dd=new Date(l.expires_at)-Date.now();exp=dd>0?'<span class="chip chip-ok">'+Math.ceil(dd/86400000)+' روز</span>':'<span class="chip chip-exp">منقضی</span>'}
      const vs=variantsOf(i);
      let vrows='';
      vs.forEach((u,j)=>{
        vrows+='<div class="urlrow" style="margin-top:6px;margin-bottom:0"><span class="urltext">'+esc(u)+'</span>'
          +'<button class="btn-icon" onclick="pubCopyV('+i+','+j+')"><i class="ti ti-copy"></i></button>'
          +'<button class="btn-icon" onclick="pubQrV('+i+','+j+')"><i class="ti ti-qrcode"></i></button></div>';
      });
      return '<div class="lcard'+(ok?'':' off')+'">'
        +'<div class="lc-head"><span class="lc-name">'+esc(l.label)+'</span><span class="lc-actions">'
        +'<span class="chip"><i class="ti ti-plug"></i>'+(l.connections||0)+'</span>'
        +'</span></div>'
        +'<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px">'
        +'<span class="chip '+(ok?'chip-ok':'chip-exp')+'">'+(ok?'فعال':'غیرفعال')+'</span>'
        +'<span class="chip">'+esc(l.protocol)+'</span>'+exp
        +(l.clean_ip?'<span class="chip chip-gold">'+esc(l.clean_ip)+'</span>':'')
        +(l.multi_ip?'<span class="chip chip-gold">مولتی ('+vs.length+' لینک)</span>':'')
        +'</div>'
        +'<div class="ubar"><i style="width:'+pct+'%"></i></div>'
        +'<div class="utxt">'+esc(l.used_fmt)+' از '+esc(l.limit_fmt)+'</div>'
        +vrows
        +'</div>';
    }).join(''):'<div class="empty">فعلاً کانفیگی در این اشتراک نیست</div>';
  }catch(e){$('#gName').textContent='خطا در بارگذاری'}
}
 $('#btnUnlock').addEventListener('click',()=>load($('#pwInput').value.trim()));
 $('#pwInput').addEventListener('keydown',e=>{if(e.key==='Enter')load($('#pwInput').value.trim())});
 $('#mQr').addEventListener('click',e=>{if(e.target.id==='mQr')e.target.classList.remove('show')});
load();
</script>
</body></html>"""

# ═══════════════════════════════ مونتاژ نهایی ═══════════════════════════════
LOGIN_HTML = (_LOGIN_TPL
    .replace("__LOGO_SVG__", LOGO_SVG)
    .replace("__BLOOD__", BLOOD_HTML)
    .replace("__ORA_CSS__", _ORA_CSS))

DASHBOARD_HTML = (_DASH_TPL
    .replace("__LOGO_SVG__", LOGO_SVG)
    .replace("__BLOOD__", BLOOD_HTML)
    .replace("__ORA_CSS__", _ORA_CSS))

PUBLIC_PAGE_HTML = (_PUB_TPL
    .replace("__LOGO_SVG__", LOGO_SVG)
    .replace("__BLOOD__", BLOOD_HTML)
    .replace("__ORA_CSS__", _ORA_CSS))

def get_public_page_html(uuid_key: str) -> str:
    return PUBLIC_PAGE_HTML.replace("__UUID_KEY__", uuid_key)