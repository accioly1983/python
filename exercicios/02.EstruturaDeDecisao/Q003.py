''' Exercício 03: Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. '''

entrada = input('informe uma letra:')

letra = entrada[:1]

if letra == 'F':
    print(f'F - Feminino -> {letra}')
elif letra == 'M':
    print(f'M - Masculino -> {letra}')
else:
    print(f'Invalido! -> {letra}')