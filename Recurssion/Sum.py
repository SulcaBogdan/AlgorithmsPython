def suma(arr):
    total = 0
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        total += arr[0]
        return total
    else:
        return arr[0] + suma(arr[1:])



print(suma([1,55,44]))