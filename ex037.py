num = int(input('Digite um número: '))
base = str(input('Escolha qual será a base de conversão: '
                 '\n[0] - binário'
                 '\n[1] - octal'
                 '\n[2] - hexadecimal\n'
                 '\033[35mSua escolha: \033[m')).strip()
if base == '0':
    #vem com um "0b" na frente, que significa binário
    print(bin(num)[2:]) #existe essa forma de fazer (sem variável, tendo cuidado com o local do colchetes.
elif base == '1':
    octa = oct(num) #vem com um "0o" na frente, que significa octal
    print(str(octa[2:])) #existe também essa forma de fazer (c/ variável e tendo cuidado com o local dos colchetes)
elif base == '2':
    xd = hex(num) #vem com um "0x" na frente, que significa hexadecimal
    print(str(xd[2:]))
else:
    print('Comando inválido. Tente novamente, escolhendo um dos seguintes números: 0, 1 ou 2.')