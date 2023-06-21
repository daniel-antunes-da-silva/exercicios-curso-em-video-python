import random
from time import sleep
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('O computador já escolheu, e agora, qual a sua?')
jogador = str(input('[PEDRA]'
                    '\n[PAPEL]'
                    '\n[TESOURA]'
                    '\nSua escolha: ')).strip().upper()
print('='*10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('='*10)
print(f'\nComputador escolheu: {computador}')
if computador == jogador:
    print(f'Empate! {computador} vs {jogador}')
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'TESOURA' and jogador == 'PAPEL' or computador == 'PAPEL' and jogador == 'PEDRA':
    print(f'Você perdeu! {computador} ganha de {jogador}.')
else:
    print(f'Você ganhou! {jogador} ganha de {computador}')
