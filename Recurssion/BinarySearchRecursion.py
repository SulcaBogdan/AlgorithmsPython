def binary_search_recursion(lista, low, high, item):
    mid = int(low + (high - low) / 2)
    if item == lista[mid]:
        return mid
    elif item > lista[mid]:
        return binary_search_recursion(lista, mid+1, high, item)
    elif item < lista[mid]:
        return binary_search_recursion(lista, low, mid-1, item)
    return None


lista = [1,2,3,4,5,6,7,8,9,10]
print(binary_search_recursion(lista, 0, len(lista)-1, 9))


