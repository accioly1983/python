'''Exercicio 13:
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem. '''


base = expoente = 0
while True:
    try:
        base = int(input('Informe o número da base: '))
        break
    except:
        print(f'Pemitido apenas número inteiro!')


while True:
    try:
        expoente = int(input('Informe o número do expoente: '))
        break
    except:
        print(f'Pemitido apenas número inteiro!')

print(f'Base: {base} Expoente:{expoente} >> Resultado: {(base**expoente)} ')