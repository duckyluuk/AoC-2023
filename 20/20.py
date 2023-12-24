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
lines = read_lines_list('20')

info = {}
starts = []
cycles = {}
source = None
for ln in lines:
    name, dest = ln.split(' -> ')
    dest = dest.split(', ')
    if 'rx' in dest:
        source = name[1:]
    info[name[1:]] = {
        'dest': dest,
        'type': name[0],
        'state': 0 if name[0] == '%' else {}
    }
    
for k in info:
    for dest in info[k]['dest']:
        if dest == source:
            starts.append(k)
            cycles[k] = 0
        if dest in info and info[dest]['type'] == '&':
            info[dest]['state'][k] = 0

# part 1
print("PART 1:")
high = 0
low = 0

for i in range(1000):
    low += 1
    queue = [[dest, 0, 'roadcaster'] for dest in info['roadcaster']['dest']]

    while queue:
        # print(queue)
        dest, pulse, origin = queue.pop(0)
        if pulse == 0:
            low += 1
        elif pulse == 1:
            high += 1
        if not dest in info: continue
        node = info[dest]
        if node['type'] == '%':
            if pulse == 0:
                node['state'] = 1-node['state']
                for d in node['dest']:
                    queue.append([d, node['state'], dest])
        if node['type'] == '&':
            node['state'][origin] = pulse
            if all([node['state'][d] for d in node['state']]):
                for d in node['dest']:
                    queue.append([d, 0, dest])
            else:
                for d in node['dest']:
                    queue.append([d, 1, dest])
            
print(low * high)


# part 2
print("PART 2:")
press = 0

while starts:
    press += 1
    queue = [[dest, 0, 'roadcaster'] for dest in info['roadcaster']['dest']]

    while queue:
        # print(queue)
        dest, pulse, origin = queue.pop(0)
        if dest in starts and pulse == 0:
            if cycles[dest] == 0:
                cycles[dest] = press
            else:
                cycles[dest] = press - cycles[dest]
                print(press)
                starts.remove(dest)


        if not dest in info: continue
        node = info[dest]
        if node['type'] == '%':
            if pulse == 0:
                node['state'] = 1-node['state']
                for d in node['dest']:
                    queue.append([d, node['state'], dest])
        if node['type'] == '&':
            node['state'][origin] = pulse
            if all([node['state'][d] for d in node['state']]):
                for d in node['dest']:
                    queue.append([d, 0, dest])
            else:
                for d in node['dest']:
                    queue.append([d, 1, dest])
    
print(math.lcm(*[cycles[x] for x in cycles]))
n=1
for x in cycles:
    n *= cycles[x]
print(n)
print(cycles)
print("took %s seconds" % (time.time() - start_time))