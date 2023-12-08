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

moves, _, *lines = read_lines_list("8")

start_time = time.time()

# input parsing
maps = {line[:3]: [line[7:10], line[12:15]] for line in lines}

# part 1
print("PART 1:")
ans = 0

moveIndex = 0
position = "AAA"
while position != "ZZZ":
    move = moves[moveIndex]
    moveIndex = (moveIndex + 1) % len(moves)
    if move == "L":
        position = maps[position][0]
    else:
        position = maps[position][1]
    ans += 1



print(ans)



# part 2
print("PART 2:")
ans_2 = 0

moveIndex = 0
positions = list(filter(lambda x: x[-1] == "A", maps.keys()))
move_amount = []
for position in positions:
    count = 0
    while position[-1] != "Z":
        move = moves[moveIndex]
        moveIndex = (moveIndex + 1) % len(moves)
        if move == "L":
            position = maps[position][0]
        else:
            position = maps[position][1]
        count += 1
    move_amount.append(count)
    moveIndex = 0
    
print(move_amount)
# find lcm of all move amounts
ans_2 = math.lcm(*move_amount)

print(ans_2)



print("took %s seconds" % (time.time() - start_time))