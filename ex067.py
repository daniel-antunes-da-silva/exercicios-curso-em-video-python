cont = 1
n = int(input('Qual número você quer fazer a tabuada? '))
while cont < 12:
    tabuada = n * cont
    print(f'{cont} x {n} = {tabuada}')
    cont += 1
    if cont == 11:
        n = int(input('Qual número quer fazer a tabuada? '))
        cont = 1
        if n < 0:
            break
print('Programa encerrado por digitar valor negativo!')
