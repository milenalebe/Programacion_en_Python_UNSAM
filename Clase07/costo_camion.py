import informe_final
import sys

def f_principal():
    print(len(sys.argv))
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    camion = informe_final.calcular_costo_camion(sys.argv[1])
    costo = 0
    for c in camion:
        costo += c[3] 
    print("Costo total: " + str(round(costo)))
    return costo

if __name__ == '__main__':
    f_principal()