'''Exercicio 03:
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''

nome = sexo = estado_civil = ''
idade = 0
salario = 0.0


nome = input('Informe seu nome:')
while len(nome) < 3:
    print(f'Nome inválido! Nome tem que ser maior que 3 caracteres!')
    nome = input('Informe seu nome:')

while True:
    try:
       idade = int(input('Informe uma idade entre 0 e 150: '))
    except ValueError:
       print(f'Caro usuário entrar com um valor inteiro entre 0 e 150! ')
    else:
        if not (0<idade<150):
            print(f'Idade Inválida {idade}! Informe uma idade entre 0 e 150: ')
        else:
            break

while True:
    try:
       salario = float(input('Informe seu salário: '))     
    except ValueError:
       print(f'Caro usuário o valor informado deve ser um número real maior que 0: ')
    else:
        if not (salario>0):
            print(f'Salário Inválido: R$ {salario} ! O salário tem que ser maior que 0! ')
        else:
            break




while True:
    try:
       sexo = input('Informe seu sexo (M-Masculino, F-Feminino ou I-Indefinido): ')
    finally:
        if len(sexo)>2 or sexo not in ('SsMmIi'):
            print(f'Sexo Inválido!Tente novamnete! Caro usário vc informar uma das opções a seguir (M-Masculino, F-Feminino ou I-Indefinido) ')       
        else:
            break


while True:
    try:
       estado_civil = input('Informe seu estado civil (S-Solteiro(a), C-Casado(a), D-Divorciado(a) ou V-viuvo(a)): ')       
    finally:
       if len(estado_civil)>2 or estado_civil not in ('SsCcDdVv'):
           print(f'Sexo informado é inválido: {estado_civil} ! Tente novamnete!')
       else:
           break

print(f'--------------DADOS COLETADOS-------------')
print(f'Nome:{nome}')
print(f'Idade:{idade}')
print(f'Salário:{salario}')
print(f'Sexo:{sexo}')
print(f'Estado Civil:{estado_civil}')
