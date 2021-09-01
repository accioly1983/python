'''Exercicio 07:
Faça um programa que leia 5 números e informe o maior número.'''


i = maior = 0


while i<5:
    try:
        valor = float(input(f'Informe o número {i}:'))
        if valor > maior:
            maior = valor
        i+=1
    except:
        print(f'Entre com um valor válido!!')

print(f'O maior valor foi {maior}') 