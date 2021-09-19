def propagar(fosforos, flag = False):
    fuego = False
    resultado = []
    for f in fosforos:
        if f == 1:
            fuego = True
            resultado.append(f)
        if f == 0:
            if fuego == True:
                resultado.append(1)
            else:
                resultado.append(f)
        if f == -1:
            fuego = False
            resultado.append(f)
    if flag == False:
        resultado = propagar(resultado, True)
    return resultado

print(propagar( [1,0,-1,0,1,0,0,-1,0,0,-1,0,0,-1,0,0,1,1]))