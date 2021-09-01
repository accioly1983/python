'''Exercicio 16:
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série 
até que o valor seja maior que 500. '''

n_penultimo = 0
n_ultimo = 1
termo = 3

print(f'Termo 1 = {n_penultimo}')
print(f'Termo 2 = {n_ultimo}')
while n_ultimo <= 500:
    print(f'Termo {termo} = {n_penultimo+n_ultimo} ')
    n_aux = n_ultimo
    n_ultimo = (n_penultimo+n_ultimo)
    n_penultimo = n_aux
    termo+=1 