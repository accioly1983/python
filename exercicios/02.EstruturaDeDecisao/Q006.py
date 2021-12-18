'''Exercício 006: Faça um Programa que leia três números e mostre o maior deles. '''

maior=0
num_1 = float(input('Informe o número 1: '))
num_2 = float(input('Informe o número 2: '))
num_3 = float(input('Informe o número 3: '))

'''
#Solução 1: Não é a melhor opção pois não é escalável. Não é escalável pq duplica da linha 10 a 18 qdo adiciona uma nova variável.
if num_1 > num_2:
    if num_1 > num_3:
        maior = num_1
    else:
        maior = num_3
else:
    if num_2 > num_3:
        maior = num_2
    else:
        maior = num_3
'''
'''
# Solução 2: solução melhor que a solução 1 e mais escalável
if (num_1 >= num_2) and (num_1>=num3):
    maior = num_1
else:
    if num_2 >= num_3:
        maior = num_2
    else:
        maior = num_3

'''
'''
#Solução 3: Solução semelhante a solução 2 porém com elif e mais organizado.
if (num_1 >= num_2) and (num_1>=num3):
    maior = num_1
elif num_2 >= num_3:
    maior = num_2
else:
    maior = num_3

'''
#Solução 4: Melhor solução entre as anteriores. Estrutura escalável de forma simples, tem o menor tamanho, crescimento menor em relação as soluções anteriores e fácil para colocar um laço.
maior = num_1
if num_2 > maior:
    maior = num_2
if num_3 > maior:
    maior = num_3

'''
#Solução Otimizada para N números: Solução com repetição para n números.
qtd_numeros = int(input('Digite a qtd de números desejados:'))
maior = int(input('Digite o primeiro número:'))

for i in range(1,qtd_numeros):
    valor = int(input('Digite o número {i+1}: '))
    if valor > maior:
        maior = valor

'''

print(f'O maior entre {num_1},{num_2} e {num_3} é {maior}')
