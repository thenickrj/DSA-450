# Maximum and minimum of an array using minimum number of comparisons


# Method 1 (Simple Linear search)
"""
Initialize values of min and max as minimum and maximum of the first two elements respectively.
Starting from 3rd, compare each element with max and min, and change max and min accordingly
(i.e., if the element is smaller than min then change min,
else if the element is greater than max then change max, else ignore the element)
"""


class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> pair:
    minMax = pair()
    if n == 1:
        minMax.min = arr[0]
        minMax.max = arr[0]

    if arr[1] > arr[0]:
        minMax.min = arr[0]
        minMax.max = arr[1]
    else:
        minMax.max = arr[0]
        minMax.min = arr[1]

    for i in range(2, n):
        if arr[i] > minMax.max:
            minMax.max = arr[i]
        elif arr[i] < minMax.min:
            minMax.min = arr[i]
    return minMax


if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    minMax = getMinMax(arr, len(arr))
    print("The minimum value is", minMax.min)
    print("The maximum value is", minMax.max)

#  Time Complexity: O(n)



# METHOD 2 (Tournament Method)
"""
Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return
"""


def getMinMax(low, high, arr):
    arr_min = arr[low]
    arr_max = arr[high]

    # if there is one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[high]
        return (arr_min, arr_max)

    # if there is two element
    if low + 1 == high:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_min = arr[low]
            arr_max = arr[high]
        return (arr_min, arr_max)

    else:
        mid = int((low + high) / 2)
        arr_min1, arr_max1 = getMinMax(low, mid, arr)
        arr_min2, arr_max2 = getMinMax(mid + 1, high, arr)
    return (min(arr_min1, arr_min2), max(arr_max1, arr_max2))


arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_min, arr_max = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)

# Time Complexity: O(n)


