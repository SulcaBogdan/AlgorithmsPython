
def binary_search(list , item):
    low = 0
    high = len(my_list)-1
    count = 0
    while low <= high:
        mid = int((low + high) / 2)
        if item == list[mid]:
            print(f"Number of searchings -> {count}" )
            return f"Element found at index {mid}"
        elif item > list[mid]:
            low = mid + 1
            count+=1
        else:
            high = mid - 1
            count += 1
    return None


my_list = [i for i in range(100)]
print(my_list)
print(binary_search(my_list, 2))



