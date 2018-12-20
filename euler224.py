# https://www.hackerrank.com/contests/projecteuler/challenges/euler224

import itertools

def num_barely_obtuse(max_per):
    """
    Given a maximum perimeter, this function calculates the number of 'barely obtuse'
    triangles that are possible.  A barely obtuse triangle is one where the three sides a<=b<=c
    satisfy a**2 + b**2 = c**2 - 1
    :param max_per: the maximum perimeter the triangles are allowed to have
    :return: an int giving the number of possible 'barely obtuse triangles'
    """

    # Sides a, b, c.
    # a + b + c <= max_per
    pairs_of_squares = set()
    c_squared_minus_1 = set()
    for a, b in itertools.combinations(range(1, max_per), 2):
        pairs_of_squares.add(a**2 + b**2)
    for c in range(1, max_per):
        c_squared_minus_1.add(c**2 - 1)
    return len(pairs_of_squares.intersection(c_squared_minus_1))




Q = int(input())
for query in range(Q):
    N = int(input())
    print(num_barely_obtuse(N))