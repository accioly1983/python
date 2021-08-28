'''Exercício 11:
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo. '''

num_1 = int(input('Informe o primeiro numero inteiro: '))
num_2 = int(input('Informe o segundo numero inteiro: '))
num_3 = float(input('Informe um valor: '))
result_produto = (2*num_1)*num_2//2
result_soma = (3*num_1) + num_3
result_cubo = num_3 ** 3
print(f'O poduto do dobro do primeiro {num_1} com metade do segundo {num_2}/2 é : {result_produto} ')
print(f'A soma do primeiro {num_1} com terceiro {num_3} é : {result_soma} ')
print(f'O terceiro {num_3} elevado ao cubo é : {result_cubo} ')