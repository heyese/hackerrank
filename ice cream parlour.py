# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

import math
import os
import random
import re
import sys
import itertools


def whatFlavors(costs, money):
    # Use itertools to give me the cost of all pairs of icecream flavours
    compliment_flavours = {}
    for index, cost in enumerate(costs):
        if cost in compliment_flavours:
            return f'{min(index + 1, compliment_flavours[cost])} {max(index + 1, compliment_flavours[cost])}'
        else:
            compliment_flavours[money - cost] = index + 1



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        costs = list(map(int, input().rstrip().split()))

        print(whatFlavors(costs, money))
