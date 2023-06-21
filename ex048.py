s = 0
for c in range(1, 501, 2): #pular de 2 em 2 para evitar excesso de processamento com o if. Ou seja, uma forma de agilizar o programa.
    if c % 3 == 0 and c % 2 != 0:
        print(f'{c} é divisível por 3.')
        s = s + c
print(f'A soma dos números divisíveis por 3 é de: {s}')
