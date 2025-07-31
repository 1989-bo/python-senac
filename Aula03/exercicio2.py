

class Aluno:

    def __init__(self, nome, nota1, nota2, nota3, media):
        
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media
      


    def apresentacao (self):
        print(f"{nome}, sua média de nota foi {media} ")

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media =  ((nota1+nota2+nota3)/3)



estudante = Aluno({nome}, {nota1}, {nota2}, {nota3}, {media})




estudante.apresentacao()











