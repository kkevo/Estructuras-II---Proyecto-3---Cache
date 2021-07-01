def toBin(num, n):
    """ Devuelve un numero binario
    con n cantidad de bits. """

    # Obtains binary number
    result = bin(num).replace("0b", "")

    # Adds zeros to the left if necessary
    if len(result) < n:
        return '0' * (n - len(result)) + result
    else:
        return result


def lruPolicy(tag, associativity, cache):
    ##########################
    # Is the idx necessary?? #
    ##########################
    for cache_pos in range(associativity):
        # Set structure: valid, tag, LRU value, data
        # check if the entry has data
        if cache[cache_pos][0]:
            # if the tags match it's a hit
            if cache[cache_pos][1] == tag:
                # update the LRU values to comply with the replacement policy
                for i in range(associativity):
                    if cache[i][2] > cache[cache_pos][2]:
                        cache[i][2] = cache[i][2] - 1

                # this is the last recently used
                cache[cache_pos][2] = associativity - 1

                # 1 means it was a hit
                return 1  # return hit??

            # if the block is not valid or the tags does not match, it's a miss

            # look for the Least Recently Used (lru)
            for i in range(associativity):
                if cache[i][2] < cache[cache_pos][2]:
                    lru = i

            # replace that block with the new data
            # set the valid bit in one
            cache[lru][0] = 1
            # replace the old tag with the new one
            cache[lru][1] = tag

            # update the LRU values to comply with the replacement policy
            for i in range(associativity):
                if cache[i][2] > cache[cache_pos][2]:
                    cache[i][2] = cache[i][2] - 1

            cache[cache_pos][2] = associativity - 1

            # 0 means it was a miss
            return 0  # return miss??
