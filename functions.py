import time

def toBin(num, n):
    """ Returns binary number
    with n bits. """

    # Obtains binary number
    result = bin(num).replace("0b", "")

    # Adds zeros to the left if necessary
    if len(result) < n:
        return '0' * (n - len(result)) + result
    else:
        return result


def sendToCPU(block_size):
    CPU = []

    start = time.time()
    CPU.append(1)
    end = time.time()
    time_optimized = end-start

    start = time.time()
    for byte in range(block_size):
        CPU.append(byte)
    end = time.time()
    time_not_optimized = end-start

    return time_optimized, time_not_optimized


def lruPolicy(cache, index, tag, associativity, offset, block_size):
    ''' Implements LRU policy. Returns:
    - 1 for hit and 0 for miss
    - Time needed to send 1 byte to the CPU
    - Time needed to send whole block to the CPU'''
 
    for way in cache:
        # check if there's a hit
        if (way[index][0] == 1 and tag == way[index][1]):
            
            # this is the last recently used
            if (way[index][2] != associativity):
                current_LRU = way[index][2] 
                way[index][2] = associativity + 1                
                for way2 in cache:
                    if (way2[index][2] > current_LRU):
                        way2[index][2] -= 1            
            # hit
            return 1, 0, 0, 0

        # check if set is invalid
        if (way[index][0] == 0):
            
            way[index][0] = 1
            way[index][1] = tag
            
            # this is the last recently used
            if (way[index][2] != associativity):
                current_LRU = way[index][2] 
                way[index][2] = associativity + 1
                for way2 in cache:
                    if (way2[index][2] > current_LRU):
                        way2[index][2] -= 1            
            time_optimized, time_not_optimized = sendToCPU(block_size)
            # miss
            return 0, time_optimized, time_not_optimized, 0

    lru_list = []

    for i in range(associativity):
        lru_list.append(cache[i][index][2])
    
    # se obtiene el la posicion del menos usado
    lru = min(range(len(lru_list)), key=lru_list.__getitem__)
    
    current_LRU = cache[lru][index][2]
    # update tag
    cache[lru][index][1] = tag
    # this is the last recently used
    cache[lru][index][2] = associativity + 1
    for way2 in cache:
        if (way2[index][2] > current_LRU):
            way2[index][2] -= 1     

    time_optimized, time_not_optimized = sendToCPU(block_size)
    return 0, time_optimized, time_not_optimized, 1