# Para verificar se a palavra começa com "SANTO".
cidade = input('Qual a sua cidade? ')
cidade = cidade.upper().split() #criei uma lista
print(f'A cidade começa com "SANTO"?', 'SANTO' in cidade[0]) #coloquei pra saber se tem a palavra 'SANTO' com upper na primeira palavra da string

