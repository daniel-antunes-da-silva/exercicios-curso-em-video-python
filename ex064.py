from time import sleep
n = tot_n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s = s + n
        tot_n = tot_n + 1
    else:
        print('Programa encerrando...')
        sleep(1)
print(f'O total de números digitados foi {tot_n}')
print(f'A soma entre eles foi {s}')
