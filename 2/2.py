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
lines = read_lines_list("2")

start_time = time.time()


# part 1
print("PART 1:")
i = 0

ans = sum(range(1, 101))
for line in lines:
    i = i + 1
    line = line.strip()
    line = line.split(": ")[1]
    groups = line.split("; ")
    for group in groups:
        RED = 0
        GREEN = 0
        BLUE = 0
        
        for color in group.split(", "):
            amount, color = color.split(" ")
            amount = int(amount)
            if color == "red":
                RED = RED + amount
            elif color == "green":
                GREEN = GREEN + amount
            elif color == "blue":
                BLUE = BLUE + amount
            else:
                print("ERROR")
                exit()
        
        if RED > 12 or GREEN > 13 or BLUE > 14:
            ans = ans - i
            break





print(ans)



# part 2
print("PART 2:")
i = 0
ans_2 = 0

for line in lines:
    i = i + 1
    line = line.strip()
    line = line.split(": ")[1]
    groups = line.split("; ")
    MIN_RED = 0
    MIN_GREEN = 0
    MIN_BLUE = 0
    for group in groups:
        RED = 0
        GREEN = 0
        BLUE = 0
        
        for color in group.split(", "):
            amount, color = color.split(" ")
            amount = int(amount)
            if color == "red":
                RED = RED + amount
            elif color == "green":
                GREEN = GREEN + amount
            elif color == "blue":
                BLUE = BLUE + amount
            else:
                print("ERROR")
                exit()
        
        if RED > MIN_RED:
            MIN_RED = RED
        if GREEN > MIN_GREEN:
            MIN_GREEN = GREEN
        if BLUE > MIN_BLUE:
            MIN_BLUE = BLUE
            
    ans_2 += MIN_RED * MIN_GREEN * MIN_BLUE

print(ans_2)



print("took %s seconds" % (time.time() - start_time))