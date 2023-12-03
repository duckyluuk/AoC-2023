# input parsing: 11 bytes
*I,=open("3/3.txt")

# Part 1: 244 bytes
print(sum(int(l[j:k])for i,l in enumerate(I)for j in range(len(l)-1)for k in range(j,j+4)if(1-l[j-1:k].isdigit())*l[j:k].isdigit()*(k>=len(l)or 1-l[k].isdigit())*any(c not in"1234567890.\n"for x in I[max(0,i-1):i+2]for c in x[max(0,j-1):k+1])))
# Expanded:
print(sum(int(l[j:k])
    for i,l in enumerate(I) 
    for j in range(len(l)-1)
    for k in range(j,j+4)
    if(1-l[j-1:k].isdigit())*l[j:k].isdigit()*(k>=len(l)or 1-l[k].isdigit())*
    any(c not in"1234567890.\n"for x in I[max(0,i-1):i+2]for c in x[max(0,j-1):k+1])
)) 

# Part 2: 271 bytes
print(sum(len(q:=[int(m[x:k])for m in I[max(0,i-1):i+2]for x in range(max(0,j-3),j+2)for k in range(max(x,j),x+4)if(k>=len(m)or 1-m[k].isdigit())*m[x:k].isdigit()*((x<1)or 1-m[x-1].isdigit())])==2and q[0]*q[1]for i,l in enumerate(I)for j in range(len(l)-1)if"*"==l[j]))
# Expanded:
print(sum(len(q:=[int(m[x:k])
        for m in I[max(0,i-1):i+2]
        for x in range(max(0,j-3),j+2) 
        for k in range(max(x,j),x+4)
        if(k>=len(m)or 1-m[k].isdigit())*m[x:k].isdigit()*((x<1)or 1-m[x-1].isdigit())
       ])==2and q[0]*q[1]
    for i,l in enumerate(I)
    for j in range(len(l)-1)
    if"*"==l[j]
))


# Both Parts: 334 bytes
print(*[I:=[*open("3/3.txt")],*map(sum,zip(*[(sum(q:=[int(m[x:k])for m in I[max(0,i-1):i+2]for x in range(max(0,j-3),j+2)for k in range(max(x,j),x+4)if(k>=len(m)or 1-m[k].isdigit())*m[x:k].isdigit()*((x<1)or 1-m[x-1].isdigit())]),len(q)==2and q[0]*q[1]*(l[j]=="*"))for i,l in enumerate(I)for j in range(len(l)-1)if l[j]in"*#%@&-=+/$"]))][1:])
# Expanded:
print(*[I:=[*open("3/3.txt")],*map(sum,zip(*[(sum(q:=[int(m[x:k])
        for m in I[max(0,i-1):i+2]
        for x in range(max(0,j-3),j+2) 
        for k in range(max(x,j),x+4)
        if(k>=len(m)or 1-m[k].isdigit())*m[x:k].isdigit()*((x<1)or 1-m[x-1].isdigit())
       ]),len(q)==2and q[0]*q[1]*(l[j]=="*"))
    for i,l in enumerate(I)
    for j in range(len(l)-1)
    if l[j]in"*#%@&-=+/$"
]))][1:])