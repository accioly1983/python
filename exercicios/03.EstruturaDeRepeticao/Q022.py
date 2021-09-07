'''Exercício 22:
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. '''



while True:
    try:
        num = int(input('Informe o número inteiro: '))           
    except:
        print('Opção inválida!! A aplicação espera um número inteiro!')
    else:
        contador = 0
        for x in range(1,num+1):
            if num%x==0:
                contador+=1            
                                         
        if contador ==2:
            print(f'{num} é um número primo!')
        else:     
            print(f'Divisível por: ',end='')
            for x in range(1,num+1):
                if num%x == 0:
                    print(f'[{x}]',end='')
            print(f'\n{num} NÃO é um número primo!',end='\n')  
            break  
       