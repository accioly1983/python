'''Exercício 08:
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês. '''

valor_hora = float(input('Informe seu valor por hora:'))
horas_trabalhadas = float(input('Informe quantidade de horas trabalhas no mês:'))
salario = horas_trabalhadas * valor_hora
print(f'Hora: R${valor_hora}\nQtd(h):{horas_trabalhadas}\nSalario: R${salario}')