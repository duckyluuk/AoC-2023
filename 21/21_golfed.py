# Both Parts, 493 bytes
R=str.replace
S=sum;M=map
*L,=open(0)
def Q(x,y,N):
 G=[R(l,*"S.")for l in L];G[y]=G[y][:x]+"O"+G[y][x+1:131]
 for n in'*'*N:[G:=[*M("".join,zip(*[R(l,"O.","OX")for l in G][::-1]))]for i in'*'*4];G=[R(R(l,*"O."),*"XO")for l in G]
 return S([l.count("O")for l in G])
F,I,O=map(Q,z:=[65]*3,z,[131,130,64])
A=S(M(Q,[65,65,0,130],[0,130,65,65],[130]*4))
B=S(M(Q,a:=[130,0]*2,b:=[130,130,0,0],[64]*4))
C=S(M(Q,b,a,[195]*4))
print(O,A+S(B+(i and C)+[F*(i*4or 1),I*i*4][i%2]for i in range(202300)))