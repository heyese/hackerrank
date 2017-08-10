#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import string
import re

def sherlockAndAnagramsBruteForce(s):
    # Complete this function
    num_anagrams = 0
    for i in range(len(s)):
        j = i + 1
        while j <= len(s):
            length = 1
            while length <= len(s) - i - 1:
                if sorted((s[i:i + length])) == sorted((s[j:j + length])):
                    num_anagrams += 1
                length += 1
            j += 1
    return num_anagrams

def sherlockAndAnagrams(s):
    # Complete this function
    # Ahem - without trying to brute force it

    # You can't have two strings be anagrams of each other without a pair of a particular character.
    # You only need one pair - for example:  'aifa' -> 'aif' and 'ifa'
    # So - identify all pairs of characters.
    # Now - how do we identify all anagrams associated with a particular pair of characters?
    # For a pair of anagrams, if they overlap, then the first character of the left hand anagram must be part of a pair.
    # If they don't overlap, then every character must be part of a pair.
    # So I can consider the left most character of the first string as being the first character in the left anagram string.
    # ie.  looking at the pair of fs in  '...abcfghfxyz...', I don't need to compare
    # 'cf', 'bcf', 'abcf' with other strings, since if I work from left to right I will have
    # considered those already when I look at the pair of 'c's, 'b's and 'a's, respectively.

    # So on the left I'm comparing 'fg', 'fgh', 'fghf', ... with strings containing the other f.
    # Unfortunately, I can't consider the right hand side 'f' to be the first character in the right hand side anagram.
    # But, if you imagine comparing strings of increasing length, once these two strings overlap, it is clear that
    # anagrams will be found only when the difference in the strings appears in the rest of the string.
    # eg. If we set the first character of the right anagram to be the 'f'.
    # we check (fg, fx), (fgh, fxy), (fghf, fxyz): at this point, the strings have overlapped.
    # I see that, as I increase the size of these strings, I will only have anagrams when the difference - 'fgh' -
    # appears after the end of the right hand string.  I can easily look for all of these. (the find_remaining_anagrams function)
    # The thing to be careful of here is that I don't overcount.  (Some care needs to be taken when you're considering
    # a pair of a particular character where there are other occurrences of that same character inbetween.)

    def all_pairs(s):
        char_indexes = dict()
        for char in string.ascii_lowercase:
            i = s.find(char, 0)
            if i == -1:
                continue
            first = True
            while True:
                j = s.find(char, i+1)
                if j == -1:
                    break
                else:
                    if first:
                        char_indexes[char] = [i]
                        first = False
                    char_indexes[char].append(j)
                    i = j
        return char_indexes

    def find_remaining_anagrams(substring, string):
        # Find all anagrams of 'substring' in 'string'
        anagram_list = []
        for i in range(len(string) - len(substring) + 1):
            s1 = string[i:i + len(substring)]
            if sorted(s1) == sorted(substring):
                anagram_list.append((i, substring))
        return anagram_list

    # char_indexes is a dict, where the keys are characters that appears more than once
    # in the given string and the values are lists of indexes for those characters.
    # eg. char_indexes[x] = [i, j ,k]
    char_indexes = all_pairs(s)

    # To keep track of the anagrams I've found
    #Elements are  (left_index, right_index, length)
    anagram_set = set()
    #import pdb
    #pdb.set_trace()
    for char in char_indexes:
        # As discussed above - it is enough to consider that the left string starts at left_index.
        for i in range(len(char_indexes[char])):
            left_index = char_indexes[char][i]
            # For each character that appears more than once, we consider each of its possible pairs.
            for j in range(len(char_indexes[char][i+1:])):
                right_index = char_indexes[char][i+1:][j]
                previous_right_index = char_indexes[char][i + j]
                # Enough to consider from the right index starting just after the index of the previous occurrence
                # of char. Because I will already have considered anagrams of all lengths with existing left index and
                # right index before the index of the previous occurrence of char.
                for r_anagram_start_index in range(previous_right_index + 1, right_index + 1):
                    # Now consider anagrams of different lengths, where the minimum length ensures the right string includes
                    # the right index.
                    length = right_index - r_anagram_start_index + 1
                    while True:
                        s1 = s[left_index:left_index + length]
                        s2 = s[r_anagram_start_index: r_anagram_start_index + length]
                        # Do the two strings intersect?
                        if left_index + length > r_anagram_start_index:
                            # two strings intersect.
                            # All further possible anagrams from these starting indexes as the lengths grow can be found
                            # by looking for anagrams of the string s[left_index:r_anagram_start_index] from the point
                            # s[left_index + length]
                            starting_index = left_index + length
                            substring = s[left_index:r_anagram_start_index]
                            further_anagrams = find_remaining_anagrams(substring, s[starting_index:])
                            intersect_length = length + left_index - r_anagram_start_index
                            for (x, substring) in further_anagrams:
                                anagram_set.add((left_index, starting_index - intersect_length, starting_index + x - left_index))
                            break
                        else:
                            # No intersection - simply a case of whether the two strings are anagrams
                            if sorted(s1) == sorted(s2):
                                anagram_set.add((left_index, r_anagram_start_index, length))
                        length += 1
                        # Check we're within the string
                        if r_anagram_start_index + length > len(s):
                            break
    return len(anagram_set)


q = 5
for s in [
#'ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel', # 399
#'gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde', # 471
#'mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw', # 370
#'ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges', # 403
#'zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw' #  428
'abcababc'
]:

    result = sherlockAndAnagrams(s)
    print(result)
    result = sherlockAndAnagramsBruteForce(s)
    print(result)