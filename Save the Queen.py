# https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen


def solve(n, times):
    #  The key point here is that you can move defenders between attackers at will.
    #  This means that if you have a group of defenders, all with the same fight time,
    #  you can swap them in and out against a smaller group of attackers so that each
    #  defender's fight time is exhausted at the same moment.
    #  ie.  With k defenders, each with the same fight time x,
    #  and a (<= k) attackers, you make the most use of their fight time by
    #  swapping them in and out.  In this case, we could keep the attackers
    #  occupied for (kx)/a seconds.

    #  It is more complicated.  Imagine 2 attackers, 3 defenders, with fight times 10, 10 and 5.
    #  The two 10 defenders can obviously keep the attackers busy for the first 10 seconds, but if they do
    #  that, we won't be able to use the 5.  The best method is to have them defend for 5 seconds
    #  each.  Then we have a group of three equal 5 second defenders which can fend off the attack
    #  for another 3 * 5 / 2 = 7.5 seconds.

    #  Now imagine the same scenario but with fight times of 10, 8 and 8.
    #  Similarly, we want to use the 8s so that we end up with three defenders with equal fight times.
    #  The equation to solve is 10 -t = 8 - t/2  -> t = 4.
    #  So after 4 seconds, we have 6, 6, 6, which gives us another 3 * 6 / 2 = 9 seconds.

    #  This example gives rise to the general tactic.
    #  1)  Order your defenders into a list by decreasing fight time
    #  2)  Pit the first n against the attackers.
    #  3)  Say the nth defender has fight time k.  We know how many attackers are occupied with
    #      k-second defenders, and how many k-second defenders there are in total.
    #      As per the two examples above, we work out how many seconds it will take before
    #      the set of k-second defenders have:
    #         a)  the same time left as the defenders immediately prior to them in the list
    #         b)  the same time left as the defenders immediately after them in the list
    #  4)  Pick t, the smaller of the two.  Add t to the total defense time.  Adjust the
    #      fight time list accordingly.  If the last element is zero (zero fight time left), that
    #      indicates there are now fewer defenders (with >0 fight time) than attackers, so return.
    #  5)  Repeat ...


    times.sort(reverse=True)
    queen_time = 0
    while times[-1] != 0:

        prev_val, val, next_val = None, times[n-1], 0
        # So 'val' is the fight time of our nth defender
        # In comments, I've confusingly referred to this fight time as k from now on!
        # So our k-second defenders start at this index:
        start_index = times.index(times[n-1])
        # And the next lot of defenders (with a lower fight time) start at this index:
        start_next_index = start_index + times.count(times[n-1])
        # If these k-defenders aren't the first in the list, there is a group of
        # defenders immediately before them with a greater fight time (called prev_val)
        if start_index > 0:
            prev_val = times[start_index - 1]
        # If these k-defenders aren't the last in the list, there is a group
        # immediately after them with a smaller fight time (called next_val)
        if start_next_index != len(times):
            next_val = times[start_next_index]
        # We have this many k-second defenders:
        total_k_defenders = start_next_index - start_index
        # ... and this many of them are facing off against attackers at any one time:
        active_k_defenders = n - start_index

        # Time to match next_val (or to use up remaining time if next_val == 0)
        #  This is from:
        #  prev_val - t = val - (total_k_defenders / active_k_defenders) * t
        t_next = (val - next_val)* total_k_defenders / active_k_defenders
        # Time to match prev_val:
        if prev_val:
            if total_k_defenders == active_k_defenders:
                # prev_val decreases at same pace as val, so they'll never match
                t_prev = val
            else:
                t_prev = (prev_val - val) * total_k_defenders / (total_k_defenders - active_k_defenders)
        else:
            t_prev = None

        # Now pick the smaller value of t_prev and t_next
        # (ie. have the active_defenders fight time been drained to match
        # the defenders in front of them in the list or behind them)
        t_min = min({t_prev, t_next} - {None})
        # Take t_min off all elements up to the k_defenders
        for i in range(start_index):
            times[i] = times[i] - t_min

        # Now we have to reduce the k_defenders fight time a bit, but this is where the point about accuracy
        # comes in.  k_defenders fight time should at this point match their prior or post defenders, but due to the
        # division in calculating t_prev and t_next, may be fractionally out.  So I'm going to just set them
        # as equal to avoid that problem.
        for i in range(start_index, start_next_index):
            if t_min == t_next: # check equality with t_next first, as we could have t_next == t_prev
                times[i] = 0 if start_next_index == len(times) else times[start_next_index]
            else:
                times[i] = times[start_index - 1]

        queen_time += t_min

    print(queen_time)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    solve(n, a)

# 11.0