n1 = int(input('Número: '))
n2 = int(input('Número: '))
n3 = int(input('Número: '))
n4 = int(input('Número: '))
numeros = (n1, n2, n3, n4) #daria também para ler os números diretamente na tupla.
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
         print(c, end=' ')
    else:
        print('0', end='')
        break

