

def horario ():
    hora = int(input("Digite o horario atual: "))
    
    if hora <=5:
        print("Bom dia!")
        
    elif hora <=12:
        print("Bom dia!")
        
    elif hora >13:
        print("Boa tarde!")
        
    elif hora <=18:
        print("Boa tarde!")
        
    else:
        print("Boa noite!")
        
horario ()

        