def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} * {comprimento} é de {a}m².')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
