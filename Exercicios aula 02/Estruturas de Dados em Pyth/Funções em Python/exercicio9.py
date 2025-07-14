def contagem (frase):
    quantidade = 0
    for i in frase:
        if i != "":
            quantidade += 1
    return quantidade 

frase = "Hoje é domingo"
total = contagem(frase)
print (f"O total é {total}")

    