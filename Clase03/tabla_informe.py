"los paths se utilizaron en función de que los archivos se encuentran en la misma carpeta en la que se encuentra el código"

import csv

def calcular_costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        keys = next(rows)
        for row in rows:
            try:
                record = dict(zip(keys, row))
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
                values = (row[0], int(row[1]), float(row[2]))
            except ValueError:
                pass
            except TypeError:
                pass
    return costo_total

def leer_precios(file_name):
    precios_dict = {}
    with open(file_name, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                dict.update(precios_dict, {row[0]: row[1]})
            except IndexError:
                pass
    return precios_dict

costo_camion = calcular_costo_camion('fecha_camion.csv')
print(costo_camion)
precios = leer_precios('precios.csv')

pago = 0
costo = 0
for c in costo_camion:
    pago += c['cajones'] * c['precio']
    costo += float(precios[c['nombre']])

print('Balance: ', pago-costo)