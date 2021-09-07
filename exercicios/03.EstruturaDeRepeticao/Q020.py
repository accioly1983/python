'''Exercício 20:
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a 
números inteiros positivos e menores que 16. '''

n_fatorial  = 0
n_fatorial_total = 1
while True:
    try:
        n_fatorial = int(input('Informe o número inteiro para calcular o fatorial (Fatorial máximo até 16)(0 - PARAR): '))           
    except:
        print('Opção inválida!! A aplicação espera um número inteiro!')
    else:
        if n_fatorial>16:
            print(f'Caro usuário o fatorial deve ser menor que 16.')
        elif 0<n_fatorial<16:
            print(f'Fatorial {n_fatorial}! = ',end='')
            for x in range(n_fatorial,1,-1):
                print(f'{x}.',end='')
                n_fatorial_total*=x

            print(f'1={n_fatorial_total}')
            
        elif n_fatorial == 0:
            break
            

