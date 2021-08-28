'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
    receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
     (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago 
     pelo cliente. '''


valor_pago_morango = valor_pago_maca = 0.0
valor_desconto = 0.0

qtd_kg_morango = float(input('Informe a quantidade de Kg comprados de Morango: '))
qtd_kg_maca = float(input('Informe a quantidade de Kg comprados de Maçã: '))

if qtd_kg_morango <= 5:
    valor_pago_morango = 2.50 * qtd_kg_morango
else:
    valor_pago_morango = 2.20 * qtd_kg_morango

if qtd_kg_maca <= 5:
    valor_pago_maca = 2.50 * qtd_kg_maca
else:
    valor_pago_maca = 2.20 * qtd_kg_maca

if (qtd_kg_morango+qtd_kg_maca)>8 or (valor_pago_morango+valor_pago_maca)>25:
    valor_desconto = 10

print(f'Valor pago por {qtd_kg_morango})kg Morando:R$ {valor_pago_morango}')
print(f'Valor pago por {qtd_kg_maca})kg Maca   : R$ {valor_pago_maca}')
print(f'Valor Total ({valor_desconto}%): R$ {(valor_pago_morango+valor_pago_maca)*((100-valor_desconto)/100)}')