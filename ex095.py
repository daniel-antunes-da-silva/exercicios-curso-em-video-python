jogadores = []
aproveitamento = {}
gols = []
tot_gol = 0
gpp = []
while True:
    aproveitamento['Nome'] = str(input('Nome do jogador: ')).title()
    total_partidas = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
    for c in range(0, total_partidas):
        gpp = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gpp)
    for g in gols:
        tot_gol += g
    aproveitamento['Gols'] = gols[:]
    aproveitamento['Total de gols'] = tot_gol
    jogadores.append(aproveitamento.copy())
    tot_gol = 0
    verify = str(input('Do you want to continue? [Y/N]')).upper()[0]
    if verify in 'Nn':
        break
    elif verify in 'Yy':
        gols.clear()
    else:
        print('Wrong Answer. ', end='')
        verify = str(input('Do you want to continue? [Y/N]')).upper()[0]
print('=' * 30)
print(jogadores)
print('=='*30)
print('cod nome          gols          total')
for p, c in enumerate(jogadores):
    print(p, end=' ')
    for v in c.values():
        print(f'{v}', end=' ')
    print()
print('=='*30)
while True:
    escolha = int(input('Quer mostrar dados_cadastrados de qual jogador? Escolha um número. (999 para interromper): '))
    if escolha == 999:
        break
    print(f'Levantamento do jogador {jogadores[escolha]["Nome"]}')
    for p, c in enumerate(jogadores[escolha]['Gols']):
        print(f'  => No {p+1}º jogo fez {c} gols')


'''print(f'O jogador {aproveitamento["Nome"]} jogou {total_partidas} partidas.')
for p, g in enumerate(aproveitamento['Gols']):
    print(f'   => Na partida {p}, fez {g} gols.')'''
