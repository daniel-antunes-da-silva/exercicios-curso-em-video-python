#P.A = PROGRESSÃO ARITMÉTICA COM WHILE
pt = int(input('Qual o primeiro termo da P.A.? '))
r = int(input('Qual a razão da P.A.? '))
c = 0
decimo = pt
while c < 10:
    print(f'{decimo} → ', end='')
    c += 1
    decimo = decimo + r
print('fim')
