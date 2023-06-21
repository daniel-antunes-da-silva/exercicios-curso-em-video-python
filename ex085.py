valores = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print(valores)
valores[0].sort(), valores[1].sort()
print(f'Os números pares foram: {valores[0]}')
print(f'Os números ímpares foram: {valores[1]}')

'''valores = []
pares = []
impares = []
for c in range(0, 4):
    n = int(input('Digite um número: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(valores[:])
    else:
        impares.append(valores[:])
    valores.clear()
print('='*30)
print(f'Os valores pares foram: {pares[:]}')
print(f'Os valores ímpares foram {impares[:]}')'''