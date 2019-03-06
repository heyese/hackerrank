
import collections
import math

def primes():

    yield 2
    primes = [2]
    num = 3
    while True:
        num_prime = True
        for p in primes:
            if p > math.sqrt(num):
                break
            if not num % p:
                num_prime = False
        if num_prime:
            primes.append(num)
            yield num
        num += 2


def waiter(numbers, q):
    prime_gen = primes()
    plate_stacks = collections.defaultdict(list)
    current_plates = collections.deque(numbers)
    next_plates = collections.deque()

    for i in range(q):
        p = next(prime_gen)
        next_plates.clear()
        while True:
            try:
                plate = current_plates.pop()
            except IndexError:
                break

            if plate % p:
                next_plates.append(plate)
            else:
                plate_stacks[i].append(plate)

        current_plates = next_plates.copy()

    results = []
    for i in range(q):
        results += reversed(plate_stacks[i])
    results += reversed(next_plates)
    return results




if __name__ == '__main__':

    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    number = list(map(int, input().rstrip().split()))
    result = waiter(number, q)

    print('\n'.join(map(str, result)))
