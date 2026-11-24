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
 live='I App Store', soon='Kommer snart', visit='Besøk nettsiden →',
 company='Om selskapet',
 f=[('Foretak','Knudegaard Apps'),('Bransje','Applikasjonsutvikling'),('Adresse','Eineråsen 21D, 4790 Lillesand, Norge')],
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
 live='On the App Store', soon='Coming soon', visit='Visit the website →',
 company='Company details',
 f=[('Company','Knudegaard Apps'),('Industry','Application development'),('Address','Eineråsen 21D, 4790 Lillesand, Norway')],
 h='Contact us', clead='Questions about an app, a partnership or anything else? Write to us and we’ll get back to you as soon as we can.',
 name='Name', email='Email', msg='Message', send='Send message', sending='Sending …',
 ok='Thank you! Your message has been sent, and we’ll reply as soon as we can.', err='Something went wrong. Please try again later.',
 subject='New message from knudegaard.no', privacy='Privacy', privpath='privacy.html'),
}
for k,t in T.items():
    p=t['p']
    vals=''.join(f'<div class="value reveal"><span class="vicon" aria-hidden="true">{e}</span><h3>{a}</h3><p>{b}</p></div>' for e,a,b in t['v'])
    facts=''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in t['f'])
    def card(cls,img,name,text,badge,url,live):
        return f'''<a class="app {cls} reveal" href="{url}">
  <img src="{p}assets/{img}.png" alt="">
  <div class="apptext"><div class="apphead"><strong>{name}</strong><em class="badge{' live' if live else ''}">{badge}</em></div><p>{text}</p><span class="visit">{t['visit']}</span></div>
</a>'''
    html=f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="theme-color" content="#0f1024">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{p}style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Knudegaard Apps","address":{{"@type":"PostalAddress","streetAddress":"Eineråsen 21D","postalCode":"4790","addressLocality":"Lillesand","addressCountry":"NO"}}}}</script>
</head>
<body>
<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
  <div class="wrap">
    <header>
      <a class="brand" href="{p if p else './'}"><span class="mark">K</span>Knudegaard Apps</a>
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
  <div class="apps">
    {card('skanlio','skanlio','Skanlio',t['sk'],t['live'],'https://skanlio.app/',True)}
    {card('lumtidy','lumtidy','Lumtidy',t['lt'],t['live'],'https://lumtidy.app/',True)}
    {card('wordarc','wordarc','Wordarc',t['wa'],t['live'],'https://wordarc.app/',True)}
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
    s=s.replace(f'<link rel="stylesheet" href="{p}style.css">',f'<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{p}style.css">',1) if 'favicon' not in s else s
    s=s.replace('<body><div class="wrap">','<body class="plain"><div class="wrap">')
    open(f,'w').write(s)
open('assets/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7b5cff"/><stop offset="1" stop-color="#22b8cf"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><text x="32" y="44" text-anchor="middle" font-family="-apple-system,Helvetica,Arial" font-weight="800" font-size="34" fill="#fff">K</text></svg>')
