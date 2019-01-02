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






if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    print(f'{result}')

