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
lines = read_lines_list("3")


# part 1
print("PART 1:")
ans = 0
for i in range(len(lines)):
    line = lines[i]
    j = 0
    while j < len(line):
        num = ""
        for k in range(4):
            if line[j:j+k].isdigit():
                num = line[j:j+k]
        if num:
            check_lines = lines[max(0, i-1):min(i+2, len(lines) + 1)]
            for l in check_lines:
                l=l[max(0, j-1):min(j+len(num)+1, len(l) + 1)]
                if any(x not in "0123456789." for x in l):
                    ans+=int(num)
                    break

        j=j+len(num) + 1
        
print(ans)


# part 2
print("PART 2:")
ans_2 = 0
for i in range(len(lines)):
    line1 = lines[i]
    j = 0
    for j in range(len(line1)):
        if line1[j] == "*":
            nums = []
            for y in range(max(i-1, 0), min(i+2, len(lines))):
                line = lines[y]
                x = max(j-1, 0)
                
                while x < min(j+2, len(line1)):
                    num = ""
                    if line[x].isdigit():
                        num = line[x]
                        if x-1 >= 0 and line[x-1].isdigit():
                            num = line[x-1] + num
                            if x-2 >= 0 and line[x-2].isdigit():
                                num = line[x-2] + num
                        if x+1 < len(line) and line[x+1].isdigit():
                            num+=line[x+1]
                            if x+2 < len(line) and line[x+2].isdigit():
                                num+=line[x+2]
                                x+=1
                            x+=1
                                                 
                    x+=1
                    if num:
                        nums.append(int(num))

            if len(nums) == 2:
                ans_2+=nums[0]*nums[1]

print(ans_2)


print("took %s seconds" % (time.time() - start_time))