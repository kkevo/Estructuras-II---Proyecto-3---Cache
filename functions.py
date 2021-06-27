def toBin(num, n):
    ''' Devuelve un numero binario 
    con n cantidad de bits. '''

    # Obtains binary number
    result = bin(num).replace("0b","")

    # Adds zeros to the left if necessary
    if len(result) < n:
        return '0' * (n - len(result)) + result
    else:
        return result