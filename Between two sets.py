# https://www.hackerrank.com/challenges/between-two-sets/problem
import math
import collections

def prime_factorization(x):
    c = collections.Counter()
    factor = 2
    while x > 1:
        if not x % factor:
            x /= factor
            c[factor] += 1
        else:
            factor += 1
    return c

def getTotalX(a, b):

    # Get lowest common multiple of a
    lcm_factors = collections.Counter()
    for i in a:
        pf = prime_factorization(i)
        for factor in pf:
            lcm_factors[factor] = max(lcm_factors[factor], pf[factor])
    lcm_a = 1
    for i in lcm_factors:
        lcm_a *= i ** lcm_factors[i]

    # Get greatest common divisor for entries of b
    gcd_b = 0
    for i in b:
        gcd_b = math.gcd(i, gcd_b)

    # if lcm_a does not divide gcd_b, there is no number which is a multiple
    # of all elements of a which also divides all elements of b
    if gcd_b % lcm_a:
        return 0

    # So the numbers we are looking for are precisely those that are a multiple of lcm_a
    # that also divide gcd_b.
    # Say gcd_b = lcm_a * X.  We are after the number of factors of X.
    x = gcd_b // lcm_a
    pf = prime_factorization(x)
    num = 1
    for i in pf:
        num *= pf[i] + 1
    return num


def getTotal_2(a, b):
    # This time based on knowing the input values are small

    # Numbers that are divisible by all elements of a:
    divisible_by_a = []
    for num in range(1, 101):
        candidate = True
        for i in a:
            if num % i:
                candidate = False
                break
        if candidate:
            divisible_by_a.append(num)

    # Which of those divide all of b?
    number_dividing_b = 0
    for num in divisible_by_a:
        candidate = True
        for i in b:
            if i % num:
                candidate = False
                break
        if candidate:
            number_dividing_b += 1

    return number_dividing_b



if __name__ == '__main__':

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotal_2(a, b)
    print(f'{total}')