from time import sleep
def maior(*v):
    print('=' * 40)
    print('Analisando os dados_cadastrados informados...')
    maior_num = cont = 0
    for m in v:
        if cont == 0:
            maior_num = m
        elif m > maior_num:
            maior_num = m
        print(m, end='; ')
        sleep(0)
        cont += 1
    print(f'-> Fora informados {len(v)} valores ao todo.')
    print(f'O maior número é {maior_num}')
    print()


maior(2, 5, 9)
maior(6)
maior(10, 3, 11)
maior()
maior(1, 2)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
