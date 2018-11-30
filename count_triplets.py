# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


import collections
import itertools

def count_triplets(arr, r):
    v2 = collections.defaultdict(int)
    v3 = collections.defaultdict(int)
    count = 0
    for i in arr:
        # i could be the beginning of a triplet, the 2nd in a triplet or the third of a triplet

        # i the third of a triplet
        count += v3[i]

        # i the second of a triplet
        v3[i * r] += v2[i]

        # i the first of a triplet
        v2[i * r] += 1
    return count



arr = [5, 5, 5, 25, 25, 5, 25, 125]
r = 5
print(count_triplets(arr, 5))