vogais = {"a", "e", "i", "o", "u"}
palavra = input("Digite uma palavra: ")
letrasPalavras = set(palavra)

comum = vogais & letrasPalavras
print(f"Letras em comum são: {comum}")

