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


# input parsing
lines = read_grid_2d('14')

start_time = time.time()


# part 1
print("PART 1:")
ans = 0
for y in range(len(lines)):
    q = y
    for x in range(len(lines[0])):
        y = q
        cur = lines[y][x]
        if cur == 'O':
            lines[y][x] = '.'
            while y > 0 and lines[y-1][x] == '.':
                y -= 1
            lines[y][x] = 'O'
            ans += (len(lines) - y)

print(ans)



# part 2
print("PART 2:")
ans_2 = cycle = 0

done = {}
while cycle < 1000000000:
    cycle += 1
    
    for _ in range(4):
        for y in range(len(lines)):
            q = y
            for x in range(len(lines[0])):
                y = q
                cur = lines[y][x]
                if cur == 'O':
                    lines[y][x] = '.'
                    while y > 0 and lines[y-1][x] == '.':
                        y -= 1
                    lines[y][x] = 'O'
        lines = list(map(list, zip(*lines[::-1])))
    if ''.join(map(''.join, lines)) in done:
        diff = cycle - done[''.join(map(''.join, lines))]
        cycle += diff * ((1000000000 - cycle) // diff)
        done = {}
    done[''.join(map(''.join, lines))] = cycle

for y in range(len(lines)):
    for x in range(len(lines[0])):
        cur = lines[y][x]
        if cur == 'O':
            ans_2 += (len(lines) - y)

print(ans_2)

print("took %s seconds" % (time.time() - start_time))