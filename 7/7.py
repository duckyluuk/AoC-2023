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

lines = read_lines_list(7)

start_time = time.time()

def get_set_value(hand, jokers=False):
    nums = []
    cards = [*hand]
    joker_count = 0
    while cards:
        card = cards.pop()
        if card == "J" and jokers:
            joker_count += 1
            continue
        nums.append(cards.count(card) + 1)
        cards = list(filter(lambda x: x != card, cards))
    nums = list(sorted(nums, reverse=True)) + [0]
    if joker_count:
        nums[0] += joker_count
    return nums
    
# input parsing
lines = [*map(str.split, read_lines_list(7))]
VALUES = "23456789TJQKA"

# part 1
print("PART 1:")

sorted_cards = sorted(lines, key=lambda line: (get_set_value(line[0], False), list(map(VALUES.find, line[0]))))
print(sum([int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted_cards)]))


# part 2
print("PART 2:")

sorted_cards = sorted(lines, key=lambda line: (get_set_value(line[0], True), list(map(VALUES.find, [x if x!="J" else "1" for x in line[0]]))))
print(sum([int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted_cards)]))


print("took %s seconds" % (time.time() - start_time))