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
lns = list(map(str.split, read_lines_list('18')))

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

# part 1
print("PART 1:")
x = y = 0
points = 0
x_list, y_list = [], []
point_list = []
for dir, dist, color in lns:
    dist = int(dist)
    if dir == "U":
        y-=dist
    elif dir == "D":
        y+=dist
    elif dir == "L":
        x-=dist
    elif dir == "R":
        x+=dist
            
    points += dist
            
    x_list.append(x)
    y_list.append(y)

area = PolyArea(x_list, y_list)



# part 2
print("PART 2:")
x = y = 0
points = 0
x_list, y_list = [], []
for dir, dist, color in lns:
    dist = int(color[2:7], 16)
    dir = "RDLU"[int(color[7])]
    if dir == "U":
        y-=dist
    elif dir == "D":
        y+=dist
    elif dir == "L":
        x-=dist
    elif dir == "R":
        x+=dist
            
    points += dist
    
    x_list.append(x)
    y_list.append(y)

area = PolyArea(x_list, y_list)

print(area + points//2 + 1)




print("took %s seconds" % (time.time() - start_time))