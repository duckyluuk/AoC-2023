# Both Parts: 194 bytes
R=[0]*99
for g in open('13/13.txt').read().split('\n\n'):
 g=g.split()
 for n in 1,100:
  i=1
  while g[0][i:]:R[sum(sum(map(str.__ne__,r[i-1::-1],r[i:]))for r in g)]+=n*i;i+=1
  *g,=zip(*g)
print(*R[:2])