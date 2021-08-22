'''Exercício 05:
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. '''

nota_1 = float(input('Informe a nota 1:'))
nota_2 = float(input('Informe a nota 2:'))

media = (nota_1+nota_2)/2

msg = ''
if media == 10:
    msg = 'Aprovado com Distinção'
elif media < 7:
    msg = 'Reprovado'
elif media > 7:
    msg = 'Aprovado'

print(f' {msg} - Notas {nota_1} e {nota_2} - Media:{media}')