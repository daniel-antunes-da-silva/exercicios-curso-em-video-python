valores = []
while True:
    valor_atual = int(input('Digite um valor: '))
    if valor_atual not in valores:
        valores.append(valor_atual)
    else:
        print('Valor duplicado, não vou adicionar...')
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort()
print(valores)