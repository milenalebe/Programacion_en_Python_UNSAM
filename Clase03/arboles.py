import csv
from collections import Counter

path = 'arbolado-en-espacios-verdes.csv'

"Ejercicio 3.19: Determinar las especies en un parque"

def leer_parque(nombre_archivo, parque):
    lista = []
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as file:
        rows = csv.reader(file)
        keys = next(rows)
        for n_row, row in enumerate(rows, start=0):
            try:
                diccionario = dict(zip(keys, row))
                if(diccionario['espacio_ve'] == parque):
                    lista.append(diccionario)
            except:
                pass
    return lista
datos = leer_parque(path, 'GENERAL PAZ')
#print(datos)

"Ejercicio 3.20: Contar ejemplares por especie"

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        especies.append(arbol['nombre_com'])
    return set(especies)

def contar_ejemplares(lista_arboles):
    cant_especies = Counter()
    for arbol in lista_arboles:
        cant_especies[arbol['nombre_com']] += 1
    return cant_especies
cantidad_por_especie = contar_ejemplares(datos)
#print(cantidad_por_especie)
#print(cantidad_por_especie.most_common(5))

"Ejercicio 3.21: Alturas de una especie en una lista"
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if(arbol['nombre_com'] == especie):
            alturas.append(int(arbol['altura_tot']))
    return alturas

def ejercicio_alturas(nombre_archivo = path):
    alturas_gral = obtener_alturas(leer_parque(nombre_archivo, 'GENERAL PAZ'), 'Jacarandá')
    alturas_andes = obtener_alturas(leer_parque(nombre_archivo, 'ANDES, LOS'), 'Eucalipto')
    alturas_centenario = obtener_alturas(leer_parque(nombre_archivo, 'CENTENARIO'), 'Eucalipto')
    # cómo mejorar esto con un print(f'')?
    print('Alturas de Jacaranda en general paz:', 'Maxima:', max(alturas_gral), 'Promedio', sum(alturas_gral)/len(alturas_gral))
    print('Alturas de Jacaranda en centenario:','Maxima:', max(alturas_centenario),'Promedio', sum(alturas_centenario)/len(alturas_centenario))
    print('Alturas de Jacaranda en alturas_andes:','Maxima:', max(alturas_andes),'Promedio', sum(alturas_andes)/len(alturas_andes))
# ejercicio_alturas()

"Ejercicio 3.22: Inclinaciones por especie de una lista"

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if(arbol['nombre_com'] == especie):
            inclinaciones.append(int(arbol['inclinacio']))
    return inclinaciones
print(obtener_inclinaciones(datos, 'Eucalipto'))

"Ejercicio 3.23: Especie con el ejemplar más inclinado"
## falta para este ejercicio: una funcion que lea los datos de TODOS los parques, solo obtengo el mas inclinado de GRAL PAZ

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    max_inclinacion = 0
    especie_max_inclinacion = None
    for e in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, e)
        if(max(inclinaciones) > max_inclinacion):
            max_inclinacion = max(inclinaciones)
            especie_max_inclinacion = e
    for a in lista_arboles:
        if a['nombre_com'] == especie_max_inclinacion and int(a['inclinacio']) == max_inclinacion:
            return a

"Ejercicio 3.24: Especie más inclinada en promedio"

# falta

