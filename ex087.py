matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = maiorv2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        if l == 1 and matriz[l][c] > maiorv2l:
            maiorv2l = matriz[l][c]
print('='*30)
print(matriz)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^10}]', end=' ')
    print()
print('='*30)
print(f'Soma dos pares: {somapar} ')
print(f'Soma dos valores da terceira coluna: {soma3}')
print(f'Maior valor da segunda linha: {maiorv2l}')