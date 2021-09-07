'''Exercicio 08:
Faça um programa que leia 5 números e informe a soma e a média dos números. 
'''


#FORMA 00
i = soma = media = 0


while i<5:
    try:
        valor = float(input(f'Informe o número {i}:'))
        soma+=valor
        i+=1
    except:
        print(f'Entre com um valor válido!!')

print(f'A soma é {soma} e a média {(soma/i)}') 


#FORMA 01

valor =soma = media = 0
for x in range(1,6):
    valor = float(input(f'Informe o número {x}: '))
    soma+=valor
    media = soma/x
    print(f'Soma {soma} - Media {media}')

print(f'Soma {soma} Media {soma/5}')