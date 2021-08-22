'''Faça um Programa que peça um número correspondente a um determinado ano e 
em seguida informe se este ano é ou não bissexto. '''

ano = int(input('Informe o ano com 4 dígitos: '))

if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano%4 == 0) and (ano%100 == 0) and (ano%400 == 0)):
    print(f'O ano informado {ano} é bissexto')
else:
    print(f'O ano informado {ano} não é bissexto') 