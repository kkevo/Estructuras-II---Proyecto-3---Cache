def lruPolicy(cache, index, tag, associativity):
    ''' Implements LRU policy. Returns 1 for hit
    and 0 for miss. '''

    for way in cache:
        # check if there's a hit
        if (way[index][0] == 1 and tag == way[index][1]):
            
            # this is the last recently used
            if (way[index][2] != associativity):
                way[index][2] = associativity + 1
                for way2 in cache:
                    if (way2[index][2] > 1):
                        way2[index][2] -= 1
            # hit
            return 1    

        # check if set is invalid
        if (way[index][0] == 0):
            
            way[index][0] = 1
            way[index][1] = tag
            
            # this is the last recently used
            if (way[index][2] != associativity):
                way[index][2] = associativity + 1
                for way2 in cache:
                    if (way2[index][2] > 1):
                        way2[index][2] -= 1
            
            # miss
            return 0

    lru_list = []

    for i in range(associativity):
        lru_list.append(cache[i][index][2])
    
    # se obtiene el la posicion del menos usado
    lru = min(range(len(lru_list)), key=lru_list.__getitem__)

    # update tag
    cache[lru][index][1] = tag
    # this is the last recently used
    cache[lru][index][2] = associativity + 1
    for way2 in cache:
        if (way2[index][2] > 1):
            way2[index][2] -= 1     

    return 0
    