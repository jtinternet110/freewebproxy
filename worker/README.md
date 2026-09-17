# Cloudflare Worker backend — free, no API key

1. cloudflare.com par free account banayein.
2. Workers & Pages → Create → Workers → Create Worker → naam: `freewebproxy`.
3. "Edit code" → sab kuch delete → `worker.js` ka content paste → Save and Deploy.
4. Worker ka URL milega: `https://freewebproxy.<your-name>.workers.dev`
5. `assets/app.js` mein daal dein:

```js
var PROXY = {
  mode: "custom",
  nodes: {
    us: "https://freewebproxy.<your-name>.workers.dev",
    uk: "https://freewebproxy.<your-name>.workers.dev",
    de: "https://freewebproxy.<your-name>.workers.dev",
    nl: "https://freewebproxy.<your-name>.workers.dev",
    sg: "https://freewebproxy.<your-name>.workers.dev"
  }
};
```

Free limits: 100,000 requests / din, 10 ms CPU per request. Kaafi hai.

## Custom subdomain (optional)
Worker → Settings → Triggers → Add Custom Domain → `proxy.freewebproxy.aimpak.com`
(Domain Cloudflare DNS par hona chahiye.)
