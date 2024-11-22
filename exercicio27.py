import numpy as np

matriz = np.array([[1, 5], [2, 3]])
vetor_v = np.array([1, 2])
vetor_transformado = np.dot(matriz, vetor_v)
print(vetor_transformado)
