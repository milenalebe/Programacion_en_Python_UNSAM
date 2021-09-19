import csv
def leer_camion_tupla(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                lote = (row[0], int(row[1]), float(row[2]))
                camion.append(lote)
            except ValueError:
                pass
    return camion

def leer_camion_dict(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        keys = next(rows)
        for row in rows:
            try:
                values = (row[0], int(row[1]), float(row[2]))
                camion.append(dict(zip(keys, values)))
            except ValueError:
                pass
    return camion

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

camiones = leer_camion_dict('camion.csv')
precios = leer_precios('precios.csv')

pago = 0
costo = 0
for c in camiones:
    pago += c['cajones'] * c['precio']
    costo += float(precios[c['nombre']])

print('Balance: ', pago-costo)