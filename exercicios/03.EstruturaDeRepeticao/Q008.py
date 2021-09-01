'''Exercicio 08:
Faça um programa que leia 5 números e informe a soma e a média dos números. 
'''

i = soma = media = 0


while i<5:
    try:
        valor = float(input(f'Informe o número {i}:'))
        soma+=valor
        i+=1
    except:
        print(f'Entre com um valor válido!!')

print(f'A soma é {soma} e a média {(soma/i)}') 