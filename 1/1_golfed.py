# input parsing: 17 bytes
*I,=open("1.txt")


print("PART 1:")
# Part 1: 72 bytes
print(sum((d:=[int(c)for c in l if c.isdigit()])[0]*10+d[-1]for l in I))


print("PART 2:")
# Part 2: 179 bytes

print("v1") 
# 182 bytes, 1 line
print(sum((d:=[n%9+1 for i in range(len(l))for n,w in enumerate("one two three four five six seven eight nine 1 2 3 4 5 6 7 8 9".split())if l[i:i+len(w)]==w])[0]*10+d[-1]for l in I))


print("v2") 
# 179 bytes, 2 lines, ~10x faster
c="1 one | 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine"
print(sum(c.find(f(c.split(),key=g))//7*m+m for l in I for m,f,g in[(10,min,(l+c).find),(1,max,(c+l).rfind)]))
