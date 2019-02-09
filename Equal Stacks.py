import os
import sys
import collections as c


#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    poss_heights = []
    for h in h1, h2, h3:
        full_height = sum(h)
        heights = c.deque([full_height])
        for cyl in h:
            heights.append(heights[-1] - cyl)
        poss_heights.append(heights)

    height_matches = 0
    last_popped = 0
    while True:
        height = -1
        for h in poss_heights:
            if not h:
                continue
            if h[0] > height:
                height = h[0]
                stack_to_pop = h
        popped = stack_to_pop.popleft()
        if popped == last_popped:
            height_matches += 1
        else:
            height_matches = 0
        last_popped = popped
        if height_matches == 2:
            return popped


if __name__ == '__main__':

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(f'{result}')