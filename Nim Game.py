#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import itertools
import bisect
import math
import sys
import datetime



# https://www.hackerrank.com/challenges/nim-game-1/submissions/code/51345787

# I've looked up the solution to Nim.
# My recursive strategy just wasn't cutting it - just couldn't pass all the tests, even with optimisations.
# Idea is to calculate the 'nim sum' - a kind of vector addition of the positions modulo 2.
# If the initial position has nim sum = 0, it's a losing position.  Else it's a winning position.

def nim_sum(towers):
    nim_sum = 0
    for t in towers:
        nim_sum = nim_sum ^ t
    return nim_sum



# Deal with the input
g = int(input().strip())
for game in range(g):
    n = int(input().strip())
    tower_heights = [i for i in map(int, input().strip().split()) if i != 0]
    if nim_sum(tower_heights) == 0:
        print('Second')
    else:
        print('First')
