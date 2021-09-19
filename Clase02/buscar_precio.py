import os
import csv

def buscar_precio(fruta):
    file_name = 'precios.csv'
    with open(file_name, 'rt') as file:
        while(True): 
            try:
                linea = next(file)
                linea = linea.split(',')
                if linea[0] == fruta:
                    print(linea[1])
                    break
            except StopIteration:
                print('No se encontró')
                break




buscar_precio('Lechuga')
