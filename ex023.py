numero = int(input('Digite um número entre 0 e 99999: ')) #string
u = numero % 10 #unidade
d = numero // 10 % 10 #dezena
c = numero // 100 % 10 #centena
m = numero // 1000 % 10 #milhar
dm = numero // 10000 #dezena de milhar
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')
print('Dezena de milhar', dm)
