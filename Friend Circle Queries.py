#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Just couldn't make it fast enough
# Read this for info: https://www.geeksforgeeks.org/disjoint-set-data-structures-java-implementation/

# Complete the maxCircle function below.


def maxCircle(queries):
    #set_index = dict()
    size_index = dict()
    set_reps = dict()
    set_reps_rev = collections.defaultdict(list)
    max_sizes = []
    max_set_size = 2
    for a, b in queries:
        a_rep = set_reps[a] if a in set_reps else None
        b_rep = set_reps[b] if b in set_reps else None
        if not a_rep and not b_rep:
            size_index[a] = 2
            set_reps[a], set_reps[b] = a, a
            set_reps_rev[a] = [a, b]
        elif not a_rep:
            set_reps[a] = b_rep
            size_index[b_rep] += 1
            set_reps_rev[b_rep].append(a)
            max_set_size = max(max_set_size, size_index[b_rep])
        elif not b_rep:
            set_reps[b] = a_rep
            size_index[a_rep] += 1
            set_reps_rev[a_rep].append(b)
            max_set_size = max(max_set_size, size_index[a_rep])
        elif a_rep == b_rep:
            pass
        else:
            # Must have been disjoint sets
            size_index[a_rep] += size_index[b_rep]
            for i in set_reps_rev[b_rep]:
                set_reps[i] = a_rep
            set_reps_rev[a_rep].extend(set_reps_rev[b_rep])
            del(set_reps_rev[b_rep])

            max_set_size = max(max_set_size, size_index[a_rep])
        max_sizes.append(max_set_size)
    return max_sizes


if __name__ == '__main__':

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)
    print('\n'.join(map(str, ans)))


