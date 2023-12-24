# Both Parts: 749 bytes
from itertools import*
B,F={},{}
A=p=q=0
for L in open(0):
 s,e=map(eval,L.split("~"));l=[*product(*map(range,s,[x+1for x in e]))];B[p:=p+1]=[l,set(),set()]
 for c in l:F[c]=p
for i in B:
 for c in B[i][0]:
  n=(c[0],c[1],c[2]-1)
  if n in F and F[n]!=i:B[i][1]|={F[n]};B[F[n]][2]|={i}
f=1
while f:
 f=0
 for i in B:
  if len(B[i][1])<1:
   for s in B[i][2]:B[s][1]-={i}
   f=1;*map(F.pop,B[i][0]),;B[i][2]&={0};n=0
   for x,z,y in B[i][0]:
    w=y-1;c=y-2;B[i][0][n]=(x,z,w);F[x,z,w]=i;n+=1
    if F.get((x,z,c),i)!=i:B[i][1]|={F[x,z,c]};B[F[x,z,c]][2]|={i}
    elif c<0:B[i][1].add(-1)
for r in[b for b in B if any(len(B[s][1])<2 for s in B[b][2])]:
 R={r};q+=1
 while[R:=R|{i}for i in B if B[i][1]-R<{0}and i not in R]:0
 A+=len(R)-1
print(p-q,A)