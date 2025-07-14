print("Digite o lado do triangulo")
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("É um triângulo igual.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("É um triângulo de dois lados iguais.")
elif lado1 !=  lado2 and lado2 != lado3: 
        print("Todos os lado são diferentes .")
else:
    print("soma de dois lados deve ser maior que o terceiro")
    


