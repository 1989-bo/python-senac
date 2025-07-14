print("Nota do aluno")
nota = float(input("Digite sua nota de 0 a 10: "))
if nota <5:
    print("Reprovado!")
elif nota == 5 :
    print("Recuperação!")
elif nota <= 6.9:
    print("Recuperação!")
else:
    print("Aprovado! ")
    