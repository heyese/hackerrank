#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *
import sys
import bisect

input = '1 5 5'
chocs = [int(x) for x in input.split()]

amounts = [5, 2, 1]

# Adding chocolates to all but one is the same as subtracting chocolates from one,
# and it's much simpler to think in this way.
# It seems clear to me that the best first move is to keep taking 5 from each element
# until all elements are less than 5 away from the smallest element.
# The next move is then not obvious, so I think I just have to compute the number manually from there.


def moves_to_equalise_list(myList, value):
    # Know that min(myList) >= value
    # Moves I can make are take 5, take 2 and take1
    def moves_to_equalise(a, b):
        moves_used = 0
        for divisor in [5, 2, 1]:
            moves = (a - b) // divisor
            if moves == 0:
                continue
            else:
                a = a - moves * divisor
                moves_used += moves
        return moves_used

    total_moves = 0
    for i in myList:
        if (i - value) not in cached_answers:
            cached_answers[i-value] = moves_to_equalise(i, value)
        total_moves += cached_answers[i - value]
    return total_moves


num_moves = 0
chocs = sorted(chocs)

# To begin with, you take 5 from each element until all elements are less than 5 greater than the minimum element.
# At this stage, I'm either trying to make all elements = Min(chocs),
# or Min(chocs) -1, or Min(cocs) -2 , or Min(chocs) -3, or Min(chocs) -4.
# (Don't need to consider any less, as first step would be to take 5 from all elements which is clearly an
# unnecessary step)
# Actually, don't need to consider Min(chocs) -2 or Min(chocs) -1,
moves = []
cached_answers = {0: 0}
for i in [0, 1, 2, 3, 4]:
    moves.append(moves_to_equalise_list(chocs, chocs[0]-i))
print(min(moves))