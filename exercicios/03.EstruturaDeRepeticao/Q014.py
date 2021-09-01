'''Exercicio 14:
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade 
de números impares.'''

qtd_par = qtd_impar = 0
numeros = ''

for x in range(1,11):
    while True:
        try:
            numero = int(input(f'Entre com o numero {x}:'))
            break
        except:
            print(f'Permitido apenas números inteiro!')
    
    if numero%2 == 0:
        qtd_par+=1
    else:
        qtd_impar+=1
    
    numeros+= str(numero) + '|'

print(f'Quantidade total de números: {(qtd_par+qtd_impar)}')
print(f'Números: {numeros}')
print(f'Números pares: {qtd_par}')
print(f'Números ímpares: {qtd_impar}')