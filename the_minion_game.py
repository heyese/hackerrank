# https://www.hackerrank.com/challenges/the-minion-game/problem
import collections


def minion_game(string):
    counter_kevin = collections.Counter()
    counter_stuart = collections.Counter()
    vowels = set({'A', 'E', 'I', 'O', 'U'})

    for i in range(len(string)):
        counter = counter_kevin if string[i] in vowels else counter_stuart
        for j in range(i + 1, len(string) + 1):
            counter[string[i:j]] += 1

    stuart = sum(counter_stuart.values())
    kevin = sum(counter_kevin.values())

    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin {}'.format(kevin))
    else:
        print('Stuart {}'.format(stuart))


i = minion_game('BANANA')
print(i)
