n1 = int(input('Primeiro valor inteiro: '))
n2 = int(input('Segundo valor inteiro: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')
else:
    print('Não existe maior e menor. Os dois valores são iguais!')