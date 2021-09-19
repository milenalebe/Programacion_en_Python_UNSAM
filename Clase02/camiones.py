import os

costo = 0
path = 'camion.csv' 
with open(path, 'rt') as file:
    data = [line.split(',') for line in file]

# salteamos el encabezado
for row in data[1::]:
    costo += float(row[1]) * float(row[2])
print(costo)
 

