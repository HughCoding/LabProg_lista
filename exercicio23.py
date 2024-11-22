import numpy as np

numeros = np.arange(20)
numeros[numeros % 3 == 0] = -3
print(numeros)
