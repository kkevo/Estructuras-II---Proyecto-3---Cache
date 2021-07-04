from operator import itemgetter

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
                    if (way2[index][2] != 0):
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
                    if (way2[index][2] != 0):
                        way2[index][2] -= 1
            
            # miss
            return 0

    lru_list = []

    for i in range(associativity):
        lru_list.append([i, cache[i][index][2]])
    
    lru_list.sort(key=itemgetter(1))

    cache[lru_list[0][0]][index][1] = tag
    # this is the last recently used
    if (cache[lru_list[0][0]][index][2] != associativity):
        cache[lru_list[0][0]][index][2] = associativity + 1
        for way2 in cache:
            if (way2[index][2] != 0):
                way2[index][2] -= 1     

    return 0
    # for i in range(len(lru_list)):
    #     try: 
    #         if (lru_list[i][1] < lru_list[i+1][1]):
    #             cache[lru_list[i][0]][index][1] = tag
    #             cache[lru_list[i][0]][index][2] = associativity
    #     except:
    #         cache[associativity-1][index][1] = tag
    #         cache[associativity-1][index][2] = associativity
    