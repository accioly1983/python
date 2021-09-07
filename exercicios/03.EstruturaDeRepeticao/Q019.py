'''Exericio 19:
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

maior = 0
menor = 999999999999999
soma = 0

n = int(input('Informe a quantidade de números que gostaria de ler:'))

for x in range(1,n+1):
    num = int(input(f'Informe o número {x} (0 e 1000): '))
    while num<0 or num>1000:
        print('Número {num} inválido! Caro usuário o valor informado deve estar entre 0 e 1000!')
        num = int(input(f'Informe um número {x}: '))
    if num > maior:
        maior = num
    if num < menor:
        menor=num
    soma+=num

print(f'****Qtd número lidos {n} ****')
print(f'Maior      : {maior} ')
print(f'Menor      : {menor} ')
print(f'Soma total : {soma} ')