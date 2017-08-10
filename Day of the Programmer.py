#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# https://www.hackerrank.com/challenges/day-of-the-programmer

def days_per_month(month_number, year):
    if month_number in [1,3,5,7,8,10,12]:
        return 31
    elif month_number != 2:
        return 30
    else:
        if year <= 1917:
            # Julian calendar
            if year % 4 == 0:
                return 29
            else:
                return 28
        elif year >= 1919:
            # Gregorian calendar
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                return 29
            else:
                return 28
        else:
            # year = 1918 - not a gregorian leap year
            # feb 14th -> feb 28
            return 15

def day_of_the_programmer(year):
    # day of the programmer is the 256th day of the year
    days = 0
    for month in range(1, 13):
        if days + days_per_month(month, year) <= 256:
            days += days_per_month(month, year)
        else:
            break
    return '{:02d}.{:02d}.{:04d}'.format(256 - days, month, year)

print(day_of_the_programmer(2016))