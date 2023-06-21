# numeros primos
n = int(input('Digite um número: '))
primo = 0 # somatório para verificar se é primo.
for c in range(1, n + 1):
    if n % c == 0:
        primo = primo + 1 # caso seja divisível, vai add +1. no final, tem q dar um total de 2;
        print('\033[34m', c, '\033[m', end='')
    else:
        print('\033[31m', c, '\033[m', end='')
if primo == 2:
    print(f'\n{n} é um número primo, já que foi divisível 2 vezes!')
else:
    print(f'\n{n} NÃO é um número primo, pois foi divisível {primo} vezes.')