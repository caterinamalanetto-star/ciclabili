# Ciclabili – dataviz Radar QN

| Dataviz | URL | Fonte |
|---|---|---|
| Le reti ciclabili di Torino, Milano e Bologna | https://caterinamalanetto-star.github.io/ciclabili/reti-citta/ | OpenStreetMap; Istat-ACI tav. 3.4 e 4.6 |
| Da qui a lì in bici: quanta strada fai protetto? | https://caterinamalanetto-star.github.io/ciclabili/dove-arrivi/ | OpenStreetMap |
| Quante piste ciclabili ha la tua città? | https://caterinamalanetto-star.github.io/ciclabili/la-tua-citta/ | Istat, Ambiente urbano 2024, tav. 17.1, 20.1, 20.2, 21.2 |
| La ciclabile di vernice di corso Regina Margherita | https://caterinamalanetto-star.github.io/ciclabili/corso-regina/ | Istat; OpenStreetMap; Biciplan Torino 2013; Il Post |
| A 30 o a 50 all'ora | https://caterinamalanetto-star.github.io/ciclabili/velocita/ | Formule della dinamica del veicolo |
| Le promesse dei piani per la bici | https://caterinamalanetto-star.github.io/ciclabili/promesse/ | Biciplan Torino, Bologna, Cambio; IMQ 2022 |
| Densità delle piste ciclabili nelle grandi città | https://caterinamalanetto-star.github.io/ciclabili/piste-citta/ | Istat, Ambiente urbano 2024, tav. 20.1-20.2 |
| Piste ciclabili, il divario tra Nord, Centro e Mezzogiorno | https://caterinamalanetto-star.github.io/ciclabili/divario-territoriale/ | Istat, Ambiente urbano 2024, tav. 20.1 |
| Torino, Milano e Bologna: piste, incidenti e morti | https://caterinamalanetto-star.github.io/ciclabili/tre-citta/ | Istat; Istat-ACI tav. 3.4 e 4.6 |
| Morti in bicicletta in Italia, 2010-2025 | https://caterinamalanetto-star.github.io/ciclabili/morti-bici/ | Istat-ACI, Incidenti stradali 2025, tav. 4.9 |
| Variazione dei morti per tipo di utente, 2024-2025 | https://caterinamalanetto-star.github.io/ciclabili/variazione-vittime/ | Istat-ACI, tav. 4.9 |
| Contro chi muoiono i ciclisti | https://caterinamalanetto-star.github.io/ciclabili/contro-chi/ | Istat-ACI, tav. A1 |
| Bologna, morti in strada prima e dopo la Città 30 | https://caterinamalanetto-star.github.io/ciclabili/bologna-citta30/ | Istat-ACI, tav. 4.6 |

Dati in `data/` (CSV con `;` e virgola decimale). Le mappe `reti-citta` e `dove-arrivi` usano MapLibre e la base cartografica OpenFreeMap; `reti-citta-schema` è la versione senza base cartografica.

### Metodo delle mappe (`reti-citta`)

Estrazione Overpass del 20/11/2026. Separati dalle auto: `highway=cycleway` (inclusi gli attraversamenti ciclabili) o `cycleway*=track`. Corsie dipinte: `cycleway*=lane`. Esclusi `shared_lane` (solo segnaletica). Lunghezze sulle linee della strada. Tratti collegati se distano al massimo 15 m. Script: `strumenti/reti-osm.py`.

## Snippet per il CMS

### Le reti ciclabili di Torino, Milano e Bologna

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/reti-citta/" width="100%" height="1260" frameborder="0" scrolling="no" title="Le reti ciclabili di Torino, Milano e Bologna"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Da qui a lì in bici: quanta strada fai protetto?

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/dove-arrivi/" width="100%" height="1170" frameborder="0" scrolling="no" title="Da qui a lì in bici: quanta strada fai protetto?"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Quante piste ciclabili ha la tua città?

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/la-tua-citta/" width="100%" height="1010" frameborder="0" scrolling="no" title="Quante piste ciclabili ha la tua città?"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### La ciclabile di vernice di corso Regina Margherita

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/corso-regina/" width="100%" height="1050" frameborder="0" scrolling="no" title="La ciclabile di vernice di corso Regina Margherita"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### A 30 o a 50 all'ora

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/velocita/" width="100%" height="1180" frameborder="0" scrolling="no" title="A 30 o a 50 all&#x27;ora"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Le promesse dei piani per la bici

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/promesse/" width="100%" height="720" frameborder="0" scrolling="no" title="Le promesse dei piani per la bici"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Densità delle piste ciclabili nelle grandi città

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/piste-citta/" width="100%" height="700" frameborder="0" scrolling="no" title="Densità delle piste ciclabili nelle grandi città"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Piste ciclabili, il divario tra Nord, Centro e Mezzogiorno

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/divario-territoriale/" width="100%" height="630" frameborder="0" scrolling="no" title="Piste ciclabili, il divario tra Nord, Centro e Mezzogiorno"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Torino, Milano e Bologna: piste, incidenti e morti

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/tre-citta/" width="100%" height="520" frameborder="0" scrolling="no" title="Torino, Milano e Bologna: piste, incidenti e morti"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Morti in bicicletta in Italia, 2010-2025

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/morti-bici/" width="100%" height="660" frameborder="0" scrolling="no" title="Morti in bicicletta in Italia, 2010-2025"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Variazione dei morti per tipo di utente, 2024-2025

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/variazione-vittime/" width="100%" height="460" frameborder="0" scrolling="no" title="Variazione dei morti per tipo di utente, 2024-2025"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Contro chi muoiono i ciclisti

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/contro-chi/" width="100%" height="700" frameborder="0" scrolling="no" title="Contro chi muoiono i ciclisti"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

### Bologna, morti in strada prima e dopo la Città 30

```html
<iframe src="https://caterinamalanetto-star.github.io/ciclabili/bologna-citta30/" width="100%" height="700" frameborder="0" scrolling="no" title="Bologna, morti in strada prima e dopo la Città 30"></iframe>
<script>
(function(){if(window.__radarQNv3)return;window.__radarQNv3=1;var O="https://caterinamalanetto-star.github.io";var MQ=window.matchMedia("(prefers-color-scheme:dark)");function frames(){return Array.prototype.filter.call(document.getElementsByTagName("iframe"),function(f){return(f.getAttribute("src")||"").indexOf(O+"/")===0;});}function theme(){var t=document.documentElement.getAttribute("data-theme");return t==="dark"||t==="light"?t:(MQ.matches?"dark":"light");}function bgOf(el){while(el){if(el.nodeType!==1)return null;var c=getComputedStyle(el).backgroundColor;if(c)if(c!=="transparent")if(!/rgba\([^)]*,\s*0\)$/.test(c))return c;el=el.parentElement;}return null;}function send(f){try{f.contentWindow.postMessage({sentinel:"radar-qn",type:"theme",theme:theme(),bg:bgOf(f.parentElement)},O);}catch(e){}}function sendAll(){frames().forEach(send);}function hook(){frames().forEach(function(f){if(f.__radarQN)return;f.__radarQN=1;f.addEventListener("load",function(){send(f);});});}window.addEventListener("message",function(e){if(e.origin!==O)return;var d=e.data;if(!d)return;if(d.sentinel!=="radar-qn")return;if(d.type!=="height")return;frames().forEach(function(f){if(f.contentWindow!==e.source)return;var h=Math.ceil(+d.height);if(h===Math.min(Math.max(h,1),20000))f.style.height=h+"px";send(f);});});new MutationObserver(function(){sendAll();setTimeout(sendAll,400);}).observe(document.documentElement,{attributes:true,attributeFilter:["data-theme"]});if(MQ.addEventListener)MQ.addEventListener("change",sendAll);hook();sendAll();[500,1500,4000].forEach(function(t){setTimeout(function(){hook();sendAll();},t);});window.addEventListener("load",function(){hook();sendAll();});})();
</script>
```

