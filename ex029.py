print('A velocidade permitida é de até 80km/h')
vel = float(input('Qual a velocidade do carro? '))
multa = (vel - 80) * 7 #a velocidade que estava, menos a velocidade permitida de 80, vezes 7. Ou seja, 7 reais pra cada km acima.
if vel > 80:
    print(f'Você foi multado em R${multa:.2f} por exceder em {vel - 80:.2f}km a velocidade permitida')
else:
    print('Velocidade ok')
