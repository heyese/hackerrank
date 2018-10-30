# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import datetime


def min_bribes(n):
    num_moves = 0
    for i in range(len(n), 0, -1):
        found = False
        for j in range(1, 4):
            if i == n[i-j]:
                found = True
                num_moves += j - 1
                n.pop(i-j)
                break
        if found is False:
            return 'Too chaotic'
    return num_moves

def min_bribes_slow(n):
    num_moves = 0
    #debug = []
    for i in range(len(n), 0, -1):
        index = n.index(i)
        # We want index + 1 = i
        if index + 1 < i - 2:
            return 'Too chaotic'
        num_moves += i - index - 1
        n.pop(index)
        #debug.insert(0, i)
        #print('Old list: {}'.format(n))
        #print('new list: {}'.format(debug))
    return num_moves




n = [2, 1, 5, 3, 4]
i = datetime.datetime.now()
print(min_bribes_slow(n))
print(datetime.datetime.now() - i)
n = [2, 1, 5, 3, 4]
i = datetime.datetime.now()
print(min_bribes(n))
print(datetime.datetime.now() - i)
