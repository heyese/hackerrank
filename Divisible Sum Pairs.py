
import collections
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c = collections.Counter()
    pairs = 0
    for i in range(n-1, -1, -1):
        pairs += c[(k-ar[i]) % k]
        c[ar[i] % k] += 1
    return pairs

if __name__ == '__main__':

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(f'{result}')


FWmBbPwJot47yceIq4M1