import random

def repartir_mano_truco():
    numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    cartas = [[n, p] for n in numeros for p in palos]
    return random.sample(cartas, 3)

def es_envido_valor(mano, valor):
    "devuelve 1 si la mano tiene un envido con el valor especificado y 0 si no"
    numeros = [carta[0] if carta[0] < 10 else 0 for carta in mano]
    palos = [carta[1] for carta in mano]
    if len(set(palos)) == 1: # si todas las cartas tienen el mismo palo
        return 1 if(20 + sum(sorted(numeros)[1::]) == valor) else 0 
    if palos[0] == palos[1]:
        return 1 if((20 + numeros[0] + numeros[1]) == valor) else 0
    if palos[0] == palos[2]:
        return 1 if((20 + numeros[0] + numeros[2]) == valor) else 0
    if palos[1] == palos[2]:
        return 1 if((20 + numeros[1] + numeros[2]) == valor) else 0
    else:
        return 1 if max(numeros) == valor else 0

def main():
    N = 1000000
    resul = [["valor envido","probabilidad"]]
    for valor in [31,32,33]:
        G = sum([es_envido_valor(repartir_mano_truco(), valor) for i in range(N)])
        prob = G/N
        print(f'Tiré {N} veces, de las cuales {G} salió envido de {valor} puntos')
        print(f'Podemos estimar la probabilidad de sacar envido de {valor} puntos mediante {prob:.6f}.')
        resul.append([valor, prob])
    print(resul[i] + '\n' for i in range(len(resul)))

if __name__ == "__main__":
    main()