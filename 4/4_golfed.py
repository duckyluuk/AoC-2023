# Input Parsing: 26 bytes
*I,=map(str.split,open("4/4.txt"))

# Part 1: 54 bytes

print(sum(2**len(({*g[:12]}&{*g[12:]}))//2for g in I))

# Part 2: 110 bytes
n=[i:=0]*999
for g in I:
 n[i]+=1
 for j in range(len({*g[:12]}&{*g[12:]})):n[j+i+1]+=n[i]
 i+=1
print(sum(n))


# Both Parts: 153 bytes
a=i=0
n=[0]*999
for g in map(str.split,open("4/4.txt")):
 a+=2**(q:=len({*g[:12]}&{*g[12:]}))//2
 n[i]+=1
 for j in range(q):n[j+i+1]+=n[i]
 i+=1
print(a,sum(n))
