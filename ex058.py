from random import randint
computador = randint(0, 10)
print(computador)
tot_palpites = 1
jogador = int(input('Tente adivinhar o número que pensei, entre 0 e 10: '))
while jogador != computador:
    jogador = int(input('Você errou, tente novamente: '))
    tot_palpites = tot_palpites + 1
print(f'Você venceu! Pensei no número {computador}. Foram necessárias {tot_palpites} tentativas para você vencer!')
