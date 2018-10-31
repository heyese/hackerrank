# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interviw&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections  import Counter
def freqQuery(queries):
    """

    :param queries: list of lists of length 2
    :return:
    """
    output = []
    count = Counter()
    freq = Counter()
    for operation, num in queries:
        if operation == 1:
            freq[count[num]] = max(0, freq[count[num]] - 1)
            count[num] += 1
            freq[count[num]] += 1
        elif operation == 2:
            if count[num] > 0:
                freq[count[num]] = freq[count[num]] - 1
                count[num] = count[num] - 1
                freq[count[num]] += 1
        else:
            # Is any integer in count exactly num times?
            # Needed to use second dict here, as running through count.values() was too slow
            # Got caught out, as I initially said 'if num in freq', which caught every value
            # that had been initialised, even if freq[num] = 0!
            # ie. to begin with, x in freq is False
            # then freq[x] = 1 -> x in freq is True
            # then freq[x] = 0 -> x in freq is STILL TRUE

            if freq[num] > 0:
                output.append(1)
            else:
                output.append(0)
    return output

i = '''
3 5
3 3
1 10000004
1 10000016
1 10000011
3 10
1 10000006
3 5
2 4
2 3
2 6
1 10000037
3 10
3 3
1 10000013
1 10000013
3 10
3 10
1 10000025
1 10000021
2 7
1 10000002
3 7
3 9
2 9
2 8
3 4
3 4
1 10000025
3 6
1 10000037
2 9
2 8
1 10000042
2 7
2 10
1 10000002
2 2
2 4
2 5
1 10000005
1 10000021
1 10000031
3 4
1 10000013
1 10000045
3 8
3 2
3 4
1 10000024
3 5
2 2
2 5
3 3
2 1
3 6
1 10000021
2 4
3 1
3 5
1 10000049
1 10000010
1 10000036
2 8
1 10000001
3 2
1 10000017
1 10000002
1 10000003
3 2
1 10000048
1 10000009
3 3
1 10000031
1 10000044
3 7
1 10000025
1 10000041
1 10000031
1 10000049
2 6
1 10000015
3 2
3 1
2 9
2 2
3 8
2 9
1 10000018
3 8
2 6
2 6
1 10000027
2 1
3 6
1 10000030
1 10000044
1 10000014
3 3
2 8
3 6
1 10000031
3 7
1 10000050
1 10000011
1 10000002
1 10000016
2 5
2 3
1 10000048
3 5
3 10
2 4
3 7
3 10
1 10000013
1 10000040
3 9
3 1
1 10000007
2 7
2 8
3 5
3 5
1 10000048
1 10000020
1 10000026
3 3
1 10000033
1 10000009
1 10000041
2 10
1 10000039
2 7
2 1
2 9
2 10
2 9
1 10000035
1 10000042
1 10000046
3 10
1 10000004
3 10
2 8
3 5
3 2
3 7
3 4
2 4
2 4
2 2
3 2
1 10000040
2 8
1 10000001
1 10000009
3 4
1 10000044
3 3
3 2
2 4
1 10000025
1 10000040
3 2
3 5
2 10
3 1
1 10000003
2 4
3 5
2 9
2 5
1 10000028
1 10000010
1 10000012
1 10000034
3 1
3 1
3 7
2 4
2 6
3 8
2 7
3 5
1 10000026
3 8
1 10000035
3 9
3 3
3 7
3 2
2 8
1 10000001
3 3
2 1
3 8
2 2
2 1
2 2
1 10000027
3 7
3 10
2 2
1 10000036
1 10000021
3 5
1 10000020
1 10000001
3 7
2 8
3 7
1 10000042
1 10000016
2 3
1 10000018
2 3
2 2
2 2
2 3
3 4
2 9
1 10000034
2 1
3 1
1 10000046
3 1
3 10
2 9
3 4
1 10000002
3 5
2 2
2 3
1 10000048
2 10
3 4
1 10000035
3 9
3 4
1 10000041
1 10000016
3 2
2 5
2 3
2 5
1 10000002
3 5
1 10000008
3 4
2 9
3 2
1 10000034
3 2
1 10000014
1 10000016
1 10000019
2 5
1 10000006
2 9
1 10000020
2 7
2 4
3 1
3 1
1 10000043
1 10000012
2 4
1 10000027
3 10
3 10
2 10
2 8
2 1
1 10000004
3 2
1 10000007
1 10000007
1 10000049
1 10000015
3 10
3 7
1 10000018
2 5
3 1
2 1
2 1
3 1
1 10000007
3 8
3 10
2 8
2 6
2 3
1 10000001
2 6
2 7
2 2
2 10
2 6
3 2
1 10000041
1 10000035
2 1
3 1
2 10
2 4
3 10
2 6
3 2
3 4
3 6
3 9
1 10000041
1 10000002
3 1
1 10000023
3 2
3 1
1 10000030
3 9
2 10
1 10000007
2 6
1 10000014
1 10000007
1 10000002
2 1
1 10000019
2 3
2 6
1 10000002
2 3
2 10
2 4
1 10000043
1 10000041
3 7
1 10000002
1 10000036
3 9
1 10000027
3 3
3 9
2 9
1 10000045
2 9
2 2
3 8
1 10000049
3 3
3 7
1 10000019
3 9
2 4
2 4
1 10000038
3 5
1 10000034
2 8
1 10000047
2 9
2 1
1 10000039
2 10
3 4
2 4
2 10
1 10000002
3 7
3 8
1 10000012
3 6
3 10
3 10
1 10000034
3 6
1 10000030
3 7
1 10000024
2 1
3 9
1 10000012
2 1
3 10
3 5
1 10000034
1 10000017
2 10
2 8
3 6
3 8
3 8
1 10000036
3 7
2 10
2 1
2 2
2 1
2 4
1 10000010
1 10000038
2 6
1 10000025
1 10000010
2 7
1 10000011
1 10000025
3 9
1 10000037
1 10000048
1 10000049
1 10000038
2 9
1 10000049
3 7
2 4
1 10000032
1 10000035
3 5
2 1
3 10
2 2
3 1
1 10000047
3 10
2 2
2 9
1 10000023
3 2
1 10000042
2 3
2 2
2 9
2 9
2 3
3 8
3 1
3 7
2 6
1 10000010
2 7
1 10000034
1 10000047
1 10000037
2 4
2 5
2 2
2 5
3 9
2 6
2 8
3 10
3 8
2 10
3 8
3 9
3 1
3 8
3 2
1 10000034
3 9
1 10000036
2 7
3 10
3 6
1 10000031
3 7
3 7
3 10
3 2
3 6
1 10000036
1 10000037
1 10000024
1 10000024
2 10
3 8
3 6
1 10000036
2 8
1 10000043
3 5
2 7
1 10000020
1 10000044
3 6
3 1
2 6
2 3
1 10000002
2 2
2 3
2 9
3 8
1 10000002
2 4
1 10000019
2 10
1 10000050
3 8
1 10000021
1 10000027
2 5
1 10000009
2 2
3 8
3 8
2 9
3 5
3 4
1 10000028
3 8
3 8
1 10000026
1 10000029
3 4
3 1
2 9
2 9
2 3
3 2
3 10
3 6
1 10000020
3 10
2 9
3 4
3 10
3 9
1 10000005
1 10000037
1 10000011
1 10000034
3 3
1 10000020
1 10000035
2 10
1 10000049
3 6
2 5
3 2
1 10000003
3 2
2 2
1 10000029
3 10
3 5
3 1
2 1
1 10000035
1 10000024
1 10000002
2 7
2 1
3 2
1 10000026
3 9
2 7
2 5
2 9
1 10000033
2 3
2 10
1 10000016
1 10000025
3 1
2 3
3 6
3 9
1 10000030
3 10
3 3
2 4
2 3
2 4
3 2
1 10000025
2 10
1 10000023
1 10000045
3 4
2 8
1 10000046
1 10000042
3 8
1 10000019
3 7
2 8
1 10000047
1 10000003
1 10000049
1 10000030
3 5
3 8
2 7
1 10000049
3 10
1 10000001
1 10000017
2 8
2 10
3 8
3 10
3 4
1 10000021
1 10000035
1 10000027
3 7
3 4
1 10000001
3 1
3 10
2 8
1 10000038
1 10000001
3 7
2 9
1 10000020
1 10000037
3 5
2 2
3 5
3 6
1 10000049
2 4
1 10000033
2 7
2 5
2 5
2 5
1 10000002
1 10000015
2 3
3 4
1 10000030
3 3
1 10000048
1 10000006
2 9
3 4
1 10000007
2 1
3 3
1 10000006
3 8
1 10000015
3 5
2 6
2 4
1 10000033
1 10000013
3 8
3 9
1 10000048
3 6
2 2
1 10000032
1 10000004
1 10000048
3 7
3 9
1 10000049
3 1
1 10000021
1 10000012
3 2
2 5
1 10000012
2 7
3 3
2 5
3 5
2 5
2 9
1 10000033
2 2
3 3
3 9
1 10000030
1 10000029
2 1
1 10000044
3 6
1 10000029
1 10000041
3 3
3 2
2 5
1 10000046
1 10000039
2 1
3 6
2 9
2 3
2 6
3 3
3 4
3 10
1 10000014
1 10000002
3 4
2 8
3 7
2 8
1 10000006
1 10000011
3 2
3 10
1 10000039
3 3
3 8
3 9
1 10000018
3 5
1 10000029
2 8
3 9
1 10000020
1 10000034
3 7
3 10
3 4
1 10000022
1 10000048
2 8
3 10
3 10
1 10000031
3 1
3 3
1 10000035
2 5
3 2
1 10000011
1 10000004
3 9
2 3
1 10000047
1 10000049
1 10000011
1 10000021
1 10000028
3 1
2 8
1 10000045
1 10000039
1 10000048
1 10000003
2 10
2 1
2 1
1 10000019
1 10000007
2 3
2 8
2 4
2 2
2 8
3 7
1 10000032
2 2
3 1
2 8
1 10000024
2 3
3 4
2 4
3 5
2 2
3 4
3 7
2 3
3 2
3 7
1 10000032
1 10000048
1 10000017
1 10000031
2 2
3 6
3 4
3 3
1 10000044
1 10000022
2 5
2 1
3 7
3 8
1 10000030
3 3
1 10000021
3 2
3 5
2 1
1 10000037
1 10000019
3 4
2 2
2 5
1 10000037
1 10000036
2 1
3 1
2 9
2 9
3 3
2 6
3 5
2 5
1 10000039
2 10
2 10
3 1
3 5
3 1
2 7
2 8
3 8
1 10000036
3 9
3 2
2 7
2 2
3 7
2 7
3 10
2 7
1 10000012
2 2
3 2
2 8
3 7
2 2
2 9
2 7
1 10000013
2 3
1 10000024
1 10000047
1 10000039
2 2
3 9
3 9
2 3
2 5
2 9
1 10000011
2 4
2 8
3 7
1 10000035
1 10000010
1 10000005
3 6
1 10000018
2 3
2 6
2 6
3 4
1 10000009
2 7
1 10000013
2 7
3 1
2 3
3 3
1 10000003
1 10000037
1 10000016
1 10000001
1 10000026
3 7
1 10000011
1 10000024
2 1
3 8
3 4
2 2
1 10000011
1 10000042
1 10000048
2 5
3 3
3 2
1 10000043
1 10000022
1 10000004
1 10000038
3 7
1 10000019
1 10000046
1 10000014
2 3
2 2
1 10000006
2 6
3 6
3 8
2 2
3 1
3 10
3 9
2 9
1 10000021
1 10000014
1 10000030
2 8
1 10000018
3 1
3 10
2 1
1 10000030
3 7
1 10000015
3 1
1 10000049
2 6
2 6
1 10000038
1 10000004
3 6
3 5
2 9
1 10000038
1 10000038
3 4
3 5
1 10000033
2 3
1 10000029
1 10000043
2 3
2 7
3 1
1 10000015
3 1
1 10000012
3 4
1 10000050
1 10000042
2 5
2 10
1 10000021
1 10000031
1 10000026
2 3
2 1
2 1
1 10000040
3 8
3 6
1 10000045
2 4
1 10000035
2 3
1 10000041
1 10000010
2 9
1 10000023
2 5
3 7
1 10000017
2 7
1 10000044
2 10
3 3
1 10000026
3 1
2 6
1 10000025
3 5
3 2
3 6
1 10000027
2 3
3 1
2 10
1 10000005
2 3
3 1
3 5
1 10000038
3 6
2 8
3 4
2 10
2 9
3 4
3 8
2 3
3 8
2 5
1 10000010
1 10000016
1 10000020
3 1
1 10000020
2 5
2 1'''
q = [list(map(int, j.split())) for j in i.strip().split('\n')]
#q = [(a,b) for (a,b) in q if b == 2]
output = freqQuery(q)
#output2 = other(q)
print(output)