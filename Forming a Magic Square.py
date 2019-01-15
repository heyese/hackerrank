# https://www.hackerrank.com/challenges/magic-square-forming/problem

import math
import os
import random
import re
import sys

class Magic_Square():
    def __init__(self):
        self.coords = {
        (0, 0): 8,
        (1, 0): 3,
        (2, 0): 4,
        (0, 1): 1,
        (1, 1): 5,
        (2, 1): 9,
        (0, 2): 6,
        (1, 2): 7,
        (2, 2): 2,
    }

    def rotate_90_degress(self, row, column):
        '''
        Given row, column coordinates, rotate them by 90 degrees (anti-clockwise, the way I've done it).
        So (1, 1) -> (1, 3) -> (3, 3) -> (3, 1)
        '''
        rotate_90 = {
            (0, 0): (0, 2),
            (1, 0): (0, 1),
            (2, 0): (0, 0),
            (0, 1): (1, 2),
            (1, 1): (1, 1),
            (2, 1): (1, 0),
            (0, 2): (2, 2),
            (1, 2): (2, 1),
            (2, 2): (2, 0),
        }
        x, y = rotate_90[(row, column)]
        return x, y

    def reflect(self, row, column):
        '''
        Imagine a mirror lying down the middle column, and reflect all given coordinates as such
        '''
        reflect_dict = {
            (0, 0): (0, 2),
            (1, 0): (1, 2),
            (2, 0): (2, 2),
            (0, 1): (0, 1),
            (1, 1): (1, 1),
            (2, 1): (2, 1),
            (0, 2): (0, 0),
            (1, 2): (1, 0),
            (2, 2): (2, 0),
        }
        x, y = reflect_dict[(row, column)]
        return x, y

    def find_cost(self, matrix, num_reflects, num_rotates):
        cost = 0
        for row in range(3):
            for column in range(3):
                x, y = row, column
                for _ in range(num_reflects):
                    x, y = self.reflect(x, y)
                for _ in range(num_rotates):
                    x, y = self.rotate_90_degress(x, y)
                cost += abs(matrix[row][column] - self.coords[(x, y)])
        return cost


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    '''
    The point is that there is is, subject to rotations and reflections, only one 3 * 3 magic square.
    With four 90 degree rotations and one reflection, that gives 8 possibilities.  So this function
    should find the cost of converting the given matrix to each of those 8 and return the minimum cost.
    The 3 * 3 solution:
    ---------
    8   1   6
    3   5   7
    4   9   2
    ---------
    '''

    magic_square = Magic_Square()

    min_cost = None
    for num_reflects in range(2):
        for num_rotates in range(4):
            cost = magic_square.find_cost(s, num_reflects, num_rotates)
            if min_cost is None or cost < min_cost:
                min_cost = cost

    return min_cost


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(f'{result}')