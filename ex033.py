n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
#if n1 > n2 and n1 > n3:
if n2 < n1 > n3: #pode ser escrito dessa forma.
    print('maior', n1)
if n2 > n1 and n2 > n3:
    print('maior', n2)
if n3 > n1 and n3 > n2:
    print('maior', n3)
if n1 < n2 and n1 < n3:
    print('menor', n1)
if n2 < n1 and n2 < n3:
    print('Menor', n2)
if n3 < n1 and n3 < n2:
    print('Menor', n3)
