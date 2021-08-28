'''Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 
    e quatro notas de 1. '''

valor_saque = float(input('Informe o valor do saque (valor máximo R$ 600.00): '))
if 10<valor_saque<=600:
    qtd_notas_1 = qtd_notas_5 = qtd_notas_10 = qtd_notas_50 = qtd_notas_100 = 0

    qtd_notas_100, valor_saque = divmod(valor_saque,100)
    qtd_notas_50, valor_saque = divmod(valor_saque,50)
    qtd_notas_10, valor_saque = divmod(valor_saque,10)
    qtd_notas_5, valor_saque = divmod(valor_saque,5)
    qtd_notas_1 = valor_saque

    print(f'Valor do Saque R$ {valor_saque}')
    print(f'-------------------------------')
    if qtd_notas_100>0:
        print(f'Notas de R$ 100 reais:{qtd_notas_100}')
    if qtd_notas_50>0:
        print(f'Notas de R$ 50  reais:{qtd_notas_50}')
    if qtd_notas_10>0:
        print(f'Notas de R$ 10  reais:{qtd_notas_10}')
    if qtd_notas_5>0:    
        print(f'Notas de R$ 5   reais:{qtd_notas_5}')
    if qtd_notas_1>0:    
        print(f'Notas de R$ 1   real :{qtd_notas_1}')
else:
    print(f'Valor Permitido! mínimo de R$ 10,00 e valor máximo de R$ 600,00')