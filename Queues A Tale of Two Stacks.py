#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

# Asked to implement a queue using two stacks.
# Only way I can think of is to stick everything on stack 1.
# Then whenever we need to print or pop something from the 'queue', I push all the
# elements from stack 1 to stack 2 (thus reversing the ordering), then view or pop, and then push everything back again.

# A much more optimised version of the above is to only transfer elements onto stack2 when it is empty.
# ie. if you did 3 pop() operations in a row, it doesn't make sense to keep putting all the elements back onto stack1
# after each operation.

# In fact, I never need to put the elements back onto stack1!  So there is a put stack and a pop stack - I only ever
# need to occasionally transfer elements from the put to the pop.



class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        # If stack2 is empty, transfer stack1 across
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
            return x
        y = self.stack2[-1]
        return y

    def pop(self):
        # If stack2 is empty, transfer stack1 across
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
        y = self.stack2.pop()
        return y

    def put(self, value):
        self.stack1.append(value)
