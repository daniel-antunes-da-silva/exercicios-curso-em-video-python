from time import sleep
from datetime import date
nasc = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - nasc
print('A sua classificação é... ')
sleep(2)
if nasc < date.today().year:
    if idade <= 9:
        print('Mirim, idade: ', idade)
    elif idade <= 14:
        print('Infantil, idade: ', idade)
    elif idade <= 19:
        print('Junior, idade: ', idade)
    elif idade <= 20:
        print('Sênior, idade: ', idade)
    elif idade > 20:
        print('Master, idade: ', idade)
else:
    print('O seu ano de nascimento está errado. Revise, por favor!')
final = input('pronto, aperte enter para fechar o programa!')