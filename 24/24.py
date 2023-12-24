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

def line_intersection(line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
		return 0, 0

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return x, y


# input parsing
lines = read_lines_list("24")
hailstones = []
for ln in lines:
    x, y, z, vx, vy, vz = eval(ln.replace(" @", ","))
    hailstones.append([x, y, z, vx, vy, vz])


# part 1
print("PART 1:")
ans = 0
MIN = 200000000000000
MAX = 400000000000000  
for i in range(len(hailstones)):
    stone1 = hailstones[i]
    for j in range(i+1, len(hailstones)):
        stone2 = hailstones[j]
        x, y = line_intersection(((stone1[0], stone1[1]), (stone1[0] + stone1[3], stone1[1] + stone1[4])), ((stone2[0], stone2[1]), (stone2[0] + stone2[3], stone2[1] + stone2[4])))
        if MIN <= x <= MAX and MIN <= y <= MAX:
            # past detection
            if (x - stone1[0]) / stone1[3] < 0: continue
            if (y - stone1[1]) / stone1[4] < 0: continue
            if (x - stone2[0]) / stone2[3] < 0: continue
            if (y - stone2[1]) / stone2[4] < 0: continue
            ans += 1

print(ans)



# part 2
print("PART 2:")
# i have no idea how this works but 
from z3 import Int, Solver, sat
fx,fy,fz,opt = Int("fx"), Int("fy"), Int("fz"), Solver()
fdx,fdy,fdz = Int("fdx"), Int("fdy"), Int("fdz")
for i, (x,y,z, dx,dy,dz) in enumerate(hailstones[:3]):
    t = Int(f"t{i}")
    opt.add(t >= 0)
    opt.add(x + dx * t == fx + fdx * t)
    opt.add(y + dy * t == fy + fdy * t)
    opt.add(z + dz * t == fz + fdz * t)
assert str(opt.check()) == 'sat'
print(opt.model().eval(fx + fy + fz))

print("took %s seconds" % (time.time() - start_time))