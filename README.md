# FreeWebProxy — freewebproxy.aimpak.com

Static, dependency-free web-proxy front-end. Vanilla HTML/CSS/JS, no build step needed.

## Files
- `index.html` … `contact.html` — 9 pages
- `assets/style.css`, `assets/app.js`, `assets/favicon.svg`
- `robots.txt`, `sitemap.xml`, `.htaccess`
- `build.py` + `pages.py` — optional page generator (do NOT upload to server)

## Connecting a proxy backend
Edit `assets/app.js`, top of file:

```js
var PROXY = {
  mode: "phpproxy",            // or "ultraviolet" | "rammerhead"
  nodes: { de: "https://freewebproxy.aimpak.com/proxy", ... }
};
```

## Deploy
- cPanel: upload everything except `build.py`, `pages.py`, `README.md` into the subdomain root.
- GitHub: push to `main`, the Action in `.github/workflows/deploy.yml` FTPs it to cPanel.

Design and Develop by 1TenHost.

## Free backend
See `worker/README.md` — Cloudflare Worker, free tier, no API key.
