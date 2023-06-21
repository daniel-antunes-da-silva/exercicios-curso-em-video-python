from random import randint
def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os números gerados aleatoriamente foram: {lista}')


def somapar():
    sp = 0
    print('Os valores pares foram: ', end='')
    for v in aleatorios:
        if v % 2 == 0:
            print(v, end='; ')
            sp += v
    print(f'-> A soma entre eles é {sp}.')


aleatorios = []
sorteia(aleatorios)
somapar()
