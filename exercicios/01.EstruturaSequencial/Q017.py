'''Exercício 17:
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser 
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R80,00ouemgalõesde3,6litros,quecustamR 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias. '''

import math

area = float(
    input('Informe o tamanho metros quadrados da area a ser pintada: '))
qtd_litros = (area/6)*1.10
total_latas_18litros = math.ceil(qtd_litros/18)
total_galoes_3_6litros = math.ceil(qtd_litros/3.6)

# Otimizado
total_latas_18litros_otimizado = math.floor(qtd_litros/18)
total_litros_restantes = qtd_litros % 18
total_galoes_3_6litros_otimizado = math.ceil(
total_litros_restantes/3.6)


print(f'Area {area}')
print(
    f'comprar apenas latas de 18 litros: {total_latas_18litros} -- Valor {total_latas_18litros*80.00}')
print(
    f'comprar apenas galões de 3,6 litros: {total_galoes_3_6litros} -- Valor{total_galoes_3_6litros*25.00} ')
print(f'lata(s) {total_latas_18litros_otimizado} de 18 litro(s) e {total_galoes_3_6litros_otimizado} gal(ão|ões) de 3,6 litros. -- Valor {((total_latas_18litros_otimizado*80.00)+(total_galoes_3_6litros_otimizado*25.00))} ')
