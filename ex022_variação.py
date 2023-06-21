nome = str(input('Digite o nome: '))
print(nome.upper())
print(nome.lower())
space = nome.count(' ') #quantidade de espaços na sequencia de caracteres
print(space)
qtd_letras = len(nome)
print(f'A quantidade de letras, sem espaço, é: {qtd_letras - space}')
#esse código apresenta o mesmo resultado do ex022, é apenas uma variação.
