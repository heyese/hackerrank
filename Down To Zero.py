import os
import sys

#
# Complete the downToZero function below.
#
def prime_factorisation(x):
    i = 2
    factors = []
    while x != 1:
        if x % i == 0:
            factors.append(i)
            x /= i
        else:
            i += 1
    return factors

def downToZero(n, factors=None):
    if not factors:
        factors = prime_factorisation(n)
    if n == 1:
        return 1
    elif len(factors) == 1:
        # n is prime - have to reduce by 1
        return 1 + downToZero(n-1)
    product = 1
    for index, factor in enumerate(factors):
        product *= factor
        if product >= (n / product):
            return 1 + downToZero(product, factors[:index+1])
        elif index + 2 == len(factors):
            return 1 + downToZero(n // product, factors[-1:])

if __name__ == '__main__':

    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = downToZero(n)
        print(f'{result}')

    #print(prime_factorisation(100))
