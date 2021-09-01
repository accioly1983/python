'''Exercicio 17:
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 '''



n_fatorial  = 0
n_fatorial_total = 1
while True:
    try:
        n_fatorial = int(input('Informe o número inteiro para calcular o fatorial: '))
        break
    except:
        print('Opção inválida!! A aplicação espera um número inteiro!')

print(f'Fatorial {n_fatorial}! = ',end='')
for x in range(n_fatorial,1,-1):
    print(f'{x}.',end='')
    n_fatorial_total*=x

print(f'1={n_fatorial_total}')