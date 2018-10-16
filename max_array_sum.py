'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.
'''


def non_adj_sub_arrays_recursion(arr):
    """
    Given an array, this yields all the possible sub-arrays
    of non-adjacent elements
    :param arr:
    :return yields a sub-array:
    """

    for index, i in enumerate(arr):
        if index + 2 < len(arr):
            for j in non_adj_sub_arrays(arr[index + 2:]):
                yield [i] + j
        else:
            yield [i]
    yield []


def maxSubsetSumRecursion(arr):
    max_sum = None
    for a in non_adj_sub_arrays(arr):
        if len(a) > 0:
            if max_sum is None or sum(a) > max_sum:
                max_sum = sum(a)
    return max_sum


print(maxSubsetSum([8, -1, -1]))
