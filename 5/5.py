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
lines = read_raw_text("5").split("\n\n")

start_time = time.time()

seeds = list(map(int,lines[0].split()[1:]))
maps = [[list(map(int,ln.split())) for ln in cat.split("\n")[1:]] for cat in lines[1:]]



# part 1
print("PART 1:")
for cat in maps:
    for i, num in enumerate(seeds):
        for new_start, old_start, new_size in cat:

            if old_start <= num < old_start + new_size:
                seeds[i] = new_start + num - old_start
                break
                
print(min(seeds))



# part 2
print("PART 2:")
seeds = list(map(int,lines[0].split()[1:]))
maps = [[list(map(int,ln.split())) for ln in cat.split("\n")[1:]] for cat in lines[1:]]

ranges = [[seeds[i], seeds[i]+seeds[i+1]] for i in range(0, len(seeds), 2)]
for cat in maps:
    new_ranges = []
    while ranges:
        start, end = ranges.pop(0)
        added = False
        for new_start, old_start, new_size in cat:
            if old_start <= start < old_start + new_size or old_start <= end < old_start + new_size:
                # keep overlapping ranges
                update_start = new_start + min(max(start - old_start, 0), new_size-1)
                update_end = new_start + min(max(end - old_start, 0), new_size-1)
                new_ranges.append([update_start, update_end])
                added = True
                # remaining left side
                cut_start = update_start - new_start + old_start - 1
                if start < cut_start:
                    ranges.append([start, cut_start])
                # remaining right side
                cut_end = update_end - new_start + old_start + 1
                if end > cut_end:
                    ranges.append([cut_end, end])
                    
        if not added:
            new_ranges.append([start, end])
    ranges = new_ranges

print(min(x[0] for x in ranges))



print("took %s seconds" % (time.time() - start_time))