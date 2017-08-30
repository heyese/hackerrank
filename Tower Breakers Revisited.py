#!/bin/env python
import bisect
import sys
import datetime
import math


# https://www.hackerrank.com/challenges/tower-breakers-revisited-1

# As was apparent to me initially, it's easier to see what's going on when you instead consider the tower heights
# as being given by the number of prime factors they have.
# I see now, having looked at the Nim problem, that you then have a game of Nim.

def timer(func):
    def new_func(towers):
        then = datetime.datetime.now()
        j = func(towers)
        now = datetime.datetime.now()
        difference = now - then
        print('That took %s.%s seconds' % (difference.seconds, difference.microseconds))
        return j
    return new_func

def populate_primes_with_bisect(x):
    """Populates the primes list for all primes < x"""
    nums = [i for i in range(3, x+1, 2)]
    primes = [2]
    while True:
        try:
            p = nums.pop(0)
        except:
            break
        primes.append(p)
        j = p**2
        while j <= x:
            index = bisect.bisect_left(nums, j)
            try:
                if nums[index] == j:
                    nums.pop(index)
            except:
                pass
            j += 2 * p
    return primes

def num_prime_factors(x):
    num_factors = 0
    root = math.sqrt(x)
    for i in primes:
        if i > root:
            break
        while True:
            if x % i == 0:
                num_factors += 1
                x = x // i
            else:
                break
        if x == 1:
            break
    if x != 1:
        # x is itself a prime
        num_factors += 1
    return num_factors

def num_factors_list(l):
    num_factors_l = []
    for i in l:
        num_factors_l.append(num_prime_factors(i))
    return num_factors_l

def nim_sum(towers):
    nim_sum = 0
    for t in towers:
        nim_sum = nim_sum ^ t
    return nim_sum

# Can have tower heights up to 10**6, and I need to factorise these.
# Calculate the primes up to math.sqrt(10**6).  Then, any tower height
# not divisible by these primes must itself be prime.
primes = populate_primes_with_bisect(int(math.sqrt(10**6)))

# Deal with the input
#T = int(input().strip())
for game in range(1):
    #N = int(input().strip())
    #tower_heights = [i for i in map(int, input().strip().split()) if i != 1]
    tower_heights = [2]
    tower_heights_in_prime_factors = num_factors_list(tower_heights)
    print(tower_heights_in_prime_factors)
    if nim_sum(tower_heights_in_prime_factors) == 0:
        print(2)
    else:
        print(1)
