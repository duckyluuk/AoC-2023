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
grid = read_grid_2d("23")



# part 1
print("PART 1:")
ans = 0

queue = [(1, 0, 0, [(1, 0)])]
while len(queue) > 0:
    x,y,steps,path = queue.pop(0)
    if x>0:
        if grid[y][x-1] in ".<":
            if (x-1,y) not in path:
                queue.append((x-1,y,steps+1,path+[(x-1,y)]))
    if x<len(grid[0])-1:
        if grid[y][x+1] in ".>":
            if (x+1,y) not in path:
                queue.append((x+1,y,steps+1,path+[(x+1,y)]))
    if y>0:
        if grid[y-1][x] in ".^":
            if (x,y-1) not in path:
                queue.append((x,y-1,steps+1,path+[(x,y-1)]))
    if y<len(grid)-1:
        if grid[y+1][x] in ".v":
            if (x,y+1) not in path:
                queue.append((x,y+1,steps+1,path+[(x,y+1)]))
    if x == len(grid[0])-2 and y == len(grid)-1:
        ans = max(ans, steps)

print(ans)



# part 2
print("PART 2:")
ans_2 = 0

reduced_map = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != "#":
            adjacent = {}
            if x > 0:
                if grid[y][x-1] != "#":
                    adjacent[(x-1, y)] = 1 
            if x < len(grid[0])-1:
                if grid[y][x+1] != "#":
                    adjacent[(x+1, y)] = 1
            if y > 0:
                if grid[y-1][x] != "#":
                    adjacent[(x, y-1)] = 1
            if y < len(grid)-1:
                if grid[y+1][x] != "#":
                    adjacent[(x, y+1)] = 1
            reduced_map[(x,y)] = adjacent

keys = list(reduced_map.keys())
for pos in keys:
    if len(reduced_map[pos]) == 2:
        path_a, path_b = reduced_map[pos]
        del reduced_map[path_a][pos], reduced_map[path_b][pos]
        reduced_map[path_a][path_b] = reduced_map[pos][path_a] + reduced_map[pos][path_b]
        reduced_map[path_b][path_a] = reduced_map[pos][path_b] + reduced_map[pos][path_a]
        del reduced_map[pos]

queue = [((1, 0), 0, [(1, 0)])]
while len(queue) > 0:
    pos,steps,path = queue.pop()
    neighbors = reduced_map[pos]
    for neighbor in neighbors:
        if neighbor not in path:
            queue.append((neighbor, steps+neighbors[neighbor], path+[neighbor]))
    if pos == (len(grid[0])-2, len(grid)-1):
        ans_2 = max(ans_2, steps)
       

print(ans_2)



print("took %s seconds" % (time.time() - start_time))