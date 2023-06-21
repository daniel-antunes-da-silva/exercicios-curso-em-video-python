# Sorteador de números para mega sena, em ordem crescente.
from time import sleep
from random import randint
total_jogos = []
palpites = []
jogos = int(input('Quantos jogos quer fazer? '))
print('Sorteando números...')
for c in range(0, jogos):
    #Enquanto o valor a (aleatório) não estiver na lista PALPITES, vai continuar adicionando até chegar no tamanho 6.
    while True:
        a = randint(1, 60)
        if a not in palpites:
            palpites.append(a)
        if len(palpites) == 6:
            break
    total_jogos.append(palpites[:])
    palpites.clear()
#print(total_jogos)
for pos, j in enumerate(total_jogos):
    sleep(0.5)
    j.sort()
    print(f'Jogo {pos + 1}: {j}')