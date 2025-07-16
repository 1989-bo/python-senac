
import matplotlib.pyplot as plt

categorias = ['Python', 'Java Script', 'Java', 'C#', 'C++']
quantidade = [80, 60, 40, 35, 80]

plt.bar(categorias, quantidade)

plt.title("Linguagens mais usadas")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade")

plt.show()


