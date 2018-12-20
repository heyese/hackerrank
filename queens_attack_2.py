import math
import os
import random
import re
import sys
import itertools

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    # Have a dictionary, lengths, that gives the number of spaces the queen can move in each direction
    lengths = {
        'up': n - r_q,
        'down': r_q - 1,
        'left': c_q - 1,
        'right': n - c_q,
        'up_left': min(n-r_q, c_q-1),
        'up_right': min(n-r_q, n-c_q),
        'down_left': min(r_q-1, c_q-1),
        'down_right': min(r_q-1, n-c_q),
    }

    # Now we cycle through the obstacles and update the dictionary as we go along
    for r,c in obstacles:
        if r == r_q:
            if c < c_q:
                lengths['left'] = min(lengths['left'], c_q - c - 1)
                # The -1 on the c_q-c-1 above reflects that if someone is in this position, the queen can't move to it
            else:
                lengths['right'] = min(lengths['right'], c - c_q - 1)
        elif c == c_q:
            if r < r_q:
                lengths['down'] = min(lengths['down'], r_q - r - 1)
            else:
                lengths['up'] = min(lengths['up'], r - r_q - 1)
        elif (r - r_q) / (c - c_q) == 1:
            if r > r_q:
                lengths['up_right'] = min(lengths['up_right'], r - r_q - 1)
            else:
                lengths['down_left'] = min(lengths['down_left'], r_q - r - 1)
        elif (r - r_q) / (c - c_q) == -1:
            if r > r_q:
                lengths['up_left'] = min(lengths['up_left'], r - r_q - 1)
            else:
                lengths['down_right'] = min(lengths['down_right'], r_q - r - 1)

    # To find the number of spaces the queen can move to, we just return the sum of the dictionary values
    return sum(lengths.values())




if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)