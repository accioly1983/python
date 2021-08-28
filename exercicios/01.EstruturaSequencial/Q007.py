'''Exercício 07:
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. '''
pi = 3.1415
quadrado = float(input('Informe lado do quadrado:'))
area = quadrado ** 2
dobro = 2 * area
print(f'Quadrado com lado de {quadrado} possui área {area} e o dobro da área é {area}')