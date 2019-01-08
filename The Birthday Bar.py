
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    total = 0
    n = len(s)
    sum = 0
    for i in range(n):
        sum += s[i]
        if i > m-3:
            if i-m >= 0:
                sum -= s[i - m]
            if sum == d:
                total += 1
    return total


if __name__ == '__main__':

    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(f'{result}')