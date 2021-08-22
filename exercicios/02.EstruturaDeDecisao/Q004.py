'''Exercício 04: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

entrada = input('Informe uma letra: ')

letra = entrada[0:1]

if letra in 'aeiou':
    print(f'Vogal - {letra}')
elif letra in 'bcdfghjklmnpqrstvxzw':
    print(f'Consoante - {letra}')
else:
    print(f'Caracter Inválido - {letra}')