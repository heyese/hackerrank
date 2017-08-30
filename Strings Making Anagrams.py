#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *


# https://www.hackerrank.com/challenges/ctci-making-anagrams

# Feels like the most sensible thing to do here is:
#   * sort both lists
#   * walk through both lists at the same time, constructing a third list with the common letters
#   * whenever two characters are different, pick the one that occurs earlier in the alphabet and 'delete' it - move
#     onto the next character in that list
#   * when you reach the end of one of the strings, stop.  Your 3rd list is the common anagram.  The number of deletes
#     it took is the number of deleted characters, plus the number of characters left in the longer of the two lists.


def number_needed(a, b):
    a = sorted(a)
    b = sorted(b)
    i, j = 0, 0
    deletes = 0
    #anagram = ''
    while True:
        try:
            if a[i] < b[j]:
                i += 1
                deletes += 1
            elif a[i] > b[j]:
                j += 1
                deletes += 1
            else:  # a[i] == b[j]
                # Common letter
                #anagram += a[i]
                i += 1
                j += 1
        except:
            break
    if i == len(a):
        deletes += len(b[i:])
    else:
        deletes += len(a[i:])
    return deletes

#a = input().strip()
#b = input().strip()

a = 'sdjsajjw'
b = 'sahjdhwjasdas'

print(number_needed(a, b))