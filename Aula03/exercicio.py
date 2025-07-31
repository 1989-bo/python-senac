

class Loja:

    def __init__(self, produto, cor, tamanho, preco):

        self.produto = produto
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def apresentacao(self):
        print(f"O {produto}, com a cor {cor}, no tamanho {tamanho}, tem o valor de {preco} reais ")

produto = input("Digite qual o produto: ")
cor = input("Digite qual a cor que deseja: ")
tamanho = input("Digite qual o tamanho: ")
preco = float(input("Digite o valor do produto: "))

catalogo = Loja ({produto}, {cor}, {tamanho}, {preco} )


catalogo.apresentacao()


        

        
        

        