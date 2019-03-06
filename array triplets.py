#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(a):
    n = len(a)
    for i in range(1, n -1):
        for j in range(1, n - i):
            k = n - i - j
            if i >= j >= k:
                # Pull out all subsets of these sizes from a




if __name__ == '__main__':

    a_count = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = solve(a)
    print(f'{result}')
