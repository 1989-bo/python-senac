print("Digite uma letra")
letra = input("Digite uma letra: ")
if letra <= ('a-z'):
    print("Minuscula")
elif letra == ('A-Z'):
    print("Maiuscula")
else:
    print("Caractere especial")
