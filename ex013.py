print('Vou calcular o seu aumento salarial de 15%...')
sal = float(input('Qual o seu salário? '))
ns = sal + (sal * 15 / 100)
print(f'O seu novo salário, a partir do próximo mês, é de R${ns:.2f}')
