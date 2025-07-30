

class Carro:

    def __init__(self, nome, modelo, ano, combustivel, cor, valor):

        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel
        self.cor = cor
        self.valor = valor

    def vendas(self):
        print(f"O carro da marca {self.nome}, do modelo {self.modelo}, ano {self.ano}, combustivel {self.combustivel}, da cor {self.cor} está a venda pelo valor de {self.valor}!!!!")

BMW = Carro ("BMW", "X1", 2008, "gasolina", "azul", 250.000)

AUDI = Carro ("Audi", "Q6", "2010", "Hibrido", "Amarela", 275.000)

BMW.vendas()
AUDI.vendas()





