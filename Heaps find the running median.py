#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

#https://www.hackerrank.com/challenges/ctci-find-the-running-median?h_r=next-challenge&h_v=zen

# Heap is a data structure that isn't fully sorted.
# Means elements with certain characteristics can be found quickly, and maintaining
# the semi-sorted structure is also quick.

# For a median, you just need to know either the middle or middle two elements.
# So can see that maintaining two heaps can be used for this - a maxHeap (easy to pop off largest element) with elements
# less than the median, and a minHeap (easy to pop off the smallest elements) with elements greater than the media.
# When you get a new element, you put it into the appropriate heap depending on it's relation to the previous median.
# When heap sizes become unbalanced, you make the obvious move - smallest element from the big numbers to the small,
# or biggest element from the small numbers to the big.


import heapq

a = []
minHeap = []  # Elements > median
maxHeap = []  # Elements < median
numbers = [2, 6, 3, 6, 3, 6, 5, 8, 23, 12, 34, 1, 1, 10, 1000, 20, 7, 20, 21, 21, 21, 21, 21, 30, 30, 30]
first = True

# Will use 'x' to track the relative size of heaps.
# x = -1 -> maxHeap has an additional element
# x = 0 -> heaps are equal size
# x = 1 -> minHeap has an additional element
#n = int(input().strip())
#for i in range(n):
for i in range(len(numbers)):
    #num = int(input().strip())
    num = numbers[i]
    if first:
        maxHeap.append(-num)
        median = num
        x = -1
        first = False

    elif num > median:
        heapq.heappush(minHeap, num)
        if x == 1:
            # Have now added two elements in a row to this heap
            # Pass the smallest element over to the maxHeap
            a = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -a)
            # Now heaps are equal size
            x = 0
            # Now know the two piles have equal numbers of elements
            # -> The new median is the average of the max from the maxHeap (which is 'a'), and min from the minHeap
            median = (a + minHeap[0]) / 2
        elif x == -1:
            # Heaps are now of equal size
            x = 0
            median = (minHeap[0] - maxHeap[0]) / 2
        else:  # x == 0:
            # minHeap now has an extra element
            x = 1
            # median is min from minHeap
            median = minHeap[0]

    elif num < median:
        # Use -num, as the heapq heap implementation is for a minHeap.
        heapq.heappush(maxHeap, -num)
        if x == -1:
            a = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, a)
            x = 0
            median = (a - maxHeap[0]) / 2
        elif x == 1:
            # Heaps are now of equal size
            x = 0
            median = (minHeap[0] - maxHeap[0]) / 2
        else:  # x == 0
            x = -1
            median = -maxHeap[0]

    else:  # num == median:
        # Just want to keep the piles even, if possible
        if x == 0:
            heapq.heappush(minHeap, num)
            x = 1
            median = num
        elif x == -1:
            heapq.heappush(minHeap, num)
            x = 0
            median = (minHeap[0] - maxHeap[0]) / 2
        else:  # x == 1
            heapq.heappush(maxHeap, -num)
            x = 0
            median = (minHeap[0] - maxHeap[0]) / 2
    print('Added %s. Median is: %.1f, x = %s' % (num, median, x))




