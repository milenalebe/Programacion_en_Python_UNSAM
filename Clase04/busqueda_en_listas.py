def buscar_u_elemento(lista, e): 
    '''Devuelve el mayor índice de un elemento igual a e en la lista, o -1 si e no está en la lista'''
    pos = -1  
    for i, elem in enumerate(lista):
        if elem == e:
            pos = i
    return pos

def buscar_n_elemento(lista, e):
    '''Devuelve la cantidad de ocurrencias de e en lista'''
    n = 0
    for elem in enumerate(lista):
        if elem == e:
            n+=1
    return n


def maximo(lista):
    '''Devuelve el máximo de una lista'''
    max = lista[0]
    for e in lista[1:]: 
        if e > max:
            max = e
    return max

def minimo(lista):
    '''Devuelve el mínimo de una lista'''
    min = lista[0]
    for e in lista[1:]: 
        if e < min: 
            min = e
    return min
