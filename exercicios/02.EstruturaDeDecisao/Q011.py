'''Exercício 012: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado 
    no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. '''


salario_atual = float(input('Informe o seu salario atual: '))

salario_novo = 0.0
percentual_aumento = 0.0
if salario_atual <= 280.00:
    percentual_aumento=20
elif salario_atual > 280.00 and salario_atual < 700.00:
    percentual_aumento=15
elif salario_atual > 700.00 and salario_atual < 1500.00:
    percentual_aumento=10
elif salario_atual > 1500.00:
    percentual_aumento=5

print(f'+ Salario atual antes do reajuste: {salario_atual}')
print(f'+ Percentual de aumento: {percentual_aumento}')
print(f'+ Valor do aumento : {salario_atual*(percentual_aumento/100)}')
print(f'+ Novo salario : {salario_atual*(percentual_aumento/100+1)}')
