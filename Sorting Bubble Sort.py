#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# https://www.hackerrank.com/challenges/ctci-bubble-sort
# Bubble sort:
# Go through list, comparing each element with the next one.  If the pair are out of order, swap them.
# Idea is that all elements slowly bubble across to their correct place, after repeated loops through the list.
# On the 1st loop, the last element will be correct (larger or smaller than all the rest).
# On the second, the last but one.
# If the length is n, can see you will need at most n-1 loops to get the list in order.

# Dummy input list
a = [3, 2, 1, 5, 2, 4, 7, 6, 3, 6, 6, 7]

totalSwaps = 0
for i in range(len(a)):
    numberOfSwaps = 0
    for j in range(len(a) - i - 1):
        if a[j] > a[j+1]:
            (a[j], a[j+1]) = (a[j+1], a[j])
            numberOfSwaps += 1

    totalSwaps += numberOfSwaps
    if numberOfSwaps == 0:
        break

print('Array is sorted in %s swaps.' % totalSwaps)
print('First Element: %s' % a[0])
print('Last Element: %s' % a[-1])
