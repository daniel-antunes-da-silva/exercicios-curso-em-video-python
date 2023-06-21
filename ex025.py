cores = {'limpa': '\033[m',
         'verde_negrito': '\033[1;32m',
         'vermelho_negrito': '\033[1;31m',
         'branco_negrito': '\033[1;97m',
         'azul_negrito': '\033[1;34m'}
nome = input('Digite seu nome: ')
nome = nome.upper()
print('Existe a palavra "Silva" no nome? ', 'SILVA' in nome)
print('Onde está localizado? Posição:', nome.find('SILVA'))
print(f'Vou trocar esse seu sobrenome pela palavra "leão marinho"')
print(nome.replace('SILVA', f'{cores["azul_negrito"]}Leão Marinho {cores["limpa"]}'))