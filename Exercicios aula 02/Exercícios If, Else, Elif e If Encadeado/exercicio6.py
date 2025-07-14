print("Comparando numeros")
numero = float(input("Digite um numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))
if numero > numero2 and numero > numero3:
    print(f"O numero {numero} é maior!")
elif numero2 > numero and numero2 > numero3:
    print(f"O numero2 {numero2} é maior")
else:
    print(f"O numero {numero3} é maior!")
    