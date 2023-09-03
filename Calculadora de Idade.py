#Não Funcional

print('### BEM VINDO A CALCULADORA DE IDADE ###\n\nvamos começar pedindo algumas informaçoẽs.\n')

m1_12 = (31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)

nome = input('Digite o seu nome: ')

ano1 = int(input('\nDigite o ano atual: '))

print('\nBeleza, agora gostaríamos de saber o dia, mês e ano em que você nasceu:\n')

dia2 = int(input('Digite o dia: '))
while dia2 > 31:
    dia2 = int(input('\nVish, esse número não faz sentido. Digite novamente: \n'))
else:
  pass

print('''\nEscolha o seu mês de nasciemento:


[1] - Janeiro               [7] - Julho

[2] - Fevereiro             [8] - Agosto

[3] - Março                 [9] - Setembro

[4] - Abril                 [10] - Outubro

[5] - Maio                  [11] - Novembro

[6] - Junho                 [12] - Dezembro''')

mes2 = int(input('\nDigite o número correspondente: '))
while mes2 > 12:
  print('\n\n.No máximo são 12 meses.\n\n')
else:
  pass

mes3 = find.(m1_12) #Uia

ano2 = int(input('\nDigite o ano: '))

f1 = (ano1 - ano2 - 1)

diaf = 365 - dia2 + mes3

print(f'Você possui {f1} anos e {diaf} dias.')