#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# Given a divisor and a set of integers,
# find the size of the greatest possible subset
# such that no pair of integers are divisible by k.

k = 3
ints = {1,2,5, 7, 12, 6}

# Initial approach:
# Find all pairs of integers divisible by k
# Keep eliminating integers, starting from those with the highest number of occurrences,
# until all pairs have lost at least 1 integer
# The remaining integers, along with any others that weren't in pairs, then form the subset

# Find all pairs whose sum is divisible by k
import itertools
def pairs_divisible_by_k(ints):
    all_pairs = itertools.combinations(list(ints), 2)
    pairs = set()
    for p in all_pairs:
        if sum(p) % k == 0:
            pairs.add(p)
    return pairs


# Eliminate the integer that occurs in most pairs, and repeat ...
import collections


class Pairs(object):
    def __init__(self, pairs):
        self.pairs = pairs

    def which_integers_should_go(self):
        get_rid = []
        while len(self.pairs) > 0:
            i = self.next_int_to_lose()
            if log: print("Get rid of: %s" % i)
            get_rid.append(i)
            self.pairs = {p for p in self.pairs if i not in p}
        return get_rid

    def next_int_to_lose(self):
        chains = [[]]
        while True:
            myDict = collections.defaultdict(list)
            if log: print("Chains are: %s" % str(chains))
            for chain in chains:
                if log: print("Considering chain: %s" % str(chain))
                maxFreq, new_chains = self.best_ints_to_lose(current_chain=chain)
                if log: print("New chains: %s" % str(new_chains))
                if new_chains is None:
                    # Can't get any more subsets
                    if log: print("No more subsets - best chain is: %s" % chain)
                    return chain[0]
                for new_chain in new_chains:
                    myDict[maxFreq].append(new_chain)
            maxFreq = max([i for i in myDict])
            if len(myDict[maxFreq]) == 1:
                chain = myDict[maxFreq][0]
                if log: print('Best chain is: %s' % chain)
                break
            else:
                chains = myDict[maxFreq]

        return chain[0]

    def best_ints_to_lose(self, current_chain=None):
        # Calculate current pairs from self.pairs,
        # removing the current_chain elements
        pairs = {p for p in self.pairs if len(set(p).intersection(set(current_chain))) == 0}
        if len(pairs) == 0:
            return 0, None
        # Identify those elements that occur most frequently in pairs
        num_freq = collections.defaultdict(int)
        for p in pairs:
            for i in p:
                num_freq[i] += 1
        maxFreq = max(num_freq.values())
        losers = [i for i in num_freq if num_freq[i] == maxFreq]
        if log: print("Returning: (%s, %s)" % (maxFreq, [current_chain + [l] for l in losers]))
        return maxFreq, [current_chain + [l] for l in losers]

log = False
pairs = pairs_divisible_by_k(ints)
if log: print("Pairs divisible by %s are: %s" % (k, str(pairs)))
pairs_object = Pairs(pairs)
integers = pairs_object.which_integers_should_go()
print(len(ints) - len(integers))
