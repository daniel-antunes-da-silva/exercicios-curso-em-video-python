sal = float(input('Qual seu salário? R$'))
if sal > 1250:
    sal = sal + (sal * 10 / 100)
    print(f'Você recebeu um aumento de 10%, e seu novo salário é: R${sal:.2f}')
if sal <= 1250:
    sal = sal + (sal * 15 / 100)
    print(f'Você recebeu um aumento de 15%, e seu novo salário é: R${sal:.2f} ')
print('FIM')