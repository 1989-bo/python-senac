

class Aluno:    #class para ajudar na criação do objeto
    def __init__(self, nome, idade, cidade, curso, renda, peso, altura): #metodo é uma função
        
        self.nome = nome #atributo
        self.idade = idade #atributo
        self.cidade = cidade #atributo
        self.curso = curso #atributo
        self.renda = renda #atributo
        self.peso = peso #atributo
        self.altura = altura #atributo

    def apresentacao(self):
        print(f"Olá meu nome é {self.nome} tenho {self.idade} anos, moro na cidade de {self.cidade}, faço curso de {self.curso}, minha renda mensal é de {self.renda}, tenho {self.peso} e minha altura é de {self.altura}")


#criação do objeto e como argumento os atributos pessoais
aluno1 = Aluno("Bruno", 36, "São Paulo", "Python", 15.000, 81, 1.75)

#exibir metodo não é necessário print somente chamar o objeto
aluno1.apresentacao()


