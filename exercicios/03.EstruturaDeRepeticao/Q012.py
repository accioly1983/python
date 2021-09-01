'''Exercicio 12:
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50'''
tabuada = 0

while True:
    try:
        tabuada = int(input('Informe o número da tabuada: '))
        break
    except:
        print(f'Só é permitido números inteiros!')


print(f'Tabuada de {tabuada}')
for i in range(0,11):
    print(f'{tabuada} X {i} = {(tabuada*i)}')