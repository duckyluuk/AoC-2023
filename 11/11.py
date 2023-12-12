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
lines = read_lines_list('11')

y_gaps = []
x_gaps = []
new_lines = []
galaxies = []
for line in range(len(lines)):
    if lines[line].count("#") == 0:
        y_gaps.append(line)

    new_lines.append(list(lines[line]))

    for i in range(len(lines[line])):
        if lines[line][i] == "#":
            galaxies.append((i, line))

new_lines = list(zip(*new_lines))

new_lines_2 = []
for line in range(len(new_lines)):
    if new_lines[line].count("#") == 0:
        x_gaps.append(line)

    new_lines_2.append(list(new_lines[line]))
new_lines_2 = list(zip(*new_lines_2))


def find_distance(galaxy_1, galaxy_2, expand):
    dis = 0
    x_positions = sorted([galaxy_1[0], galaxy_2[0]])
    for x in range(x_positions[0], x_positions[1]):
        if x in x_gaps:
            dis += expand
        else:
            dis += 1
    y_positions = sorted([galaxy_1[1], galaxy_2[1]])
    for y in range(y_positions[0], y_positions[1]):
        if y in y_gaps:
            dis += expand
        else:
            dis += 1
    return dis

# part 1
print("PART 1:")
ans = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        ans += find_distance(galaxies[i], galaxies[j], 2)

print(ans)


# part 2
print("PART 2:")
ans_2 = 0

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):    
        ans_2 += find_distance(galaxies[i], galaxies[j], 1000000)

print(ans_2)


print("took %s seconds" % (time.time() - start_time))