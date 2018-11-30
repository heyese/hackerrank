# https://www.hackerrank.com/challenges/coin-change/problem

def getWaysNow(n, c, cache={}):
    """
    The coin change problem.  For n some int, and ordered c, a tuple of different coin sizes,
    how many distinct ways (ordering of the coins doesn't matter) can I give change equal to n.
    eg. n = 5 and c = [1, 5], the answer is 2.  ie. {1,1,1,1,1} and {5}
    cache is a dict with saved solutions.
    :return: int
    """
    sum = 0
    if n == 0:
        return 1

    if len(c) == 1:
        if n % c[0] == 0:
            return 1
        else:
            return 0

    for i in range(0, n + 1, c[-1]):
        # num = number of largest coin used
        if (n - i, c[:-1]) not in cache:
            cache[(n - i, c[:-1])] = getWaysNow(n - i, c[:-1])
        sum += cache[(n - i, c[:-1])]
    return sum

def getWays(n, c):

    c.sort()
    c = tuple(c)
    return getWaysNow(n, c)



print(getWays(10, [2, 5, 3, 6]))