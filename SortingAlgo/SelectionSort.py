#Functie de gasire a celui mai mic element dintr o lista O(n x n)
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


#Algoritmul de sortare prin selectare. Acesta foloseste functia de mai sus pentru a pune in ordine elementele cele mai mici.
#Folosim functia pop() pentru a sterge din array elementul mic si sa l returneze ca parametru in functia append().
#Astfel cand functia findSmallest este apelata dinou cel mai mic element va fi diferit deoarece s a sters din array celalalt element.
#Timp de O(n**2)
def selectionSort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array

#Exemplu de utilizare a selectionSort
arr = [1,5,7,4,3,2,12,44,55,77]

print(findSmallest(arr))
print(selectionSort(arr))