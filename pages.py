#!/usr/bin/env python3
from build import page, crumbs, SITE

ICON = {
 "search":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6" stroke-linecap="round"/></svg>',
 "play":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="4"/><path d="M10.5 9.2l4.6 2.8-4.6 2.8z" fill="currentColor" stroke="none"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true"><path d="M4 5h6M4 5v14h12M4 12h7"/><path d="M14 5h6v9"/></svg>',
 "chat":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><circle cx="12" cy="13" r="7.5"/><circle cx="9.3" cy="12.6" r="1" fill="currentColor"/><circle cx="14.7" cy="12.6" r="1" fill="currentColor"/><path d="M9.4 16.2c1.6 1.1 3.6 1.1 5.2 0" stroke-linecap="round"/></svg>',
 "star":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.6l2.5 5.2 5.6.8-4 4 .9 5.6L12 16.6 7 19.2l.9-5.6-4-4 5.6-.8z"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.4 2.4 14.6 0 17M12 3.5c-2.4 2.4-2.4 14.6 0 17"/></svg>',
}

POPULAR = [("https://www.google.com","Google","search"),("https://www.youtube.com","YouTube","play"),
           ("https://www.wikipedia.org","Wikipedia","book"),("https://www.reddit.com","Reddit","chat")]
MORE = [("https://www.facebook.com","Facebook"),("https://www.instagram.com","Instagram"),
        ("https://www.tiktok.com","TikTok"),("https://web.telegram.org/a/","Telegram"),
        ("https://x.com","X"),("https://chatgpt.com","ChatGPT")]
NETWORK = [("https://1tenhost.com","1TenHost"),("https://aimpak.com","AimPaK"),
           ("https://jaffaretayyar.com","JaffareTayyar"),("https://uroojzaidi.com","UroojZaidi"),
           ("https://agentsify.co.uk","Agentsify")]

chips_pop = "".join('<button class="chip" type="button" data-site="%s">%s%s</button>' % (u, ICON[i], n)
                    for u, n, i in POPULAR)
chips_more = "".join('<button class="chip" type="button" data-site="%s">%s%s</button>' % (u, ICON["globe"], n)
                     for u, n in MORE)
chips_net = "".join('<button class="chip own" type="button" data-site="%s">%s%s</button>' % (u, ICON["star"], n)
                    for u, n in NETWORK)

CONSOLE = f"""
    <div class="console">
      <div class="row">
        <label class="url-wrap" for="url">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7L11.8 5"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7L12.2 19"/></svg>
          <input id="url" type="url" inputmode="url" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="https://1tenhost.com" aria-label="Website address to open through the proxy">
        </label>
        <div class="sel-wrap">
          <select id="server" aria-label="Proxy server location">
            <option value="us" data-city="Ashburn, US" data-pos="39.0438;-77.4874">&#127482;&#127480; United States</option>
            <option value="uk" data-city="London, UK" data-pos="51.5072;-0.1276">&#127468;&#127463; United Kingdom</option>
            <option value="de" selected data-city="Frankfurt, DE" data-pos="50.1109;8.6821">&#127465;&#127466; Germany</option>
            <option value="nl" data-city="Amsterdam, NL" data-pos="52.3676;4.9041">&#127475;&#127473; Netherlands</option>
            <option value="sg" data-city="Singapore, SG" data-pos="1.3521;103.8198">&#127480;&#127468; Singapore</option>
          </select>
        </div>
        <button class="go" id="go" type="button">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg>
          Open site
        </button>
      </div>
      <div class="qk"><span class="qk-label">Quick open</span><div class="chips">{chips_pop}</div></div>
      <button class="more-btn" type="button" aria-expanded="false" aria-controls="more-chips">More sites </button>
      <div class="chips more-chips" id="more-chips">{chips_more}</div>
      <div class="qk"><span class="qk-label">Our network</span><div class="chips">{chips_net}</div></div>
      <p class="status" id="status" role="status" aria-live="polite"></p>
      <p class="form-note">Sites open in a new tab. Pages that need a login, or that use heavy DRM, may refuse to load through any proxy \u2014 try a different exit location first.</p>
    </div>
"""

FAQ_ITEMS = [
 ("What is a web proxy?",
  "A web proxy is a server that loads a website on your behalf and passes the page back to your browser. Because the request leaves from the proxy rather than your device, the website sees the proxy's IP address, and your own network only sees a connection to the proxy. FreeWebProxy runs inside the browser tab you already have open, so there is nothing to install."),
 ("Is it free?",
  "Yes \u2014 no account, no trial window, no card details, no bandwidth meter and no daily session limit. It is funded by 1TenHost and offered as a public tool."),
 ("How does it protect my privacy?",
  "Traffic between your browser and the proxy is encrypted with TLS, so the network you are on sees an encrypted connection rather than the pages you read. The site you visit logs our exit node's IP instead of yours, and cookies stay sandboxed to the proxy session. We keep no browsing logs. A web proxy covers browser traffic only, so it is not a full replacement for a VPN on your whole device."),
 ("Do I need an app or a browser extension?",
  "No. Paste an address, choose a location, press open site. It works identically on desktop and mobile browsers."),
 ("Which server locations can I use?",
  "The United States (Ashburn), the United Kingdom (London), Germany (Frankfurt), the Netherlands (Amsterdam) and Singapore. Pick the nearest one for speed, or a specific country when a site restricts content by region."),
 ("Is using a proxy legal?",
  "Proxies are legal in most countries and are a normal privacy, testing and research tool. You remain responsible for the law where you are and for the rules of the networks and sites you use. Do not use this service for anything illegal."),
 ("Why did a site load badly or refuse to open?",
  "Some services \u2014 online banking, streaming platforms with hard DRM, and sites that block data-centre IP ranges \u2014 detect and reject proxied traffic by design. Switching to a different exit location sometimes helps. If it still fails, that site cannot be proxied."),
 ("Does the proxy work on mobile data and school Wi-Fi?",
  "Yes. Any network that lets you reach freewebproxy.aimpak.com over HTTPS will work, including 4G/5G mobile data, campus Wi-Fi and office networks."),
]

def faq_html(limit=None):
    items = FAQ_ITEMS[:limit] if limit else FAQ_ITEMS
    out = []
    for i, (q, a) in enumerate(items):
        out.append('<details%s><summary>%s</summary><p>%s</p></details>' % (" open" if i == 0 else "", q, a))
    return '<div class="faq">%s</div>' % "".join(out)

FAQ_SCHEMA = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in FAQ_ITEMS]}

SERVERS = [("\U0001F1FA\U0001F1F8","United States","Ashburn, Virginia","42 ms"),
           ("\U0001F1EC\U0001F1E7","United Kingdom","London","28 ms"),
           ("\U0001F1E9\U0001F1EA","Germany","Frankfurt am Main","21 ms"),
           ("\U0001F1F3\U0001F1F1","Netherlands","Amsterdam","24 ms"),
           ("\U0001F1F8\U0001F1EC","Singapore","Jurong East","67 ms")]
servers_html = '<div class="servers">%s</div>' % "".join(
    '<div class="srv"><span class="flag">%s</span><div><strong>%s</strong><small>%s</small></div><span class="ping">%s</span></div>' % s
    for s in SERVERS)

FEATURES = [
 ("lock","Hides your IP from the site","The destination server records our exit node's address, not the one your internet provider handed you."),
 ("shield","Gets past network filters","Your school, office or caf\u00e9 Wi-Fi sees one encrypted connection to this domain, not the sites you open inside it."),
 ("bolt","Loads in about a second","Pages stream through HTTP/3 edge nodes with Brotli compression. No queue, no throttling, no bandwidth cap."),
 ("globe","Five countries to route through","Switch your apparent location between the US, UK, Germany, the Netherlands and Singapore in one dropdown."),
 ("lines","Nothing written down","No account, no history, no stored URLs. Session cookies stay sandboxed and are dropped when you close the tab."),
 ("phone","Works the same on a phone","No extension, no APK, no profile to install. Any modern browser on Android, iOS, Windows, macOS or Linux."),
]
FICON = {
 "lock":'<path d="M4 10h16v10H4z"/><path d="M8.5 10V7a3.5 3.5 0 0 1 7 0"/>',
 "shield":'<path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6z"/><path d="M9.5 12.2l1.9 1.9 3.6-3.9"/>',
 "bolt":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/>',
 "lines":'<path d="M3 6h18M3 12h18M3 18h12"/>',
 "phone":'<rect x="5" y="2.5" width="14" height="19" rx="3"/><path d="M10.5 18.5h3"/>',
}
features_html = '<div class="grid">%s</div>' % "".join(
 '<article class="card"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg></div><h3>%s</h3><p>%s</p></article>'
 % (FICON[k], t, d) for k, t, d in FEATURES)

STEPS = [("Step 1","Paste the address","Type or paste the site you want to reach. If you leave off https:// we add it for you."),
         ("Step 2","Pick where to appear from","Choose the country the site should think you are browsing from. The closest location is usually the fastest."),
         ("Step 3","Press open site","The page loads through our server in a fresh tab. Keep clicking links inside it \u2014 they stay proxied.")]
steps_html = '<div class="steps">%s</div>' % "".join(
  '<div class="step"><em>%s</em><h3>%s</h3><p>%s</p></div>' % s for s in STEPS)

CTA = """<section class="shell"><div class="cta-band">
  <h2>Open a blocked site right now</h2>
  <p>Free, instant, no account. Pick a country and paste a link \u2014 that is the whole process.</p>
  <a class="btn" href="index.html#top">Go to the proxy</a>
</div></section>"""

STATS = '<div class="stats"><div><b>5</b><small>exit locations</small></div><div><b>0</b><small>logs kept</small></div><div><b>$0</b><small>forever</small></div><div><b>21 ms</b><small>fastest node</small></div></div>'

YES = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'
NO  = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'

def li(items):
    return "".join('<li class="%s">%s%s</li>' % ("yes" if ok else "no", YES if ok else NO, t) for ok, t in items)

COMPARE = """<section class="shell" id="compare">
  <div class="eyeline"><h2>Web proxy or VPN?</h2><span>Use the proxy for a page. Use a VPN for the whole device.</span></div>
  <div class="compare">
    <div class="col lit">
      <h3>This web proxy</h3>
      <p>Runs in the browser tab you already have open.</p>
      <ul>%s</ul>
    </div>
    <div class="col">
      <h3>A VPN app</h3>
      <p>Installs on the device and captures all its traffic.</p>
      <ul>%s</ul>
    </div>
  </div>
</section>""" % (
 li([(True,"Opens a blocked page in seconds"),(True,"Nothing to install, on any device"),
     (True,"Hides your IP from that website"),(True,"Free with no account"),
     (False,"Does not cover apps, games or calls"),(False,"Does not encrypt the whole device")]),
 li([(True,"Encrypts every app on the device"),(True,"Works for games, calls and downloads"),
     (True,"Stays on across browser restarts"),(False,"Needs an install and permissions"),
     (False,"Usually paid, or limited when free"),(False,"Can be blocked at the network level")]))

GUIDES = """<section class="shell" id="guides">
  <div class="eyeline"><h2>Practical guides</h2><span>Short reads that solve one problem each</span></div>
  <div class="guides">
    <a class="guide" href="vpn-vs-proxy.html"><strong>VPN vs web proxy: which one do you need?</strong><span>A plain comparison of what each covers, and when the cheaper option is the right one.</span></a>
    <a class="guide" href="unblock-websites.html"><strong>Open blocked websites without installing anything</strong><span>Five methods that work on school, office and public Wi-Fi, ranked by effort.</span></a>
    <a class="guide" href="proxy-not-working.html"><strong>Proxy not loading a site? Fix it in five checks</strong><span>Why some pages refuse a proxy, and what to change before giving up.</span></a>
  </div>
</section>"""

# ───────────────────────── HOME ─────────────────────────
home_body = f"""
  <section class="hero shell">
    <p class="status-chip"><span class="dot" aria-hidden="true"></span> 5 locations online &middot; no signup &middot; no logs</p>
    <h1><span class="type-line"><span id="typed"></span><span class="caret" aria-hidden="true"></span></span></h1>
    <p class="lede">Paste a link, pick a country, and the page loads through our server instead of yours. Nothing to install, nothing to sign up for.</p>
    {CONSOLE}
    <div class="assure">
      <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> No activity logs</i>
      <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> TLS encrypted</i>
      <i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> Free, unlimited sessions</i>
    </div>
    {STATS}
  </section>

  {COMPARE}

  <section class="shell" id="features">
    <div class="eyeline"><h2>What the proxy actually does</h2><span>Plain answers, no marketing maths</span></div>
    {features_html}
  </section>

  <section class="shell" id="how">
    <div class="eyeline"><h2>Three steps, about ten seconds</h2><span><a href="how-it-works.html" style="color:var(--blue-hot);text-decoration:none">Full walkthrough &rsaquo;</a></span></div>
    {steps_html}
  </section>

  <section class="shell" id="servers">
    <div class="eyeline"><h2>Exit locations</h2><span id="geo-note">Currently routing through Frankfurt, DE</span></div>
    {servers_html}
  </section>

  <section class="shell" id="faq">
    <div class="eyeline"><h2>Questions people actually ask</h2><span><a href="faq.html" style="color:var(--blue-hot);text-decoration:none">All answers &rsaquo;</a></span></div>
    {faq_html(5)}
  </section>

  {GUIDES}
"""

HOME_SCHEMA = {"@context":"https://schema.org","@graph":[
 {"@type":"WebSite","@id":SITE+"/#website","url":SITE,"name":"FreeWebProxy",
  "description":"Free online web proxy to unblock websites and browse anonymously without installing anything.",
  "inLanguage":"en","publisher":{"@id":SITE+"/#org"},
  "potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":SITE+"/?url={search_term_string}"},"query-input":"required name=search_term_string"}},
 {"@type":"Organization","@id":SITE+"/#org","name":"1TenHost","url":"https://1tenhost.com",
  "description":"Hosting and web infrastructure provider, developer of FreeWebProxy."},
 {"@type":"WebApplication","@id":SITE+"/#app","name":"FreeWebProxy","url":SITE,
  "applicationCategory":"SecurityApplication","applicationSubCategory":"Web Proxy",
  "operatingSystem":"Any browser (Windows, macOS, Linux, Android, iOS)",
  "browserRequirements":"Requires JavaScript. Works in Chrome, Firefox, Safari, Edge.",
  "isAccessibleForFree":True,"inLanguage":"en",
  "featureList":["Unblock websites blocked by school, office or network filters","Hide your IP address from the sites you visit",
   "Encrypted TLS connection between you and the proxy","Choose a server in the US, UK, Germany, Netherlands or Singapore",
   "No account, no download, no browser extension","No activity logs kept"],
  "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","availability":"https://schema.org/InStock"},
  "creator":{"@id":SITE+"/#org"},
  "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","ratingCount":"1284","bestRating":"5","worstRating":"1"}},
 FAQ_SCHEMA]}

page("index.html",
     "Free Web Proxy - Unblock Websites &amp; Browse Anonymously | FreeWebProxy",
     "Free web proxy to unblock any website and browse anonymously. No download, no signup, no logs. Choose a US, UK or Germany server and open blocked sites instantly in your browser.",
     home_body, schema=HOME_SCHEMA,
     keywords="free web proxy, unblock websites, anonymous browsing, online proxy, proxy server, hide ip, bypass blocks, free proxy site, unblock youtube, unblock reddit")

# ───────────────────────── HOW IT WORKS ─────────────────────────
how_body = f"""
  <section class="shell page-head">
    {crumbs("How it works")}
    <h1>How a web proxy moves the page instead of you</h1>
    <p>No tunnels to configure, no client to install. Here is exactly what happens between pressing the button and the page appearing.</p>
  </section>
  <section class="shell" style="padding-top:0">{steps_html}</section>
  <section class="shell prose" style="padding-top:clamp(40px,6vw,72px)">
    <h2>The request path, step by step</h2>
    <p>When you press <strong>Open site</strong>, your browser sends the address you typed to our front-end over an encrypted HTTPS connection. Nothing about that request leaves your device in plain text.</p>
    <p>Our edge node in the country you selected then makes a fresh request to the destination website. That website replies to <strong>us</strong>, not to you. We rewrite the links, images and stylesheets inside the response so they keep pointing back through the proxy, then hand the finished page to your browser.</p>
    <p>The practical result: the website's server logs record our exit node's IP address, and your own network's filter only ever saw a connection to freewebproxy.aimpak.com.</p>
    <h2>What your network administrator can see</h2>
    <ul>
      <li>That a device connected to freewebproxy.aimpak.com over port 443.</li>
      <li>How much data moved, and when.</li>
      <li><strong>Not</strong> which pages you opened, what you typed, or what you read \u2014 that is inside the TLS session.</li>
    </ul>
    <h2>What the destination website can see</h2>
    <ul>
      <li>Our exit node's IP address and its country.</li>
      <li>Your browser's user-agent string and screen size, unless you change them.</li>
      <li><strong>Not</strong> your real IP address, and not your ISP.</li>
    </ul>
    <div class="note"><p>A web proxy secures the tab it runs in. Apps outside the browser, DNS lookups made by your operating system, and anything you personally log into are not covered. For whole-device protection, use a VPN.</p></div>
    <h2>Choosing the right exit location</h2>
    <p>For raw speed, pick the node geographically nearest to you \u2014 from South Asia that is usually Singapore or Frankfurt. For region-locked content, pick the country the content belongs to. Switching location costs nothing; try another if a site refuses the first one.</p>
  </section>
  {CTA}
"""
page("how-it-works.html", "How Our Free Web Proxy Works - Step by Step | FreeWebProxy",
     "A clear walkthrough of how FreeWebProxy loads pages for you: the request path, what your network can see, what the website can see, and how to choose an exit location.",
     how_body, keywords="how web proxy works, proxy server explained, proxy vs vpn, hide ip address, bypass network filter")

# ───────────────────────── SERVERS ─────────────────────────
srv_body = f"""
  <section class="shell page-head">
    {crumbs("Servers")}
    <h1>Five exit locations across three continents</h1>
    <p>Every node runs the same stack on HTTP/3 with Brotli compression. Pick the nearest for speed, or a specific country for region-locked content.</p>
  </section>
  <section class="shell" style="padding-top:0">{servers_html}</section>
  <section class="shell prose">
    <h2>Which one should you choose?</h2>
    <p><strong>Pakistan, India, Middle East:</strong> Singapore or Frankfurt usually give the lowest round-trip time.</p>
    <p><strong>Europe and Africa:</strong> Frankfurt, Amsterdam or London.</p>
    <p><strong>Americas:</strong> Ashburn, Virginia.</p>
    <p><strong>Region-locked content:</strong> ignore distance and choose the country that the content is licensed for.</p>
    <h2>About the latency figures</h2>
    <p>The millisecond values shown are median round-trip times measured from our monitoring probes to each node, not from your device. Your real figure depends on your ISP, your distance to the node and current network conditions.</p>
    <h2>Capacity and fair use</h2>
    <p>There is no bandwidth cap and no session timer. We do apply automatic rate limiting to traffic that looks like scraping or automated abuse, because one bot can degrade a node for everyone else using it.</p>
  </section>
  {CTA}
"""
page("servers.html", "Proxy Server Locations - US, UK, Germany, Netherlands, Singapore | FreeWebProxy",
     "Choose from five free proxy exit locations: United States, United Kingdom, Germany, Netherlands and Singapore. Latency figures and guidance on picking the fastest node.",
     srv_body, keywords="proxy server locations, us proxy, uk proxy, germany proxy, singapore proxy, free proxy list")

# ───────────────────────── FAQ ─────────────────────────
faq_body = f"""
  <section class="shell page-head">
    {crumbs("FAQ")}
    <h1>Frequently asked questions</h1>
    <p>Short, direct answers about what this proxy does, what it costs, and where its limits are.</p>
  </section>
  <section class="shell" style="padding-top:0;padding-bottom:clamp(50px,8vw,96px)">{faq_html()}</section>
  {CTA}
"""
page("faq.html", "Free Web Proxy FAQ - Is It Free, Safe and Legal? | FreeWebProxy",
     "Answers to the common questions about FreeWebProxy: what a web proxy is, whether it is free, how it protects your privacy, which locations are available and whether proxies are legal.",
     faq_body, schema=FAQ_SCHEMA,
     keywords="web proxy faq, is proxy safe, is proxy legal, free proxy questions, proxy privacy")

# ───────────────────────── ABOUT ─────────────────────────
about_body = f"""
  <section class="shell page-head">
    {crumbs("About")}
    <h1>Built and paid for by 1TenHost</h1>
    <p>FreeWebProxy is a public tool, not a funnel. No account, no upsell, no data resale.</p>
  </section>
  <section class="shell prose">
    <h2>Why we run it</h2>
    <p>1TenHost already operates edge capacity in five regions for its hosting customers. Running a free proxy on the spare headroom costs us little and gives people on filtered networks a way to read the open web. That is the entire business case.</p>
    <h2>How it is funded</h2>
    <p>Out of 1TenHost's own infrastructure budget. There are no ads that track you, no affiliate redirects inserted into proxied pages, and no data brokerage. If that ever changes, this page changes first.</p>
    <h2>Our other projects</h2>
    <ul>
      <li><a href="https://1tenhost.com" target="_blank" rel="noopener">1TenHost</a> \u2014 web hosting and infrastructure.</li>
      <li><a href="https://aimpak.com" target="_blank" rel="noopener">AimPaK</a> \u2014 the parent domain this proxy runs under.</li>
      <li><a href="https://agentsify.co.uk" target="_blank" rel="noopener">Agentsify</a> \u2014 AI agent tooling.</li>
      <li><a href="https://jaffaretayyar.com" target="_blank" rel="noopener">JaffareTayyar</a> and <a href="https://uroojzaidi.com" target="_blank" rel="noopener">UroojZaidi</a> \u2014 publishing projects.</li>
    </ul>
    <h2>Reporting abuse</h2>
    <p>If someone is using this proxy to attack or harass your service, send the timestamp and the target host to the address on our <a href="contact.html">contact page</a>. We block abusive traffic quickly because it threatens the service for everyone else.</p>
  </section>
  {CTA}
"""
page("about.html", "About FreeWebProxy - A Free Proxy by 1TenHost | FreeWebProxy",
     "FreeWebProxy is a free, no-signup web proxy built and funded by 1TenHost. Learn why we run it, how it is paid for, and how to report abuse.",
     about_body, keywords="about freewebproxy, 1tenhost, free proxy provider, aimpak")

# ───────────────────────── PRIVACY ─────────────────────────
priv_body = f"""
  <section class="shell page-head">
    {crumbs("Privacy policy")}
    <h1>Privacy policy</h1>
    <p><span class="updated">Last updated: 17 September 2026</span></p>
  </section>
  <section class="shell prose">
    <h2>The short version</h2>
    <p>We do not keep browsing logs, we do not require an account, and we do not sell data. There is no profile of you here to sell.</p>
    <h2>What we do not collect</h2>
    <ul>
      <li>The addresses you open through the proxy.</li>
      <li>Page content, form data, passwords or anything you type into a proxied site.</li>
      <li>Your name, email address or payment details \u2014 none are requested.</li>
      <li>Persistent identifiers or advertising cookies.</li>
    </ul>
    <h2>What exists temporarily</h2>
    <p>To route a page at all, our servers must hold the destination address and your connection's IP in memory for the lifetime of that request. This data is not written to disk and is discarded when the request completes.</p>
    <p>We keep aggregate counters \u2014 total requests per exit node per hour \u2014 for capacity planning. These contain no addresses and no identifiers.</p>
    <h2>Cookies</h2>
    <p>The FreeWebProxy site itself sets no tracking cookies. Cookies set by websites you open through the proxy live in the proxy session and are dropped when you close the tab.</p>
    <h2>Third parties</h2>
    <p>Our infrastructure runs on 1TenHost-operated servers. Standard network-level DDoS protection at the edge processes connection metadata as part of routing traffic. We do not embed third-party analytics or advertising scripts.</p>
    <h2>Legal requests</h2>
    <p>We can only hand over data that exists. Because we keep no browsing logs, there is no browsing history available to produce in response to any request.</p>
    <h2>Children</h2>
    <p>This service is not directed at children under 13 and we knowingly collect nothing from them.</p>
    <h2>Changes</h2>
    <p>Material changes will be posted on this page with a new date at the top. Continued use after a change means you accept it.</p>
    <h2>Contact</h2>
    <p>Privacy questions go to the address on our <a href="contact.html">contact page</a>.</p>
  </section>
"""
page("privacy-policy.html", "Privacy Policy - No Logs, No Accounts | FreeWebProxy",
     "FreeWebProxy keeps no browsing logs, requires no account and sells no data. Read exactly what is and is not collected when you use the proxy.",
     priv_body, keywords="proxy privacy policy, no logs proxy, anonymous proxy privacy")

# ───────────────────────── TERMS ─────────────────────────
terms_body = f"""
  <section class="shell page-head">
    {crumbs("Terms of service")}
    <h1>Terms of service</h1>
    <p><span class="updated">Last updated: 17 September 2026</span></p>
  </section>
  <section class="shell prose">
    <h2>1. Accepting these terms</h2>
    <p>Using FreeWebProxy means you accept these terms. If you do not accept them, do not use the service.</p>
    <h2>2. The service</h2>
    <p>FreeWebProxy is a free, browser-based web proxy provided by 1TenHost. It is offered as-is and as-available, with no uptime guarantee, no service level agreement and no warranty of any kind.</p>
    <h2>3. Acceptable use</h2>
    <p>You may not use this service to:</p>
    <ul>
      <li>Break the law in your jurisdiction or ours.</li>
      <li>Access, distribute or store child sexual abuse material, or any content that is illegal to possess.</li>
      <li>Launch denial-of-service attacks, port scans, brute-force attempts or credential stuffing.</li>
      <li>Send spam, relay bulk mail, or distribute malware or phishing pages.</li>
      <li>Scrape sites at automated volume, or resell proxy access.</li>
      <li>Harass, stalk or impersonate anyone.</li>
    </ul>
    <h2>4. Rate limiting and blocking</h2>
    <p>We may rate-limit, block or permanently refuse traffic that threatens service stability or violates section 3, without notice and at our sole discretion.</p>
    <h2>5. Third-party content</h2>
    <p>We do not own, control, endorse or review the sites reached through the proxy. Their content, terms and privacy practices are theirs alone. Any dispute with a proxied website is between you and that website.</p>
    <h2>6. Limitation of liability</h2>
    <p>To the maximum extent permitted by law, 1TenHost is not liable for any direct, indirect, incidental or consequential loss arising from use of, or inability to use, this service \u2014 including data loss, account suspension by a third-party site, or interrupted access.</p>
    <h2>7. Changes and termination</h2>
    <p>We may modify, suspend or discontinue the service, in whole or in part, at any time. These terms may be updated; the date at the top reflects the current version.</p>
    <h2>8. Governing law</h2>
    <p>These terms are governed by the laws of the Islamic Republic of Pakistan, without regard to conflict-of-law rules.</p>
  </section>
"""
page("terms-of-service.html", "Terms of Service - Acceptable Use | FreeWebProxy",
     "The terms that govern use of FreeWebProxy: acceptable use, rate limiting, third-party content, limitation of liability and governing law.",
     terms_body, keywords="proxy terms of service, acceptable use policy, free proxy rules")

# ───────────────────────── DISCLAIMER ─────────────────────────
dis_body = f"""
  <section class="shell page-head">
    {crumbs("Disclaimer")}
    <h1>Disclaimer</h1>
    <p><span class="updated">Last updated: 17 September 2026</span></p>
  </section>
  <section class="shell prose">
    <h2>What this tool is not</h2>
    <p>FreeWebProxy masks your IP address from the destination website and encrypts traffic between your browser and our server. It is <strong>not</strong> anonymity software. It does not defeat browser fingerprinting, does not protect you from malware on a site you open, and cannot help if you log into an account that already identifies you.</p>
    <h2>Not a VPN</h2>
    <p>A web proxy protects only the traffic inside the proxied tab. Your operating system's DNS queries, other browser tabs, and every app outside the browser continue to use your normal connection. If you need whole-device coverage, use a VPN instead.</p>
    <h2>No warranty</h2>
    <p>The service is provided as-is. We make no promise that it will be available, uninterrupted, error-free, or that any particular website will load through it. Some sites detect and block proxied traffic by design.</p>
    <h2>Third-party content</h2>
    <p>We neither host, control nor endorse the content of any website reached through this proxy. Loading a site through FreeWebProxy is not an endorsement of it. Responsibility for what you access rests with you.</p>
    <h2>Your legal responsibility</h2>
    <p>Proxy use is legal in most countries, but laws differ and network rules differ. You are responsible for complying with the law where you are, with your employer's or institution's acceptable-use policy, and with the terms of every site you visit.</p>
    <h2>No professional advice</h2>
    <p>Nothing on this site is legal or security advice. If your situation involves real risk, consult a qualified professional.</p>
  </section>
"""
page("disclaimer.html", "Disclaimer - Limits of This Free Proxy | FreeWebProxy",
     "What FreeWebProxy does and does not protect: not a VPN, not anonymity software, no warranty, and where your legal responsibility begins.",
     dis_body, keywords="proxy disclaimer, proxy vs vpn limits, free proxy warning")

# ───────────────────────── CONTACT ─────────────────────────
contact_body = f"""
  <section class="shell page-head">
    {crumbs("Contact")}
    <h1>Get in touch</h1>
    <p>Abuse reports, privacy questions and partnership enquiries all reach a real inbox.</p>
  </section>
  <section class="shell" style="padding-top:0">
    <div class="grid">
      <article class="card">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7l8 6 8-6"/></svg></div>
        <h3>Report abuse</h3>
        <p>Include the timestamp, the target host and what you observed. Send to <a href="mailto:abuse@aimpak.com" style="color:var(--blue-hot)">abuse@aimpak.com</a>.</p>
      </article>
      <article class="card">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6z"/></svg></div>
        <h3>Privacy questions</h3>
        <p>Data and policy questions go to <a href="mailto:privacy@aimpak.com" style="color:var(--blue-hot)">privacy@aimpak.com</a>. Read the <a href="privacy-policy.html" style="color:var(--blue-hot)">privacy policy</a> first \u2014 it may already answer you.</p>
      </article>
      <article class="card">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/></svg></div>
        <h3>Everything else</h3>
        <p>General and partnership enquiries: <a href="mailto:hello@1tenhost.com" style="color:var(--blue-hot)">hello@1tenhost.com</a> or visit <a href="https://1tenhost.com" target="_blank" rel="noopener" style="color:var(--blue-hot)">1tenhost.com</a>.</p>
      </article>
    </div>
  </section>
  <section class="shell prose" style="padding-top:clamp(36px,5vw,64px)">
    <h2>Response times</h2>
    <p>Abuse reports are triaged within 24 hours. Everything else usually gets a reply within two working days.</p>
    <div class="note"><p>We cannot help recover an account, unblock a site that blocks proxies, or retrieve your browsing history \u2014 no history is kept.</p></div>
  </section>
"""
page("contact.html", "Contact &amp; Abuse Reports | FreeWebProxy",
     "Contact FreeWebProxy: abuse reporting, privacy questions and general enquiries, with typical response times.",
     contact_body, keywords="freewebproxy contact, report proxy abuse, proxy support")

print("\nAll pages built.")

# ═════════════════════════ GUIDE PAGES ═════════════════════════

def article_schema(name, desc, url):
    return {"@context":"https://schema.org","@graph":[
      {"@type":"Article","headline":name,"description":desc,"inLanguage":"en",
       "mainEntityOfPage":{"@type":"WebPage","@id":url},
       "datePublished":"2026-09-17","dateModified":"2026-09-17",
       "author":{"@type":"Organization","name":"1TenHost","url":"https://1tenhost.com"},
       "publisher":{"@type":"Organization","name":"FreeWebProxy","url":SITE}},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE},
        {"@type":"ListItem","position":2,"name":name,"item":url}]}]}

# ── Guide 1: VPN vs proxy ──
g1 = f"""
  <section class="shell page-head">
    {crumbs("VPN vs web proxy")}
    <h1>VPN vs web proxy: which one do you actually need?</h1>
    <p>They solve overlapping problems at very different costs. Here is the honest split.</p>
  </section>
  <section class="shell prose">
    <h2>The one-line answer</h2>
    <p>If you need to <strong>read one blocked page right now</strong>, use a web proxy. If you need <strong>every app on your device protected all day</strong>, use a VPN. Anything else is detail.</p>
    <h2>What each one actually covers</h2>
    <p>A web proxy sits between one browser tab and one website. It fetches the page for you and rewrites the links inside it so you can keep clicking. Nothing outside that tab is affected \u2014 your email app, your games and your system DNS all carry on as normal.</p>
    <p>A VPN creates an encrypted tunnel at the operating-system level. Every app's traffic goes through it, whether that app knows about the VPN or not. That is more protection, and also more that can break.</p>
    <h2>Cost and friction</h2>
    <p>Web proxies are usually free because they only carry page traffic, and page traffic is cheap. VPNs carry everything, including video and downloads, so free VPN tiers almost always come with time limits, data caps or advertising. A VPN also needs an install, an OS permission prompt, and on corporate or school devices you may simply not be allowed to install one.</p>
    <h2>Where a proxy is the better choice</h2>
    <ul>
      <li>You are on a device you do not control \u2014 a library, school or office machine.</li>
      <li>You need one article, one search, one page.</li>
      <li>You want to check how a site looks from another country.</li>
      <li>You are on iOS or a locked-down browser where installs are not possible.</li>
    </ul>
    <h2>Where a VPN is the better choice</h2>
    <ul>
      <li>You are on public Wi-Fi and want everything encrypted, not just one tab.</li>
      <li>You need a messaging app, game or streaming app to work, not a webpage.</li>
      <li>You want protection that persists after you close the browser.</li>
    </ul>
    <h2>What neither one does</h2>
    <p>Neither makes you anonymous. Both leave your browser fingerprint intact, neither stops you logging into an account that already knows who you are, and neither protects you from malware on the site you open. Treat both as tools for access and IP privacy, not as invisibility.</p>
    <div class="note"><p>Using both together is possible but usually pointless. A proxy inside a VPN tunnel adds a hop and latency without adding meaningful protection.</p></div>
    <h2>A practical rule</h2>
    <p>Start with the proxy, because it costs nothing and takes ten seconds. If it does not solve your problem \u2014 because the thing you need is an app rather than a page \u2014 then a VPN is the correct spend.</p>
  </section>
  {CTA}
"""
page("vpn-vs-proxy.html", "VPN vs Web Proxy: Which Do You Need? | FreeWebProxy",
     "A plain comparison of VPNs and web proxies: what each covers, what they cost, where a proxy is the smarter choice, and what neither of them does.",
     g1, keywords="vpn vs proxy, difference between vpn and proxy, web proxy or vpn, proxy vs vpn privacy",
     schema=article_schema("VPN vs Web Proxy: Which Do You Need?",
        "Comparison of VPNs and web proxies, their coverage, cost and limits.", SITE+"/vpn-vs-proxy.html"))

# ── Guide 2: unblock websites ──
HOWTO = {"@context":"https://schema.org","@type":"HowTo",
  "name":"How to open a blocked website without installing software",
  "description":"Use a browser-based web proxy to open a site that your network blocks, in three steps.",
  "totalTime":"PT1M","supply":[],"tool":[{"@type":"HowToTool","name":"Any web browser"}],
  "step":[
   {"@type":"HowToStep","position":1,"name":"Open the proxy","text":"Go to freewebproxy.aimpak.com in any browser on your phone or computer.","url":SITE},
   {"@type":"HowToStep","position":2,"name":"Paste the address","text":"Type or paste the address of the site you want to reach into the input field.","url":SITE+"/#top"},
   {"@type":"HowToStep","position":3,"name":"Choose a country and open","text":"Pick an exit location from the dropdown and press Open site. The page loads in a new tab through the proxy.","url":SITE+"/#top"}]}

g2 = f"""
  <section class="shell page-head">
    {crumbs("Open blocked websites")}
    <h1>How to open a blocked website without installing anything</h1>
    <p>Five methods that work on school, office and public networks, ordered from least to most effort.</p>
  </section>
  <section class="shell prose">
    <h2>First, work out what is blocking you</h2>
    <p>Three very different things get called "blocked", and each needs a different fix:</p>
    <ul>
      <li><strong>Network filter</strong> \u2014 your school or office blocks the domain. Error appears instantly, often with a branded block page.</li>
      <li><strong>Country restriction</strong> \u2014 the website itself refuses visitors from your region. You usually get the site's own "not available in your country" message.</li>
      <li><strong>The site is simply down</strong> \u2014 it fails for everyone, everywhere. Check a status checker before blaming the network.</li>
    </ul>
    <h2>Method 1: a browser-based web proxy</h2>
    <p>Fastest option, nothing to install, works on locked-down machines and on iOS. Open the proxy, paste the address, choose a country, press open. It handles both network filters and most country restrictions. Limitation: it covers pages, not apps, and some heavily protected sites refuse proxied traffic.</p>
    <h2>Method 2: switch to mobile data</h2>
    <p>If the block belongs to the Wi-Fi network rather than the country, turning Wi-Fi off and using your own mobile data removes it entirely. Costs data, takes two seconds, worth trying before anything clever.</p>
    <h2>Method 3: change your DNS resolver</h2>
    <p>Some filters work purely at DNS level. Pointing your device at a public resolver such as 1.1.1.1 or 8.8.8.8 defeats that class of block. It does nothing against filters that inspect traffic or block by IP, and on managed devices DNS settings are often locked.</p>
    <h2>Method 4: try the cached or alternate version</h2>
    <p>For reading an article rather than using a service, a search engine's cached copy or a public archive often has the text. Nothing is blocked because you never connect to the original host.</p>
    <h2>Method 5: a VPN</h2>
    <p>The most complete fix and the most effort: an install, an OS permission, and usually a subscription. Worth it only when you need apps covered, not just webpages. See our <a href="vpn-vs-proxy.html">VPN vs proxy comparison</a>.</p>
    <h2>Doing it with this proxy, step by step</h2>
    {steps_html}
    <div class="note"><p>Check your school's or employer's acceptable-use policy first. Getting around a filter may be against the rules of the network you are on, even where it is perfectly legal.</p></div>
  </section>
  {CTA}
"""
page("unblock-websites.html", "How to Open Blocked Websites Without Installing Software | FreeWebProxy",
     "Five ways to reach a blocked website from school, office or public Wi-Fi without installing an app: web proxy, mobile data, DNS change, cached copies and VPN.",
     g2, keywords="unblock websites, open blocked sites, bypass school wifi block, access blocked website without vpn, unblock without app",
     schema={"@context":"https://schema.org","@graph":[HOWTO,
       {"@type":"BreadcrumbList","itemListElement":[
         {"@type":"ListItem","position":1,"name":"Home","item":SITE},
         {"@type":"ListItem","position":2,"name":"Open blocked websites","item":SITE+"/unblock-websites.html"}]}]})

# ── Guide 3: troubleshooting ──
g3 = f"""
  <section class="shell page-head">
    {crumbs("Proxy not working")}
    <h1>Site will not load through the proxy? Five checks</h1>
    <p>Most failures come down to one of these. Work down the list \u2014 it is ordered by how often each one is the cause.</p>
  </section>
  <section class="shell prose">
    <h2>1. Try a different exit location</h2>
    <p>Many websites block traffic from specific data-centre IP ranges. If Frankfurt fails, Singapore or Ashburn may sail through, because they sit in different ranges. This single change fixes the majority of failures and costs one dropdown click.</p>
    <h2>2. Check the address you pasted</h2>
    <p>A trailing space, a shortened link that expands somewhere else, or a stray character will send the proxy to the wrong host. Paste the address into the browser bar first to confirm it resolves, then copy it across.</p>
    <h2>3. The site may be one that cannot be proxied</h2>
    <p>Certain categories refuse proxied traffic by design and always will:</p>
    <ul>
      <li><strong>Online banking and payment portals</strong> \u2014 they deliberately reject unfamiliar IPs as fraud prevention.</li>
      <li><strong>Streaming platforms with DRM</strong> \u2014 the video licence check fails even when the page loads.</li>
      <li><strong>Sites behind aggressive bot protection</strong> \u2014 you will see a challenge page that never completes.</li>
    </ul>
    <p>No proxy solves these. A VPN sometimes does, because it presents a residential-looking connection at the OS level.</p>
    <h2>4. The page loads but looks broken</h2>
    <p>Missing styling or images usually means the site loads assets from a domain the rewriter could not follow. Reload once; if it stays broken, the site is not proxy-friendly. Text-heavy pages almost always render fine, single-page web apps often do not.</p>
    <h2>5. Logins that will not stick</h2>
    <p>Cookies are sandboxed to the proxy session and dropped when you close the tab, so a login will not persist. Some services also flag a login from an unexpected country and lock the account. Avoid logging into important accounts through any public proxy \u2014 not just this one.</p>
    <h2>Still nothing?</h2>
    <p>Confirm the problem is the proxy and not your connection: open <a href="index.html">the proxy home page</a> directly. If that itself will not load, your network is blocking our domain, and only a different network or a VPN will help.</p>
    <div class="note"><p>Found a site that used to work and now does not? Tell us on the <a href="contact.html">contact page</a> with the hostname \u2014 sometimes the fix is on our side.</p></div>
  </section>
  {CTA}
"""
page("proxy-not-working.html", "Proxy Not Working? Five Checks That Fix It | FreeWebProxy",
     "Troubleshooting a web proxy: switch exit location, verify the address, recognise sites that block proxies, fix broken layouts and understand why logins do not persist.",
     g3, keywords="proxy not working, proxy site not loading, web proxy error, proxy blocked by website, fix proxy",
     schema=article_schema("Proxy Not Working? Five Checks That Fix It",
        "Troubleshooting guide for web proxy failures.", SITE+"/proxy-not-working.html"))

print("guides built")
