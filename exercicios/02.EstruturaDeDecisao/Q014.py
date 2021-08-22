'''Exercício 014: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o 
    conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. '''

  
nota_1 = float(input('Informe a nota 1:'))
nota_2 = float(input('Informe a nota 2:'))
media = (nota_1+nota_2)/2
conceito = ''
situacao= ''
if media > 9.0 and media <=10:
  situacao = 'APROVADO'
  conceito = 'Entre 9.0 e 10.0        A'
elif  media > 7.5 and media <=9.0:
  situacao = 'APROVADO'
  conceito = 'Entre 7.5 e 9.0         B'
elif  media > 6.0 and media <=7.5:
  situacao = 'APROVADO'
  conceito = 'Entre 6.0 e 7.5         C'
elif  media > 4.0 and media <=6.0:
  situacao = 'REPROVADO'
  conceito = 'Entre 4.0 e 6.0         D'
elif  media >= 0.0 and media <=4.0:
  situacao = 'REPROVADO'
  conceito = 'Entre 4.0 e zero        E'
else:
  situacao = 'Inválida!'
  conceito = 'Indeterminado'


print(f'Notas: {nota_1} e {nota_2}. Média {media}. Situação {situacao} do aluno. Conceito {conceito}')
