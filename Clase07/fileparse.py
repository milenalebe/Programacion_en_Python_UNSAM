# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        
        if select and has_headers:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        elif (select or has_headers) and not silence_errors:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if types and indices:
                fila = [func(val) for func, val in zip(types, fila) ]
            elif types and not silence_errors:
                raise(RuntimeError("Para tipos, necesito indices."))
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro = (tuple(fila))
            registros.append(registro)

    return registros
    
precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
print(precios)