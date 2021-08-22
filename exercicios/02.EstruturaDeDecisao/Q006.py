'''Exercício 006: Faça um Programa que leia três números e mostre o maior deles. '''


num_1 = float(input('Informe o número 1: '))
num_2 = float(input('Informe o número 2: '))
num_3 = float(input('Informe o número 3: '))


maior = 0
if num_1 >= num_2 and num_1 >= num_3:
    maior = num_1
elif num_2 >= num_3:
    maior = num_2
else:
    maior = num_3

print(f'O maior entre {num_1},{num_2} e {num_3} é {maior}')