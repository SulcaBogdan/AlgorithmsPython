def calculSalariu(timp):
    bani_terapie_per_ora = 30
    bani_shadow_per_ora = 50
    if timp == "zi":
        q1 = int(input("Cate ore de shadow ai facut?"))
        q2 = int(input("Cate ore de terapie ai facut?"))
        return ((q2*bani_terapie_per_ora) + (q1*bani_shadow_per_ora))
    elif timp =="zile":
        zile = int(input("cate zile vrei sa calculezi?"))
        if zile == 2:
            q1 = int(input("Cate ore de shadow ai facut?"))
            q2 = int(input("Cate ore de terapie ai facut?"))
            return ((q1*bani_shadow_per_ora) + (q2*bani_terapie_per_ora))
        elif zile == 3:
            q1 = int(input("Cate ore de shadow ai facut?"))
            q2 = int(input("Cate ore de terapie ai facut?"))
            return ((q1 * bani_shadow_per_ora) + (q2 * bani_terapie_per_ora))
        elif zile == 4:
            q1 = int(input("Cate ore de shadow ai facut?"))
            q2 = int(input("Cate ore de terapie ai facut?"))
            return ((q1 * bani_shadow_per_ora) + (q2 * bani_terapie_per_ora))

    elif timp == "saptamana":
        q1 = int(input("Cate ore de shadow ai facut?"))
        q2 = int(input("Cate ore de terapie ai facut?"))
        return (((q1 * bani_shadow_per_ora) + (q2 * bani_terapie_per_ora)))
    elif timp == "saptamani":
        saptamani = int(input("Cate saptamani vrei sa calculezi?"))
        if saptamani == 2:
            q1 = int(input("Cate ore de shadow ai facut?"))
            q2 = int(input("Cate ore de terapie ai facut?"))
            return ((q1*bani_shadow_per_ora) + (q2*bani_terapie_per_ora))
        elif saptamani == 3:
            q1 = int(input("Cate ore de shadow ai facut?"))
            q2 = int(input("Cate ore de terapie ai facut?"))
            return ((q1 * bani_shadow_per_ora) + (q2 * bani_terapie_per_ora))
    elif timp == "luna":
        q1 = int(input("Cate ore de shadow ai facut?"))
        q2 = int(input("Cate ore de terapie ai facut?"))
        return ((q1 * bani_shadow_per_ora) + (q2 * bani_terapie_per_ora))














def shuffle(nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list


print(shuffle([2,5,1,3,4,7], 3))



















