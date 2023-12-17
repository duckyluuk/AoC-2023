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

from heapq import heappush, heappop

# input parsing
lines = to_nums(read_grid_2d('17'))

start_time = time.time()

# part 1
print("PART 1:")


# Failed attempted solution using prepared graph class (with modifying the dijkstra function).. maybe next time

# graph = grid_to_graph(lines)
# print(sum([int(node.value) for node in graph.shortest_path(graph.nodes[0], graph.nodes[-1])[1]]))
# print([node.pos for node in graph.shortest_path(graph.nodes[0], graph.nodes[-1])[1]])

queue = [(0, 0, 0, None, None)]
visited = set()
costs = {}
while queue:
    cost, x, y, last_dx, last_dy = heappop(queue)
    if (x, y, last_dx, last_dy) in visited:
        continue
    
    visited.add((x,y, last_dx, last_dy))
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        new_cost = cost
        if (last_dx == dx and last_dy == dy) or (last_dx == -dx and last_dy == -dy):
            continue
        
        nx = x
        ny = y
        for dis in range(1, 4):
            nx = nx + dx
            ny = ny + dy
            if nx < 0 or nx >= len(lines) or ny < 0 or ny >= len(lines[0]):
                continue
            new_cost += lines[ny][nx]
            if costs.get((nx, ny, dx, dy)) and costs[(nx,ny, dx, dy)] <= new_cost:
                continue
            
            costs[(nx, ny, dx, dy)] = new_cost
            heappush(queue, (new_cost, nx, ny, dx, dy))

for x,y,dx, dy in costs:
    if [x, y] == [len(lines[0])-1, len(lines)-1]:
        print(costs[(x,y,dx, dy)])
        break

# part 2
print("PART 2:")

queue = [(0, 0, 0, None, None)]
visited = set()
costs = {}
while queue:
    cost, x, y, last_dx, last_dy = heappop(queue)
    if (x, y, last_dx, last_dy) in visited:
        continue
    
    visited.add((x,y, last_dx, last_dy))
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        new_cost = cost
        if (last_dx == dx and last_dy == dy) or (last_dx == -dx and last_dy == -dy):
            continue
        nx = x
        ny = y
        for dis in range(1, 4):
            nx = nx + dx
            ny = ny + dy
            if nx < 0 or nx >= len(lines) or ny < 0 or ny >= len(lines[0]):
                continue
            new_cost += lines[ny][nx]
        for dis in range(4, 11):
            nx = nx + dx
            ny = ny + dy
            if nx < 0 or nx >= len(lines) or ny < 0 or ny >= len(lines[0]):
                continue
            new_cost += lines[ny][nx]
            if costs.get((nx, ny, dx, dy)) and costs[(nx,ny, dx, dy)] <= new_cost:
                continue
            
            costs[(nx, ny, dx, dy)] = new_cost
            heappush(queue, (new_cost, nx, ny, dx, dy))

for x,y,dx, dy in costs:
    if [x, y] == [len(lines[0])-1, len(lines)-1]:
        print(costs[(x,y,dx, dy)])
        break
    

print("took %s seconds" % (time.time() - start_time))