/*
    Cache L1 with LRU policy
    UCR IE-521

*/

#include<headersCache.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>


#define KB 1024 // KB is 1024 bytes
#define ADDRSIZE 32

using namespace std;

int field_size_get(struct cache_params,
struct cache_field_size *field_size)
{
    // Offset is calculated as log2(block_size)
    field_size -> offset = log2(cache_params.block_size);
    // Index is calculated log2(cache_size/block_size*asociativity)
    field_size->idx=log2((cache_params.size*KB)/(cache_params.block_size*cache_params.asociativity));
    // Tag is calculated as addres size - offset - index
    field_size->tag=ADDRSIZE-field_size->offset-field_size->idx;
    return OK;
}

