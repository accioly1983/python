'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer 
    pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário'''


import math

print(f'Expressao na forma ax2 + bx + c:')
a = float(input('Valor da variavel a:'))
if a == 0:
    print(f'A Equação não é do segundo grau! Tchau')
    exit(1)
else:
    b = float(input('Valor da variavel b:'))
    c = float(input('Valor da variavel c:'))
    delta = (b**2) - 4*a*c

    if delta == 0:
        print(f'Delta {delta} = 0 -A equação possui apenas uma raiz real;')
    elif delta > 0:
        print(f'Delta {delta} > 0 - A equação possui duas raizes reais;')
    else:
        print(f'Delta {delta} < 0 - A equação não possui raizes reais;')
