from functools import*
C=cache(lambda l,g,c=0:1-("#"in l)if g<(0,)else 0if l<"#"else(l[0]!="."and C(l[1:],g,c+1))+(l>"$"and(c==g[0]and C(l[1:],g[1:]))+(c<1and C(l[1:],g))))
*I,=open("12/12.txt")
for i in 1,5:print(sum([C('?'.join([l]*i)+".",eval(r)*i)for l,r in map(str.split,I)]))