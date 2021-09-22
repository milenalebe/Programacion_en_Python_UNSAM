import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

caminos = []

ax = plt.subplot(2, 1, 1)
plt.xticks([]), plt.yticks([-500,0,500])
for i in range(12):
    pasos = randomwalk(N)
    ax.plot(pasos,label=f'{i}')
    ax.set_title('12 Caminatas al azar')
    plt.ylim(-800, 800)
    caminos.append(pasos)

max_dist_origen = 0
min_dist_origen = 0
print(caminos)
for c in caminos:
    if max(abs(c)) > max_dist_origen:
        max_dist_origen = max(abs(c))
        max_camino = c

        if min_dist_origen == 0:
            min_dist_origen = max(abs(c))
            min_camino = c
    if max(abs(c)) < min_dist_origen:
        min_dist_origen = max(abs(c))
        min_camino = c
        
      
ax = plt.subplot(2, 2, 3)
plt.plot(max_camino)
plt.xticks([]), plt.yticks([-500, 0, 500])
plt.ylim(-800, 800)
ax.set_title('Caminata más alejada ')

ax = plt.subplot(2, 2, 4) 
plt.plot(min_camino)
plt.xticks([]), plt.yticks([-500, 0, 500])
plt.ylim(-800, 800)
ax.set_title('Caminata menos intrépida ')

print(caminos)

plt.show()