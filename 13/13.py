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


lines = read_groups('13')

start_time = time.time()

# input parsing
lines = [list(map(list,l))for l in lines]


# part 1
print("PART 1:")
ans = 0
for grid in lines:
    for i in range(len(grid[0])-1):
        if all([grid[j][:i+1][::-1][:min(i+1,len(grid[0])-i-1)] == grid[j][i+1:][:min(i+1,len(grid[0])-i-1)] for j in range(len(grid))]):
            ans += i+1
            break

    grid = list(zip(*grid))
    for i in range(len(grid[0])-1):
        if all([grid[j][:i+1][::-1][:min(i+1,len(grid[0])-i-1)] == grid[j][i+1:][:min(i+1,len(grid[0])-i-1)] for j in range(len(grid))]):
            ans += (i+1)*100
            break

print(ans)


# part 2
print("PART 2:")
ans_2 = 0
for grid in lines:
    for i in range(len(grid[0])-1):
        mistakes = 0
        for j in range(len(grid)):
            if grid[j][:i+1][::-1][:min(i+1,len(grid[0])-i-1)] != grid[j][i+1:][:min(i+1,len(grid[0])-i-1)]:
                mistakes += 1
        if mistakes == 1:
            ans_2 += i+1
            break

    grid = list(zip(*grid))
    for i in range(len(grid[0])-1):
        mistakes = 0
        for j in range(len(grid)):
            if grid[j][:i+1][::-1][:min(i+1,len(grid[0])-i-1)] != grid[j][i+1:][:min(i+1,len(grid[0])-i-1)]:
                mistakes += 1
        if mistakes == 1:
            ans_2 += (i+1)*100
            break

print(ans_2)



print("took %s seconds" % (time.time() - start_time))