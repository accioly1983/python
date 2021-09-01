'''Exercicio 06
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro. '''
print('-'*50)
print(f'-----VERTICAL-----')
#print vertical
for x in range(1,20):
    print(f'{x}')

print('-'*50)
print(f'-----HORIZONTAL-----')
#print horizontal
for x in range(1,20):
    print(f'{x} ',end='')