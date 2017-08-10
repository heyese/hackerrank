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





# Deal with the input
g = int(input().strip())
for game in range(g):
    n = int(input().strip())
    tower_heights = [i for i in map(int, input().strip().split()) if i != 0]

    # Strip pairs of towers of same height out - reasoning given in the function
    tower_heights_pairs_stripped = strip_pairs(tower_heights)
    if who_wins(tower_heights_pairs_stripped) == 1:
        print('First')
    else:
        print('Second')