#escolher alunos e a ordem deles para apagar o quadro.
import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
#lista = f'{n1}, {n2}, {n3}, {n4}'.split() #essa ou a forma de baixo estão corretas.
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de alunos é {lista}')
