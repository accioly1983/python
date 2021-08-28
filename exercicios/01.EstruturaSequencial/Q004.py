'''Exercício 04:
Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
nota_1 = float(input('Informe 1 notal bimestral:'))
nota_2 = float(input('Informe 2 notal bimestral:'))
nota_3 = float(input('Informe 3 notal bimestral:'))
nota_4 = float(input('Informe 4 notal bimestral:'))
media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print(f'A média das notas [{nota_1},{nota_2},{nota_3},{nota_4}]. Média igual a {media} ')