def invertir_lista(lista):
    invertida = []
    for i, e in enumerate(lista): 
        invertida.insert(-i, e)
    return invertida

def invertir_lista_comprension(lista):
    '''Devuelve la lista invertida'''
    return [lista[i] for i in range(-len(lista)+1, -1)]

def invertir_lista_muy_pythonesco(lista):
    '''Devuelve la lista invertida'''
    return lista[::-1]

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

