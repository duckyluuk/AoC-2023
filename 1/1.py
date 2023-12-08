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
import re
import time

# input parsing
lns = read_lines_list("1")

start_time = time.time()


print("PART 1:")
lines = lns
lines = [[char for char in line if char in "0123456789"] for line in lines]

print(sum([int(line[0] + line[-1]) for line in lines]))



print("PART 2:")
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
lines = open("1/1.txt").readlines()

for i in range(len(lines)):
    line = lines[i]
    new_line = ""
    
    for j in range(len(line)):
        if line[j] in "0123456789":
            new_line += line[j]
            continue
        
        for word in words:
            if line[j:j+len(word)] == word:
                new_line += str(words.index(word))
                break

    lines[i] = new_line


print(sum([int(line[0] + line[-1]) for line in lines]))



print("took %s seconds" % (time.time() - start_time))