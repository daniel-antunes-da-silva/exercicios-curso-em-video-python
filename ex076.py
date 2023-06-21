print(' ='*15, '\n' ' MERCADINHO DO DANIEL', '\n', '= '*15)
listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90, 'Abacaxi', 7.99, 'Uva', 6, 'Carne moída', 22.90)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30} R$', end=' ')
    print(f'{listagem[c+1]:>5.2f}')
