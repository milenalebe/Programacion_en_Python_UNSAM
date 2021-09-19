import csv

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
    print(costo)
 
costo_camion(file_name)