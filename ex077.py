palavras = ('Aprender', 'Escoltar', 'Fools', 'Foolish', 'Farmer', 'Computador')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')


'''for palavra in palavras:
    print(palavra)
    for letra in palavra:
        print(letra.lower() in 'aeiou')'''

'''print(len(palavras[0]))
print(palavras[1].lower() in 'a' or 'e' or 'i' or 'o' or 'u')
print(palavras[1].lower().index('a', 'e'))
if palavras[1].lower() in 'a' or 'e' or 'i' or 'o' or 'u':
    print()
#acho q é um for dentro de outro for'''