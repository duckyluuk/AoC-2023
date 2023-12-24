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
lines = read_lines_list('21')

x,y,=max((lines[t].find("S"),t)for t in range(len(lines)))
lines[y] = lines[y].replace("S", "O")
STEPS = 64
# part 1
print("PART 1:")
for n in range(STEPS):
    for y in range(len(lines)):
        lines[y] = lines[y].replace("O", "X")

    for i in range(4):
        for y in range(len(lines)):
            lines[y] = lines[y].replace("X.", "XO")
        lines = list(map(''.join,zip(*lines[::-1])))

    for y in range(len(lines)):
        lines[y] = lines[y].replace("X", ".")

for line in lines:
    print(line)
print(sum([line.count("O") for line in lines]))



# part 2
# lines = read_lines_list('21')
# x,y,=max((lines[t].find("S"),t)for t in range(len(lines)))
# lines[y] = lines[y].replace("S", ".")
# x, y = 65, 65
# lines[y] = lines[y][:x] + "O" + lines[y][x+1:]
# STEPS = 65 + 130
# # part 1
# print("PART 1:")
# for n in range(STEPS):
#     for y in range(len(lines)):
#         lines[y] = lines[y].replace("O", "X")

#     for i in range(4):
#         for y in range(len(lines)):
#             lines[y] = lines[y].replace("X.", "XO")
#         lines = list(map(''.join,zip(*lines[::-1])))

#     for y in range(len(lines)):
#         lines[y] = lines[y].replace("X", ".")

# print(sum([line.count("O") for line in lines]))
# for line in lines:
#     print(line)

# x,y,=max((lines[t].find("S"),t)for t in range(len(lines)))
# lines[y] = lines[y].replace("S", ".")
# STEPS = 131*2+65
# # repeat the grid in a 3x3 pattern
# y = y + len(lines)*2
# x = x + len(lines[0])*2
# lines = [line*5 for line in lines]*5
# lines[y] = lines[y][:x] + "O" + lines[y][x+1:]

# for n in range(STEPS):
#     for y in range(len(lines)):
#         lines[y] = lines[y].replace("O", "X")

#     for i in range(4):
#         for y in range(len(lines)):
#             lines[y] = lines[y].replace("X.", "XO").replace(".X", "OX")
#         lines = list(map(''.join,zip(*lines[::-1])))

#     for y in range(len(lines)):
#         lines[y] = lines[y].replace("X", ".")

# i=0
# for line in lines:
#     i+=1
#     print(line[:131], line[131:131*2], line[131*2:131*3], line[131*3:131*4], line[131*4:131*5])
#     if i%131==0:
#         print()
# print(sum([line.count("O") for line in lines]))


FULL_GRID = 7613 # PART 1, x=65, y=65, steps=131
INVERSE_GRID = 7623 # PART 1, x=65, y=65, steps=130
TOP_POINT = 5749 # PART 1, x=65, y=0, steps=130
BOTTOM_POINT = 5753 # PART 1, x=65, y=130, steps=130
RIGHT_POINT = 5746 # PART 1, x=0, y=65, steps=130
LEFT_POINT = 5756 # PART 1, x=130, y=65, steps=130
DIAG_TOP_LEFT_SHORT = 976 # PART 1, x=130, y=130, steps=64
DIAG_TOP_LEFT_LONG = 6683 # PART 1, x=130, y=130, steps=195
DIAG_TOP_RIGHT_SHORT = 972 # PART 1, x=0, y=130, steps=64
DIAG_TOP_RIGHT_LONG = 6679 # PART 1, x=0, y=130, steps=195
DIAG_BOTTOM_LEFT_SHORT = 958 # PART 1, x=130, y=0, steps=64
DIAG_BOTTOM_LEFT_LONG = 6686 # PART 1, x=130, y=0, steps=195
DIAG_BOTTOM_RIGHT_SHORT = 971 # PART 1, x=0, y=0, steps=64
DIAG_BOTTOM_RIGHT_LONG = 6680 # PART 1, x=0, y=0, steps=195

EXPANSION_SIZE = (26501365 - 65) // 131

result = TOP_POINT + BOTTOM_POINT + RIGHT_POINT + LEFT_POINT + \
    (DIAG_TOP_LEFT_SHORT * EXPANSION_SIZE) + (DIAG_TOP_LEFT_LONG * (EXPANSION_SIZE - 1)) + \
    (DIAG_TOP_RIGHT_SHORT * EXPANSION_SIZE) + (DIAG_TOP_RIGHT_LONG * (EXPANSION_SIZE - 1)) + \
    (DIAG_BOTTOM_LEFT_SHORT * EXPANSION_SIZE) + (DIAG_BOTTOM_LEFT_LONG * (EXPANSION_SIZE - 1)) + \
    (DIAG_BOTTOM_RIGHT_SHORT * EXPANSION_SIZE) + (DIAG_BOTTOM_RIGHT_LONG * (EXPANSION_SIZE - 1))

for i in range(EXPANSION_SIZE):
    if i%2:
        result += INVERSE_GRID * i * 4
    else:
        result += FULL_GRID * (i * 4 or 1)
        
print(result)
print("took %s seconds" % (time.time() - start_time))