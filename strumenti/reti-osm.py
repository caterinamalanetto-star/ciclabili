import json,math,collections,sys
def hav(a,b):
    R=6371008.8; la1,la2=math.radians(a[1]),math.radians(b[1]); dl=math.radians(b[0]-a[0]); dp=la2-la1
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(la1)*math.cos(la2)*math.sin(dl/2)**2))
def cls(p):
    vals=[p.get(k,'') for k in ('cycleway','cycleway:left','cycleway:right','cycleway:both')]
    if p.get('highway')=='cycleway': return 'P'
    if 'track' in vals: return 'P'
    if 'lane' in vals: return 'C'
    return None
TOL=15
cities=[('Torino','/mnt/user-data/uploads/1c0fe39a-export.geojson','Corso Regina Margherita'),
        ('Milano','/mnt/user-data/uploads/eea3c020-export__1_.geojson',None),
        ('Bologna','/mnt/user-data/uploads/826e5e1c-export__2_.geojson',None)]
rows=[]
for name,fn,hl in cities:
    raw=json.load(open(fn)); fs=[]
    for f in raw['features']:
        k=cls(f['properties'])
        if not k: continue
        c=f['geometry']['coordinates']; fs.append(dict(k=k,c=c,l=sum(hav(c[i],c[i+1]) for i in range(len(c)-1)),n=f['properties'].get('name','')))
    P=[f for f in fs if f['k']=='P']
    par=list(range(len(P)))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    cell=TOL/111000; grid=collections.defaultdict(list)
    for i,f in enumerate(P):
        for pt in f['c']: grid[(int(pt[0]/cell/1.4),int(pt[1]/cell))].append((i,pt))
    for (gx,gy),items in grid.items():
        near=[q for dx in (-1,0,1) for dy in (-1,0,1) for q in grid.get((gx+dx,gy+dy),[])]
        for i,p in items:
            for j,q in near:
                if i<j and find(i)!=find(j) and hav(p,q)<=TOL: par[find(i)]=find(j)
    comp=collections.Counter()
    for i,f in enumerate(P): comp[find(i)]+=f['l']
    big=max(comp,key=comp.get); v=sorted(comp.values(),reverse=True)
    kmP=sum(f['l'] for f in P)/1000; kmC=sum(f['l'] for f in fs if f['k']=='C')/1000
    hlkm=sum(f['l'] for f in fs if f['k']=='C' and hl and hl in f['n'])/1000
    topC=collections.Counter()
    for f in fs:
        if f['k']=='C': topC[f['n'] or '(senza nome)']+=f['l']
    print(name,'prot',round(kmP,1),'corsie',round(kmC,1),'quota prot',round(kmP/(kmP+kmC)*100,1),'pezzi',len(v),'big',round(v[0]/1000,1),round(v[0]/1000/kmP*100,1),'%','<500m',sum(1 for x in v if x<500),'top corsie',[(n,round(l/1000,1)) for n,l in topC.most_common(3)])
    rows.append((name,kmP,kmC,len(v),v[0]/1000,sum(1 for x in v if x<500)))
    out=[]
    for i,f in enumerate(P):
        out.append({"type":"Feature","properties":{"t":"principale" if find(i)==big else "protetta"},"geometry":{"type":"LineString","coordinates":[[round(x,5),round(y,5)] for x,y in f['c']]}})
    for f in fs:
        if f['k']=='C':
            out.append({"type":"Feature","properties":{"t":"corsia","hl":1 if hl and hl in f['n'] else 0},"geometry":{"type":"LineString","coordinates":[[round(x,5),round(y,5)] for x,y in f['c']]}})
    json.dump({"type":"FeatureCollection","features":out},open(f'ciclabili/data/rete-{name.lower()}.geojson','w'),separators=(',',':'))
f1=lambda x:f"{x:.1f}".replace('.',',')
with open('ciclabili/data/reti-osm.csv','w') as o:
    o.write('Città;Km separati dalle auto;Km corsie dipinte;Pezzi separati;Km rete continua più grande;Pezzi sotto 500 m\n')
    for r in rows: o.write(f"{r[0]};{f1(r[1])};{f1(r[2])};{r[3]};{f1(r[4])};{r[5]}\n")
print(open('ciclabili/data/reti-osm.csv').read())
