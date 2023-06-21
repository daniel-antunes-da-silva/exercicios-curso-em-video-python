tot_gasto = produtocaro = cont = maisbarato = 0
nomebarato = ''
while True:
    nome = str(input('Produto: '))
    valor = float(input('Valor R$: '))
    tot_gasto += valor
    cont += 1
    if valor > 1000:
        produtocaro += 1
    if cont == 1 or valor < maisbarato:
        maisbarato = valor
        nomebarato = nome
    resp = str(input('Quer continuar? S/N')).upper().strip()
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? S/N')).upper().strip()
    if resp == 'N':
        print('---'*15, '\nPrograma encerrado por escolha do usuário.\n', '---'*15)
        break
print(f'O total de produtos registrados foi {cont}')
print(f'Total gasto na compra: R${tot_gasto}')
print(f'{produtocaro} produto(s) custaram mais de R$1000,00.')
print(f'O nome do produto mais barato registrado é {nomebarato}, custando {maisbarato}')
