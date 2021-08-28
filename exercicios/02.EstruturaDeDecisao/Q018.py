'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. '''


data = input('Informe uma data no formato dd/mm/aaaa. ex: 01/01/1950 : ')


if len(data) == 10:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])    

    if (0<dia<=31) and (0<mes<12) and (0<ano<=2021):
        print(f'Data Válida {data}')
    else:
        print(f'Data Inválida {data}')

else:
    print(f'Formato de data informado inválido! ') 
