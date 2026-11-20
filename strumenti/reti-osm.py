import json,math,collections,heapq
def hav(a,b):
    R=6371008.8; la1,la2=math.radians(a[1]),math.radians(b[1]); dl=math.radians(b[0]-a[0]); dp=la2-la1
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(la1)*math.cos(la2)*math.sin(dl/2)**2))
SURF={'asphalt':'asfalto','paving_stones':'autobloccanti','concrete':'cemento','gravel':'ghiaia','fine_gravel':'ghiaino','compacted':'terra battuta','sett':'pavé','cobblestone':'ciottoli','unpaved':'sterrato','ground':'terra','paved':'pavimentata','dirt':'terra','grass':'erba','wood':'legno','pebblestone':'ciottoli','concrete:plates':'lastre di cemento'}
def classify(p):
    vals=[p.get(k,'') for k in ('cycleway','cycleway:left','cycleway:right','cycleway:both')]
    if p.get('highway')=='cycleway':
        if p.get('cycleway')=='crossing': return 'P','Attraversamento ciclabile'
        if p.get('segregated')=='yes': return 'P','Pista ciclabile, separata anche dai pedoni'
        if p.get('foot') in ('designated','yes'): return 'P','Pista ciclopedonale, condivisa con i pedoni'
        return 'P','Pista ciclabile separata dalle auto'
    if 'track' in vals: return 'P','Pista a lato della strada, separata dalle auto'
    if 'lane' in vals: return 'C','Corsia ciclabile solo dipinta sulla carreggiata'
    return None,None
TOL=15
cities=[('Torino','/mnt/user-data/uploads/1c0fe39a-export.geojson','Corso Regina Margherita'),
        ('Milano','/mnt/user-data/uploads/eea3c020-export__1_.geojson',None),
        ('Bologna','/mnt/user-data/uploads/74f1ee07-export__4_.geojson',None)]
for name,fn,hl in cities:
    fs=[]
    for f in json.load(open(fn))['features']:
        p=f['properties']; k,desc=classify(p)
        if not k: continue
        c=f['geometry']['coordinates']
        fs.append(dict(k=k,d=desc,c=c,l=sum(hav(c[i],c[i+1]) for i in range(len(c)-1)),p=p))
    P=[f for f in fs if f['k']=='P']
    # union-find con tolleranza
    par=list(range(len(P)))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    cell=TOL/111000; grid=collections.defaultdict(list)
    for i,f in enumerate(P):
        for pt in f['c']: grid[(int(pt[0]/cell/1.4),int(pt[1]/cell))].append((i,tuple(pt)))
    links=[]
    for (gx,gy),items in grid.items():
        near=[q for dx in (-1,0,1) for dy in (-1,0,1) for q in grid.get((gx+dx,gy+dy),[])]
        for i,p in items:
            for j,q in near:
                if i!=j and hav(p,q)<=TOL:
                    links.append((p,q))
                    if find(i)!=find(j): par[find(i)]=find(j)
    comp=collections.Counter()
    for i,f in enumerate(P): comp[find(i)]+=f['l']
    big=max(comp,key=comp.get)
    # grafo della componente principale per il percorso della bici
    G=collections.defaultdict(dict)
    for i,f in enumerate(P):
        if find(i)!=big: continue
        c=[tuple(x) for x in f['c']]
        for a,b in zip(c,c[1:]):
            w=hav(a,b); G[a][b]=w; G[b][a]=w
    for p,q in links:
        if p in G and q in G and p!=q: w=hav(p,q); G[p][q]=w; G[q][p]=w
    def dij(s):
        D={s:0}; prev={}; h=[(0,s)]
        while h:
            d,u=heapq.heappop(h)
            if d>D[u]: continue
            for v,w in G[u].items():
                if d+w<D.get(v,1e18): D[v]=d+w; prev[v]=u; heapq.heappush(h,(d+w,v))
        return D,prev
    s=next(iter(G)); D,_=dij(s); a=max(D,key=D.get); D,prev=dij(a); b=max(D,key=D.get)
    route=[b]
    while route[-1]!=a: route.append(prev[route[-1]])
    rlen=D[b]
    out=[]
    for i,f in enumerate(P):
        p=f['p']; t='principale' if find(i)==big else 'protetta'
        props={"t":t,"d":f['d'],"m":round(f['l'])}
        if p.get('name'): props['n']=p['name']
        if p.get('surface') in SURF: props['s']=SURF[p['surface']]
        if p.get('lit') in ('yes','no'): props['i']='sì' if p['lit']=='yes' else 'no'
        if p.get('width'): props['w']=p['width']
        if p.get('oneway')=='yes' or p.get('oneway:bicycle')=='yes': props['o']=1
        out.append({"type":"Feature","properties":props,"geometry":{"type":"LineString","coordinates":[[round(x,5),round(y,5)] for x,y in f['c']]}})
    for f in fs:
        if f['k']!='C': continue
        p=f['p']; props={"t":"corsia","d":f['d'],"m":round(f['l'])}
        if p.get('name'): props['n']=p['name']
        if p.get('maxspeed'): props['v']=p['maxspeed']
        if p.get('surface') in SURF: props['s']=SURF[p['surface']]
        if p.get('lit') in ('yes','no'): props['i']='sì' if p['lit']=='yes' else 'no'
        if hl and hl in p.get('name',''): props['hl']=1
        out.append({"type":"Feature","properties":props,"geometry":{"type":"LineString","coordinates":[[round(x,5),round(y,5)] for x,y in f['c']]}})
    # semplifica il percorso togliendo punti ravvicinati
    rs=[route[0]]
    for pt in route[1:]:
        if hav(rs[-1],pt)>8: rs.append(pt)
    out.append({"type":"Feature","properties":{"t":"percorso","m":round(rlen)},"geometry":{"type":"LineString","coordinates":[[round(x,5),round(y,5)] for x,y in rs]}})
    json.dump({"type":"FeatureCollection","features":out},open(f'ciclabili/data/rete-{name.lower()}.geojson','w'),separators=(',',':'),ensure_ascii=False)
    print(name,len(out),'percorso bici km',round(rlen/1000,1))
