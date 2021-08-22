'''Exercício 01: Faça um Programa que peça dois números e imprima o maior deles. '''

num_1 = float(input('Informe o primeiro número: '))
num_2 = float(input('Informe o segundo número: '))

maior = -1
if num_1 > num_2:
    maior = num_1
else:
    maior = num_2

print (f'O maior número [{num_1}. {num_2}] é {maior}')