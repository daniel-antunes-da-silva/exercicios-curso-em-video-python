from datetime import date
ano = int(input('Digite o ano que quer analisar! Caso queira o ano atual, digite 0 '))
if ano == 0:
    ano = date.today().year #pega o ano atual do sistema, da biblioteca datetime (date)
if ano % 4 == 0 and ano % 100 != 0 :
    print(f'Ano bissexto {ano}')
else:
    print(f'Ano não bissexto {ano}')



'''ano = int(input('Em que ano estamos? '))
if ano % 4 == 0:
    if ano % 400 == 0:
        print(f'O ano de {ano} é bissexto.')
    else:
        print(f'O ano de {ano} não é bissexto1')
else:
    print(f'{ano} não é um ano bissexto2.')
'''