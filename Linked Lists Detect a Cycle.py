#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


# Initial, slightly pathetic solution, based on the fact that they've told
# me there won't be more than 100 elements in the list!
def has_cycle_poorly_implemented(head):
    i = 0
    node = head
    while i <= 100:
        if not node:
            return False
        node = node.next
        i += 1
    return True

# Alternative (memory efficient) is to have two pointers going round the list, one at twice the speed of the other,
# such that you know if there's a loop they will meet each other.
def has_cycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while True:
        if fast and fast.next:  # Don't need to test slow, as fast will already have tested it
            slow = slow.next
            fast = fast.next.next
        else:
            # End of the list - it's not looped
            return False
        if fast == slow:
            # Fast has caught up with slow
            return True
