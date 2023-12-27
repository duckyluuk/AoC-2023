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
lines = read_lines_list("25")



# part 1
print("PART 1:")
ans = 0

# nodes = {}

# for line in lines:
#     start, connects = line.split(": ")
#     connects = connects.split(" ")
#     nodes[start] = connects
#     for connect in connects:
#         if connect not in nodes:
#             nodes[connect] = []
#         nodes[connect].append(start)

nodes = set()
import networkx as nx
G = nx.Graph()
for line in lines:
    start, connects = line.split(": ")
    connects = connects.split(" ")
    nodes.add(start)
    for connect in connects:
        nodes.add(connect)
        G.add_edge(start, connect)

cuts = nx.minimum_edge_cut(G)
G.remove_edges_from(cuts)

a, b = list(nx.connected_components(G))
print(len(a) * len(b))


# part 2
print("PART 2:")
ans_2 = "brrr"



print(ans_2)



print("took %s seconds" % (time.time() - start_time))