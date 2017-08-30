#!/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

#https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# If left stem is a binary search tree
# and right stem is a binary search tree,
# and self.left < self.data < self.right,
#  --> whole tree is a binary search tree

def treesInOrder(root, trees=None):
    if not trees:
        trees = []
    if root:
        if root.left:
            trees = treesInOrder(root.left, trees)
        trees.append(root.data)
        if root.right:
            trees = treesInOrder(root.right, trees)
    return trees

def checkBSTUsingList(root):
    trees = treesInOrder(root, trees=None)
    i = trees[0]
    for j in trees[1:]:
        if j <= i:
            return False
        i = j
    return True

def checkBST(root, min=float('-Infinity'), max=float('Infinity')):
    if not root:
        return True
    if min < root.data < max \
        and checkBST(root.left, min, root.data) \
        and checkBST(root.right, root.data, max):
        return True
