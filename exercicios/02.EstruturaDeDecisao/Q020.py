'''Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. '''

nota_1 = float(input('Informe a primeira nota:  '))
nota_2 = float(input('Informe a segunda nota:  '))
nota_3 = float(input('Informe a terceira nota:  '))


media = (nota_1 + nota_2 + nota_3)/3

msg = ''

if media >= 7:
    msg = 'Aprovado'
elif media < 7:
    msg = 'Reprovado'
elif media == 10:
    msg = 'Aprovado com Distinção'

print(f'Aluno com Média: {media} - Situação: {msg}')

