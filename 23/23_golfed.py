# many credits to @boxy and @biz from code.golf on discord
# Both Parts: 392 bytes
s=open(0).read()
v=[k:=142]*k*k
def d(c):b=t;v[c]=0;[b:=max(b,g[c][n]+d(n))for n in g[c]if v[n]if c-i];v[c]=1;return b
for x in'>z':
 g,*q=[{}for _ in v],(1,1,0,0)
 for c,L,p,P in q:
  if~-len(l:=[(n,1,c,c)for z in[k,-k,-1,k**(s[c]>x)][(s[c]<x)-1:]if-~-(c in g[P])*s[n:=c+z]*(n^p)>s])or(z:=k*~-~-k-4)<c:g[P][c]=L;exec("iq,+t==lP , L"[c<z::2])
  else:q+=[(n,L+1,c,P)for n,*_ in l]
 print(d(0))