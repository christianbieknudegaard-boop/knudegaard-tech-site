"""Builds the Off the Hook pages (English at the root, Norwegian in nb/). Run: python3 generate.py"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

BASE = 'https://knudegaard.no/offthehook/'
UPDATED = {'en': '25 November 2026', 'nb': '25. november 2026'}

# id, name, rarity (0 common, 1 rare, 2 epic, 3 legendary), power (en, nb)
FISH = [
    ('clown', 'Clownfish', 0, ('The escape artist you start with', 'Rømningseksperten du starter med')),
    ('tang', 'Blue Tang', 0, ('Extra slim, harder to hook', 'Ekstra slank, vanskeligere å hekte')),
    ('angel', 'Angelfish', 0, ('Golden lures twice as often', 'Dobbelt så mange gullsluker')),
    ('puffer', 'Puffer', 0, ('Shrugs off the first hit', 'Tåler det første treffet')),
    ('betta', 'Betta', 0, ('The flashiest fins in the sea', 'De flotteste finnene i havet')),
    ('octo', 'Octopus', 1, ('Grabs pearls from twice as far', 'Henter perler dobbelt så langt unna')),
    ('dolphin', 'Dolphin', 1, ('Close calls pay double', 'Nestentreff gir dobbelt')),
    ('turtle', 'Sea Turtle', 1, ('An extra heart every run', 'Et ekstra hjerte hver runde')),
    ('ray', 'Manta Ray', 1, ('Power-ups last 50% longer', 'Krefter varer 50 % lenger')),
    ('seahorse', 'Seahorse', 1, ('Makes friends twice as fast', 'Får venner dobbelt så fort')),
    ('mandarin', 'Mandarin Fish', 1, ('Close-call combos pay double', 'Nestentreff-kombo gir dobbelt')),
    ('axolotl', 'Axolotl', 1, ('Comes back to life once a run', 'Kommer tilbake til livet én gang')),
    ('shark', 'Shark', 2, ('Bites through a hook every 12 s', 'Biter over en krok hvert 12. sekund')),
    ('lion', 'Lionfish', 2, ('Rips through the first net', 'River seg gjennom det første garnet')),
    ('angler', 'Anglerfish', 2, ('Lures in twice the power-ups', 'Lokker til seg dobbelt så mange krefter')),
    ('eel', 'Electric Eel', 2, ('Immune to jellyfish', 'Immun mot maneter')),
    ('sword', 'Swordfish', 2, ('Starts every run at turbo speed', 'Starter hver runde i turbofart')),
    ('koi', 'Koi', 2, ('FRENZY twice as often', 'FRENZY dobbelt så ofte')),
    ('flying', 'Flying Fish', 2, ('Leaps over a hook every 15 s', 'Hopper over en krok hvert 15. sekund')),
    ('hammer', 'Hammerhead', 2, ('Bites a hook every 8 s', 'Biter over en krok hvert 8. sekund')),
    ('beluga', 'Beluga', 2, ('Up to 5 friends at once', 'Opptil 5 venner samtidig')),
    ('narwhal', 'Narwhal', 3, ('Snaps a hook every 6 s', 'Knekker en krok hvert 6. sekund')),
    ('orca', 'Orca', 3, ('Starts big and bites hooks', 'Starter stor og biter over kroker')),
    ('goldkoi', 'Golden Koi', 3, ('Every pearl is worth double', 'Hver perle er verdt det dobbelte')),
]
RARITY = {'en': ['COMMON', 'RARE', 'EPIC', 'LEGENDARY'], 'nb': ['VANLIG', 'SJELDEN', 'EPISK', 'LEGENDARISK']}
POWERED = sum(1 for f in FISH if f[0] not in ('clown', 'betta'))

T = {
'en': dict(
    lang='en', p='', other='nb/', home='./', locale='en_US',
    pages=dict(index='index.html', support='support.html', privacy='privacy.html', terms='terms.html'),
    other_pages=dict(index='nb/', support='nb/hjelp.html', privacy='nb/personvern.html', terms='nb/vilkar.html'),
    nav_play='How to play', nav_fish='Fish', nav_full='Full version', nav_support='Support', nav_privacy='Privacy', nav_terms='Terms of Use', nav_home='Home',
    title='Off the Hook – You’re the fish. Don’t get caught.',
    desc='Off the Hook is an underwater escape game for iPhone. Swim up from the coral reef to the deep, dodge hooks, nets and trawlers, and collect 24 fish. No ads.',
    h1a='You’re the fish.', h1b='Don’t get caught.',
    lead='Swim up from the coral reef to the deep. Slip between hooks, nets, traps and trawlers, collect pearls and unlock a whole ocean of fish with their own powers.',
    cta='Coming soon to the App Store', note='Free · For iPhone · No ads',
    shots=[('01-reef', 'Dodging hooks and nets on the coral reef'), ('02-kelp', 'Swimming up through the kelp forest'), ('03-deep', 'Glowing plants and jellyfish in the deep'),
           ('04-home', 'The home screen'), ('05-gameover', 'Netted! The result after a run'), ('06-daily', 'Daily gift and missions'), ('07-shop', 'The shop with the full version and the fish collection')],
    promises=[('No ads. Ever.', 'Not between runs, not for extra lives, not anywhere.'), ('Free to play', 'The whole ocean, 12 fish, daily missions and the leaderboard are free.'),
              ('One purchase', 'The full version is a single payment. No subscription, no coins to buy.'), ('Private', 'No account, no tracking. Your progress stays on your iPhone.')],
    play_h='How to play', play_sub='One finger. Easy to learn in seconds, hard to put down.',
    steps=[('Swipe to steer', 'Slide your finger left and right. Your fish always swims up.'),
           ('Dodge everything', 'Hooks, nets, lobster traps, jellyfish and the dreaded trawler. Brush past a hook for a close-call bonus.'),
           ('Grow bigger', 'Eat pearls and snatch the bait to grow. A bigger fish earns a bigger pearl multiplier.'),
           ('Spell FRENZY', 'Collect all six letters and go wild: faster, stronger and worth more.')],
    zones_h='Four zones, one long swim', zones_sub='The deeper you go, the darker and trickier it gets.',
    zones=[('0 m', 'Coral Reef', 'Bright, warm and full of colour.'), ('300 m', 'Kelp Forest', 'Weave through swaying kelp.'),
           ('700 m', 'Open Sea', 'Nets and trawlers, nowhere to hide.'), ('1200 m', 'The Deep', 'Glowing plants and jellyfish in the dark.')],
    feat_h='Lots to discover', feat_sub='Every run is different.',
    feats=[('🫧', 'Power-ups', 'Bubble shield, pearl magnet and turbo. Grab them on the way up.'),
           ('🐠', 'Fish friends', 'Rescue little fish and they swim with you and help collect pearls.'),
           ('🎁', 'Daily gift and missions', 'Three new missions every day and a gift that grows with your streak.'),
           ('🏆', 'Game Center', 'Climb the leaderboard for best distance and unlock eight achievements.'),
           ('⚡', 'Upgrades', 'Spend pearls on a stronger magnet, extra hearts, golden bait and longer power-ups.'),
           ('📸', 'Share your run', 'Show off your best run with a share card for friends.')],
    fish_h='24 fish to collect', fish_sub=f'Start as a little clownfish. Buy fish with pearls or earn them by playing. {POWERED} of them have their own power.',
    full_h='Full version', full_sub='Off the Hook is free, with no ads. If you love it, the full version opens up the rest of the ocean for a single payment.',
    free_t='Free', free_per='Everything you need to play',
    free=['All four zones', '12 common and rare fish', 'Daily gift and missions', 'Upgrades, power-ups and fish friends', 'Game Center leaderboard and achievements'],
    full_t='Full version', full_per='One-time purchase · no subscription',
    full=['All 12 epic and legendary fish <span>(Shark, Narwhal, Orca, Golden Koi …)</span>', 'Double pearls from every run', '+1000 pearls right away', 'Restore on all your devices <span>(and with Family Sharing)</span>'],
    footer='Made in Norway by', company='Knudegaard Apps',
),
'nb': dict(
    lang='nb', p='../', other='../', home='./', locale='nb_NO',
    pages=dict(index='index.html', support='hjelp.html', privacy='personvern.html', terms='vilkar.html'),
    other_pages=dict(index='../', support='../support.html', privacy='../privacy.html', terms='../terms.html'),
    nav_play='Slik spiller du', nav_fish='Fisker', nav_full='Fullversjon', nav_support='Hjelp', nav_privacy='Personvern', nav_terms='Vilkår', nav_home='Forside',
    title='Off the Hook – Du er fisken. Ikke bli fanget.',
    desc='Off the Hook er et undervannsspill for iPhone. Svøm fra korallrevet til dypet, unngå kroker, garn og tråler, og samle 24 fisker. Ingen reklame.',
    h1a='Du er fisken.', h1b='Ikke bli fanget.',
    lead='Svøm opp fra korallrevet til dypet. Smett mellom kroker, garn, teiner og trålere, samle perler og lås opp et helt hav av fisker med egne krefter.',
    cta='Kommer snart i App Store', note='Gratis · For iPhone · Ingen reklame',
    shots=[('01-reef', 'Unngå kroker og garn på korallrevet'), ('02-kelp', 'Opp gjennom tareskogen'), ('03-deep', 'Lysende planter og maneter i dypet'),
           ('04-home', 'Startskjermen'), ('05-gameover', 'Fanget i garnet! Resultatet etter en runde'), ('06-daily', 'Daglig gave og oppdrag'), ('07-shop', 'Butikken med fullversjonen og fiskesamlingen')],
    promises=[('Ingen reklame. Aldri.', 'Ikke mellom rundene, ikke for ekstra liv, ingen steder.'), ('Gratis å spille', 'Hele havet, 12 fisker, daglige oppdrag og topplisten er gratis.'),
              ('Ett kjøp', 'Fullversjonen er én betaling. Ingen abonnement, ingen mynter å kjøpe.'), ('Privat', 'Ingen konto, ingen sporing. Fremgangen blir på iPhonen din.')],
    play_h='Slik spiller du', play_sub='Én finger. Lært på sekunder, vanskelig å legge fra seg.',
    steps=[('Sveip for å styre', 'Dra fingeren til venstre og høyre. Fisken svømmer alltid oppover.'),
           ('Unngå alt', 'Kroker, garn, hummerteiner, maneter og den fryktede tråleren. Snei forbi en krok for nestentreff-bonus.'),
           ('Bli større', 'Spis perler og napp agnet for å vokse. En større fisk gir høyere perlemultiplikator.'),
           ('Stav FRENZY', 'Samle alle seks bokstavene og gå amok: raskere, sterkere og mer verdt.')],
    zones_h='Fire soner, én lang svømmetur', zones_sub='Jo dypere du kommer, jo mørkere og vanskeligere blir det.',
    zones=[('0 m', 'Korallrevet', 'Lyst, varmt og fullt av farger.'), ('300 m', 'Tareskogen', 'Svøm mellom vaiende tare.'),
           ('700 m', 'Åpent hav', 'Garn og trålere, ingen steder å gjemme seg.'), ('1200 m', 'Dypet', 'Lysende planter og maneter i mørket.')],
    feat_h='Mye å oppdage', feat_sub='Hver runde er forskjellig.',
    feats=[('🫧', 'Krefter', 'Bobleskjold, perlemagnet og turbo. Plukk dem opp på vei opp.'),
           ('🐠', 'Fiskevenner', 'Redd små fisker, så svømmer de med deg og hjelper til med perlene.'),
           ('🎁', 'Daglig gave og oppdrag', 'Tre nye oppdrag hver dag og en gave som vokser med rekken din.'),
           ('🏆', 'Game Center', 'Klatre på topplisten for lengste distanse og lås opp åtte prestasjoner.'),
           ('⚡', 'Oppgraderinger', 'Bruk perler på sterkere magnet, ekstra hjerter, gullagn og krefter som varer lenger.'),
           ('📸', 'Del runden', 'Vis frem den beste runden din med et delekort til venner.')],
    fish_h='24 fisker å samle', fish_sub=f'Start som en liten klovnefisk. Kjøp fisker for perler eller tjen dem ved å spille. {POWERED} av dem har sin egen kraft.',
    full_h='Fullversjon', full_sub='Off the Hook er gratis og uten reklame. Liker du det, åpner fullversjonen resten av havet for én betaling.',
    free_t='Gratis', free_per='Alt du trenger for å spille',
    free=['Alle fire soner', '12 vanlige og sjeldne fisker', 'Daglig gave og oppdrag', 'Oppgraderinger, krefter og fiskevenner', 'Toppliste og prestasjoner i Game Center'],
    full_t='Fullversjon', full_per='Engangskjøp · ingen abonnement',
    full=['Alle 12 episke og legendariske fisker <span>(Shark, Narwhal, Orca, Golden Koi …)</span>', 'Dobbelt så mange perler fra hver runde', '+1000 perler med en gang', 'Gjenopprett på alle enhetene dine <span>(og med Familiedeling)</span>'],
    footer='Laget i Norge av', company='Knudegaard Apps',
),
}


def head(t, title, desc, page):
    p = t['p']
    en_url = BASE + ('' if page == 'index' else T['en']['pages'][page])
    nb_url = BASE + 'nb/' + ('' if page == 'index' else T['nb']['pages'][page])
    return f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}assets/og.png">
<meta property="og:locale" content="{t['locale']}">
<meta name="theme-color" content="#08345c">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="nb" href="{nb_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<link rel="icon" href="{p}assets/favicon.png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}style.css?v=2">
</head>
<body>
'''


def nav(t, page):
    pg = t['pages']
    cur = lambda k: ' aria-current="page"' if k == page else ''
    extra = ''
    if page == 'index':
        extra = (f'<a class="hide-sm" href="#play">{t["nav_play"]}</a>\n    <a class="hide-sm" href="#fish">{t["nav_fish"]}</a>\n    '
                 f'<a class="hide-sm" href="#full">{t["nav_full"]}</a>\n    ')
    en_cur = ' aria-current="page"' if t['lang'] == 'en' else ''
    nb_cur = ' aria-current="page"' if t['lang'] == 'nb' else ''
    other = t['other_pages'][page]
    en_link = other if t['lang'] == 'nb' else pg[page] if page != 'index' else './'
    nb_link = other if t['lang'] == 'en' else pg[page] if page != 'index' else './'
    return f'''<nav class="wrap"><div class="bar">
  <a class="logo" href="./"><img src="{t['p']}assets/icon-256.png" alt="">Off the Hook</a>
  <div class="links">
    {extra}<a href="{pg['support']}"{cur('support')}>{t['nav_support']}</a>
    <a class="hide-xs" href="{pg['privacy']}"{cur('privacy')}>{t['nav_privacy']}</a>
    <span class="langs"><a href="{en_link}"{en_cur} lang="en">EN</a> <a href="{nb_link}"{nb_cur} lang="nb">NO</a></span>
  </div>
</div></nav>
'''


def footer(t, page):
    pg = t['pages']
    links = [('index', './', t['nav_home']), ('support', pg['support'], t['nav_support']),
             ('privacy', pg['privacy'], t['nav_privacy']), ('terms', pg['terms'], t['nav_terms'])]
    ls = '\n    '.join(f'<a href="{h}">{n}</a>' for k, h, n in links if k != page)
    return f'''
<footer class="wrap">
  <div class="links">
    {ls}
  </div>
  © 2026 Off the Hook · {t['footer']} <a href="https://knudegaard.no/{'' if t['lang'] == 'nb' else 'en/'}">{t['company']}</a>
</footer>
</body>
</html>
'''


def index(t):
    p, lang = t['p'], t['lang']
    school = ''.join(f'<img src="{p}assets/fish/{i}.webp" alt="">' for i in ['tang', 'octo', 'puffer', 'clown', 'turtle', 'angel', 'seahorse'])
    shots = '\n      '.join(f'<img src="{p}assets/screens/{f}.webp" width="600" height="1304" loading="lazy" alt="{a}">' for f, a in t['shots'])
    promises = '\n      '.join(f'<div class="promise glass"><div class="tick">✓</div><div><b>{a}</b><span>{b}</span></div></div>' for a, b in t['promises'])
    steps = '\n      '.join(f'<div class="step glass"><b>{a}</b><span>{b}</span></div>' for a, b in t['steps'])
    zones = '\n      '.join(f'<div class="zone z{k + 1}"><small>{m}</small><b>{n}</b><span>{d}</span></div>' for k, (m, n, d) in enumerate(t['zones']))
    feats = '\n      '.join(f'<div class="card glass"><div class="ic" aria-hidden="true">{e}</div><h3>{a}</h3><p>{b}</p></div>' for e, a, b in t['feats'])
    fishes = '\n      '.join(
        f'<div class="fish glass r{r}"><img src="{p}assets/fish/{i}.webp" alt="" loading="lazy"><i>{RARITY[lang][r]}</i><b>{n}</b>'
        f'<span style="display:block;color:var(--muted);font-size:12.5px;line-height:1.35;margin-top:3px">{pw[0 if lang == "en" else 1]}</span></div>'
        for i, n, r, pw in FISH)
    free = ''.join(f'<li>{x}</li>' for x in t['free'])
    full = ''.join(f'<li>{x}</li>' for x in t['full'])
    return head(t, t['title'], t['desc'], 'index') + nav(t, 'index') + f'''
<main class="wrap">
  <header class="hero">
    <div class="school" aria-hidden="true">{school}</div>
    <h1>{t['h1a']}<br><span class="grad">{t['h1b']}</span></h1>
    <p class="lead">{t['lead']}</p>
    <span class="cta soon"> {t['cta']}</span>
    <p class="note">{t['note']}</p>
  </header>

  <section class="shots" aria-label="Screenshots">
    <div class="strip">
      {shots}
    </div>
  </section>

  <section>
    <div class="promises">
      {promises}
    </div>
  </section>

  <section id="play">
    <h2>{t['play_h']}</h2>
    <p class="sub">{t['play_sub']}</p>
    <div class="steps">
      {steps}
    </div>
  </section>

  <section id="zones">
    <h2>{t['zones_h']}</h2>
    <p class="sub">{t['zones_sub']}</p>
    <div class="zones">
      {zones}
    </div>
  </section>

  <section id="features">
    <h2>{t['feat_h']}</h2>
    <p class="sub">{t['feat_sub']}</p>
    <div class="grid">
      {feats}
    </div>
  </section>

  <section id="fish">
    <h2>{t['fish_h']}</h2>
    <p class="sub">{t['fish_sub']}</p>
    <div class="fishes">
      {fishes}
    </div>
  </section>

  <section id="full">
    <h2>{t['full_h']}</h2>
    <p class="sub">{t['full_sub']}</p>
    <div class="plus">
      <div class="tier glass">
        <h3>{t['free_t']}</h3>
        <div class="per">{t['free_per']}</div>
        <ul>{free}</ul>
      </div>
      <div class="tier glass best">
        <h3><span class="crown">♛ {t['full_t']}</span></h3>
        <div class="per">{t['full_per']}</div>
        <ul>{full}</ul>
      </div>
    </div>
  </section>
</main>
''' + footer(t, 'index')


def doc(t, page, title, desc, body):
    return head(t, f'{title} – Off the Hook', desc, page) + nav(t, page) + f'''
<main class="wrap">
  <article class="doc glass">
{body}
  </article>
</main>
''' + footer(t, page)


CONTACT = {'en': 'https://knudegaard.no/en/#kontakt', 'nb': 'https://knudegaard.no/#kontakt'}

SUPPORT = {
'en': ('Support', 'Help with Off the Hook: playing, the full version, Game Center and contact.', f'''    <h1>Support</h1>
    <p class="meta">We read every message and usually reply within a day or two.</p>
    <p class="summary">Write to us through the <a href="{CONTACT['en']}">contact form</a>. If something went wrong, tell us your iPhone model, iOS version and what happened. A screenshot helps a lot.</p>

    <h2>Playing</h2>
    <details><summary>How do I steer?</summary><p>Put a finger anywhere on the screen and slide it left or right. The fish follows your finger and always swims upward on its own.</p></details>
    <details><summary>What ends a run?</summary><p>Hooks, nets, lobster traps, jellyfish and trawlers all cost a heart. When you run out of hearts, you're caught. Extra hearts come from the Extra Fin upgrade and from fish like the Sea Turtle.</p></details>
    <details><summary>How do I get more pearls?</summary><p>Collect pearls on the way up, snatch the bait off hooks, brush past hooks for close-call bonuses and grow bigger for a higher multiplier. Daily missions and the daily gift give pearls too.</p></details>
    <details><summary>What is FRENZY?</summary><p>Collect the letters F-R-E-N-Z-Y during a run. When you have all six, your fish goes into a frenzy for a short time: faster, stronger and worth more.</p></details>
    <details><summary>How do fish powers work?</summary><p>{POWERED} of the 24 fish have their own power, shown on each fish in the shop. Some work all the time (like a smaller hitbox or double pearls), some protect you once per run (like the Puffer), and some recharge (like the Shark's bite). Powers that recharge or can be used up show a small badge at the top of the screen during a run.</p></details>
    <details><summary>How do I unlock a fish?</summary><p>Most fish are bought with pearls in the shop. Some are earned by playing, for example by swimming far or making fish friends. The shop shows how far along you are.</p></details>

    <h2>Full version</h2>
    <details><summary>What does the full version include?</summary><p>All 12 epic and legendary fish, double pearls from every run and 1000 bonus pearls right away. It is a single payment, not a subscription, and the game never shows ads either way.</p></details>
    <details><summary>I bought the full version but it's not active</summary><p>Open the Shop and tap “Restore purchase”. Make sure you're signed in with the same Apple Account you used to buy it. If the purchase is waiting for approval (Ask to Buy), it turns on as soon as it's approved.</p></details>
    <details><summary>Can my family use it?</summary><p>If Family Sharing is turned on, family members can restore the full version on their own devices.</p></details>
    <details><summary>How do I get a refund?</summary><p>Purchases are handled by Apple. You can request a refund at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p></details>

    <h2>Game Center</h2>
    <details><summary>The leaderboard doesn't open</summary><p>Open the Settings app → Game Center and make sure you're signed in, then open the game again and tap “Ranks”.</p></details>

    <h2>Data</h2>
    <details><summary>Will I lose my progress if I change phones?</summary><p>Your progress is stored on your iPhone and moves with it when you restore from an iCloud or computer backup. If you delete the game, the progress is deleted too. The full version can always be restored.</p></details>
    <details><summary>What do you know about me?</summary><p>Nothing. Off the Hook has no accounts and collects no data. Read the <a href="privacy.html">privacy policy</a> for details.</p></details>'''),
'nb': ('Hjelp', 'Hjelp med Off the Hook: spillet, fullversjonen, Game Center og kontakt.', f'''    <h1>Hjelp</h1>
    <p class="meta">Vi leser alle meldinger og svarer vanligvis innen en dag eller to.</p>
    <p class="summary">Skriv til oss via <a href="{CONTACT['nb']}">kontaktskjemaet</a>. Har noe gått galt, fortell hvilken iPhone og iOS-versjon du har og hva som skjedde. Et skjermbilde hjelper mye.</p>

    <h2>Spillet</h2>
    <details><summary>Hvordan styrer jeg?</summary><p>Sett en finger hvor som helst på skjermen og dra den til venstre eller høyre. Fisken følger fingeren og svømmer alltid oppover av seg selv.</p></details>
    <details><summary>Hva avslutter en runde?</summary><p>Kroker, garn, hummerteiner, maneter og trålere koster et hjerte. Når hjertene er brukt opp, er du fanget. Flere hjerter får du med oppgraderingen Extra Fin og fisker som havskilpadden.</p></details>
    <details><summary>Hvordan får jeg flere perler?</summary><p>Samle perler på vei opp, napp agnet av krokene, snei forbi kroker for nestentreff-bonus og bli større for høyere multiplikator. Daglige oppdrag og den daglige gaven gir også perler.</p></details>
    <details><summary>Hva er FRENZY?</summary><p>Samle bokstavene F-R-E-N-Z-Y i løpet av en runde. Når du har alle seks, går fisken amok en kort stund: raskere, sterkere og mer verdt.</p></details>
    <details><summary>Hvordan virker fiskenes krefter?</summary><p>{POWERED} av de 24 fiskene har sin egen kraft, som står på hver fisk i butikken. Noen virker hele tiden (som mindre treffflate eller doble perler), noen beskytter deg én gang per runde (som kulefisken), og noen lades opp igjen (som haiens bitt). Krefter som lades opp eller brukes opp vises med et lite merke øverst på skjermen mens du spiller.</p></details>
    <details><summary>Hvordan låser jeg opp en fisk?</summary><p>De fleste fiskene kjøpes for perler i butikken. Noen får du ved å spille, for eksempel ved å svømme langt eller få fiskevenner. Butikken viser hvor langt du har kommet.</p></details>

    <h2>Fullversjon</h2>
    <details><summary>Hva får jeg med fullversjonen?</summary><p>Alle 12 episke og legendariske fisker, dobbelt så mange perler fra hver runde og 1000 bonusperler med en gang. Det er én betaling, ikke et abonnement, og spillet viser aldri reklame uansett.</p></details>
    <details><summary>Jeg har kjøpt fullversjonen, men den er ikke aktiv</summary><p>Åpne butikken (Shop) og trykk «Restore purchase». Du må være logget inn med samme Apple-konto som du kjøpte med. Venter kjøpet på godkjenning (Spør om kjøp), slås det på så snart det er godkjent.</p></details>
    <details><summary>Kan familien min bruke den?</summary><p>Er Familiedeling slått på, kan familiemedlemmer gjenopprette fullversjonen på sine egne enheter.</p></details>
    <details><summary>Hvordan får jeg pengene tilbake?</summary><p>Kjøp håndteres av Apple. Du kan be om refusjon på <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p></details>

    <h2>Game Center</h2>
    <details><summary>Topplisten åpner ikke</summary><p>Åpne Innstillinger → Game Center og sjekk at du er logget inn. Åpne så spillet igjen og trykk «Ranks».</p></details>

    <h2>Data</h2>
    <details><summary>Mister jeg fremgangen hvis jeg bytter telefon?</summary><p>Fremgangen lagres på iPhonen og følger med når du gjenoppretter fra sikkerhetskopi i iCloud eller på datamaskinen. Sletter du spillet, slettes fremgangen også. Fullversjonen kan alltid gjenopprettes.</p></details>
    <details><summary>Hva vet dere om meg?</summary><p>Ingenting. Off the Hook har ingen kontoer og samler ikke inn data. Les <a href="personvern.html">personvernerklæringen</a> for detaljer.</p></details>'''),
}

PRIVACY = {
'en': ('Privacy Policy', 'Off the Hook collects no personal data. No ads, no tracking, no analytics.', f'''    <h1>Privacy Policy</h1>
    <p class="meta">Effective {UPDATED['en']}</p>
    <p class="summary"><b>In short:</b> Off the Hook collects no personal data. There are no accounts, no analytics, no ads and no tracking. Your progress and settings stay on your iPhone. The leaderboard goes through Apple's Game Center, and purchases through the App Store.</p>

    <h2>Who we are</h2>
    <p>Off the Hook is a game for iPhone made by Knudegaard Apps (org. no. 938 917 523), Eineråsen 21D, 4790 Lillesand, Norway. In this policy “we” means Knudegaard Apps. You can reach us through our <a href="{CONTACT['en']}">contact form</a>.</p>

    <h2>Data we collect</h2>
    <p>None. Off the Hook has no user accounts and no servers that receive your data. It contains no analytics, advertising or tracking SDKs, and we do not track you across apps or websites.</p>

    <h2>Stored on your iPhone</h2>
    <p>Your best distance, pearls, fish, upgrades, daily missions, daily-gift streak and sound settings are stored only in the app's private storage on your device. They are included in your normal iCloud or computer backup, which Apple handles, and removed if you delete the app.</p>

    <h2>Game Center</h2>
    <p>If you are signed in to Game Center, the game sends your best distance to the leaderboard and your achievement progress to Apple. Other players can see your Game Center name and score on the leaderboard. Signing in is handled by iOS, and Apple's <a href="https://www.apple.com/legal/privacy/">privacy policy</a> applies. You can turn Game Center off in Settings → Game Center.</p>

    <h2>Purchases</h2>
    <p>The full version is a one-time purchase handled entirely by Apple through the App Store. We never see your name, email address or payment details. Off the Hook only checks with Apple, on your device, whether the full version is active.</p>

    <h2>Children</h2>
    <p>Off the Hook is suitable for all ages and does not collect data from anyone, including children. Apple's parental controls (Screen Time) can limit purchases and Game Center.</p>

    <h2>Your rights</h2>
    <p>Because we don't hold any personal data about you, there is nothing for us to access, correct or delete. You can remove everything Off the Hook stores by deleting the app. You are welcome to contact us with any questions, and you can complain to the Norwegian Data Protection Authority (<a href="https://www.datatilsynet.no/en/">Datatilsynet</a>).</p>

    <h2>Changes</h2>
    <p>If we change this policy, we'll update this page and the date above. If a change ever means data about you leaves your device, we'll ask for your permission in the app first.</p>

    <h2>Contact</h2>
    <p><a href="{CONTACT['en']}">Contact form at knudegaard.no</a></p>'''),
'nb': ('Personvern', 'Off the Hook samler ikke inn personopplysninger. Ingen reklame, ingen sporing, ingen analyse.', f'''    <h1>Personvern</h1>
    <p class="meta">Gjelder fra {UPDATED['nb']}</p>
    <p class="summary"><b>Kort fortalt:</b> Off the Hook samler ikke inn personopplysninger. Ingen kontoer, ingen analyse, ingen reklame og ingen sporing. Fremgangen og innstillingene blir på iPhonen din. Topplisten går via Apples Game Center, og kjøp via App Store.</p>

    <h2>Hvem vi er</h2>
    <p>Off the Hook er et spill for iPhone laget av Knudegaard Apps (org.nr. 938 917 523), Eineråsen 21D, 4790 Lillesand. «Vi» betyr Knudegaard Apps. Du når oss via <a href="{CONTACT['nb']}">kontaktskjemaet</a>.</p>

    <h2>Hva vi samler inn</h2>
    <p>Ingenting. Off the Hook har ingen brukerkontoer og ingen servere som tar imot data om deg. Spillet inneholder ingen analyse-, reklame- eller sporingsverktøy, og vi sporer deg ikke på tvers av apper eller nettsider.</p>

    <h2>Lagret på iPhonen</h2>
    <p>Beste distanse, perler, fisker, oppgraderinger, daglige oppdrag, rekken for daglig gave og lydinnstillinger lagres bare i appens private lagring på enheten. De blir med i den vanlige sikkerhetskopien til iCloud eller datamaskinen, som Apple står for, og slettes hvis du sletter appen.</p>

    <h2>Game Center</h2>
    <p>Er du logget inn i Game Center, sender spillet beste distanse til topplisten og fremgang på prestasjoner til Apple. Andre spillere kan se Game Center-navnet og poengsummen din på topplisten. Innloggingen håndteres av iOS, og Apples <a href="https://www.apple.com/no/legal/privacy/">personvernerklæring</a> gjelder. Du kan slå av Game Center under Innstillinger → Game Center.</p>

    <h2>Kjøp</h2>
    <p>Fullversjonen er et engangskjøp som håndteres helt av Apple gjennom App Store. Vi ser aldri navn, e-postadresse eller betalingsinformasjon. Off the Hook sjekker bare med Apple, på enheten din, om fullversjonen er aktiv.</p>

    <h2>Barn</h2>
    <p>Off the Hook passer for alle aldre og samler ikke inn data fra noen, heller ikke barn. Apples foreldrekontroll (Skjermtid) kan begrense kjøp og Game Center.</p>

    <h2>Dine rettigheter</h2>
    <p>Vi har ingen personopplysninger om deg, så det finnes ingenting å gi innsyn i, rette eller slette. Du fjerner alt Off the Hook lagrer ved å slette appen. Ta gjerne kontakt med spørsmål, og du kan klage til <a href="https://www.datatilsynet.no/">Datatilsynet</a>.</p>

    <h2>Endringer</h2>
    <p>Endrer vi erklæringen, oppdaterer vi denne siden og datoen over. Skulle en endring bety at data om deg forlater enheten, spør vi om lov i appen først.</p>

    <h2>Kontakt</h2>
    <p><a href="{CONTACT['nb']}">Kontaktskjema på knudegaard.no</a></p>'''),
}

TERMS = {
'en': ('Terms of Use', 'Terms of use for Off the Hook and the full version.', f'''    <h1>Terms of Use</h1>
    <p class="meta">Effective {UPDATED['en']}</p>
    <p class="summary">Off the Hook is licensed to you under Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard Licensed Application End User License Agreement</a>. The points below add what is specific to Off the Hook.</p>

    <h2>Full version</h2>
    <ul>
      <li>The full version is a one-time, non-consumable in-app purchase. It is not a subscription and does not renew.</li>
      <li>Payment is charged to your Apple Account when you confirm the purchase. The price is shown in the App Store in your local currency before you buy.</li>
      <li>You can restore the full version on any device signed in with the same Apple Account, and with family members if Family Sharing is on.</li>
      <li>Refunds are handled by Apple under the App Store's terms.</li>
    </ul>

    <h2>Pearls</h2>
    <p>Pearls are earned in the game and can only be spent in the game. They can't be bought, sold or exchanged for money, and they have no value outside Off the Hook.</p>

    <h2>Game Center</h2>
    <p>The leaderboard and achievements use Apple's Game Center. Please play fair and don't use tools or tricks to cheat. Game Center's own terms apply to player names and profiles.</p>

    <h2>The app</h2>
    <p>We work hard to keep Off the Hook running well, but it is provided “as is”. Features may change over time. To the extent the law allows, we are not liable for indirect losses from using the app. Nothing in these terms limits your rights as a consumer under the law where you live.</p>

    <h2>Changes</h2>
    <p>If we change these terms, we'll update this page and the date above.</p>

    <h2>Contact</h2>
    <p>Knudegaard Apps, Eineråsen 21D, 4790 Lillesand, Norway · <a href="{CONTACT['en']}">contact form</a></p>'''),
'nb': ('Vilkår', 'Vilkår for bruk av Off the Hook og fullversjonen.', f'''    <h1>Vilkår for bruk</h1>
    <p class="meta">Gjelder fra {UPDATED['nb']}</p>
    <p class="summary">Off the Hook lisensieres til deg under Apples <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">standard lisensavtale for apper (EULA)</a>. Punktene under gjelder i tillegg for Off the Hook.</p>

    <h2>Fullversjon</h2>
    <ul>
      <li>Fullversjonen er et engangskjøp i appen. Det er ikke et abonnement og fornyes ikke.</li>
      <li>Beløpet trekkes fra Apple-kontoen din når du bekrefter kjøpet. Prisen vises i App Store i din valuta før du kjøper.</li>
      <li>Du kan gjenopprette fullversjonen på alle enheter med samme Apple-konto, og hos familiemedlemmer hvis Familiedeling er på.</li>
      <li>Refusjon håndteres av Apple etter App Stores vilkår.</li>
    </ul>

    <h2>Perler</h2>
    <p>Perler tjenes i spillet og kan bare brukes i spillet. De kan ikke kjøpes, selges eller veksles inn i penger, og har ingen verdi utenfor Off the Hook.</p>

    <h2>Game Center</h2>
    <p>Topplisten og prestasjonene bruker Apples Game Center. Spill rettferdig, og ikke bruk verktøy eller triks for å jukse. Game Centers egne vilkår gjelder for spillernavn og profiler.</p>

    <h2>Appen</h2>
    <p>Vi jobber for at Off the Hook skal fungere godt, men appen leveres «som den er». Funksjoner kan endres over tid. Så langt loven tillater, er vi ikke ansvarlige for indirekte tap ved bruk av appen. Ingenting i disse vilkårene begrenser dine rettigheter som forbruker.</p>

    <h2>Endringer</h2>
    <p>Endrer vi vilkårene, oppdaterer vi denne siden og datoen over.</p>

    <h2>Kontakt</h2>
    <p>Knudegaard Apps, Eineråsen 21D, 4790 Lillesand · <a href="{CONTACT['nb']}">kontaktskjema</a></p>'''),
}

for lang, t in T.items():
    d = '' if lang == 'en' else 'nb/'
    if d:
        os.makedirs(d, exist_ok=True)
    open(d + t['pages']['index'], 'w').write(index(t))
    for page, src in [('support', SUPPORT), ('privacy', PRIVACY), ('terms', TERMS)]:
        title, desc, body = src[lang]
        open(d + t['pages'][page], 'w').write(doc(t, page, title, desc, body))
print('ok')
