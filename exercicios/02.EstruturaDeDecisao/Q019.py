'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
 dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 
    311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''

numero = int(input("Informe um valor menor que 1000: "))

msg = 'Valor 0 não possui centenas, dezenas ou unidades'

if numero != 0:

    centenas_int, numero = divmod(numero,100)
    dezenas_int, numero = divmod(numero,10)
    unidades_int = numero

    if centenas_int==1:
        msg = str(centenas_int) + ' centena,'
    elif centenas_int > 1:
        msg = str(centenas_int) + ' centenas,'

    if dezenas_int==1:
        msg += str(dezenas_int) + ' dezena e '
    elif dezenas_int > 1:
        msg += str(dezenas_int) + ' dezenas e '

    if unidades_int==1:
        msg += str(unidades_int) + ' unidade.'
    elif dezenas_int > 1:
        msg += str(unidades_int) + ' unidades.'


print(f'{msg}')