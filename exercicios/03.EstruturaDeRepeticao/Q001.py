'''Exercicio 01:
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido. '''

nota = 0

while True:
    try:
       nota = float(input('Informe uma nota de zero a dez: '))
       while  nota<0 or nota>10:
           nota = float(input(f'{nota} Opção Inválida! Informe uma nota de zero a dez: '))           
       break
    except ValueError:
       print(f'{nota} Opção Inválida! Informe uma nota entre zero e dez! ')

print(f'Valor válido: {nota}')