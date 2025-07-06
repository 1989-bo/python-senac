print('Calculadora de IMC')
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
peso = float(input('Digite seu peso em (kg):'))
altura = float(input('Digite sua altura em (m):'))
IMC = peso / (altura**2)
if IMC<18.5:
    print('Seu IMC está abaixo do peso')
elif IMC>=18.5 <= 24.9:
    print('Seu IMC está peso normal')
elif IMC >=25 <=29.9:
    print('Seu IMC está sobrepeso')
else:
    print('Seu IMC está Obesidade')
    
    
    
    
    
    
    
    
    

