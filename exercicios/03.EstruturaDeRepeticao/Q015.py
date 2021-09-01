'''Exercicio 15:
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a 
série até o n−ésimo termo. '''

n_termo = int(input('Informe o n-esimo termo: '))

n_ultimo = n_penultimo = 1

print(f'Termo 1 = {n_penultimo}')
print(f'Termo 2 = {n_ultimo}')
for i in range(2,n_termo+1):
       print(f'Termo {i} = {n_penultimo+n_ultimo}')
       n_aux = n_ultimo
       n_ultimo = (n_penultimo+n_ultimo)
       n_penultimo = n_aux