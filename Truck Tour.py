

#
# Complete the truckTour function below.

# This works, but it's too slow
def truckTourSlow(petrolpumps):

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

def truckTour(petrolpumps):
    # Imagine plotting values of p-d.
    # Now imagine tracing through the line with two points - at any one time, only one of the points is advancing.
    # The behind point represents the pump you're currently considering starting at.
    # The ahead point is how far you get before you run out of fuel.
    # When you run out of fuel (ie. p-d at ahead is lower than p-d behind), you advance to the next petrol pump
    # where this isn't the case.
    times_round = 0
    journey = []
    start = True
    while True:
        for i, (p, d) in enumerate(petrolpumps):
            if start:
                journey.append(p-d)
                start = False
            else:
                journey.append(journey[-1] + p - d)
        times_round += 1
        num_pumps = i
        if times_round == 2:
            break
    print(journey)

    behind_index, ahead_index = 0, 0
    while ahead_index - behind_index < num_pumps:
        if journey[ahead_index] < journey[behind_index]:
            # Can't get all the way round starting from pump[behind_index]
            behind_index += 1
            continue
        ahead_index += 1
    print(behind_index)



if __name__ == '__main__':

    n = int(input())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    result = truckTour(petrolpumps)
    print(f'{result}')
