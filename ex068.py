from random import randint
print('=-='*10)
print('Vamos jogar par ou ímpar')
print('=-='*10)
tot_win = 0
while True:
    computador = randint(0, 10)
    n = int(input('Digite um valor: '))
    escolha_jogador = str(input('Par ou ímpar? [P / I]: ')).upper()
    resultado = n + computador
    if resultado % 2 == 0:
        print(f'Você jogou {n} e o computador {computador}. Resultado deu {resultado}, que é PAR. ', end='')
        if escolha_jogador == 'P':
            print('Por isso, você venceu!')
            tot_win = tot_win + 1
        else:
            print('Por isso, você perdeu!')
            break
    else:
        print(f'Você jogou {n} e o computador jogou {computador}. Resultado deu {resultado}, que é ÍMPAR. ', end='')
        if escolha_jogador == 'I':
            print('Por isso, você venceu!')
            tot_win += 1
        else:
            print('Por isso, você perdeu!')
            break
    print('-----'*5)
print('____'*10)
print(f'O total de vezes que você ganhou foi {tot_win}!')
