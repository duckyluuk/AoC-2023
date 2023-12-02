# input parsing: 70 bytes
I=[l.split(":")[1].replace(*";,").strip().split(", ")for l in open("2/2.txt")]

# Part 1: 99 bytes
print(sum(i*all(int(c[:2])*('dgb'[n]in c)<n+13for n in[0,1,2]for c in l)for i,l in enumerate(I,1)))

# Part 2: 90 bytes
print(sum(eval('*'.join(str(max(int(c[:2])*(n in c)for c in l))for n in'dgb'))for l in I))