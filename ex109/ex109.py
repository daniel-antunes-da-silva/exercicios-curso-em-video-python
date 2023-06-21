import moeda
v = float(input('Digite o valor: R$'))
print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, show=True)}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}')
print(f'Aumentando 10% o valor fica {moeda.aumentar(v, 10, True)}')
print(f'Reduzindo 13% o valor fica {moeda.diminuir(v, 13, True)}')
