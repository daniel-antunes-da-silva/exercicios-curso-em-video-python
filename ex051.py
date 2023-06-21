'''#PROGRESSÃO ARITMÉTICA
p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da P.A: '))
print('1º termo: ', p)
for c in range(2, 11):
    p = p + r
    print(f'{c}º termo: ', p)
'''

p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da P.A: '))
for c in range(1, 11):
    print(f'{c}º termo: ', p)
    p = p + r
