

import matplotlib.pyplot as plt

categorias = ['Motorola', 'Sansumg', 'Apple', 'Nokia', 'LG']
quantidade = [80, 50, 150, 202, 320]

plt.bar(categorias, quantidade)

plt.title("Celulares mais vendidos nessa semana")
plt.xlabel("Marcas")
plt.ylabel("Qtd Semanal")

plt.show()
