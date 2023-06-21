def contador(inicio, fim, passo):
    print('='*30)
    if passo == 0 and inicio < fim:
        passo = 1
        print('O passo digitado foi 0, portanto, é um valor inválido,'
              ' e o programa funcionará somando 1.')
    elif passo == 0 and inicio > fim:
        passo = -1
        print('O passo digitado foi 0, portanto, é um valor inválido,'
              ' e o programa funcionará subtraindo 1.')
    elif passo < 0:
        passo = -(passo)
    if inicio < fim and passo != 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
    elif inicio > fim and passo < 0:
        print(f'Contagem de {inicio} até {fim} de {-(passo)} em {-(passo)}')
        for c in range(inicio, fim - 1, passo):
            print(c, end=' ')
    elif inicio > fim and passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ')
    print('Fim')
    print('='*30)


contador(1, 10, 1)
contador(10, 0, -1)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
