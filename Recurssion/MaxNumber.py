def maxNumber(arr):
    if not arr:
        return 0
    return max(arr[0], maxNumber(arr[1:]))


print(maxNumber([1,4,65,3,4,5,32]))