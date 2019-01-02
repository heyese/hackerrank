# https://www.hackerrank.com/challenges/pairs/problem

import collections


# Complete the pairs function below.
def pairs(k, arr):
    c = collections.Counter()
    num_pairs = 0
    for i in arr:
        num_pairs += c[i]
        c[i-k] += 1
        c[i+k] += 1
    return num_pairs

if __name__ == '__main__':

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(f'{result}')