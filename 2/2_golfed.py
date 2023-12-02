# input parsing: 80 bytes
I=[[g.split(", ")for g in l.strip().split(": ")[1].split("; ")]for l in open("2/2.txt")]

print("PART 1:")
# Part 1: 135 bytes
print(sum(all(sum(int(c.split()[0])for c in g if ord(c[-1])%4==n)<[13,15,14][n]for n in[0,1,2]for g in l)*i for i,l in enumerate(I,1)))

print("PART 2:")
# Part 2: 120 bytes
print(sum(eval('*'.join(str(max(int(c.split()[0])for g in l for c in g if ord(c[-1])%4==n))for n in[0,1,2]))for l in I))