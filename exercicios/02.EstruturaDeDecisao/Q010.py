'''Exercício 010: Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. '''


turno = input('Informe o turno que estuda (M-Matutino,V-Vespertino ou N-Noturno):')
msg_turno = ''
if turno == 'M':
    msg_turno = 'M - Matutino!'
elif turno == 'V':
    msg_turno = 'V - Vespertino!'
elif turno == 'N':
    msg_turno = 'N - Noturno!'
else:
    msg_turno = 'Valor inválido!'

print(f'O turno informado foi {msg_turno}!')