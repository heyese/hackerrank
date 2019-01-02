# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

import string

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    # Instinctive approach:
    # Create a dict which, for a given letter, returns its index in the alphabet
    # Split input into two same length strings (dropping middle character if necessary)
    # Reverse the second string
    # Sum the absolute difference between alphabet indexes of each letter

    # Nifty dict comprehension to get the alphabet indexes:
    indexes = {c:i for (i, c) in enumerate(string.ascii_lowercase)}
    # Remember to reverse order of second half
    # And remember that (-3)//2 != -(3//2) !!
    half1, half2 = s[:len(s)//2], reversed(s[-(len(s)//2):])

    moves = 0
    # Iterate through half2, since it's the generator
    for i, c2 in enumerate(half2):
        c1 = half1[i]
        moves += abs(indexes[c1]-indexes[c2])
    return moves

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        print(f'{result}')

