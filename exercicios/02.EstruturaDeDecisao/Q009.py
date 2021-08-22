'''Exercício 009: Faça um Programa que leia três números e mostre-os em ordem decrescente. '''


number_1 = float(input('Numero 1:'))
number_2 = float(input('Numero 2:'))
number_3 = float(input('Numero 3:'))

maior = 0
medio = 0
menor = 0

if number_1 < number_2 and number_1 < number_3:
    menor = number_1
    if number_2 < number_3:
        maior = number_3
        medio = number_2
    else:
        maior = number_2
        medio = number_3
elif number_2 < number_3:
    menor = number_2 
    if number_1 < number_3:
        maior = number_3
        medio = number_1
    else:
        maior = number_1
        medio = number_3
else:
    menor = number_3
    if number_1 < number_2:
        maior = number_2
        medio = number_1
    else:
        maior = number_1
        medio = number_2

print(f'Input:{number_1},{number_2},{number_3} - Ordem: {maior},{medio},{menor}')