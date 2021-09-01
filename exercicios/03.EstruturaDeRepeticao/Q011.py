'''Exercicio 11:
Altere o programa anterior para mostrar no final a soma dos números. '''

num_a = num_b =0

while True:
    try:
        num_a = int(input('Informe o primeiro número: '))
        num_b = int(input('Informe o segundo número: '))
        if num_b < num_a:
            num_a,num_b = num_b,num_a
            
        break
    except:
        print(f'Só é permitindo número inteiro!')

soma = 0 
for x in range(num_a+1,num_b):
    print(f'{x}',end="|")
    soma+=x

print(f'>> Soma: {soma}')