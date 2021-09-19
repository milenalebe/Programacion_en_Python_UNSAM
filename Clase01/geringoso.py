cadena = 'Murcielago'
capadepenapa = ''
for c in cadena:
    if(c in 'aeiou'):
        capadepenapa += c + 'p' + c
    else:
        capadepenapa += c
print(capadepenapa)