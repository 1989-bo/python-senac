print("Calculo sálario")
horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor de cada hora trabalhada: "))
salario = horas*valor
if salario <= 1000:
    print("Sálario baixo")
elif salario >= 1001 and salario <= 3000:
    print("Sálario médio")
else:
    print("Sálario alto")
    