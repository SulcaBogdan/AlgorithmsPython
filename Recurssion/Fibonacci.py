
#Remembering the result of fibonacci function and storing it into a dictionary to boost the speed and time.
cache = {}
def fibonacci(num):
    global cache
    if num in cache:
        return cache[num]
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        result = fibonacci(num-1) + fibonacci(num-2)
        cache[num] = result
        return result

#Am creat un dictionar gol unde vom insera perechile de chei si valori a numerelor n fibonacci
#Dupa ce este apelata functia fibonacci(n) si n se afla ca si cheie in dictionarul cache atunci se va returna imediat valoarea acesteia
#Asadar se scoate un timp constant de O(1)


