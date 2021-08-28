'''Exercício 15:

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
 
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
 
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Informe o valor por hora trabalhada:'))
qtd_horas = float(input('Informe a quantidade de horas trabalhadas: '))
sal_bruto = valor_hora * qtd_horas
sal_desconto_ir = sal_bruto * 0.11
sal_desconto_inss = (sal_bruto - sal_desconto_ir) * 0.08
sal_desconto_sindicado = (sal_bruto-sal_desconto_ir-sal_desconto_inss)*0.05
salario_liquido = sal_bruto - sal_desconto_ir - sal_desconto_inss - sal_desconto_sindicado
print(f'+ Salario Bruto: R$ {sal_bruto}')
print(f'- IR (11%): R$ {sal_desconto_ir}')
print(f'- INSS (8%): R$ {sal_desconto_inss}')
print(f'- Sindicato (5%): R$ {sal_desconto_sindicado}')
print(f'= Salario Liquido: R$ {salario_liquido}')