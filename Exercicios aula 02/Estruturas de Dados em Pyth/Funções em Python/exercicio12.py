

def mediaNotas (nota1, nota2, nota3):
    resultado = (nota1+nota2+nota3)/3
    print(f"A média das 3 notas é de {resultado}")

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))

mediaNotas(nota1, nota2, nota3)