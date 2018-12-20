# https://www.hackerrank.com/challenges/validating-postalcode/problem

import re

# Need a regex that matches only integers in the
# range from 100,000 to 999,999 inclusive.

regex_integer_in_range = re.compile('[1-9][0-9]{5}$')


# Need a regex to pick all alternating repetitive digiit pairs
# Find all gives non-overlapping matches, so I need to use look ahead
regex_alternating_repetitive_digit_pair = re.compile(r'(\d)(?=.\1)')