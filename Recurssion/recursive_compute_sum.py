def recursive_compute_sum(lista):
    if len(lista) == 0:
        return 0
    else:
        first = lista[0]
        rest = lista[1:]
        suma = first + recursive_compute_sum(rest)
        return suma


print(recursive_compute_sum([1,2,3,4,5]))