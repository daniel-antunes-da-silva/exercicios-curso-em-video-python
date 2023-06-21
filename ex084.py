pessoas = []
dados = []
tot_pessoas = menor_peso = maior_peso = 0
nome_menor = nome_maior = ''
while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(float(input('Peso em Kg: ')))
    pessoas.append(dados[:])
    dados.clear()
    tot_pessoas += 1
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(pessoas)
print('='*30)
print(f'Ao todo, você cadastrou {tot_pessoas} pessoas')
print('Pessoas mais leves: ', end=' ')
for p in pessoas:
    if p[1] <= 70:
        print(f'{p[0]}.', end=' ')
    if p == pessoas[0]:
        menor_peso = p[1]
    else:
        if p[1] < menor_peso:
            menor_peso = p[1]
            nome_menor = p[0]
print(f'Menor peso é {menor_peso:.2f} kg do(a) {nome_menor}.')
print('Pessoas mais pesadas: ', end=' ')
for p in pessoas:
    if p[1] >= 90:
        print(f'{p[0]}.', end=' ')
    if p == pessoas[0] or p[1] > maior_peso:
        maior_peso = p[1]
        nome_maior = p[0]
print(f'Maior peso é {maior_peso} kg do(a) {nome_maior}')
