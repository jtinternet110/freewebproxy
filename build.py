#!/usr/bin/env python3
# FreeWebProxy page builder — writes every page from one shared shell.
import os, json, re, pathlib

OUT = pathlib.Path("/home/claude/site")
SITE = "https://freewebproxy.aimpak.com"

LOGO = """<svg viewBox="0 0 32 32" fill="none" aria-hidden="true"><defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00D4FF"/><stop offset="1" stop-color="#A855F7"/></linearGradient></defs><circle cx="16" cy="16" r="13" stroke="url(#%s)" stroke-width="2.4"/><ellipse cx="16" cy="16" rx="6" ry="13" stroke="url(#%s)" stroke-width="1.9"/><path d="M3 16h26" stroke="url(#%s)" stroke-width="1.9"/></svg>"""
LOGO_H = LOGO % (("lg1",) * 4)
LOGO_F = LOGO % (("lg2",) * 4)

NAVLINKS = [("index.html", "Proxy"), ("how-it-works.html", "How it works"),
            ("servers.html", "Servers"), ("faq.html", "FAQ"), ("about.html", "About")]


def header(current):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == current else "", t)
        for h, t in NAVLINKS)
    return f"""<header>
  <div class="bar">
    <a class="brand" href="index.html" aria-label="FreeWebProxy home">{LOGO_H}Free<b>WebProxy</b></a>
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav id="nav">{links}<a class="pill" href="index.html#top">Open a site</a></nav>
  </div>
</header>"""


FOOTER = f"""<footer>
  <div class="shell">
    <div class="f-top">
      <div>
        <a class="brand" href="index.html" aria-label="FreeWebProxy home">{LOGO_F}Free<b>WebProxy</b></a>
        <p>A free, no-signup web proxy for opening blocked sites and keeping your address to yourself.</p>
      </div>
      <div class="f-nav">
        <div class="f-col">
          <strong>Product</strong>
          <a href="index.html">Web proxy</a>
          <a href="how-it-works.html">How it works</a>
          <a href="servers.html">Server locations</a>
          <a href="faq.html">FAQ</a>
        </div>
        <div class="f-col">
          <strong>Guides</strong>
          <a href="vpn-vs-proxy.html">VPN vs web proxy</a>
          <a href="unblock-websites.html">Open blocked sites</a>
          <a href="proxy-not-working.html">Proxy not working</a>
        </div>
        <div class="f-col">
          <strong>Legal</strong>
          <a href="privacy-policy.html">Privacy policy</a>
          <a href="terms-of-service.html">Terms of service</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="contact.html">Contact</a>
        </div>
        <div class="f-col">
          <strong>Network</strong>
          <a href="https://1tenhost.com" target="_blank" rel="noopener">1TenHost</a>
          <a href="https://aimpak.com" target="_blank" rel="noopener">AimPaK</a>
          <a href="https://agentsify.co.uk" target="_blank" rel="noopener">Agentsify</a>
          <a href="about.html">About us</a>
        </div>
      </div>
    </div>
    <div class="f-base">
      <span>&copy; <span id="yr">2026</span> FreeWebProxy &middot; freewebproxy.aimpak.com</span>
      <span class="credit">Design and Develop by <a href="https://1tenhost.com" target="_blank" rel="noopener">1TenHost</a></span>
    </div>
  </div>
</footer>"""


def page(fname, title, desc, body, current=None, schema=None, keywords=None, breadcrumb=None):
    canon = SITE + ("/" if fname == "index.html" else "/" + fname)
    ld = ""
    if schema:
        ld = '<script type="application/ld+json">%s</script>' % json.dumps(schema, separators=(",", ":"))
    kw = keywords or "free web proxy, unblock websites, anonymous browsing, online proxy, hide ip"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="author" content="1TenHost">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#070912">
<meta name="color-scheme" content="dark">
<meta name="geo.region" content="PK-SD">
<meta name="geo.placename" content="Karachi, Sindh, Pakistan">
<meta name="geo.position" content="24.8607;67.0011">
<meta name="ICBM" content="24.8607, 67.0011">
<meta name="language" content="English">
<meta name="coverage" content="Worldwide">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FreeWebProxy">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="{SITE}/assets/og-cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/og-cover.png">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
{ld}
</head>
<body>
<div class="field" aria-hidden="true"><span class="orb a"></span><span class="orb b"></span></div>
{header(current or fname)}
<main id="top">
{body}
</main>
{FOOTER}
<script src="assets/app.js" defer></script>
</body>
</html>
"""
    (OUT / fname).write_text(html, encoding="utf-8")
    print("wrote", fname, len(html), "bytes")


def crumbs(name):
    return ('<p class="crumb"><a href="index.html">Home</a> &rsaquo; <span>%s</span></p>' % name)
