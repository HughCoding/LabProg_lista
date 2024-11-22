import numpy as np

vetor_a = np.array([1, 2, 3])
vetor_b = np.array([4, 5, 6])

produto_escalar = np.dot(vetor_a, vetor_b)
produto_externo = np.outer(vetor_a, vetor_b)

print(produto_escalar)
print(produto_externo)
