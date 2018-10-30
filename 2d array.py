#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def hour_glass_sum(x,y, arr):
    """
    arr is a list of lists.
    0,0 is top left element in arr
    (x,y) -> x is the column, y is the row.
    (3,2) is 4th element in 3rd row
    (x,y) is used to identify the top left point of the hourglass.
    :return: sum of the 'hourglass', as defined in the question,
    or None if an hourglass doesn't exist at point (x,y)
    """
    sum = 0
    for i in range(3):
        for j in range(3):
            if x + i < len(arr[y]) and y + j < len(arr):
                if not (j == 1 and i in {0, 2}):
                    sum += arr[y+j][x+i]
            else:
                return None
    return sum

def max_hour_glass_sum(arr):
    max_sum = None
    for x in range(len(arr[0])-2):
        for y in range(len(arr)-2):
            max_sum = hour_glass_sum(x, y, arr) if max_sum is None else max(max_sum, hour_glass_sum(x, y, arr))
    return max_sum






arr = []
arr.append([1,2,3,4,5])
arr.append([1,2,3,4,5])
arr.append([1,2,3,4,5])
arr.append([1,2,3,4,5])
print(max_hour_glass_sum(arr))

