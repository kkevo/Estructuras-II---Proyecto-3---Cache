#include <iostream>
#include <string>
#include <headersCache.h>


using namespace std;

int lru_replacement_policy (int idx,
                           int tag,
                           int associativity,
                           bool loadstore,
                           entry* cache_blocks,
                           operation_result* operation_result);

int main(int argc, char * argv[]){
    return 0;
}


int lru_replacement_policy  (int idx,
                             int tag,
                             int associativity,
                             bool loadstore,
                             entry* cache_blocks,
                             operation_result* result){
    //Se inicializa en miss
    bool state = false;

    //se recorre el cache primeramente buscando si el valor actual del addres
    // ya existe en el cache
    for(int cache_pos = 0; cache_pos < asociativity; cache_pos++){
        //se revisa si la posicion fue escrita antes por medio del bit de valido
        //si no fue escrita se sigue a la siguiente posicion
        if(cache_blocks[cache_pos].valid == 1){
            //Se revisa si el tag es el mismo, si coincide entonces es un hit
            if(cache_blocks[cache_pos].tag == tag){
                state = true;

                //Se revisa si la instruccion es de store y se actualizan los resultados
                if(loadstore == 1){
                    result -> miss_hit = HIT_STORE;
                }
                else{
                    result ->  miss_hit = HIT_LOAD;
                }

                //Se actualizan los valores de la politica de remplazo para hacer compliance con LRU
                for(int j = 0; j < associativity; j++){
                    if(cache_blocks[j].rp_value > cache_blocks[i].rp_value){
                    cache_blocks[j].rp_value--;
                    }
                }
                // El bloque utilizado fue se pone de primero en la poltica de remplazo
                cache_blocks[cache_pos].rp_value = associativity - 1; 
                return 0;
            }//fin del hit
        }
    }

    //miss
   if(!state){

      //Se buscar por el LRU que tiene el valor 0 en la politica de remplazo
      for(int i = 0; i < associativity; i++){
         if(cache_blocks[i].rp_value == 0){

            
            result->evicted_address = cache_blocks[i].tag; //Esta direccion fue remplazada

            if(loadstore == 1){
               result->miss_hit = MISS_STORE;
            }
            else{
               result->miss_hit = MISS_LOAD;
            }

            //Se actualizan los valores de la politica de remplazo para hacer compliance con LRU
            for(int j = 0; j < associativity; j++){
               if(cache_blocks[j].rp_value > cache_blocks[i].rp_value){
                  cache_blocks[j].rp_value--;
               }
            }
            
             // El bloque utilizado fue se pone de primero en la poltica de remplazo
            cache_blocks[i].rp_value = associativity - 1;

            //Se actualizan los valores del bloque actual
            cache_blocks[i].tag = tag;
            cache_blocks[i].valid = true;
            break;
         }
      }
      return 0;
   }// fin del miss




    return 1;
}

