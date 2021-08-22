'''Exercício 02: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''

valor = float(input('Informe um valor: '))

msg = ''
if valor > 0:
    msg = 'Valor positivo'
elif valor<0:
    msg = 'Valor Negativo'
else:
    msg = 'Valor Neutro'

print(f'{msg} - {valor}')