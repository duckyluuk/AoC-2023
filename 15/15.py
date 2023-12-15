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
lines = read_raw_text("15").split(",")



# part 1
print("PART 1:")
ans = 0
for ln in lines:
    num = 0
    for char in ln:
        num += ord(char)
        num *= 17
        num %= 256
    ans += num

print(ans)



# part 2
print("PART 2:")
ans_2 = 0

boxes = [[] for x in range(256)]
for ln in lines:
    num = 0
    for char in ln:
        if 122 >= ord(char) >= 97:
            num += ord(char)
            num *= 17
            num %= 256
    if ln[-1] == "-":
        for i in range(len(boxes[num])):
            if boxes[num][i][0] == ln[:-1]:
                boxes[num].pop(i)
                break
    else:
        for i in range(len(boxes[num])):
            if boxes[num][i][0] == ln[:-2]:
                boxes[num][i][1] = int(ln[-1])
                change = True
                break
        else:
            boxes[num].append([ln[:-2], int(ln[-1])])

n=1
for box in boxes:
    i=1
    for num in box:
        ans_2 += i*num[1]*n
        i+=1
    n+=1

print(ans_2)



print("took %s seconds" % (time.time() - start_time))