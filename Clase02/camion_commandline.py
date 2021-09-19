import csv
import sys

file_name = 'missing.csv' 

def costo_camion(path):
    costo = 0
    with open(path, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                costo += float(row[1]) * float(row[2])
            except ValueError:
                pass
    return costo

    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)