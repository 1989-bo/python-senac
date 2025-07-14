def numeroMaior (numero):
    maior = numero[0]
    for i in numero:
        if i > maior:
            maior = i
    return maior

numero = [4, 8, 12, 16, 20]
maiorValor = numeroMaior(numero)
print(f"O maior numero da lista é {maiorValor}")
 
    