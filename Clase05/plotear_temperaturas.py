import os
import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas():
    path = '../Data/temperaturas.npy'
    temperaturas = np.load(path)
    plt.hist(temperaturas,bins= 18)
    plt.show()

if __name__ == '__main__':
    plotear_temperaturas()