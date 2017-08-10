#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *


s = 'asjdksajlkdsa'
n = 7


remainder = n % len(s)
num_whole_strings = n // len(s)
print(num_whole_strings * s.count('a') + s[:remainder].count('a'))
