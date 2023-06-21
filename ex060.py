#FATORIAL WHILE
n = int(input('Digite um número: '))
fatorial = n
while n != 1:
    print(f'{n} x ', end='')
    n = n - 1
    fatorial = fatorial * n
print(f'1 --> Fatorial = {fatorial}')

#FATORIAL FOR
'''n = int(input('Digite um número: '))
fatorial = n
for n in range(n - 1, 0, -1):
    print(f'{n + 1} x ', end='')
    fatorial *= n
print(f'1 = {fatorial}')'''

## EXISTE TAMBÉM O MÓDULO FATORIAL, DA BIBLIOTECA MATH, QUE FACILITA ESSE EXERCÍCIO.