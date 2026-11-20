/* Radar – QN · script per la pagina ospite (CMS): altezza degli iframe e tema.
   Versione leggibile dello snippet inline (assets/embed.min.js).
   Prima di usarlo sostituisci ACCOUNT con l'account GitHub su cui sono pubblicate le dataviz.
   v3: nessun carattere minore, maggiore o "e commerciale" (alcuni CMS li riscrivono e rompono lo script);
   chiede l'altezza agli iframe all'avvio e al caricamento di ciascuno, così funziona anche
   se il CMS esegue lo script dopo che gli iframe hanno già mandato il primo messaggio. */
(function () {
  if (window.__radarQNv3) return;
  window.__radarQNv3 = 1;
  var O = "https://ACCOUNT.github.io";
  var MQ = window.matchMedia("(prefers-color-scheme: dark)");

  function frames() {
    return Array.prototype.filter.call(document.getElementsByTagName("iframe"), function (f) {
      return (f.getAttribute("src") || "").indexOf(O + "/") === 0;
    });
  }
  function theme() {
    var t = document.documentElement.getAttribute("data-theme");
    return t === "dark" || t === "light" ? t : (MQ.matches ? "dark" : "light");
  }
  function bgOf(el) {
    while (el) {
      if (el.nodeType !== 1) return null;
      var c = getComputedStyle(el).backgroundColor;
      if (c) if (c !== "transparent") if (!/rgba\([^)]*,\s*0\)$/.test(c)) return c;
      el = el.parentElement;
    }
    return null;
  }
  function send(f) {
    try { f.contentWindow.postMessage({ sentinel: "radar-qn", type: "theme", theme: theme(), bg: bgOf(f.parentElement) }, O); } catch (e) {}
  }
  function sendAll() { frames().forEach(send); }
  function hook() {
    frames().forEach(function (f) {
      if (f.__radarQN) return;
      f.__radarQN = 1;
      f.addEventListener("load", function () { send(f); });
    });
  }

  window.addEventListener("message", function (e) {
    if (e.origin !== O) return;
    var d = e.data;
    if (!d) return;
    if (d.sentinel !== "radar-qn") return;
    if (d.type !== "height") return;
    frames().forEach(function (f) {
      if (f.contentWindow !== e.source) return;
      var h = Math.ceil(+d.height);
      if (h === Math.min(Math.max(h, 1), 20000)) f.style.height = h + "px";
      send(f);
    });
  });
  new MutationObserver(function () { sendAll(); setTimeout(sendAll, 400); })
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  if (MQ.addEventListener) MQ.addEventListener("change", sendAll);

  hook(); sendAll();
  [500, 1500, 4000].forEach(function (t) { setTimeout(function () { hook(); sendAll(); }, t); });
  window.addEventListener("load", function () { hook(); sendAll(); });
})();
