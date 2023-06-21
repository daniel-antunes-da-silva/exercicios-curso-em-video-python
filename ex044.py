from time import sleep
pp = float(input('Qual o valor do produto? ')) #preço do produto
#método de pagamento
mp = str(input('Qual o método de pagamento? '  
               '\n[1] - À vista no dinheiro ou pix' #10% desconto
               '\n[2] - À vista no cartão' #5% desconto
               '\n[3] - Em até 2x no cartão' #preço normal
               '\n[4] - 3x ou mais no cartão' #20% juros
               '\nSua escolha: '))
if mp == '1':
    pp = pp - (pp * 10 / 100)
    print(f'Você recebeu um desconto de 10% por pagamento à vista no dinheiro ou pix. O novo preço é R${pp:.2f}')
elif mp == '2':
    pp = pp - (pp * 5 / 100)
    print(f'Você recebeu um desconto de 5% por pagamento à vista no cartão. O novo preço é R${pp:.2f}')
elif mp == '3':
    print(f'O preço do produto é R${pp:.2f}, sem desconto ou acréscimos.')
elif mp == '4':
    qp = int(input('Em quantas parcelas você quer pagar?')) #quantidade de parcelas
    pp = pp + (pp * 20 / 100)
    print(f'Você vai pagar 20% a mais pelo produto, por escolher parcelamento em 3x ou mais.')
    sleep(2)
    print(f'Você pagará R${(pp / qp):.2f} por parcela, ou seja, {qp}x de R${(pp / qp):.2f}, totalizando R${pp:.2f}')
else:
    print('Opção inválida, tente novamente.')