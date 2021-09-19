import csv

#%%
# Ejercicio 4.15: 
def leer_parque(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as file:
        rows = csv.reader(file)
        keys = next(rows)
        return [dict(zip(keys, values)) for values in rows]
# Leer el archivo
path = '../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_parque(path)

#%%
# Ejercicio 4.16: Obtener las alturas de los árboles Jacarandá:
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#%%
# Ejercicio 4.17: Obtener tuplas (alturas, diametros) de los Jacarandá:
A_D = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#%%
# Ejercicio 4.18: 
# funcion que recibe lista de nombres de especies y una lista de diccionarios con datos de arboles
# y devuelve un diccionario de clave especie y valor lista de tuplas (altos, diametros) correspondientes
def medidas_de_especies(especies,arboleda):
    return {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}

dato = medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'],arboleda)
print(dato)
