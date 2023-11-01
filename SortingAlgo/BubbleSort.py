from typing import List

ex_list = [4,3,2,1,6,8,9,12,24,13,14,44,33,22,11,22,33,44,55]

#Bubble sort
def bubble_sort(lista:List[int])->List[int]:
    swapped = True
    count = 0
    while swapped:
        swapped = False
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                swapped = True
                count += 1
    print(f"Your bubble sort algo has done {count} operations")
    return  lista

print(bubble_sort(ex_list))




