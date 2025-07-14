print('Nota do aluno')
nome=input('Digite seu nome: ')
idade=input('Digite sua idade: ')
nota = float(input('Digite sua nota entre 0 e 10: '))
if nota>=7:
    print(f'Sua nota foi {nota} você foi aprovado!') 
elif nota>=5 <=6.9:
    print(f'Sua nota foi {nota} você está em recuperação!') 
else:
    print(f'Sua nota foi {nota} você foi reprovado!') 
    
    
    
