import time
import sys
import math
# Files
from functions import toBin


# Constants
addr_size = 32
KB = 1024


# FALTA: Hacer que los valores esten entre los limites
cache_size = int(sys.argv[1]) # Between 32 and 128, in KB
block_size = int(sys.argv[2]) # Between 32 and 128, in bytes
asociativity = int(sys.argv[3]) # Number of ways, between 4 and 16

offset = math.log(block_size, 2)
index = math.log(cache_size*KB/(block_size*asociativity), 2)
tag = addr_size - offset - index

print("Cache size:", cache_size, "\n",
      "Block size:", block_size, "\n",
      "Asociativity:", asociativity)

file = open("data2", "r")

start = time.time()

cache = []
for i in range(asociativity):
    way = []
    for j in range(int(2**index)):
        # Set structure: valid, tag, data, LRU value
        way.append([0, 0, [x for x in range(block_size)], 0])
    cache.append(way)
        
print(cache[0][0])

for line in file:
    addr = toBin(int(line[4], 16), 4).replace("0b", "") + toBin(int(line[5], 16), 4).replace("0b", "") + toBin(int(line[6], 16), 4).replace("0b", "") + toBin(int(line[7], 16), 4).replace("0b", "") + toBin(int(line[8], 16), 4).replace("0b", "") + toBin(int(line[9], 16), 4).replace("0b", "") + toBin(int(line[10], 16), 4).replace("0b", "") + toBin(int(line[11], 16), 4).replace("0b", "")
    addr_tag = addr[0 : int(tag)]
    addr_index = addr[int(tag) : int(tag)+int(index)]
    addr_offset = addr[int(tag)+int(index) : int(tag)+int(index)+int(offset)]
    # print(addr)
    # print("Tag: ", addr_tag)
    # print("Index: ", addr_index)
    # print("Offset: ", addr_offset)
    # print()


end = time.time()

print("Execution time: ", end-start)

