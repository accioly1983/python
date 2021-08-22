'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos 
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para
o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a
empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
    dispostas conforme o exemplo abaixo. 
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00'''


valor_hora_trabalhada = float(input('Informe quanto você recebe por hora trabalhada: '))
carga_horaria_trabalhada = float(input('Informe a quantidade de horas trabalhada no mês: '))

salario_bruto_mensal = valor_hora_trabalhada * carga_horaria_trabalhada

percentual_fgts = 11
percentual_inss = 10 
percentual_sindicado = 3
percentual_ir = 0

if salario_bruto_mensal > 2500.00:
    percentual_ir = 20
elif 1500 < salario_bruto_mensal <= 2500:
    percentual_ir = 10
elif 900< salario_bruto_mensal <=1500:
    percentual_ir = 5
else:
    percentual_ir = 0


print('Cálculo Salarial (SEM DESCONTO SINDICATO)')
print('-----------------------------------------')

print(f'Salario Bruto:({valor_hora_trabalhada} * {carga_horaria_trabalhada})       : R$ {salario_bruto_mensal}')
print(f'(-) IR (5%)                       : R$ {salario_bruto_mensal * (percentual_ir/100)}')
print(f'(-) INSS (10%)                    : R$ {salario_bruto_mensal * (percentual_inss/100)}')
print(f'FGTS (11%)                        : R$ {salario_bruto_mensal * (percentual_fgts/100)}')
print(f'Total de descontos                : R$ {salario_bruto_mensal * ((percentual_ir + percentual_inss)/100)}')
print(f'Salario líquido                   : R$ {salario_bruto_mensal * (( (100 - (percentual_ir + percentual_inss + percentual_fgts)+ percentual_fgts )/100))}')


print ('')
print('Cálculo Salarial (COM DESCONTO SINDICATO)')
print('-----------------------------------------')

print(f'Salario Bruto:({valor_hora_trabalhada} * {carga_horaria_trabalhada})       : R$ {salario_bruto_mensal}')
print(f'(-) Sindicado (3%)                : R$ {salario_bruto_mensal * (percentual_sindicado/100)}')
print(f'(-) IR (5%)                       : R$ {salario_bruto_mensal * (percentual_ir/100)}')
print(f'(-) INSS (10%)                    : R$ {salario_bruto_mensal * (percentual_inss/100)}')
print(f'FGTS (11%)                        : R$ {salario_bruto_mensal * (percentual_fgts/100)}')
print(f'Total de descontos                : R$ {salario_bruto_mensal * ((percentual_ir + percentual_inss)/100)}')
print(f'Salario líquido                   : R$ {salario_bruto_mensal * (( (100 - (percentual_ir + percentual_sindicado + percentual_inss + percentual_fgts)+ percentual_fgts )/100))}')
