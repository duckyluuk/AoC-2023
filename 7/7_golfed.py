# Both Parts: 256 bytes
*I,=map(str.split,open("7/7.txt"))
for d in"_J":
 def V(h):n=sorted(h.count(x)for x in{*h}if x!=d)[::-1]+[0];n[0]+=h.count(d);return n
 print(sum(i*int(b)for i,(_,b)in enumerate(sorted(I,key=lambda l:[V(l[0]),[*map("23456789TJQKA".find,l[0].replace(d,"1"))]]),1)))