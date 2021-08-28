'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre 
    a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
    ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
     Caso contrário, ele será classificado como "Inocente". '''


resp_01 = input('Telefonou para a vítima?[S/N] ').upper()
resp_02 = input('Esteve no local do crime?[S/N] ').upper()
resp_03 = input('Mora perto da vítima?[S/N] ').upper()
resp_04 = input('Devia para a vítima?[S/N] ').upper()
resp_05 = input('Já trabalhou com a vítima?[S/N] ').upper()

situacao = ''
if resp_02 == 'S':
    situacao = 'Suspeita'
elif resp_04 == 'S' and resp_05 == 'S':
    situacao = 'Cúmplice'
elif resp_05 == 'S':
    situacao = 'Assassino'
else:
    situacao='Inocente'


print(f'Situação atual do envolvido é {situacao}')

