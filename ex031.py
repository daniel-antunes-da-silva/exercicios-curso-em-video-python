dist = float(input('Qual a distância da viagem em km? '))
if dist <= 200:
    print(f'O valor da viagem é de R${0.5 * dist:.2f}, considerando R$0,50 por km rodado')
if dist > 200:
    print(f' O valor da viagem é de R${0.45 * dist:.2f}, considerando R$0,45 por km rodado')
ask = str(input('Deseja aceitar a corrida? ')).strip().lower()
print('Ok, o motorista está a caminho' if ask == 'sim' else 'Viagem cancelada')
