'''Exercício 008: Faça um programa que pergunte o preço de três produtos 
e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''

produto_1 = float(input('Informe quanto custa o 1 produto: '))
produto_2 = float(input('Informe quanto custa o 2 produto: '))
produto_3 = float(input('Informe quanto custa o 3 produto: '))

menor = 0
if produto_1 < produto_2 and produto_1 < produto_3:
    menor = produto_1
elif produto_2 < produto_3:
    menor = produto_2
else:
    menor = produto_3

print(f'Comprar o produto (P1={produto_1},P2={produto_2}, P3={produto_3}) com o menor valor {menor}')