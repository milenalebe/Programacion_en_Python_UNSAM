import random

def tirar():
    return random.choices(range(7),k=5) 

def es_generala():
    if(len(set(tirar())) == 1):
        return True
    else:
        return False

def prob_generala(N):
    G = [es_generala() for i in range(N)]
    return sum(G)/N
    
print(prob_generala(10000))