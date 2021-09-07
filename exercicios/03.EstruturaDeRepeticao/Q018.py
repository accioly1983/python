'''Exericio 18:
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a 
soma dos valores. '''

maior = 0
menor = 999999999999999
soma = 0

n = int(input('Informe a quantidade de números que gostaria de ler:'))

for x in range(1,n+1):
    num = int(input(f'Informe o número {x}:'))
    if num > maior:
        maior = num
    if num < menor:
        menor=num
    soma+=num

print(f'****Qtd número lidos {n} ****')
print(f'Maior      : {maior} ')
print(f'Menor      : {menor} ')
print(f'Soma total : {soma} ')

