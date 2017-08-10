#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *


# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/sherlock-and-cost?h_r=internal-search

# Given an array B and need to come up with the maximum 'cost' value of an array
# A where 1 <= A[i] <= B[i] for each i and cost is given by the sum of the absolute
# value of the differences of the consecutive pairs of elements.

# Some thought shows that there must always be a solution for A that gives the maximum cost
# where, for each i, A[i] = 1 or A[i] = B[i].
# Support A is a solution of maximum cost where this is not the case.
# Choose i such that the above condition is not met.
# Then the neighbours of A[i] (or neighbour, if this is an edge element) can't both be
# smaller or equal to, or greater or equal to, as the solution would not be optimal.
# So (it can't be an edge element and) one side is strictly greater and the other is strictly smaller.
# So we can take 1 from A[i] without changing the cost of A.
# You can see we can repeat this process until A[i] = 1, showing us how to get the solution we're after.

# Now imagine we have functions H (for 'high') and L (for 'low') such that:
#   * H(B) gives the max cost of an array A with A[-1] = B[-1]
#   * L(B) gives the max cost of an array A with A[-1] = 1
# Then:
#   Cost(B) = max(H(B), L(B))
#   H(B[:i]) = max(H(B[:i-1]) + abs(B[i]-B[i-1]), L(B[:i-1]) + B[i] - 1)
#   L(B[:i]) = max(H(B[:i-1]) + B[i-1] - 1, L(B[:i-1]))


def cost(b1, b2, high=0, low=0):
    H_new = max(H + abs(b2 - b1), L + b2 - 1)
    L_new = max(H + b1 - 1, L)
    # print('H = %s.  L = %s' % (H_new, L_new))
    return H_new, L_new


#T = int(input().strip())
T = 1
for i in range(T):
    #N = int(input().strip())
    #B = [int(x) for x in input().strip().split()]
    B = [1,4,6]
    if len(B) == 1:
        # Not obvious from the question, but in the case of an array of length 1, the cost is 0
        cost_B = 0
    else:
        # Set the solutions for length = 2 (the trivial case)
        H = B[1] - 1
        L = B[0] - 1
        # print('H = %s.  L = %s' % (H, L))
        for j in range(3, len(B) + 1):
            H, L = cost(*B[j - 2: j], high=H, low=L)
        cost_B = max(H, L)
    print(cost_B)