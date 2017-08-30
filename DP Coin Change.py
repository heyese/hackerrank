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

def make_change_recursive(coins, n, memo=None):
    # Decide how many times you are going to use a coin (I like to think of going from largest
    # to smallest, but it doesn't actually matter), then use recursion on what's left!!

    if memo is None:
        memo = dict()

    # The base cases.  If you've run out of coins and still need to give out more change, this isn't a solution.
    # If you've run out of coins and don't need to give any more change, this is a solution.
    if not coins:
        if n == 0:
            return 1
        else:
            return 0

    # Use memoisation - if we've done this particular problem before, look the answer up
    if (tuple(coins), n) in memo:
        print('Using memo dict for: %s' % str((tuple(coins), n)))
        return memo[(tuple(coins), n)]

    currentCoin = coins[0]
    result = 0
    j = 0
    while j * currentCoin <= n:
        # So here I'm imagining that in my change I have j of currentCoin.
        result += make_change_recursive(coins[1:], n - j*currentCoin, memo)
        j += 1
    memo[(tuple(coins), n)] = result

    return result

n = 20
coins = (1, 2, 3, 4)
print(make_change_recursive(coins, n))

# Would be nice to write out a successful recursive solution that uses memoisation