# gerar 5 numeros
# armazenar os números na tupla
# mostrar a listagem, menor e maior valor.
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for c in numeros:
    print(c, end=' ')
#comando SORTED serve para colocar em ordem. Nesse caso, numérica.
print(f'\nO menor número é: {sorted(numeros)[0]}') #aqui eu peguei a primeira posição para ver o menor numero, ou seja, primeiro da ordem.
print(f'O maior número é: {sorted(numeros)[len(numeros) - 1]}') #aqui eu peguei a ultima posição, para ver o maior número. Ou seja, a posição len da tupla (tamanho da tupla) menos 1, já que o python começa na posição 0.



'''from random import randint
maior = menor = 0
for c in range(1, 6):
    numeros = (randint(1, 10))
    print(numeros, end=' ')
    if numeros > maior:
        maior = numeros
    if numeros < menor or c == 1:
        menor = numeros
print(f'| Maior {maior}, menor {menor}')'''