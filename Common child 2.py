#!/bin/python3

# This works pretty well but is too slow.
# Looks like I'm not allowed to use recursion, but need to learn how to tackle this directly.

# A dictionary to cache the results of my recursive lookups
commonChildStore = dict()
# And a function that returns the answer, caching the new result if necessary
def do_lookup(x):
    if x not in commonChildStore:
        commonChildStore[x] = commonChild(*x)
    return commonChildStore[x]

def commonChild(s1, s2):
    if 0 in {len(s1), len(s2)}:
        return 0
    a, b = s1[-1], s2[-1]
    s1_a, s2_b = s1[:-1], s2[:-1]
    if a == b:
        # If the last letters of the two strings are the same, they
        # are definitely part of the common child
        return 1 + do_lookup((s1_a, s2_b))
    else:
        # Otherwise, I consider 3 cases.
        # Last letter of s1 is a part of common child,
        # last letter of s2 is a part of common child
        # or neither last letters are part of common child
        index2, index1 = s2.rfind(a), s1.rfind(b)
        len1 = do_lookup((s1_a, s2[:index2])) if index2 != -1 else -1
        len2 = do_lookup((s1[:index1], s2_b)) if index1 != -1 else -1
        len3 = do_lookup((s1_a, s2_b))
        return max(len1+1, len2+1, len3)

if __name__ == '__main__':

    s1 = input()
    s2 = input()

    result = commonChild(s1, s2)
    print(f'{result}')

