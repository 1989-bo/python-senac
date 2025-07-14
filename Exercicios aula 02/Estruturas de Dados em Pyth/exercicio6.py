numeros = set()

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.add(num)

print("\nNúmeros digitados (sem repetições):", numeros)
print("Quantidade de valores únicos:", len(numeros))