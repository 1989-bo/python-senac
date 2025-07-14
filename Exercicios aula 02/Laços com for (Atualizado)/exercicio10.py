nome = 0
frutas = ""

while len(frutas) <= 10:
    frutas = input("Digite o nome da fruta: ")
    if len (frutas) <=10:
        nome += 1
        
print(f"Quantidade de frutas inseridas são {nome}")
 