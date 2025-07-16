

import matplotlib.pyplot as plt

categorias = ['Laranja', 'Limão', 'Abacaxi', 'Morango', 'Maça']
quantidade = [80, 60, 50, 60, 70]

plt.bar(categorias, quantidade, color=['orange', 'green', 'yellow', 'red', 'red'])

plt.title("Frutas mais vendidas")
plt.xlabel("Total Frutas")
plt.ylabel("Qtde total de vendas")

plt.show()


