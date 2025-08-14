
from des import conector

con = conector()
cur = con.cursor()


def mesa():
    
    status = input("Qual status da mesa: ")
    con = conector()
    cursor = con.cursor()
    cursor.execute("INSERT INTO mesa (Status) VALUES (&s,)", (status))
    

    con.commit()

    print("Reserva efetuada! ")
    
    cursor.close()
    con.close()

    


def reservar():
    id = input("Digite o ID da sua mesa: ")
    nome = input("Digite o seu nome: ")
    con = conector()
    cursor = con.cursor()
    cursor.execute("SELECT Status FROM mesa WHERE id=%s", (id,))
    status = cursor.fetchone()
    if status and status[0] == 'Disponivel':

        cursor.execute("UPDATE mesa SET Status = %s, Nome = %s WHERE ID = %s", ('Reservado',nome,id))

        con.commit()
        print("Reserva feita!")
   
    con.close()



def verificar():
    
    con = conector()
    cur = con.cursor()
    cur.execute("SELECT * FROM mesa")

    for p in cur.fetchall():
        print(p)

    cur.close()
    con.close()




def cancelar():

    con = conector()
    cur = con.cursor()

    id = int(input("Digite o ID para cancelar: "))
    cur.execute("DELETE FROM mesa WHERE id = %s", (id,))

    print("Reserva cancelada!")


    cur.close()
    con.close()


def menu():

    while True:

        print("\n1 - Fazer reserva")
        print("2 - Listar reservas feitas")
        print("3- Verificar disponibilidade")
        print("4- Excluir reserva: ")
        print("5- Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            reservar()
        elif opcao == 2:
            mesa()
        elif opcao == "3":    
            verificar()
        elif opcao == "4":
            cancelar()
        elif opcao == "5":
            break


menu()
