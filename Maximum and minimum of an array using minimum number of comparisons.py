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
