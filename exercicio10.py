import numpy as np
import matplotlib.pyplot as plt

alturas = np.random.normal(loc=170, scale=10, size=100)

# O percentil 25, 50 (mediana) e 75
percentil_25 = np.percentile(alturas, 25)
mediana = np.percentile(alturas, 50)
percentil_75 = np.percentile(alturas, 75)

print(percentil_25)
print(mediana)
print(percentil_75)

# A quantidade de pessoas com altura acima de 180 cm
acima_180 = np.sum(alturas > 180)
print(acima_180)

# Plote um histograma dos dados usando Matplotlib (não precisa detalhar o código da plotagem).
plt.hist(alturas, bins=10, edgecolor='black', alpha=0.7)
plt.title('Histograma')
plt.xlabel('Altura em cm')
plt.ylabel('Frequência')
plt.show()
