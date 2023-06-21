from random import sample
from time import sleep
jogos = []
palpites = []
num_jogos = int(input('Quantos jogos você quer q eu sorteie?'))
print('GERANDO OS JOGOS...')
sleep(1)
for c in range(0, num_jogos):
    jogo = sample(range(1, 61), 6) #vai gerar 6 numeros aleatórios entre 1 e 60 (o 61 n conta),
    # e os números não se repetem
    jogo.sort()
    palpites.append(jogo)
    jogos.append(palpites[:])
    palpites.clear()
    print(jogos[c])
    sleep(0.5)
