from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
cadastro['Idade'] = ano_atual - ano_nasc
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
while cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    aposentadoria = cadastro['Ano de contratação'] - ano_nasc + 35 #idade que a pessoa vai se aposentar
    cadastro['Aposentadoria'] = aposentadoria
    break
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} é igual a {v}')
print('FIM')
