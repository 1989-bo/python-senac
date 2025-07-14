print("Temperatura")
celsius = float(input("Digite a temperatura em graus celsius: "))
if celsius < 0:
    print("Está congelando!")
elif celsius <= 25:
    print("Temperatura amena!")
else:
    print("Está quente!")
    