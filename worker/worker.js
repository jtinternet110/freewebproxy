/**
 * FreeWebProxy — Cloudflare Worker backend
 * Free tier: 100,000 requests/day. No credit card, no API key.
 *
 * Deploy: Cloudflare dashboard → Workers & Pages → Create → Worker
 *         → paste this file → Deploy → add route proxy.freewebproxy.aimpak.com
 *
 * Front-end config (assets/app.js):
 *   mode: "custom",
 *   nodes: { de: "https://proxy.freewebproxy.aimpak.com", ... }
 */

const HOME = "https://freewebproxy.aimpak.com";

// hosts this proxy will never fetch (abuse / SSRF protection)
const BLOCKED = [
  /^localhost$/i, /^127\./, /^10\./, /^192\.168\./, /^169\.254\./,
  /^172\.(1[6-9]|2\d|3[01])\./, /\.local$/i, /^\[?::1\]?$/
];

function bad(msg, code = 400) {
  return new Response(msg, { status: code, headers: { "content-type": "text/plain; charset=utf-8" } });
}

export default {
  async fetch(request) {
    const here = new URL(request.url);

    // health check
    if (here.pathname === "/health") return new Response("ok");

    const raw = here.searchParams.get("u");
    if (!raw) return Response.redirect(HOME, 302);

    let target;
    try {
      target = new URL(raw);
    } catch {
      return bad("Invalid address.");
    }
    if (!/^https?:$/.test(target.protocol)) return bad("Only http and https are supported.");
    if (BLOCKED.some(re => re.test(target.hostname))) return bad("That host is not allowed.", 403);

    // forward the request
    const upstream = new Request(target.toString(), {
      method: request.method,
      headers: {
        "user-agent": request.headers.get("user-agent") || "Mozilla/5.0",
        "accept": request.headers.get("accept") || "text/html,*/*",
        "accept-language": request.headers.get("accept-language") || "en-US,en;q=0.9",
        "referer": target.origin + "/"
      },
      body: ["GET", "HEAD"].includes(request.method) ? null : request.body,
      redirect: "follow"
    });

    let res;
    try {
      res = await fetch(upstream);
    } catch (e) {
      return bad("Could not reach that site. Try another exit location.", 502);
    }

    const type = res.headers.get("content-type") || "";
    const headers = new Headers();
    headers.set("content-type", type || "text/html; charset=utf-8");
    headers.set("cache-control", "no-store");
    headers.set("x-robots-tag", "noindex, nofollow");
    headers.delete("content-security-policy");
    headers.delete("x-frame-options");

    // non-HTML (images, css, js, json) → stream straight through
    if (!type.includes("text/html")) {
      return new Response(res.body, { status: res.status, headers });
    }

    // HTML → rewrite links so browsing stays inside the proxy
    let html = await res.text();
    const self = here.origin + here.pathname + "?u=";

    const abs = (link) => {
      try { return self + encodeURIComponent(new URL(link, target).toString()); }
      catch { return link; }
    };

    html = html
      .replace(/\s(href|src|action)=["']([^"'>]+)["']/gi, (m, attr, link) => {
        if (/^(data:|blob:|javascript:|mailto:|tel:|#)/i.test(link)) return m;
        return ` ${attr}="${abs(link)}"`;
      })
      .replace(/\ssrcset=["']([^"']+)["']/gi, (m, set) => {
        const out = set.split(",").map(part => {
          const bits = part.trim().split(/\s+/);
          bits[0] = abs(bits[0]);
          return bits.join(" ");
        }).join(", ");
        return ` srcset="${out}"`;
      })
      .replace(/<base\b[^>]*>/gi, "")
      .replace(/integrity=["'][^"']*["']/gi, "");

    // small "back to proxy" bar
    const bar = `<div style="position:fixed;inset:auto 0 0 0;z-index:2147483647;display:flex;gap:12px;
      align-items:center;justify-content:center;padding:9px 14px;background:#0B0F1E;color:#E9EDFA;
      font:14px/1.4 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;border-top:1px solid #2A3557">
      <span style="opacity:.7">Browsing via FreeWebProxy</span>
      <a href="${HOME}" style="color:#00D4FF;text-decoration:none;font-weight:600">&larr; Back to proxy</a>
    </div>`;
    html = html.includes("</body>") ? html.replace("</body>", bar + "</body>") : html + bar;

    return new Response(html, { status: res.status, headers });
  }
};
