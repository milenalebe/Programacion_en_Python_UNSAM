import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def main():
    N = 10000
    M = []
    for i in range(N):
        x,y = generar_punto()
        if x**2 + y**2 <= 1:
            M.append(1)
        else:
            M.append(0)
    pi = sum(M)*4 /N
    print(f'Generando {N} puntos, el valor estimado para pi es de {pi}')

if __name__ == '__main__':
    main()