import random
import numpy as np
import os

def medir_temp(n):
    mu, sigma = 0, 0.2
    temp = 37.5
    return [random.normalvariate(mu,sigma) + temp for i in range(n)]

def resumen_temp(n):
    temp = medir_temp(n)
    save_temp(temp)
    if(n%2 == 0):
        return(max(temp), min(temp), sum(temp)/n, (sorted(temp)[n//2] + sorted(temp)[(n//2)+1])/2)
    else:
        return(max(temp), min(temp), sum(temp)/n, sorted(temp)[(n//2) +1])

def save_temp(temp):
    try:
        path = str(os.getcwd()) + '\Ejercicios\ejercicios_python\Data'
        np.save(path + '\\ temperaturas', np.array(temp))    
    except FileNotFoundError:
        try: 
            new_path = input('Error para guardar los resultados. Ingrese un directorio para reintentar guardarlos allí: ')
            np.save(new_path + '\\ temperaturas', np.array(temp))
        except:
            print("Directorio incorrecto")

if __name__ == "__main__":
    N = 999
    resul = resumen_temp(N)
    print(np.array(resul))

    