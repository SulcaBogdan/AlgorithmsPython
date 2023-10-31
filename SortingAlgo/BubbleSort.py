from typing import List

ex_list = [4,3,2,1,6,8,9,12,24,13,14]

#Bubble sort
def bubble_sort(lista:List[int])->List[int]:
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                swapped = True
    return  lista


print(bubble_sort(ex_list))




