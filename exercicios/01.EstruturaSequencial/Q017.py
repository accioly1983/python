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

ex17_area = float(
    input('Informe o tamanho metros quadrados da area a ser pintada: '))
ex17_qtd_litros = (ex17_area/6)*1.10
ex17_total_latas_18litros = math.ceil(ex17_qtd_litros/18)
ex17_total_galoes_3_6litros = math.ceil(ex17_qtd_litros/3.6)

# Otimizado
ex17_total_latas_18litros_otimizado = math.floor(ex17_qtd_litros/18)
ex17_total_litros_restantes = ex17_qtd_litros % 18
ex17_total_galoes_3_6litros_otimizado = math.ceil(
ex17_total_litros_restantes/3.6)


print(f'Area {ex17_area}')
print(
    f'comprar apenas latas de 18 litros: {ex17_total_latas_18litros} -- Valor {ex17_total_latas_18litros*80.00}')
print(
    f'comprar apenas galões de 3,6 litros: {ex17_total_galoes_3_6litros} -- Valor{ex17_total_galoes_3_6litros*25.00} ')
print(f'lata(s) {ex17_total_latas_18litros_otimizado} de 18 litro(s) e {ex17_total_galoes_3_6litros_otimizado} gal(ão|ões) de 3,6 litros. -- Valor {((ex17_total_latas_18litros_otimizado*80.00)+(ex17_total_galoes_3_6litros_otimizado*25.00))} ')
