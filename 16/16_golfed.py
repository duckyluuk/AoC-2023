# Both parts, 377 bytes
I=*open("16/16.txt"),
h=[]
for i in range(440):
 Q=[([0,r:=i//4,r,109][z:=i%4],[r,0,109,r][z],1+z//~1,~(~z%~2))];V=set()
 while Q:*Q,q=Q;x,y,s,t=q;Q+=[[],[z:=(x+s,y+t,s,t)],[[(x+1,y,1,0),(x-1,y,-1,0)],[z]][s],[[(x,y+1,0,1),(x,y-1,0,-1)],[z]][t],[(x-t,y-s,-t,-s)],[(x+t,y+s,t,s)]][(q in V)==0<=x<110>y>=0!=V.add(q)and" .-|/".find(I[y][x])]
 h+=len({(v[:2])for v in V}),
print(h[0],max(h))