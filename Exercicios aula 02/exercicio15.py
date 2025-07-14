print("Calculadora IMC")
nome = (input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura**2)
if IMC < 18.5:
    print("Abaixo do peso")
elif 18.5<= 24.9:
    print("Peso normal")
elif 25<=IMC < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")
    