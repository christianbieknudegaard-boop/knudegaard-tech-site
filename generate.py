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
 v=[('🚫','Ingen reklame','Appene våre tjener penger på at de er gode, ikke på oppmerksomheten din.'),('🔒','Personvern først','Mest mulig skjer på telefonen din. Vi selger aldri data.'),('🇳🇴','Laget i Norge','Utviklet i Lillesand, for brukere over hele verden.')],
 apps='Våre apper', appslead='Små verktøy og spill, hver med én tydelig jobb.',
 sk='Skann dokumenter, få dem lest høyt og lytt mens du gjør noe annet.', lt='Rydd bildebiblioteket raskt: duplikater, skjermbilder og store videoer.', wa='Ordspill der du bygger en bro av ord tvers over brettet. På norsk og engelsk.',
 oh='Du er fisken. Svøm opp fra korallrevet, unngå kroker og garn, og samle 24 fisker, de fleste med sin egen kraft.',
 live='I App Store', soon='Kommer snart', visit='Besøk nettsiden →',
 ios='iPhone og iPad', android='Android', st_live='I App Store', st_test='I testing', st_later='Kommer senere',
 ios_sum='Skanlio, Lumtidy og Wordarc ligger i App Store. Off the Hook kommer snart.', android_sum='Skanlio, Lumtidy, Wordarc og Off the Hook er i testing nå.',
 company='Om selskapet',
 f=[('Foretak','Knudegaard Apps'),('Bransje','Applikasjonsutvikling'),('Adresse','Eineråsen 21D, 4790 Lillesand, Norge'),('Org.nr.','938 917 523')],
 h='Kontakt oss', clead='Spørsmål om en app, samarbeid eller noe annet? Skriv til oss, så svarer vi så fort vi kan.',
 name='Navn', email='E-post', msg='Melding', send='Send melding', sending='Sender …',
 ok='Takk! Meldingen er sendt, og vi svarer så fort vi kan.', err='Noe gikk galt. Prøv igjen litt senere.',
 subject='Ny melding fra knudegaard.no', privacy='Personvern', privpath='personvern.html'),
'en':dict(file='en/index.html',p='../',lang='en',other='../',otherlabel='Norsk',title='Knudegaard Apps – app development in Lillesand, Norway',
 desc='Knudegaard Apps builds apps for iPhone, iPad and Android. Thoughtful apps with no ads and no unnecessary data collection.',
 eyebrow='Application development from Lillesand, Norway',
 h1a='Apps that make everyday life', h1b='a little easier.',
 lead='We build apps for iPhone, iPad and Android. Calm, thoughtful and ad-free, and they never collect more data than they need.',
 cta1='See the apps', cta2='Contact us',
 v=[('🚫','No ads','Our apps earn money by being good, not by selling your attention.'),('🔒','Privacy first','As much as possible happens on your phone. We never sell data.'),('🇳🇴','Made in Norway','Built in Lillesand, for people all over the world.')],
 apps='Our apps', appslead='Small tools and games, each with one clear job.',
 sk='Scan documents, have them read aloud and listen while you do something else.', lt='Tidy your photo library fast: duplicates, screenshots and large videos.', wa='A word game where you build a bridge of words across the board. In English and Norwegian.',
 oh='You’re the fish. Swim up from the reef, dodge hooks and nets, and collect 24 fish, most with a power of their own.',
 live='On the App Store', soon='Coming soon', visit='Visit the website →',
 ios='iPhone and iPad', android='Android', st_live='On the App Store', st_test='In testing', st_later='Coming later',
 ios_sum='Skanlio, Lumtidy and Wordarc are on the App Store. Off the Hook is coming soon.', android_sum='Skanlio, Lumtidy, Wordarc and Off the Hook are in testing now.',
 company='Company details',
 f=[('Company','Knudegaard Apps'),('Industry','Application development'),('Address','Eineråsen 21D, 4790 Lillesand, Norway'),('Org. no.','938 917 523')],
 h='Contact us', clead='Questions about an app, a partnership or anything else? Write to us and we’ll get back to you as soon as we can.',
 name='Name', email='Email', msg='Message', send='Send message', sending='Sending …',
 ok='Thank you! Your message has been sent, and we’ll reply as soon as we can.', err='Something went wrong. Please try again later.',
 subject='New message from knudegaard.no', privacy='Privacy', privpath='privacy.html'),
}
for k,t in T.items():
    p=t['p']
    vals=''.join(f'<div class="value reveal"><span class="vicon" aria-hidden="true">{e}</span><h3>{a}</h3><p>{b}</p></div>' for e,a,b in t['v'])
    facts=''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in t['f'])
    ST={'live':('live',t['st_live']),'test':('test',t['st_test']),'soon':('soon',t['soon']),'later':('',t['st_later'])}
    def chip(label,status):
        c,s=ST[status]
        return f'<li class="plat {c}"><span>{label}</span><b>{s}</b></li>'
    def card(cls,img,name,text,url,ios,android):
        return f'''<a class="app {cls} reveal" href="{url}">
  <img src="{p}assets/{img}.png" alt="">
  <div class="apptext"><div class="apphead"><strong>{name}</strong></div><p>{text}</p>
  <ul class="plats">{chip(t['ios'],ios)}{chip(t['android'],android)}</ul>
  <span class="visit">{t['visit']}</span></div>
</a>'''
    html=f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="theme-color" content="#071c31">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}style.css?v=4">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Knudegaard Apps","address":{{"@type":"PostalAddress","streetAddress":"Eineråsen 21D","postalCode":"4790","addressLocality":"Lillesand","addressCountry":"NO"}},"identifier":"938917523"}}</script>
</head>
<body>
<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
  <div class="wrap">
    <header>
      <a class="brand" href="{p if p else './'}"><img class="mark" src="{p}assets/logo.svg" alt="" width="32" height="32">Knudegaard Apps</a>
      <a class="lang" href="{t['other']}">{t['otherlabel']}</a>
    </header>
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

  <h2 id="apper" class="reveal">{t['apps']}</h2>
  <p class="sublead reveal">{t['appslead']}</p>
  <div class="platsum reveal">
    <div class="ps ios"><strong>{t['ios']}</strong><span>{t['ios_sum']}</span></div>
    <div class="ps android"><strong>{t['android']}</strong><span>{t['android_sum']}</span></div>
  </div>
  <div class="apps">
    {card('skanlio','skanlio','Skanlio',t['sk'],'https://skanlio.app/','live','test')}
    {card('lumtidy','lumtidy','Lumtidy',t['lt'],'https://lumtidy.app/','live','test')}
    {card('wordarc','wordarc','Wordarc',t['wa'],'https://wordarc.app/','live','test')}
    {card('offthehook','offthehook','Off the Hook',t['oh'],p+'offthehook/','soon','test')}
  </div>

  <div class="twocol">
    <section class="reveal">
      <h2>{t['company']}</h2>
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
        <label>{t['name']}<input name="name" autocomplete="name" required maxlength="100"></label>
        <label>{t['email']}<input type="email" name="email" autocomplete="email" required maxlength="200"></label>
        <label>{t['msg']}<textarea name="message" rows="5" required maxlength="5000"></textarea></label>
        <button type="submit">{t['send']}</button>
        <p class="status" role="status" aria-live="polite"></p>
      </form>
    </section>
  </div>
</main>
<footer class="wrap">
  <span>© 2026 Knudegaard Apps · Lillesand</span>
  <a href="{t['privpath']}">{t['privacy']}</a>
</footer>
<script>
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
    open(f,'w').write(s)
import shutil; shutil.copy('assets/logo.svg','assets/favicon.svg')
