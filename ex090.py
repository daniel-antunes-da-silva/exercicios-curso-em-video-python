#REFAZENDO
aluno = {}
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')





'''ficha_do_aluno = []
dados_cadastrados = {}
dados_cadastrados['Nome'] = str(input('Nome do aluno: ')).capitalize()
dados_cadastrados['Média'] = float(input('Média do aluno: '))
if dados_cadastrados['média'] >= 7:
    dados_cadastrados['status'] = 'Aprovado'
else:
    dados_cadastrados['status'] = 'Reprovado'
ficha_do_aluno.append(dados_cadastrados.copy())
print(ficha_do_aluno)
for k, v in dados_cadastrados.items():
    print(f'{k} é igual a {v}')
print('FIM')'''