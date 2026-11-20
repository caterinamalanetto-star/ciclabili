"""Converte un export Overpass (strade con 'out geom') in un grafo compatto per il calcolo dei percorsi in bici.
Uso: python3 grafo-strade.py export.json citta  -> data/strade-<citta>.json"""
import json, math, sys, collections
src, city = sys.argv[1], sys.argv[2]
def hav(a, b):
    R = 6371008.8; la1, la2 = math.radians(a[1]), math.radians(b[1]); dl = math.radians(b[0]-a[0]); dp = la2-la1
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(la1)*math.cos(la2)*math.sin(dl/2)**2))
YES = ('yes', 'designated', 'permissive')
def classify(t):
    hw = t.get('highway'); bic = t.get('bicycle', '')
    if bic in ('no', 'dismount') or t.get('access') in ('no', 'private'): return None
    side = [t.get(k, '') for k in ('cycleway', 'cycleway:left', 'cycleway:right', 'cycleway:both')]
    if hw == 'cycleway' or 'track' in side: return 'P'
    if hw in ('footway', 'path', 'pedestrian'):
        if bic == 'designated': return 'P'          # percorso ciclopedonale
        if hw == 'path' or bic in YES: return 'S'    # senza auto: parchi, aree pedonali
        return None
    if hw == 'living_street': return 'S'
    if 'lane' in side: return 'C'
    return 'T'
TRAFFIC_W = {'primary': 3.0, 'primary_link': 3.0, 'secondary': 2.6, 'secondary_link': 2.6, 'tertiary': 2.1, 'tertiary_link': 2.1, 'unclassified': 1.7, 'residential': 1.6}
W = {'P': 1.0, 'S': 1.2, 'C': 1.5}
ways = []
for e in json.load(open(src))['elements']:
    if e.get('type') != 'way' or 'geometry' not in e: continue
    t = e.get('tags', {}); k = classify(t)
    if not k: continue
    ow = t.get('oneway', 'no')
    if t.get('oneway:bicycle') == 'no' or any('opposite' in t.get(x, '') for x in ('cycleway', 'cycleway:left', 'cycleway:right')): ow = 'no'
    if t.get('highway') == 'cycleway' and 'oneway' not in t: ow = 'no'
    o = 1 if ow in ('yes', 'true', '1') else (-1 if ow == '-1' else 0)
    w = W.get(k) or TRAFFIC_W.get(t.get('highway'), 1.6)
    ways.append(dict(n=e['nodes'], g=[(p['lon'], p['lat']) for p in e['geometry']], k=k, o=o, w=w, name=t.get('name', '')))
use = collections.Counter()
for w in ways:
    for i, n in enumerate(w['n']): use[n] += 2 if i in (0, len(w['n'])-1) else 1
junction = {n for n, c in use.items() if c >= 2}
nid, nodes, names, nidx, edges = {}, [], [], {}, []
def node(n, p):
    if n not in nid: nid[n] = len(nodes); nodes.append([round(p[0], 5), round(p[1], 5)])
    return nid[n]
for w in ways:
    if w['name'] not in nidx: nidx[w['name']] = len(names); names.append(w['name'])
    start = 0
    for i in range(1, len(w['n'])):
        if w['n'][i] in junction or i == len(w['n'])-1:
            seg = w['g'][start:i+1]
            L = sum(hav(seg[j], seg[j+1]) for j in range(len(seg)-1))
            a, b = node(w['n'][start], seg[0]), node(w['n'][i], seg[-1])
            if a != b:
                mid = []
                for p in seg[1:-1]: mid += [round(p[0]*1e5), round(p[1]*1e5)]
                edges.append([a, b, round(L, 1), w['k'], nidx[w['name']], w['o'], round(w['w'], 1), mid])
            start = i
out = {'citta': city, 'nodi': nodes, 'nomi': names, 'archi': edges,
       'fonte': 'OpenStreetMap contributors (ODbL)'}
json.dump(out, open(f'data/strade-{city}.json', 'w'), separators=(',', ':'), ensure_ascii=False)
tot = collections.Counter()
for e in edges: tot[e[3]] += e[2]
print(city, 'nodi', len(nodes), 'archi', len(edges), {k: round(v/1000, 1) for k, v in tot.items()})
