import random
import numpy as np

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=int)

def comprar_figu(figus_total, FIGUS_PAQUETE = 1):
    return random.choices(range(figus_total), k= FIGUS_PAQUETE)

def album_incompleto(A):
    return 0 in A

def cuantas_figus(figus_total, FIGUS_PAQUETE = 1):
    album = crear_album(figus_total)
    cant_compradas = 0
    while(album_incompleto(album)):
        figuritas_nuevas = comprar_figu(cantidad_figuritas_album)
        for i in figuritas_nuevas:
            album[i] +=1
        cant_compradas += FIGUS_PAQUETE
    return cant_compradas

def experimento_figus(n_repeticiones, figus_total):
    return np.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)])

if __name__ == '__main__':
    cantidad_figuritas_album = 6
    N = 1000
    print(experimento_figus(N, cantidad_figuritas_album))