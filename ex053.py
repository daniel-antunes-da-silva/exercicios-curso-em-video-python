frase = str(input('Digite sua frase: ')).upper().strip().replace(' ', '')
tam = len(frase)
inverso = ''.join(frase[tam::-1])
if inverso == frase:
    print(f'"{inverso}" É palíndromo')
else:
    print(f'"{frase}" Não é palíndromo')

#print(tam) ajudaram a chegar na resolução
#print(frase[tam::-1]) #ajudaram a chegar na resolução