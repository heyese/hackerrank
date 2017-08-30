#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# https://www.hackerrank.com/challenges/ctci-balanced-brackets

# Looks like, as hinted at, I just need to implement a stack.
# When I each time I hit a closing bracket, I check that the last element added was an opening bracket of that type



class Stack:

    class Node:
        def __init__(self, bracket):
            self.bracket = bracket
            self.next = None

    def __init__(self):
        self.top = None

    partner_brackets = {
        '}': '{',
        ']': '[',
        ')': '(',
    }

    def process_bracket(self, bracket):
        status = True
        if bracket in ['{', '[', '(']:
            self.add(bracket)
        else:
            status = self.remove(self.partner_brackets[bracket])
        return status

    def process_bracket_string(self, bracket_string):
        self.top = None
        for bracket in bracket_string:
            status = self.process_bracket(bracket)
            if not status:
                return False
        # Now we've processed all brackets, is the stack empty?
        if not self.top:
            return True
        return False

    def add(self, bracket):
        node = self.Node(bracket)
        node.next = self.top
        self.top = node

    def remove(self, bracket):
        if self.top and self.top.bracket == bracket:
            self.top = self.top.next
            return True
        else:
            # This is not a 'balanced bracket' string
            return False


stack = Stack()
string1 = '[]{{}}()'
string2 = '{{[}}'
string3 = '}[][]'
string4 = '{{[[(())]]}}'
print(stack.process_bracket_string(string1))
print(stack.process_bracket_string(string2))
print(stack.process_bracket_string(string3))
print(stack.process_bracket_string(string4))