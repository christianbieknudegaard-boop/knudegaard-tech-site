import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
KEY='a66e1077-ba51-46a3-9730-51c0641c0327'
T={
'nb':dict(file='index.html',p='',lang='nb',other='en/',otherlabel='English',title='Knudegaard Apps – apputvikling i Lillesand',
 desc='Knudegaard Apps utvikler apper for iPhone, iPad og Android. Gjennomtenkte apper uten reklame og uten unødvendig datainnsamling.',
 eyebrow='Applikasjonsutvikling fra Lillesand',
 h1a='Apper som gjør hverdagen', h1b='litt enklere.',
 lead='Vi lager apper for iPhone, iPad og Android. Rolige, gjennomtenkte og uten reklame, og de samler aldri inn mer data enn de trenger.',
 cta1='Se appene', cta2='Kontakt oss',
 v=[('noads','Ingen reklame','Appene våre tjener penger på at de er gode, ikke på oppmerksomheten din.'),('lock','Personvern først','Mest mulig skjer på telefonen din. Vi selger aldri data.'),('pin','Laget i Norge','Utviklet i Lillesand, for brukere over hele verden.')],
 apps='Våre apper', appslead='Små verktøy og spill, hver med én tydelig jobb.',
 sk='Skann dokumenter, få dem lest høyt og lytt mens du gjør noe annet.', lt='Rydd bildebiblioteket raskt: duplikater, skjermbilder og store videoer.', wa='Ordspill der du bygger en bro av ord tvers over brettet. På norsk og engelsk.',
 oh='Du er fisken. Svøm opp fra korallrevet, unngå kroker og garn, og samle 24 fisker, de fleste med sin egen kraft.',
 live='I App Store', soon='Kommer snart', visit='Besøk nettsiden →',
 ios='iPhone og iPad', android='Android', st_live='I App Store', st_test='I testing', st_later='Kommer senere',
 ios_sum='Skanlio, Lumtidy og Wordarc ligger i App Store. Off the Hook kommer snart.', android_sum='Skanlio, Lumtidy, Wordarc og Off the Hook er i testing nå.',
 company='Om selskapet', colead='Knudegaard Apps er et norsk enkeltpersonforetak som utvikler og gir ut sine egne apper.', nav=('Apper','Om oss','Kontakt'), tagline='Små, gjennomtenkte apper uten reklame. Laget i Lillesand.', fapps='Apper', fco='Selskap', orgl='Org.nr.', sec_apps='Apper', sec_co='Selskapet',
 f=[('Foretak','Knudegaard Apps'),('Bransje','Applikasjonsutvikling'),('Adresse','Eineråsen 21D, 4790 Lillesand, Norge'),('Org.nr.','938 917 523'),('Etablert','2026'),('Plattformer','iPhone, iPad og Android')],
 h='Kontakt oss', clead='Spørsmål om en app, samarbeid eller noe annet? Skriv til oss, så svarer vi så fort vi kan.',
 name='Navn', email='E-post', msg='Melding', send='Send melding', sending='Sender …',
 ok='Takk! Meldingen er sendt, og vi svarer så fort vi kan.', err='Noe gikk galt. Prøv igjen litt senere.',
 subject='Ny melding fra knudegaard.no', themel='Bytt mellom lyst og mørkt utseende', privacy='Personvern', privpath='personvern.html'),
'en':dict(file='en/index.html',p='../',lang='en',other='../',otherlabel='Norsk',title='Knudegaard Apps – app development in Lillesand, Norway',
 desc='Knudegaard Apps builds apps for iPhone, iPad and Android. Thoughtful apps with no ads and no unnecessary data collection.',
 eyebrow='Application development from Lillesand, Norway',
 h1a='Apps that make everyday life', h1b='a little easier.',
 lead='We build apps for iPhone, iPad and Android. Calm, thoughtful and ad-free, and they never collect more data than they need.',
 cta1='See the apps', cta2='Contact us',
 v=[('noads','No ads','Our apps earn money by being good, not by selling your attention.'),('lock','Privacy first','As much as possible happens on your phone. We never sell data.'),('pin','Made in Norway','Built in Lillesand, for people all over the world.')],
 apps='Our apps', appslead='Small tools and games, each with one clear job.',
 sk='Scan documents, have them read aloud and listen while you do something else.', lt='Tidy your photo library fast: duplicates, screenshots and large videos.', wa='A word game where you build a bridge of words across the board. In English and Norwegian.',
 oh='You’re the fish. Swim up from the reef, dodge hooks and nets, and collect 24 fish, most with a power of their own.',
 live='On the App Store', soon='Coming soon', visit='Visit the website →',
 ios='iPhone and iPad', android='Android', st_live='On the App Store', st_test='In testing', st_later='Coming later',
 ios_sum='Skanlio, Lumtidy and Wordarc are on the App Store. Off the Hook is coming soon.', android_sum='Skanlio, Lumtidy, Wordarc and Off the Hook are in testing now.',
 company='Company details', colead='Knudegaard Apps is a Norwegian sole proprietorship that builds and publishes its own apps.', nav=('Apps','About','Contact'), tagline='Small, thoughtful apps with no ads. Made in Lillesand, Norway.', fapps='Apps', fco='Company', orgl='Org. no.', sec_apps='Apps', sec_co='Company',
 f=[('Company','Knudegaard Apps'),('Industry','Application development'),('Address','Eineråsen 21D, 4790 Lillesand, Norway'),('Org. no.','938 917 523'),('Founded','2026'),('Platforms','iPhone, iPad and Android')],
 h='Contact us', clead='Questions about an app, a partnership or anything else? Write to us and we’ll get back to you as soon as we can.',
 name='Name', email='Email', msg='Message', send='Send message', sending='Sending …',
 ok='Thank you! Your message has been sent, and we’ll reply as soon as we can.', err='Something went wrong. Please try again later.',
 subject='New message from knudegaard.no', themel='Switch between light and dark appearance', privacy='Privacy', privpath='privacy.html'),
}
ICON={
 'noads':'<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
 'lock':'<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
 'pin':'<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'}
def svg(k): return f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>'
for k,t in T.items():
    p=t['p']
    vals=''.join(f'<div class="value reveal"><span class="vicon" aria-hidden="true">{svg(e)}</span><h3>{a}</h3><p>{b}</p></div>' for e,a,b in t['v'])
    facts=''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in t['f'])
    ST={'live':('live',t['st_live']),'test':('test',t['st_test']),'soon':('soon',t['soon']),'later':('',t['st_later'])}
    def chip(label,status):
        c,s=ST[status]
        return f'<li class="plat {c}"><span>{label}</span><b>{s}</b></li>'
    def card(cls,img,name,text,url,ios,android):
        return f'''<a class="app {cls} reveal" href="{url}">
  <div class="apphead"><img src="{p}assets/{img}.png" alt="" width="56" height="56"><strong>{name}</strong><span class="arrow" aria-hidden="true">→</span></div>
  <p>{text}</p>
  <ul class="plats">{chip(t['ios'],ios)}{chip(t['android'],android)}</ul>
</a>'''
    html=f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="theme-color" content="#071c31">
<script>try{{var m=localStorage.getItem('theme');if(m)document.documentElement.dataset.theme=m}}catch(e){{}}</script>
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}style.css?v=9">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Knudegaard Apps","address":{{"@type":"PostalAddress","streetAddress":"Eineråsen 21D","postalCode":"4790","addressLocality":"Lillesand","addressCountry":"NO"}},"identifier":"938917523"}}</script>
</head>
<body>
<header class="topbar"><div class="wrap bar">
  <a class="brand" href="{p if p else './'}"><img class="mark" src="{p}assets/logo.svg" alt="" width="40" height="40">Knudegaard Apps</a>
  <nav><a class="hide-sm" href="#apper">{t['nav'][0]}</a><a class="hide-sm" href="#selskap">{t['nav'][1]}</a><a class="hide-sm" href="#kontakt">{t['nav'][2]}</a><button class="theme" type="button" aria-label="{t['themel']}" title="{t['themel']}"><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg></button><a class="lang" href="{t['other']}">{t['otherlabel']}</a></nav>
</div></header>
<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
  <div class="wrap">
    <div class="herogrid">
      <div>
        <p class="eyebrow">{t['eyebrow']}</p>
        <h1>{t['h1a']} <span class="grad">{t['h1b']}</span></h1>
        <p class="lead">{t['lead']}</p>
        <div class="ctas"><a class="btn primary" href="#apper">{t['cta1']}</a><a class="btn ghost" href="#kontakt">{t['cta2']}</a></div>
      </div>
      <div class="stack" aria-hidden="true">
        <img class="i1" src="{p}assets/skanlio.png" alt="">
        <img class="i2" src="{p}assets/lumtidy.png" alt="">
        <img class="i3" src="{p}assets/wordarc.png" alt="">
      </div>
    </div>
  </div>
</section>
<main class="wrap">
  <section class="values">{vals}</section>

  <div class="sechead reveal" id="apper"><h2>{t['apps']}</h2><p class="sublead">{t['appslead']}</p></div>
  <div class="apps">
    {card('skanlio','skanlio','Skanlio',t['sk'],'https://skanlio.app/','live','test')}
    {card('lumtidy','lumtidy','Lumtidy',t['lt'],'https://lumtidy.app/','live','test')}
    {card('wordarc','wordarc','Wordarc',t['wa'],'https://wordarc.app/','live','test')}
    {card('offthehook','offthehook','Off the Hook',t['oh'],p+'offthehook/','soon','test')}
  </div>

  <div class="twocol">
    <section class="reveal" id="selskap">
      <h2>{t['company']}</h2>
      <p class="sublead">{t['colead']}</p>
      <dl class="facts">{facts}</dl>
    </section>
    <section class="reveal">
      <h2 id="kontakt">{t['h']}</h2>
      <p class="sublead">{t['clead']}</p>
      <form class="contact" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="{KEY}">
        <input type="hidden" name="subject" value="{t['subject']}">
        <input type="hidden" name="from_name" value="knudegaard.no">
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="row2"><label>{t['name']}<input name="name" autocomplete="name" required maxlength="100"></label>
        <label>{t['email']}<input type="email" name="email" autocomplete="email" required maxlength="200"></label></div>
        <label>{t['msg']}<textarea name="message" rows="5" required maxlength="5000"></textarea></label>
        <button type="submit">{t['send']}</button>
        <p class="status" role="status" aria-live="polite"></p>
      </form>
    </section>
  </div>
</main>
<footer class="site"><div class="wrap">
  <div class="fgrid">
    <div class="fbrand"><a class="brand" href="{p if p else './'}"><img class="mark" src="{p}assets/logo.svg" alt="" width="36" height="36">Knudegaard Apps</a><p>{t['tagline']}</p></div>
    <div><h4>{t['fapps']}</h4><a href="https://skanlio.app/">Skanlio</a><a href="https://lumtidy.app/">Lumtidy</a><a href="https://wordarc.app/">Wordarc</a><a href="{p}offthehook/">Off the Hook</a></div>
    <div><h4>{t['fco']}</h4><a href="#kontakt">{t['nav'][2]}</a><a href="{t['privpath']}">{t['privacy']}</a><a href="{t['other']}">{t['otherlabel']}</a></div>
  </div>
  <div class="fbottom"><span>© 2026 Knudegaard Apps</span><span>{t['orgl']} 938 917 523 · Eineråsen 21D, 4790 Lillesand</span></div>
</div></footer>
<script>
document.querySelector('.theme').addEventListener('click', () => {{
  const r = document.documentElement, dark = r.dataset.theme ? r.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  r.dataset.theme = dark ? 'light' : 'dark';
  try {{ localStorage.setItem('theme', r.dataset.theme); }} catch (e) {{}}
}});
const tb = document.querySelector('.topbar'), onS = () => tb.classList.toggle('scrolled', scrollY > 12); addEventListener('scroll', onS, {{ passive: true }}); onS();
const io = 'IntersectionObserver' in window ? new IntersectionObserver((es) => es.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}), {{ threshold: 0.12 }}) : null;
document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('in'));
document.querySelector('form.contact').addEventListener('submit', async (e) => {{
  e.preventDefault();
  const f = e.target, b = f.querySelector('button'), s = f.querySelector('.status');
  b.disabled = true; b.textContent = '{t['sending']}'; s.textContent = ''; s.className = 'status';
  try {{
    const r = await fetch(f.action, {{ method: 'POST', headers: {{ 'Accept': 'application/json' }}, body: new FormData(f) }});
    const j = await r.json();
    if (!r.ok || !j.success) throw new Error();
    f.reset(); s.textContent = '{t['ok']}'; s.classList.add('ok');
  }} catch {{
    s.textContent = '{t['err']}'; s.classList.add('err');
  }} finally {{
    b.disabled = false; b.textContent = '{t['send']}';
  }}
}});
</script>
</body>
</html>
'''
    open(t['file'],'w').write(html)

# Personvernsidene får ny topp og favicon, innholdet beholdes
import re
for f,p in [('personvern.html',''),('en/privacy.html','../')]:
    s=open(f).read()
    s=s.replace(f'<link rel="stylesheet" href="{p}style.css?v=3">',f'<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png"><link rel="stylesheet" href="{p}style.css?v=3">',1) if 'favicon' not in s else s
    s=s.replace('<body><div class="wrap">','<body class="plain"><div class="wrap">')
    if "localStorage.getItem('theme')" not in s:
        s=s.replace('</title>',"</title><script>try{var m=localStorage.getItem('theme');if(m)document.documentElement.dataset.theme=m}catch(e){}</script>",1)
    open(f,'w').write(s)
import shutil; shutil.copy('assets/logo.svg','assets/favicon.svg')
