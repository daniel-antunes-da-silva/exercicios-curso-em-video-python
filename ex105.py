def ajuda():
    cores = {'limpa': '\033[m',
             'verde_negrito': '\033[1;32m',
             'vermelho_negrito': '\033[1;31m',
             'branco_negrito': '\033[1;97m',
             'azul_negrito': '\033[1;34m'}
    while True:
        print(cores['verde_negrito'])
        print('-----------------------------')
        print('  SISTEMA DE AJUDA: ajuda()  ')
        print('-----------------------------')
        print(cores['azul_negrito'])
        x = str(input('Função ou biblioteca > ')).lower()
        if x == 'fim':
            print(cores['vermelho_negrito'])
            print('-------------')
            print('  Até logo')
            print('-------------')
            break
        print(cores['branco_negrito'])
        print('--------------------------------------')
        print(f'  Acessando o manual do comando "{x}"')
        print('--------------------------------------')
        help(x)

ajuda()