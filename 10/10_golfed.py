# Both Parts: 324 bytes
*G,=open("10/10.txt")
R=range(140)
x,y,*P=max((G[t].find("S"),t)for t in R)
v=-(q:=G[y-1][x]in'|F7')or G[y+1][x]in'|JL'
h=t=v==0
while'S'!=t:P+=[[x,y]];x+=h;y+=v;t=G[y][x];h+=t in'LF';h-=t in'J7';v+=t in'F7';v-=t in'JL'
print(len(P)//2,sum(sum(G[b][a]in'||FJ7LSS'[q::2]for a,b in P if(b==t)*s>a)%(2-([s,t]in P))for t in R for s in R))