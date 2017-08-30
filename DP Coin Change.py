#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *
import bisect
#  https://www.hackerrank.com/challenges/ctci-coin-change?h_r=next-challenge&h_v=zen

# n = num dollars
# m = num different types of coin for change

def make_change_iterative(coins, n):
    # Say you have k coins and want to find all the ways to get change for n.
    # Method is to imagine using j = 0, ..., k coins and compute for 1, ..., n.
    # So imagine a grid - coins used down the side and n (the sum) across the top.
    # Fill in left to right, top to bottom.
    # Two steps for each square - num times I can make this value with these coins is:
    #   * num times I can make this value not using the most recent coin (ie. the coin associated with this row) at all
    #   * plus the num time I can make this value using the coin at least once.
    solutions = dict()
    # key = ((coins used), n)
    solutions[((), 0)] = 1  # One way to make 0 with no coins
    for i in range(1, n+1):
        solutions[((), i)] = 0
    for i in range(1, len(coins)+1):
        current_coins = tuple(coins[:i])
        for j in range(0, n+1):
            if j == current_coins[-1]:
                solutions[(current_coins, j)] = solutions[(current_coins[:-1], j)] + 1
            else:
                solutions[(current_coins, j)] = solutions[(current_coins[:-1], j)] + solutions.get((current_coins, j-current_coins[-1]), 0)
    return solutions[coins, n]


n = 4
coins = (1, 2, 3)
print(make_change_iterative(coins, n))

# Would be nice to write out a successful recursive solution that uses memoisation