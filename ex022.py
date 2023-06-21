nome = str(input('Digite o nome: '))
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print('Total de letras com espaços: ', len(nome.strip()))
qtd_letras = len(''.join(dividido)) #junta todas as palavras da lista, sem espaço entre elas, e determina a quantidade de caracteres.
print(f'A quantidade de letras é: {qtd_letras}') #printa a variavel acima, com o número de letras.
print('A quantidade de letras é: ', len(''.join(dividido))) #também pode ser escrito dessa forma, direto, mesmo resultado.
print(f'O primeiro nome tem {len(dividido[0])} letras')
