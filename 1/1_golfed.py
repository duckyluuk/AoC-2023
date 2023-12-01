import time
start_time = time.time()

# Part 1
print(sum((d:=[int(c)for c in l if c.isdigit()])[0]*10+d[-1]for l in open("1/1.txt")))

print("took %s seconds" % ((time.time() - start_time)/100))
start_time = time.time()

# Part 2
print(sum((d:=[n%9+1 for i in range(len(l))for n,w in enumerate("one two three four five six seven eight nine 1 2 3 4 5 6 7 8 9".split())if l[i:i+len(w)]==w])[0]*10+d[-1]for l in open("1/1.txt")))


print("took %s seconds" % (time.time() - start_time))