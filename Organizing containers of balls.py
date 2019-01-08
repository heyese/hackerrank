import math
import os
import random
import re
import sys
import collections

def row_and_col_sums(size, matrix):
    """
    :return: dict sums[(x,y)]=sum of values on row x less element in column y
    """
    row_sums = collections.defaultdict(int)
    col_sums = collections.defaultdict(int)
    for x in range(size):
        for y in range(size):
            row_sums[x] += matrix[x][y]
            col_sums[y] += matrix[x][y]
    return row_sums, col_sums


# Complete the organizingContainers function below.
def organizingContainers(containers):
    # Looking at the matrix, see that a given ball colour can only be sorted
    # into a given container if the number of balls of that colour in
    # other containers (which is the sum of the other entries in that
    # column) is equal to the number of balls of other colours in that
    # container (which is the sum of the other entries in that row).
    # Thinking about it again, this use of the word 'other' is unnecessary -
    # if there are X balls of a particular type, and a container with X balls
    # in it, then you can definitely make swaps to put those X balls in that
    # container.  So, for a particular ball and container, if the sum of the
    # row equals the sum of the column, you can put that ball in that
    # container.  Otherwise, you can't.

    n = len(containers)  # This is number of ball typs and number of containers
    possible_ball_containers = collections.defaultdict(list)
    row_sums, col_sums = row_and_col_sums(n, containers)
    for ball in range(n):
        for container in range(n):
            if row_sums[ball] == col_sums[container]:
                possible_ball_containers[ball].append(container)

    print(f'row sums: {row_sums}')
    print(f'col sums: {col_sums}')
    print(possible_ball_containers)
    # Now I have something like this:
    # {0: [0, 1], 1: [0, 1], 2: [2]}
    #  ie. ball type 0 can be put in containers 0 and 1, as can ball type 1,
    # and ball type 2 can be put in container 2.
    # It is not enough that every ball can go into some container.
    # Consider:  | a |,  | b, c |,  |  |
    # Above, a, b and c can all go in the left container, but it's still
    # impossible.
    # Also, not enough to know that every container can hold a set of balls.
    # Consider:  | a, a |, | b, c|, | c, c |
    # Here, each container can hold the 'a's, but it's still impossible.
    # I think it is enough to know that every ball can go somewhere AND
    # every container can hold something.  This is because putting a ball type
    # into a container doesn't effect your ability to put a different ball
    # type into a different container, if you think about it.
    # Also, if ball types a and b can go into a given container, then you know
    # there are the same number of balls of type a and b (as swaps don't
    # affect the number of balls in a container).  Also, if ball type X
    # can go in multiple containers, you know those containers contain the
    # same number of balls.  Finally, you know there
    # are the same number of containers as there are balls.
    a = set()
    for i in possible_ball_containers:
        if not possible_ball_containers[i]:
            return 'Impossible'
        a = a.union(possible_ball_containers[i])
    if len(a) != n:
        return 'Impossible'
    return 'Possible'



if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        n = int(input())

        containers = []

        for _ in range(n):
            containers.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(containers)

        print(f'{result}')


# Looking at the editorial, a simple inuitive solutions is:
# Make a sorted list of the container sizes
# Make a sorted list of the number of each type of ball
# If those two lists are equal, it's possible, else not.