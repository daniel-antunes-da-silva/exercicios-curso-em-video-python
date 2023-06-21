def ficha(name='desconhecido', goals=0):
    if name == '' or name.isnumeric():
        name = 'desconhecido'
    return f'O jogador {name} fez {goals} gols no campeonato.'


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantos gols? ')).strip()
if gols.isnumeric():
    gols = int(gols)
elif gols == '':
    gols = 0
else:
    gols = int(gols == 0)
print(ficha(nome, gols))
