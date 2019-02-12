

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):

    times_round = 0
    tracker = dict()
    while True:
        for i, (p, d) in enumerate(petrolpumps):
            if i in tracker:
                # We've gone all the way round the petrol pumps!
                return i
            for j in range(i):
                if j in tracker:
                    tracker[j] += p-d
                    if tracker[j] < 0:
                        # Run out of petrol
                        del(tracker[j])
            if p-d >= 0:
                tracker[i] = p-d
        times_round += 1
        if times_round == 2:
            # It doesn't appear to be possible
            return 'Not possible'

if __name__ == '__main__':

    n = int(input())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    result = truckTour(petrolpumps)
    print(f'{result}')
