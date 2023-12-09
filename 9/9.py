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
lines = to_nums(list(map(str.split, read_lines_list("9"))))


# part 1
print("PART 1:")
ans = 0
for line in lines:
    line_list = [[*line]]
    while any(line_list[-1]):
        line = line_list[-1]
        line = [line[i] - line[i-1] for i in range(1, len(line))]
        line_list += [[*line]]
    
    line_list = line_list[::-1]
    line_list[0] += [0]
    new_num = 0
    for i in range(1, len(line_list)):
        new_num = line_list[i][-1] + new_num
        line_list[i] += [new_num]
        
    ans += new_num


print(ans)



# part 2
print("PART 2:")
ans_2 = 0

for line in lines:
    line_list = [[*line]]
    while any(line_list[-1]):
        line = line_list[-1]
        line = [line[i] - line[i-1] for i in range(1, len(line))]
        line_list += [[*line]]
    
    line_list = line_list[::-1]
    line_list[0] = [0] + line_list[0]
    new_num = 0
    for i in range(1, len(line_list)):
        new_num = line_list[i][0] - new_num
        line_list[i] = [new_num] + line_list[i]
    
    ans_2 += new_num


print(ans_2)


print("took %s seconds" % (time.time() - start_time))