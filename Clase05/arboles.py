#%%
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set

# Path del archivo con datos del arbolado en espacios verdes:
path = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')

#%%
# Ejercicio 4.15: 
def leer_parque(nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'):
    lista = []
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as file:
        rows = csv.reader(file)
        keys = next(rows)
        return [dict(zip(keys, values)) for values in rows]

#%%
# Ejercicio 4.16: Obtener las alturas de los árboles Jacarandá:
def alturas_jacarandas(path = '../Data/arbolado-en-espacios-verdes.csv'):
    arboleda = leer_parque(path)
    return [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#%%
# Ejercicio 4.17: Obtener tuplas (alturas, diametros) de los Jacarandá:
def alturas_diametros_jacarandas(path = '../Data/arbolado-en-espacios-verdes.csv'):
    arboleda = leer_parque(path)
    return [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#%%
# Ejercicio 4.18: 
# funcion que recibe lista de nombres de especies y una lista de diccionarios con datos de arboles
# y devuelve un diccionario de clave especie y valor lista de tuplas (altos, diametros) correspondientes
def medidas_de_especies(especies,arboleda):
    return {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}


#%%
# Ejercicio 5.25: Histograma de altos de Jacarandás
def histograma_altos(path = '../Data/arbolado-en-espacios-verdes.csv'):
    altos = alturas_jacarandas(path)
    plt.hist(altos,bins=20)
    plt.show()

# %%
def scatter_hd(lista_de_pares, especie = 'Jacarandas'):
    plt.scatter([par[0] for par in lista_de_pares], [par[1] for par in lista_de_pares])
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f"Relación diámetro-alto para {especie}")
    plt.xlim(0,30) 
    plt.ylim(0,100) 
    plt.show()

def scatter_hd_acumulando(lista_de_pares):
    plt.scatter([par[0] for par in lista_de_pares], [par[1] for par in lista_de_pares])
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,30) 
    plt.ylim(0,100)

def extra(arboleda, especies, medidas, especie1, especie2):
    scatter_hd_acumulando(medidas[especie1])
    scatter_hd_acumulando(medidas[especie2])
    plt.title(f"Extra: comparación entre {especie1} y {especie2}")
    plt.show()

def graficos_por_especies(path = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')):
    arboleda = leer_parque(path)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    scatter_hd(medidas['Eucalipto'], 'Eucalipto')
    scatter_hd(medidas['Palo borracho rosado'], 'Palo Borracho Rosado')
    scatter_hd(medidas['Jacarandá'])
    extra(arboleda, especies, medidas, 'Eucalipto', 'Jacarandá')


if __name__ == "__main__":
    try:
        histograma_altos()
        graficos_por_especies()
    except FileNotFoundError:
        new_path = input('No se encontró el archivo. Ingrese el directorio con el archivo csv: ')
        try:     
            histograma_altos(new_path)
            graficos_por_especies(new_path)
        except: 
            print('No se encontró el archivo.')