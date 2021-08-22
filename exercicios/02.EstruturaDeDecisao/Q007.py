'''Exercício 007: Faça um Programa que leia três números e mostre o maior e o menor deles. '''


num_1 = float(input('Informe o número 1: '))
num_2 = float(input('Informe o número 2: '))
num_3 = float(input('Informe o número 3: '))


maior = 0
menor = 0
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
    if num_2 > num_3:
        menor = num_3
    else:
        menor = num_2
elif num_2 > num_3:
    maior = num_2
    if num_1 > num_3:
        menor = num_3
    else:
        menor = num_1
else:
    maior = num_3
    if num_1 > num_2:
        menor = num_2
    else:
        menor = num_1

print(f'O maior entre {num_1},{num_2} e {num_3} é {maior}')
print(f'O menor entre {num_1},{num_2} e {num_3} é {menor}')