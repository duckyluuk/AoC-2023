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
lines = read_grid_2d('10')

start_time = time.time()

start = (29, 21) # x, y

# part 1
print("PART 1:")
ans = 1

poly = [start]

position = [start[0], start[1]-1]
last_move = [0, -1]
while lines[position[1]][position[0]] != 'S':
    poly.append([*position])
    tile = lines[position[1]][position[0]]
    if tile == "|":
        if last_move == [0, 1]:
            position[1] += 1
        elif last_move == [0, -1]:
            position[1] -= 1
    elif tile == "-":
        if last_move == [1, 0]:
            position[0] += 1
        elif last_move == [-1, 0]:
            position[0] -= 1
    elif tile == "7":
        if last_move == [1, 0]:
            position[1] += 1
            last_move = [0, 1]
        elif last_move == [0, -1]:
            position[0] -= 1
            last_move = [-1, 0]
    elif tile == "J":
        if last_move == [1, 0]:
            position[1] -= 1
            last_move = [0, -1]
        elif last_move == [0, 1]:
            position[0] -= 1
            last_move = [-1, 0]
    elif tile == "L":
        if last_move == [-1, 0]:
            position[1] -= 1
            last_move = [0, -1]
        elif last_move == [0, 1]:
            position[0] += 1
            last_move = [1, 0]
    elif tile == "F":
        if last_move == [-1, 0]:
            position[1] += 1
            last_move = [0, 1]
        elif last_move == [0, -1]:
            position[0] += 1
            last_move = [1, 0]
    else:
        print("ERROR")
        break
        
    ans += 1
        
print(ans//2)


# part 2
print("PART 2:")
ans_2 = 0

from matplotlib.path import Path

p = Path(poly)
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if [x, y] in poly:
            continue
        if p.contains_point((x, y)):
            ans_2 += 1

print(ans_2)


print("took %s seconds" % (time.time() - start_time))