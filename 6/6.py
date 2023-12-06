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
times, distances = read_lines_list('6')

start_time = time.time()

# part 1
print("PART 1:")

races = list(zip([int(x) for x in times.split()[1:]], [int(x) for x in distances.split()[1:]]))
ans = 1
for ms, mm in races:
    cnt = 0
    for i in range(ms):
        new = i* (ms - i)
        if new > mm:
            cnt += 1
    ans *= cnt

print(ans)



# part 2
print("PART 2:")

ms, mm = int(times[9:].replace(" ","")), int(distances[9:].replace(" ",""))

ans_2 = 0
for i in range(ms):
    new = i * (ms - i)
    if new > mm:
        ans_2 += 1

print(ans_2)



print("took %s seconds" % (time.time() - start_time))