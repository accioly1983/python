'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um 
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; '''


lado_a =float(input('Informe o tamanho do lado A do Triangulo:'))
lado_b =float(input('Informe o tamanho do lado B do Triangulo:'))
lado_c =float(input('Informe o tamanho do lado C do Triangulo:'))
tipo_triangulo = ''

if lado_a == lado_b == lado_c:
    tipo_triangulo = 'Triângulo Equilátero: três lados iguais;'
elif lado_a != lado_b != lado_c:
    tipo_triangulo = 'Triângulo Escaleno: três lados diferentes;'
    
else:
    tipo_triangulo = 'Triângulo Isósceles: quaisquer dois lados iguais;'


print(f'Lado A - {lado_a}, Lado B - {lado_b}, Lado C - {lado_c}  | {tipo_triangulo}')