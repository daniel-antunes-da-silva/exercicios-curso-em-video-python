#ESSE PROGRAMA FOI FEITO DE UM JEITO BURRO. O JEITO DO GUANABARA É MELHORR
matriz = [[], [], []]
for c in range(0, 1):
    for x in range(0, 3):
        n = int(input(f'Digite um número para a posição {0, x}: '))
        matriz[0].append(n)
    for y in range(0, 3):
        n = int(input(f'Digite um número para a posição {1, y}: '))
        matriz[1].append(n)
    for z in range(0, 3):
        n = int(input(f'Digite um número para a posição {2, z}: '))
        matriz[2].append(n)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('='*20)
print(f'[ {matriz[0][0]:^2} ] [ {matriz[0][1]:^2} ] [ {matriz[0][2]:^2} ]')
print(f'[ {matriz[1][0]:^2} ] [ {matriz[1][1]:^2} ] [ {matriz[1][2]:^2} ]')
print(f'[ {matriz[2][0]:^2} ] [ {matriz[2][1]:^2} ] [ {matriz[2][2]:^2} ]')

