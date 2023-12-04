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
lines = [x.split(": ")[1] for x in read_lines_list("4")]



# part 1
print("PART 1:")
ans = 0
for l in lines:
    card, winning = l.split(" | ")
    card = [int(num) for num in card.split(" ") if num != ""]
    winning = [int(num) for num in winning.split(" ") if num != ""]

    ans += 2**len(set(card) & set(winning)) // 2

print(ans)



# part 2
print("PART 2:")
ans_2 = 0
nums = [0 for i in range(len(lines))]
for i, l in enumerate(lines):
    nums[i] += 1
    ans_2 += nums[i]
    card, winning = l.split(" | ")
    card = [int(num) for num in card.split(" ") if num != ""]
    winning = [int(num) for num in winning.split(" ") if num != ""]
    
    common = len(set(card) & set(winning))
    
    for j in range(1, common + 1):
        nums[i + j] += nums[i]

print(ans_2)



print("took %s seconds" % (time.time() - start_time))