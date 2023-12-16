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
lines = read_grid_2d('16')

start_time = time.time()


# part 1
print("PART 1:")

# points are x,y,dx,dy
next = [(0,0,1,0)]
visited = set()
while next:
    tile = next.pop(0)
    x,y,dx,dy = tile
    if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
        continue
    if tile in visited:
        continue
    visited.add(tile)
    
    if lines[y][x] == '.':
        next.append((x+dx,y+dy,dx,dy))
    elif lines[y][x] == '-':
        if dx == 0:
            next.append((x+1,y,1,0))
            next.append((x-1,y,-1,0))
        else:
            next.append((x+dx,y+dy,dx,dy))
    elif lines[y][x] == '|':
        if dy == 0:
            next.append((x,y+1,0,1))
            next.append((x,y-1,0,-1))
        else:
            next.append((x+dx,y+dy,dx,dy))
    elif lines[y][x] == '/':
        dx,dy = -dy,-dx
        next.append((x+dx,y+dy,dx,dy))
    elif lines[y][x] == '\\':
        dx,dy = dy,dx
        next.append((x+dx,y+dy,dx,dy))
       
visited = set([(visited[0], visited[1]) for visited in visited])

print(len(visited))



# part 2
print("PART 2:")
high = 0

possible_starts = []
for i in range(len(lines)):
    possible_starts.append((i,0,0,1))
    possible_starts.append((i,len(lines[0])-1,0,-1))
for i in range(len(lines[0])):
    possible_starts.append((0,i,1,0))
    possible_starts.append((len(lines)-1,i,-1,0))
    
for start in possible_starts:
    next = [start]
    visited = set()
    while next:
        tile = next.pop(0)
        x,y,dx,dy = tile
        if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
            continue
        if tile in visited:
            continue
        visited.add(tile)
        
        if lines[y][x] == '.':
            next.append((x+dx,y+dy,dx,dy))
        elif lines[y][x] == '-':
            if dx == 0:
                next.append((x+1,y,1,0))
                next.append((x-1,y,-1,0))
            else:
                next.append((x+dx,y+dy,dx,dy))
        elif lines[y][x] == '|':
            if dy == 0:
                next.append((x,y+1,0,1))
                next.append((x,y-1,0,-1))
            else:
                next.append((x+dx,y+dy,dx,dy))
        elif lines[y][x] == '/':
            dx,dy = -dy,-dx
            next.append((x+dx,y+dy,dx,dy))
        elif lines[y][x] == '\\':
            dx,dy = dy,dx
            next.append((x+dx,y+dy,dx,dy))
        
    visited = set([(visited[0], visited[1]) for visited in visited])

    high = max(high, len(visited))

print(high)


print("took %s seconds" % (time.time() - start_time))