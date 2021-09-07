'''Exercicio 07:
Faça um programa que leia 5 números e informe o maior número.'''



#FORMA 00

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

#FORMA 01

maior = -1
for _ in range(5):
    maior = max(maior,float(input('Informe um número: ')))
    print(f'O valor máxímo é {maior}')