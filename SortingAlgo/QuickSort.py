def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([4,5,6,22,3,4,1,22,5,7,0,9,9,8]))


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dict_1 = {}
    dict_2 = {}
    for i in s:
        if i in dict_1:
            dict_1[i] +=1
        else:
            dict_1[i] = 1
    for j in t:
        if j in dict_2:
            dict_2[j] += 1
        else:
            dict_2[j] = 1

    print(dict_1,dict_2)
    if dict_1 == dict_2:
        return True
    return False


print(isAnagram("anagram","nagaram"))