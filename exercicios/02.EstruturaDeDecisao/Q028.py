'''    O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

        Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
        porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
        cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
        e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da 
        compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 

'''

#Cliente APENAS 1 tipo de carne
#Cartão Tabajara DESCONT 5% sobre o total da compra





#ENTRADAS
# Tipo de Carne
# Qtd Carne
tipo_carne = int(input('Informe o Tipo da Carne (1-File Duplo, 2-Alcatra, 3-Picana: '))
while tipo_carne not in (1,2,3):
        tipo_carne = int(input(f'Opção inválida -> {tipo_carne} !!. Informe o Tipo da Carne (1-File Duplo, 2-Alcatra, 3-Picana: '))


peso_carne = float(input('Informe quanto de carne foi comprado (Kg):'))
tipo_pagamento = int(input('Informe o método de pagamento (1 - Dinheiro, 2- Cartão Tabajara(5%):'))

valor_total = desconto = 0
nome_carne = ''
if tipo_carne==1 and peso_carne<=5:
    valor_total = peso_carne * 4.90
    nome_carne = '1-File Duplo'
elif tipo_carne==1 and peso_carne>5:
    nome_carne = '1-File Duplo'
    valor_total = peso_carne * 5.80

if tipo_carne==2 and peso_carne<=5:
    nome_carne = '2-Alcatra'
    valor_total = peso_carne * 5.90
elif tipo_carne==2 and peso_carne>5:
    nome_carne = '2-Alcatra'
    valor_total = peso_carne * 6.80

if tipo_carne==3 and peso_carne<=5:
    nome_carne = '3-Picanha'
    valor_total = peso_carne * 6.90
elif tipo_carne==3 and peso_carne>5:
    nome_carne = '3-Picanha'
    valor_total = peso_carne * 7.80

if tipo_pagamento == 2:
        tipo_pagamento = '2-Cartão'
        desconto = valor_total*0.05
else:
        tipo_pagamento = '1-Dinheiro'


#SAIDA
# GERAR CUPOM FISCAL (Tipo, Qtd Carne Kg, Preço Total, Tipo de Pagamento, Valor do Desconto e Valor a Pagar)

print(f'---Cupom Fiscal--------------')
print(f'Tipo          : {nome_carne}')
print(f'Qtd Carne (kg): {peso_carne}')
print(f'Tipo Pagamento: {tipo_pagamento}')
print(' Valor desconto: %.2f'%(desconto))
print(f'Valor total   : {valor_total-desconto}')
