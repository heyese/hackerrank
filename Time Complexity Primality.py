#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import math
import bisect

# https://www.hackerrank.com/challenges/ctci-big-o


def isPrime(p):
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(p))+1, 2):
        if p % i == 0:
            return False
    return True


n = 11
if isPrime(n):
    print('Prime')
else:
    print('Not prime')
