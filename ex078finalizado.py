valores = []
posicao_maior = []
posicao_menor = []
for pos in range(0, 5):
    valores.append(int(input(f'Valor para a posição {pos}: ')))
print(valores)
for p, v in enumerate(valores):
    if v == max(valores):
        posicao_maior.append(p)
    if v == min(valores):
        posicao_menor.append(p)
print(f'Maior valor: {max(valores)} nas posições ', end='')
for posicao in posicao_maior:
    print(f'{posicao}... ', end='')
print(f'\nMenor valor: {min(valores)} nas posições ', end='')
for posicao in posicao_menor:
    print(f'{posicao}... ', end='')
