

import requests

nome = input("Digite seu nome: ")
url = "https://api.agify.io?name=" + nome


resposta = requests.get(url)


dados = resposta.json()
print(f"Nome: {dados['name']}")
print(f"Idade estimada: {dados['age']}")
