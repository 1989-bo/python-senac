numeros = (
int(input("Digite o primeiro numero: ")),
int(input("Digite o segundo numero: ")), 
int(input("Digite o terceiro numero: ")),
int(input("Digite o quarto numero:" ))
)

pares = 0
for i in numeros:
    if i % 2 ==0:
        pares +=1
        
dez = 10 in numeros
print("\nQuantidade de números pares:", pares)
if dez:
    print("O número 10 está na tupla.")
else:
    print("O número 10 NÃO está na tupla.")
