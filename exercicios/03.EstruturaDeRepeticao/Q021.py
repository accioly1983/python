'''Exercício 21:
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1. '''


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
            print(f'{num} NÃO é um número primo!')
        
        break