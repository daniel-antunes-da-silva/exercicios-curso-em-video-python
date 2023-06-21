def leiadinheiro(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            print(valor)
        elif ',' in valor:
            valor = valor.replace(',', '.')
            print(valor)
        qtd_pontuacao = valor.count('.')
        if (qtd_pontuacao == 0 or qtd_pontuacao == 1) and valor.replace('.', '').isnumeric():
            valor = float(valor)
            break
        else:
            print(f'"{valor}" é um valor incorreto! ')
    return valor

''' #+ valor.count(',')  #não preciso mais
            if qtd_pontuacao > 1:
                print('Valor inserido está incorreto.')
            #else:
                #break'''
