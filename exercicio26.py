import numpy as np

array = np.random.randint(0, 11, size=30)
valores_unicos, frequencia = np.unique(array, return_counts=True)

print(valores_unicos)
print(frequencia)