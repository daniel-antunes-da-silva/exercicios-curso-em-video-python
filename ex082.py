valores = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    v = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if v == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
