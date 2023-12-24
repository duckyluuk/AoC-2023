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
lines = read_lines_list("22")
bricks, full = {}, {}

# floor so stuff doeesnt keep falling
bricks[-1] = {"cubes": [],"supported": set(),"supports": set()}
for i in range(10):
    for j in range(10):
        full[(i,j,0)] = -1
        bricks[-1]["cubes"].append((i,j,0))

# make bricks
for i, line in enumerate(lines):
    start, end = to_nums(list(map(str.split,line.split("~"),",,")))
    cubes = []
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            for z in range(start[2], end[2]+1):
                cubes.append((x,y,z))
    bricks[i] = {"cubes": cubes,"supported": set(),"supports": set()}
    for cube in cubes:
        full[cube] = i

# generate supports and supported for each brick that is on top of another brick
for i in bricks:
    for cube in bricks[i]["cubes"]:
        if (cube[0], cube[1], cube[2]-1) in full and full[(cube[0], cube[1], cube[2]-1)] != i:
            bricks[i]["supported"].add(full[(cube[0], cube[1], cube[2]-1)])
            bricks[full[(cube[0], cube[1], cube[2]-1)]]["supports"].add(i)

# part 1
print("PART 1:")
ans = 0
# let bricks that are not supported fall down
while True:
    fell = False
    for i in bricks:
        if i < 0: continue	
        if len(bricks[i]["supported"]) == 0:
            fell = True
            for cube in bricks[i]["cubes"]:
                full.pop(cube)
            for s in bricks[i]["supports"]:
                bricks[s]["supported"].remove(i)
            bricks[i]["supports"] = set()
            for n, cube in enumerate(bricks[i]["cubes"]):
                ny = cube[2]-1
                bricks[i]["cubes"][n] = (cube[0], cube[1], ny)
                full[cube[0], cube[1], ny] = i
                if(cube[0], cube[1], ny-1) in full and full[(cube[0], cube[1], ny-1)] != i:
                    bricks[i]["supported"].add(full[(cube[0], cube[1], ny-1)])
                    bricks[full[(cube[0], cube[1], ny-1)]]["supports"].add(i)

    if not fell:
        break

unsafe = set()
for i in bricks:
    if i < 0:
        continue
    if all(len(bricks[s]["supported"]) > 1 for s in bricks[i]["supports"]):
        ans += 1
    else:
        unsafe.add(i)

print(ans)


# part 2
print("PART 2:")
ans_2 = 0

for remove in unsafe:
    removed = {remove}
    update = True
    while update:
        update = False
        for i in bricks:
            if i>=0 and bricks[i]["supported"] - removed == set() and i not in removed:
                removed.add(i)
                update = True
    ans_2 += len(removed) - 1

print(ans_2)


print("took %s seconds" % (time.time() - start_time))