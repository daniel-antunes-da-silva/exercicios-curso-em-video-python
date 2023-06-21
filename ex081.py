numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(numeros)
print(f'Total de números adicionados: {len(numeros)}')
numeros.sort(reverse=True)
print(f'Ordem decrescente: {numeros}')
if 5 in numeros:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não foi digitado.')
