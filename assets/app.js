/* FreeWebProxy — app.js | Design and Develop by 1TenHost */

/* ============================================================
   1) PROXY BACKEND CONFIG  —  yahan apne server ka address dalein
   mode: "ultraviolet" | "rammerhead" | "phpproxy" | "custom"
   ============================================================ */
var PROXY = {
  mode: "phpproxy",
  nodes: {
    us: "",   // e.g. "https://us.freewebproxy.aimpak.com"
    uk: "",
    de: "",   // e.g. "https://freewebproxy.aimpak.com/proxy"
    nl: "",
    sg: ""
  },
  uvPrefix: "/service/",
  uvKey: 2,
  phpPath: "/index.php?q=",
  rhPath: "/?url="
};

function uvEncode(str){
  if(!str) return str;
  return encodeURIComponent(str.toString().split("").map(function(c,i){
    return i % 2 ? String.fromCharCode(c.charCodeAt(0) ^ PROXY.uvKey) : c;
  }).join(""));
}

function buildRoute(target, node){
  var base = (PROXY.nodes[node] || "").replace(/\/+$/, "");
  switch(PROXY.mode){
    case "ultraviolet": return base + PROXY.uvPrefix + uvEncode(target);
    case "phpproxy":    return base + PROXY.phpPath + encodeURIComponent(btoa(target));
    case "rammerhead":  return base + PROXY.rhPath + encodeURIComponent(target);
    default:            return base + "/?u=" + encodeURIComponent(target);
  }
}

function normalise(raw){
  var v = (raw || "").trim();
  if(!v) return null;
  if(!/^https?:\/\//i.test(v)){
    if(/^[a-z][a-z0-9+.-]*:/i.test(v)) return null;   // javascript:, data:, ftp: reject
    v = "https://" + v.replace(/^\/+/, "");
  }
  try{
    var u = new URL(v);
    if(!/^https?:$/.test(u.protocol)) return null;
    if(u.hostname.indexOf(".") === -1) return null;
    return u.href;
  }catch(e){ return null; }
}

/* ============================================================
   2) Mobile navigation (har page par)
   ============================================================ */
(function(){
  var burger = document.querySelector(".burger"),
      nav    = document.getElementById("nav");
  if(burger && nav){
    burger.addEventListener("click", function(){
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function(e){
      if(e.target.tagName === "A") nav.classList.remove("open");
    });
  }
  var yr = document.getElementById("yr");
  if(yr) yr.textContent = new Date().getFullYear();
})();

/* ============================================================
   3) Proxy console + typing headline (sirf home page par)
   ============================================================ */
(function(){
  var input = document.getElementById("url");
  if(!input) return;

  var server = document.getElementById("server"),
      go     = document.getElementById("go"),
      status = document.getElementById("status"),
      note   = document.getElementById("geo-note");

  function say(html, isErr){
    status.innerHTML = html;
    status.classList.toggle("err", !!isErr);
    status.classList.add("on");
  }

  function launch(){
    var target = normalise(input.value);
    if(!target){
      say("Poora web address likhein, jaise <b>https://1tenhost.com</b>", true);
      input.focus();
      return;
    }
    var opt   = server.options[server.selectedIndex],
        city  = opt.getAttribute("data-city"),
        node  = server.value,
        route = buildRoute(target, node);

    go.dataset.busy = "1";
    say("Connecting via <b>" + city + "</b> …");

    setTimeout(function(){
      go.dataset.busy = "";
      if(!PROXY.nodes[node]){
        say("Exit node for <b>" + city + "</b> abhi connect nahi hua. assets/app.js mein <b>PROXY.nodes." +
            node + "</b> set karein. Route jo khulta:<br>" + route, true);
        return;
      }
      say("Opening <b>" + target + "</b> via <b>" + city + "</b> in a new tab.");
      window.open(route, "_blank", "noopener,noreferrer");
    }, 420);
  }

  go.addEventListener("click", launch);
  input.addEventListener("keydown", function(e){ if(e.key === "Enter") launch(); });

  document.querySelectorAll(".chip[data-site]").forEach(function(btn){
    btn.addEventListener("click", function(){
      input.value = btn.getAttribute("data-site");
      launch();
    });
  });

  server.addEventListener("change", function(){
    var opt = server.options[server.selectedIndex];
    if(note) note.textContent = "Currently routing through " + opt.getAttribute("data-city");
    var pos = (opt.getAttribute("data-pos") || "").split(";");
    var g = document.querySelector('meta[name="geo.position"]');
    if(g) g.setAttribute("content", pos.join(";"));
    var i = document.querySelector('meta[name="ICBM"]');
    if(i) i.setAttribute("content", pos.join(", "));
  });

  var q = new URLSearchParams(location.search).get("url");
  if(q) input.value = q;

  /* typing headline — requestAnimationFrame, non-blocking */
  var out = document.getElementById("typed");
  if(!out) return;
  var phrases = ["Unblock any website.", "Browse completely anonymously.", "Fast, secure, free web proxy."],
      p = 0, chars = 0, erasing = false, last = 0, hold = 0;

  function tick(now){
    if(!last) last = now;
    if(hold > 0){ hold -= (now - last); last = now; requestAnimationFrame(tick); return; }
    var step = erasing ? 34 : 62;
    if(now - last >= step){
      last = now;
      var word = phrases[p];
      chars += erasing ? -1 : 1;
      out.textContent = word.slice(0, chars);
      if(!erasing && chars === word.length){ erasing = true; hold = 1500; }
      else if(erasing && chars === 0){ erasing = false; p = (p + 1) % phrases.length; hold = 260; }
    }
    requestAnimationFrame(tick);
  }

  if(window.matchMedia("(prefers-reduced-motion: reduce)").matches){
    out.textContent = phrases[0];
  }else{
    requestAnimationFrame(tick);
  }
})();

/* ============================================================
   4) "More sites" toggle
   ============================================================ */
(function(){
  var btn = document.querySelector(".more-btn"),
      box = document.getElementById("more-chips");
  if(!btn || !box) return;
  btn.addEventListener("click", function(){
    var open = box.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.firstChild.nodeValue = open ? "Show fewer sites " : "More sites ";
  });
})();
