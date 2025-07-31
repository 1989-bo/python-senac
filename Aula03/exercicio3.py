

class Livros:
    def __init__(self, titulo, autor):
        
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro =({self.titulo}, autor = {self.autor})"
    

    def apresentacao(self):
        print(f"O {titulo}, é do autor {autor} ")

titulo = "Alo"
autor = "Amarelo"

catalogo = Livros ({titulo}, {autor})

print(catalogo)







    