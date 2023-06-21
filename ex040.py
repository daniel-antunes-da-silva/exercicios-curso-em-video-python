cores = {'limpa': '\033[m',
         'verde_negrito': '\033[1;32m',
         'vermelho_negrito': '\033[1;31m',
         'branco_negrito': '\033[1;97m',
         'azul_negrito': '\033[1;34m',
         'amarelo_negrito': '\033[1;33m'}
n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
m = (n1 + n2) / 2
if (n1 and n2 >= 0) and (n1 and n2 <= 10):
    if 5 > m >= 0:
        print('Você está reprovado, média:', cores['vermelho_negrito'], f'{m:.2f}', cores['limpa'])
    elif 5 <= m < 7:
        print('Você está em recuperação, média: ', cores['amarelo_negrito'], f'{m:.2f}', cores['limpa'])
    elif 7 <= m <= 10:
        print('Parabéns!! Você está aprovado com média: ', cores['verde_negrito'], f'{m:.2f}', cores['limpa'])
    else:
        print('Algo está errado, digite novamente os valores, por favor!')
else:
    print('Algo está errado com as notas... Revise os valores, por favor!')