# https://www.hackerrank.com/challenges/beautiful-binary-string/problem


import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):

    substr = ''
    expecting = '0'
    moves = 0
    for c in b:
        if  c == expecting:
            substr += c
            expecting = '0' if expecting == '1' else '1'
            # Best use of a move is to stop two instances of the
            # '010' pattern (by changing it to 01110), which is
            # why we look at up to 5 characters at a time.
            if len(substr) == 5:
                moves += 1
                # Of course, need to remember that the end '0' could
                # be used in the next '010' pattern
                substr = '0'
        else:
            if len(substr) >= 3:
                moves +=1
            # If we've got an out of sequence character, if it's a
            # '0' then it is the first character in our next sequence
            # Otherwise we start looking again from scratch
            substr, expecting = ('0', '1') if c == '0' else ('', '0')

    # Got to remember that our final character may have been 'in sequence'
    # (ie. as expected) but we might not yet have five characters.  ie. 010 or 0101
    if len(substr) >= 3:
        moves += 1
    return moves


def beautifulBinaryString_simple(b):

    # Oh dear - this is much easier.
    # An easier idea - effectively what I was doing before, but without realising it,
    # is to work left to right and, for every '010' pattern, replace the last '0'
    # with a '1'.
    # That gets rid of all '01010' patterns and all single '010' patterns.
    # The number of replacements can easily be calculated by comparing the length
    # of the resulting string to the original.
    a = b.replace('010', '')
    return int((len(b) - len(a))/3)




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    print(f'{result}')

