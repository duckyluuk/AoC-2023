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


flow, ratings = read_groups('19')

start_time = time.time()

# input parsing
info = {}
for f in flow:
    name, rules = f[:-1].split("{")
    info[name] = [x.split(':') for x in rules.split(',')]

# part 1
print("PART 1:")
ans = 0

for r in ratings:
    position = 'in'
    x=m=a=s=0
    exec(r[1:-1].replace(',',';'))
    while position not in ['R', 'A']:
        for rule in info[position]:
            if len(rule) == 1:
                position = rule[0]
                break
            if eval(rule[0]):
                position = rule[1]
                break

    if position == 'R':
        continue
    else:
        ans += x + m + a + s

print(ans)


# part 2
print("PART 2:")
ans_2 = 0

ranges = [
    {
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000],
        'pos': 'in',
    }
]

from copy import deepcopy
while ranges:
    current = ranges.pop(0)
    if current['x'][0] >= current['x'][1] or current['m'][0] >= current['m'][1] or current['a'][0] >= current['a'][1] or current['s'][0] >= current['s'][1]:
        continue
    if current['pos'] == 'R':
        continue
    if current['pos'] == 'A':
        ans_2 += (current['x'][1] - current['x'][0] + 1) * (current['m'][1] - current['m'][0] + 1) * (current['a'][1] - current['a'][0] + 1) * (current['s'][1] - current['s'][0] + 1)
        continue
    rule = info[current['pos']]
    for r in rule:
        if len(r) == 1:
            ranges.append({**current, 'pos': r[0]})
            break
        else:
            var = r[0][0]
            op = r[0][1]
            num = int(r[0][2:])
            res = r[1]
            new_range = deepcopy(current)
            if op == '>':
                new_range[var][0] = max(current[var][0],num+1)
                current[var][1] = min(current[var][1],num)
            elif op == '<':
                new_range[var][1] = min(current[var][1],num-1)
                current[var][0] = max(current[var][0],num)

            new_range['pos'] = res
            ranges.append(new_range)


print(ans_2)

print("took %s seconds" % (time.time() - start_time))