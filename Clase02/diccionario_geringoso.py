def traducir(cadena):
    capadepenapa = ''
    for c in cadena:
        if(c in 'aeiou'):
            capadepenapa += c + 'p' + c
        else:
            capadepenapa += c
    return capadepenapa


def diccionario_geringoso(palabras):
    palabras_geringoso = [traducir(palabra) for palabra in palabras]
    tuplas = [p for p in zip(palabras, palabras_geringoso)]
    return dict(tuplas)

dic = diccionario_geringoso(['hola', 'mundo', 'como', 'estas'])
print(dic)