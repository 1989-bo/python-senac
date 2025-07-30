

class Aluno:    #class para ajudar na criação do objeto
    def __init__(self, nome, idade, cidade, curso, renda, peso, altura): #metodo 
        
        self.nome = nome #atributo
        self.idade = idade #atributo
        self.cidade = cidade #atributo
        self.curso = curso #atributo
        self.renda = renda #atributo
        self.peso = peso #atributo
        self.altura = altura #atributo

#criação do objeto e como argumento os atributos pessoais
aluno1 = Aluno("Bruno", 36, "São Paulo", "Python", 15.000, 81, 1.75)

print(aluno1.idade)


