from math import trunc
print('\033[36mAPROVAMENTO DE EMPRÉSTIMO\033[m')
print('_'*26, '\n')
vc = float(input('Valor da casa: R$'))
sal = float(input('Seu salário: R$'))
tot_mes = float(input('Total de meses para pagamento: '))
mensal = vc / tot_mes
porc = (sal * 30) / 100
if mensal > porc:
    print('EMPRÉSTIMO NEGADO!\nO valor da prestação mensal seria de R${:.2f}, '
          'excedendo 30% do salário, que é R${:.2f}.'.format(mensal, porc))
    qtd_min = vc / porc
    anos = qtd_min // 12
    meses = qtd_min % 12
    dias = (meses % 30 % 1) * 30
    print('De acordo com o seu salário, a quantidade mínima de meses deverá ser {:.1f}, ou seja, '
          '\n{} anos, {} mes(es) e {:.0f} dias.'.format(qtd_min, anos, trunc(meses), dias))
else:
   print('EMPRÉSTIMO APROVADO!\nO valor da prestação mensal será de R${:.2f}'.format(mensal))