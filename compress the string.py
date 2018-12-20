# https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools

def compress_the_string(s):
    for k, g in itertools.groupby(s):
        print('({}, {})'.format(len(list(g)), k),  end=' ')

s = '1222311'
compress_the_string(s)