from conexao import conectar

def inserir():

    con = conectar()
    cur = con.cursor()


    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    validade = input("Digite a validade: ")
    familia = input("Digite a familia: ")
    lote = input("Digite o lote: ")
    marca = input("Digite a marca: ")
    ml = int(input("Digite a quantidade em ml: "))
    ocasiao = input("Digite a ocasião: ")
    piramide = input("Digite qual a piramide: ")
    tipo = input("Digite o tipo do perfume: ")

    cur.execute("Insert INTO produtos (nome, preco, validade, familia, lote, marca, ml, ocasiao, piramide, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, preco, validade, familia, lote, marca, ml, ocasiao, piramide, tipo))
    con.commit()
    con.close()

def listar():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM produtos")
    for p in cur.fetchall():
        print(p)
    con.close()

def atualizar():
    con = conectar()
    cur = con.cursor()
    id_produto = int(input("ID do produto: "))
    preco = float(input("Novo preço: "))
    cur.execute ("UPDATE produtos SET preco = %s WHERE  id = %s", (preco, id_produto))
    con.commit()
    con.close()

def excluir():
    con = conectar()
    cur = con.cursor()
    id_produto = int(input("ID para excluir: "))
    cur.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    con.commit()
    con.close()


    
def menu():
    while True:
        print("\n1 - Inserir produto")
        print("2 - Listar produto")
        print("3 - Atualizar produto")
        print("4- Excluir produto: ")
        print("5- Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            inserir()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            excluir()
        elif opcao == "5":
            break


menu()

