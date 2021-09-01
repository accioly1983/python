'''Exercicio 02:
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''

nome = input('Informe seu nome:')
senha = input('informe uma senha:')

nome_caps = nome
senha_caps = senha

while nome_caps.upper() == senha_caps.upper():
    print(f'Caro usuário a senha não pode ser igual ao seu nome:')
    senha_caps = senha = input('informe uma senha:')
    senha_caps.upper()

print(f'Usuário:{nome}')
print(f'Senha  :{senha}')