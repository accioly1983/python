'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
     ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é 
     R$ 1,90. '''

qtd_litros_vendido = float(input('Informe a quantidade de litros vendidos: '))
tipo_de_combustivel = input('Informe o tipo de combustivel (A - álcool e G - gasolina): ').upper()

valor_alcool = 1.90
valor_gasolina = 2.50
valor_desconto = 0.0

valor_pago = 0.0

if tipo_de_combustivel == 'A':
    if qtd_litros_vendido <= 20:
        valor_desconto = 3
    else:
        valor_desconto = 5
    
    valor_pago = (qtd_litros_vendido/valor_alcool)*((100-valor_desconto) / 100)
elif tipo_de_combustivel == 'G':
    if qtd_litros_vendido <= 20:
        valor_desconto = 4
    else:
        valor_desconto = 6
    
    valor_pago = (qtd_litros_vendido/valor_gasolina)*((100-valor_desconto) / 100)

print(f'Quantidade de em litros: {qtd_litros_vendido}')
print(f'Tipo de combustivel    : {tipo_de_combustivel}')
print(f'Valor pago pelo cliente (Desconto:{valor_desconto}): R$ {valor_pago}')