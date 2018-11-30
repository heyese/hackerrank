

# Given a list of prices
# Can pick a point to buy, then a subsequent point to sell
# Want the maximum profit

def max_profit_brute_force(values):
    max = 0
    for index, buy_point in enumerate(values):
        for sell_point in values[index+1:]:
            profit = buy_point - sell_point
            if profit > max:
                max = profit
    return max


def max_profit_track_min(values):
    """
    Keeps track of previous lowest price so can easily calculate profit
    associated with selling on any particular day
    """
    prev_min = values[0]
    max = 0
    for sell_point in values[1:]:
        profit = sell_point - prev_min
        if profit > max:
            max = profit
        if sell_point < prev_min:
            prev_min = sell_point
    return max


# opening_prices = [1, 5, 2, 6, 3, 6, 2, 1]
# print(max_profit_track_min(opening_prices))
# print(max_profit_track_min(opening_prices))

def num_bits_set_to_1(x):
    """
    Given an integer x, this function returns the number of bits set to 1 in its binary form
    :param integer:
    :return: integer
    """
    import collections
    bits = collections.Counter()
    # First find min n such that 2**n > x

    while True:
        n = 0
        while 2**n <= x:
            n += 1
        bits[n-1] = 1
        x -= 2**(n-1)
        if not x:
            break
    top_power = max(bits.keys())
    output = []
    for i in range(top_power, -1, -1):
        output.append('1') if i in bits else output.append('0')
    return ''.join(output)

def parity(x):
    """
    Given an integer, this function returns 1 if the number of 1s in the
    binary representation of x is odd and 0 if it is even
    """
    sum = 0
    while x:
        sum += x & 1
        x >>= 1
    return sum % 2




def fibModGen(t1, t2):
    curr, next = t1, t2
    while True:
        yield curr
        curr, next = next, curr + next**2

def fibonacciModified(t1, t2, n):
    """
    The sequence is defined with: t(i+2) = t(i) + t(i+1)**2
    :return:  the nth term is the sequence
    """
    for index, value in enumerate(fibModGen(t1, t2)):
        if index + 1 == n:
            return value

print(fibonacciModified(0, 1, 4))