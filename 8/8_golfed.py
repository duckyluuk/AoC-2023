# Both Parts: 180 bytes
import math
M,*I=open("8/8.txt")
S={l[:3]:l[7:].split()for l in I}
for s in 3,1:print(math.lcm(*[len([p:=S[p][m>"L"][:3]for m in M[:-1]*99if"Z"*s>p[-s:]])for q in S if"A"*s==(p:=q)[-s:]]))