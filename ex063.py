#SEQUENCIA DE FIBONACCI
import math
n = int(input('Digite um número: '))
c = 2 # o c começa com 2 porque os números 0 e 1 já vão aparecer, sempre. Por isso, devemos "excluir" esses 2 da contagem.
primeiro = 0
segundo = 1
print('0 -> 1 -> ', end='')
while c < n:
    fibonacci = primeiro + segundo #o terceiro número da sequencia recebe a soma dos 2 primeiros.
    print(f'{fibonacci}', end=' -> ')
    c += 1
    primeiro = segundo #aqui o primeiro recebe o valor do segundo
    segundo = fibonacci #aqui o valor do segundo recebe o resultado da soma anterior, que gerou o resultado da sequencia fibonacci.
print('fim')