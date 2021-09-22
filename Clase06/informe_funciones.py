import csv


def calcular_costo_camion(nombre_archivo, header = True) -> list[dict]:
    """"
    parametros:
    nombre_archivo, path del archivo con datos de cajones: Producto, cantidad, Precio
    header, indica si el archivo tiene encabezado
    devuelve:
    camion, una lista de tuplas con los datos del cajon mas el costo total de cada cajon
    """
    camion = []
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        # El encabezado esta fijado
        if(header):
            next(rows)
        for row in rows:
            try:
                nombre = row[0]
                ncajones = float(row[1])
                precio_unidad = float(row[2])
                costo_total = ncajones * precio_unidad
                values = (nombre, ncajones, precio_unidad, costo_total)
                camion.append(values)
            except ValueError:
                # Sería interesante agregar un contador de filas que se han salteado por Excepción
                pass
    return camion

def leer_precios(file_name: str) -> dict:
    """
    lee un csv con dos columnas y devuelve un diccionario de la forma
    col0: col1
    """
    precios_dict = {}
    with open(file_name, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                dict.update(precios_dict, {str(row[0]): float(row[1])})
            except IndexError:
                pass
    return precios_dict



def hacer_informe(camion_costo, precios):
    """
    camion_costo: lista de diccionarios
    """
    informe = []
    for cajon in camion_costo:
        balance_unidad = -cajon[2] + precios[cajon[0]]  
        informe.append((cajon[0], cajon[1], cajon[2], balance_unidad))
    return informe

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    separator = ('--------- ---------- ---------- ----------')
    print('%10s %10s %10s %10s' % headers)
    print(separator)
    for r in informe:
        print('%10s %10d %10.2f %10.2f' % r)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion_costo = calcular_costo_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    print(type(precios))
    informe = hacer_informe(camion_costo, precios)
    imprimir_informe(informe)

