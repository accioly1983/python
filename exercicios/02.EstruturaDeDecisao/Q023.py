'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento. '''

numero = input('Informe um número: ')



if '.' not in numero:
    print(f'O número {numero} informado é inteiro.')
else:
    print(f'O número {numero} informado é decimal')

