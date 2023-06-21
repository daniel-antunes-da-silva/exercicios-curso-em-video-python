aproveitamento = {}
gols = []
tot_gol = 0
aproveitamento['Nome'] = str(input('Nome do jogador: ')).title()
total_partidas = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
for c in range(0, total_partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
for g in gols:
    tot_gol += g
aproveitamento['Gols'] = gols
aproveitamento['Total de gols'] = tot_gol
print('=' * 30)
print(aproveitamento)
print('=' * 30)
#print(tot_gol)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jogador {aproveitamento["Nome"]} jogou {total_partidas} partidas.')
for p, g in enumerate(aproveitamento['Gols']):
    print(f'   => Na partida {p}, fez {g} gols.')


#Fiz simples demais, não era pra ser assim.
'''aproveitamento = {}
aproveitamento['Nome'] = str(input('Nome do jogador: ')).title()
aproveitamento['Quantidade de partidas'] = int(input('Quantas partidas ele jogou? '))
aproveitamento['Gols por partida'] = float(input(f'Quantos gols o {aproveitamento["Nome"]} fez em cada partida?'))
aproveitamento['Total de gols'] = aproveitamento['Gols por partida'] * aproveitamento['Quantidade de partidas']
print('=' * 30)
print('Aproveitamento do Jogador')
print('=' * 30)
for k, v in aproveitamento.items():
    print(f'{k} é igual a {v}')
'''