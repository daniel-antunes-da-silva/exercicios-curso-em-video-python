#escolher 1 aluno para apagar o quadro
from random import choice
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')
s = [a1, a2, a3, a4]
print(f'A pessoa escolhida foi {choice(s)}')

