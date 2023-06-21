pessoas = []
while True:
    pessoa = {}
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Resposta errada!')
    if resp == 'N':
        break
print(pessoas)
print('='*40)
mi = 0
tot_m = ''
print(f'O total de pessoas cadastradas foram: {len(pessoas)}')
for c in pessoas:
    mi += c['Idade'] / len(pessoas)
print(f'A média de idade é {mi} anos')
print('A lista com todas as mulheres é: ', end='')
for c in pessoas:
    if c['Sexo'] == 'F':
        print(c['Nome'], end='; ')
print('A lista com todas as pessoas com a idade acima da média é: ', end='')
for c in pessoas:
    if c['Idade'] > mi: #mi = média de idade
        print(c['Nome'], end='; ')
print()
print('Also can be showed in this manner:')
print('Women list: ')
for c in pessoas:
    if c['Sexo'] == 'F':
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')
    print()
print('People list with above average age: ')
for c in pessoas:
    if c['Idade'] > mi:
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')
    print()
print('FIM')

#print(pessoa)

