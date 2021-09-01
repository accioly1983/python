'''Exercicio 10:
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
compreendido por eles. '''


num_a = num_b =0

while True:
    try:
        num_a = int(input('Informe o primeiro número: '))
        num_b = int(input('Informe o segundo número: '))
        if num_b < num_a:
            num_a,num_b = num_b,num_a
            
        break
    except:
        print(f'Só é permitindo número inteiro!')


for x in range(num_a+1,num_b):
    print(f'{x}',end="|")


