#ESSA FOI MINHA SOLUÇÃO USANDO AJUDA DO CHAT GPT, COM LAMBDA.
from random import randint
from time import sleep
jogadores = {}
print('Valores sorteados: ')
for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)
    #print(f'    Jogador {c} tirou {ranking} '))
for k, v in jogadores.items():
    print(f'{k}: {v}')
    sleep(0.5)
print(f'== {"Ranking Ordenado":~^10} ==')
#print(jogadores)
ordenado = {k: v for k in sorted(jogadores.items(), reverse=True, key=lambda item: item[1])}
#print(ordenado)
for k in ordenado.keys():
    print(f'|   => {k[0]} = {k[1]}  |')
'''for k, v in jogadores.items():
    print(f'{k} = {v}')'''
'''jog_ord = sorted(jogadores.values(), reverse=True)
print(jog_ord)
for v in jog_ord:
    print(v)
#print(jogadores)
'''

'''from random import randint
from time import sleep
ranking = []
jogadores = {}
print('Valores sorteados: ')
for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)
    #print(f'    Jogador {c} tirou {ranking} ')
    ranking.append(jogadores.copy())
    print(jogadores)
    jogadores.clear()
    #sleep(0.5)
print('Ordenado: ')
print()
for c in range(1, 5):
    for r in ranking:
        print(r[c])
print('-' * 20)
#print(jogadores)'''