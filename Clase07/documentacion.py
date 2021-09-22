def valor_absoluto(n):
    'Recibe un número n y devuelve su valor absoluto'
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    'Recibe una lista de números l y devuelve la sumatoria de todos los números pares en l'
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''Pre: Recibe dos números a y b, b debe ser mayor o igual a cero
    Post: devuelve su multiplicación'''
    assert b >=0
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    "Calcula la órbita de n según la conjetura de Collatz y termina la ejecución al alcanzar el 1"
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

for i in range(20):
    print(collatz(i))