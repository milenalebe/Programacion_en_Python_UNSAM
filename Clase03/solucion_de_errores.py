#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era semántico, devolvía False ante el primer caracter distinto de a, en lugar de luego de recorrer toda la palabra.
# otro error semántico podría ser que no se identifican las A mayusculas

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'),
tiene_a('abracadabra'),
tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Función tiene_a()
# Errores sintácticos: falta de : al definir la función y al entrar en estructuras de control,
# errores en palabras reservadas y operador de comparación confundido con operador de asignación

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'),
tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.3. Tipos
# Error de tipo: no se utiliza la función str() para analizar una cadena dada como un tipo numérico 

def tiene_uno(exp):
    expresion = str(exp)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
# %%
# Ejercicio 3.4: Alcances
# error semántico: se olvidó de agregar el return!
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
# %%
# Ejercicio 3.5: Pisando memoria
# como la variable 'registro' que se agrega a la lista 'camion' se declaraba fuera del ciclo for,
# se actualiza su valor dentro de la lista al ir modificándola

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    # registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {} # fix
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('camion.csv')
pprint(camion)


