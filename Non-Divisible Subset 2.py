#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# I've cheated, and seen a comment someone made about this puzzle.
# It was, however, awesome, and I'd like to code the idea up.

# IDEA:
# Partition the given integers into sets determined by the remainder after division with k
# eg. for k = 6, we would have a set for each remainder r in [0,1,2,3,4,5]
# An integer from any set plus an integer from any other set is then only divisible by k
# if the sum of the remainders is k.
# An exception is if both integers are divisible by k, in which case the sum of the remainders is 0.
# Clearly we can only have a single integer from the set associated with remainder 0.
# Another type of special case is k/2 for when k is even.  We can similarly only have one integer from this set.
# For all the other sets, compare the size of it with it's partner set.  (ie. for k = 6, the '1' set and the '5' set.)
# We discard the integers from the smaller set and keep all those in the larger one.

import collections
k = 3
ints = {1, 7, 2, 4}

remainder_sets = collections.defaultdict(set)
for i in ints:
    remainder = i % k
    remainder_sets[remainder].add(i)
#print(remainder_sets)
subset_length = 0
if len(remainder_sets[0]) > 0:
    # Can only have one integer from this set
    subset_length += 1
for i in range(1, k//2 + 1):
    if i == k/2:
        # Can only have one integer from this set
        if len(remainder_sets[i]) > 0:
            subset_length += 1
    else:
        num = max(len(remainder_sets[i]), len(remainder_sets[k-i]))
        subset_length += num
print(subset_length)
