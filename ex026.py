frase = input('Digite uma frase: ').strip()
tam = len(frase)
frase = frase.lower().replace('á', 'a').replace('ã', 'a')
print('Quantidade de letras "a": ', frase.count('a'))
pv = frase.find('a') + 1 #procura o "a" da forma padrão, da esquerda pra direita. A posição do python + 1
uv = frase.rfind('a') + 1  #procura o "a" começando da direita pra esquerda, r de right. Posição do python + 1
print(f'A primeira vez que a letra "a" aparece é na posição {pv} e última vez na posição {uv}')
print('Total de caracteres com espaços: ', tam)
space = frase.count(' ')
print('Total de caracteres sem espaço: ', tam - space)