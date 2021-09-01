'''Exercicio 05:
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação. '''


populacao_a = populacao_b = taxa_populacao_a = taxa_populacao_b = 0

while True:
    try:
     populacao_a = int(input('Informe a quantidade de habitantes iniciais da papulação A:'))
     break
    except:
     print(f'{populacao_a} Valor informado inválido! Informe a quantidade de habitantes iniciais da papulação A:')   


while True:
    try:
     taxa_populacao_a = float(input('Informe a de crescimento da papulação A:'))
     break
    except:
     print(f'{taxa_populacao_a} Valor informado inválido! Informe um valor real para taxa de crescimento da população A!')   


while True:
    try:
     populacao_b = int(input('Informe a quantidade de habitantes iniciais da papulação B:'))
     break
    except:
     print(f'{populacao_b} Valor informado inválido! Informe a quantidade de habitantes iniciais da papulação B!')   


while True:
    try:
     taxa_populacao_b = float(input('Informe a de crescimento da papulação B:'))
     break
    except:
     print(f'{taxa_populacao_b} Valor informado inválido! Informe um valor real para taxa de crescimento da população B!')   


qtd_anos = 0
while populacao_a <populacao_b:
    populacao_a*= ((taxa_populacao_a/100)+1)
    populacao_b*= ((taxa_populacao_b/100)+1)
    qtd_anos+=1


print(f'População A {populacao_a} iguala ou supera população B {populacao_b} em {qtd_anos} anos!')