# allow importing from parent folder
import sys
sys.path.append('../AOC-2023')

# util imports
from utils.readfile import *
from utils.calc import *
from utils.graph import *
from utils.util import *
# lib imports
import re
import math
import copy
import numpy as np
from itertools import combinations, permutations, product
import time

start_time = time.time()



# input parsing
lines = read_lines_list("12")


#part 1
print("PART 1:")
ans = 0
for line in lines:
    possible = [line.split()[0]]
    for i in range(len(line.split()[0])):
        new_possible = []
        for p in possible:
            if p[i] == "?":
                new_possible.append(p[:i] + "." + p[i+1:])
                new_possible.append(p[:i] + "#" + p[i+1:])
            else:
                new_possible.append(p)
        possible = new_possible
    for p in possible:
        # count group sizes of #
        counts = []
        count = 0
        for c in p:
            if c == "#":
                count += 1
            if c== "." and count > 0:
                counts.append(count)
                count = 0
        if count > 0:
            counts.append(count)
        ans += counts == list(map(int,line.split()[1].split(",")))

print(ans)


# part 2
print("PART 2:")
ans_2 = 0

mem = {}
def get_counts(line, goals, count):
    if (line, goals, count) in mem:
        return mem[(line, goals, count)]
    if len(goals) == 0:
        return not "#" in line
    if count > goals[0]:
        return 0
    
    if not line:
        return count == goals[0] and len(goals) == 1

    valid = 0
    if line[0] in "?#":
        valid += get_counts(line[1:], goals, count + 1)
    if line[0] in "?.":
        if count == goals[0]:
            valid += get_counts(line[1:], goals[1:], 0)
        elif count == 0:
            valid += get_counts(line[1:], goals, 0)
    mem[(line, goals, count)] = valid
    return valid

for line in lines:
    expected = tuple(map(int,line.split()[1].split(",")))*5
    line = '?'.join([line.split()[0]]*5)
    ans_2 += get_counts(line, expected, 0)

print(ans_2)


print("took %s seconds" % (time.time() - start_time))