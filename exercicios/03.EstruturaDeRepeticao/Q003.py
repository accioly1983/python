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
       while  idade<=0 or idade>150:
           idade = int(input(f'{idade} Opção Inválida! Informe uma idade entre 0 e 150: '))           
       break
    except ValueError:
       print(f'{idade} Opção Inválida! Informe uma idade entre 0 e 150! ')

while True:
    try:
       salario = float(input('Informe seu salário: '))
       while  salario<=0 :
           salario = float(input(f'{salario} Opção Inválida! Salário tem que ser maior que 0: '))           
       break
    except ValueError:
       print(f'{salario} Opção Inválida! Salário tem que ser maior que 0! ')


while True:
    try:
       sexo = input('Informe seu sexo (M-Masculino, F-Feminino ou I-Indefinido: ')
       while  len(sexo)>2 or sexo not in ('SsMmIi') :
           sexo = input(f'{sexo} Sexo Inválido!Tente novamnete! Informe seu sexo (M-Masculino, F-Feminino ou I-Indefinido: ')
       break
    except ValueError:
       print(f'{sexo} Sexo Inválido!Tente novamnete! Sexo Permitido (M-Masculino, F-Feminino ou I-Indefinido: ')


while True:
    try:
       estado_civil = input('Informe seu estado civil (S-Solteiro(a), C-Casado(a), D-Divorciado(a) ou V-viuvo(a)): ')
       while  len(estado_civil)>2 or estado_civil not in ('SsCcDdVv') :
           estado_civil = input(f'{estado_civil} Sexo Inválido!Tente novamnete! Informe seu estado civil (S-Solteiro(a), C-Casado(a), D-Divorciado(a) ou V-viuvo(a)): ')
       break
    except ValueError:
       print(f'{estado_civil} Sexo Inválido!Tente novamnete! Informe seu estado civil (S-Solteiro(a), C-Casado(a), D-Divorciado(a) ou V-viuvo(a)): ')



print(f'--------------DADOS COLETADOS-------------')
print(f'Nome:{nome}')
print(f'Idade:{idade}')
print(f'Salário:{salario}')
print(f'Sexo:{sexo}')
print(f'Estado Civil:{estado_civil}')
