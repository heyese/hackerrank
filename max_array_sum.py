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
        if i > 0:
            if index + 2 < len(arr):
                for j in non_adj_sub_arrays_recursion(arr[index + 2:]):
                    if sum(j) > 0:
                        yield [i] + j
            yield [i]
    yield []


def maxSubsetSumRecursion(arr):
    max_sum = None
    for a in non_adj_sub_arrays_recursion(arr):
        if len(a) > 0:
            if max_sum is None or sum(a) > max_sum:
                max_sum = sum(a)
    if max_sum:
        return max_sum
    else:
        return max(arr)




print(maxSubsetSumRecursion([3, 5, -7, 8, 10]))
import random
x = [random.randint(-10, 10) for i in range(1000)]
print(maxSubsetSumRecursion(x))