# Both Parts: 396 bytes
I={}
q=1
O=L=F=0
D={}
for i in open(0):
 I[z:=i[1:3]]=[i,0,d:=i.replace(*', ').split()[2:]]
 if'rx'in d:G=z
 for x in d:D[x]={**D.get(x,{}),z:0}
C={*D[G]}
while C:
 z=F<1e3;I['ro'][:2],*Q=[P:='%{{',1],['ro',0,0];F+=1
 for e,p,o in Q:
  O+=z>p;L+=z*p;t,s,l=I.get(e,P);q*=F**(C>(C:=C-{e*-~-p}))
  if P<t:D[e][o]=p;s=all(D[e].values())
  if(t>P)+1-p:I[e][1]=s=1-s;Q+=[[d,s,e]for d in l]
print(O*L,q)