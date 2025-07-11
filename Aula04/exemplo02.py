cliente = {"nome":"Pascoal","numero": 11949083773, "idade": 45, "cpf": "123456789", "endereço": "rua tito"}
print(cliente)
print(len(cliente))
print(cliente["endereço"])
del cliente["nome"]
print(cliente)
print(len(cliente))
cliente["nome"] = "Bruno"
print(cliente)
print(len(cliente))
