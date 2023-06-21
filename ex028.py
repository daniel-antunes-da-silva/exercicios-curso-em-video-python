from random import randint
from time import sleep
n = randint(0, 5) #randomiza um numero entre 0 e 5
print('Pense em um número de 0 a 5 e eu vou tentar adivinhar!')
np = int(input('Digite o número que você pensou: ')) #númeropensado
print('Processando...')
sleep(2)
print(f'Você acertou, o número é {n}' if n == np else f'Você errou, o número era {n}') #if e else simplificados.

