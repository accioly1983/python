'''Exercicio 01:
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido. '''


#FORMA 00 (Sem usar exceção e sem tratar ValueError)
nota = float(input('Informe uma nota de zero a dez: '))
while  nota<0 or nota>10:
    nota = float(input(f'Nota inválida: {nota}! Informe uma nota de zero a dez: '))           
print(f'Valor válido: {nota}')

#FORMA 01 (tratando ValueError)
while True:
    try:
       nota = float(input('Informe uma nota de zero a dez: '))
       while  nota<0 or nota>10:
           nota = float(input(f'{nota} Opção Inválida! Informe uma nota de zero a dez: '))           
       break
    except ValueError:
       print(f'{nota} Opção Inválida! Informe uma nota entre zero e dez! ')

print(f'Valor válido: {nota}')


#FORMA 02 (tratando ValueError)
while True:
    try:
        nota = float(input('Informe uma nota de zero a dez: '))
    except ValueError:
        print(f'O sistema aceita apenas número inteiros notas entre zero e dez!!')
    else:
        if 0<nota<10:
            print(f'O valor informado {nota}')
            break
        else:
            print(f'O valor informado não esta entre 0 e 10!!')