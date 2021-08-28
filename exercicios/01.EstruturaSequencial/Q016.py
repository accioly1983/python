'''Exercício 16:
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser 
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
 e o preço total. '''

area = float(input('Informe o tamanho metros quadrados da area a ser pintada: '))
lata_litros = 18
lata_valor = 80.00
qtd_litros = area/3
total_latas = qtd_litros/18
valor_latas = total_latas * lata_valor

print(f'Area {area}')
print(f'Qtd latas {total_latas}')
print(f'Qtd valor {valor_latas}')