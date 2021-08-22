'''Exercício 013: Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dia_semana = int(input('Informe um número:'))

dia = ''
if dia_semana == 1:
    dia = '1-Domingo'
elif dia_semana == 2:
    dia = '2-Segunda-feira'
elif dia_semana == 3:
    dia = '3-Terça-feira'
elif dia_semana == 4:
    dia = '4-Quarta-feira'
elif dia_semana == 5:
    dia = '5-Quinta-feira'
elif dia_semana == 6:
    dia = '6-Sexta-feira'
elif dia_semana == 7:
    dia = '7-Sabado'
else:
    dia = 'Valor inválido!!'

print(f'Você digitou {dia_semana} corresponde a {dia}')
