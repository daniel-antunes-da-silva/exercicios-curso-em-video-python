#CONSEGUI!!!!!! PORÉM, CÓDIGO BAGUNÇADO E GRANDE.
valores = []
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if c == 0:
        valores.append(n)
        print('Valor adicionado ao final da lista')
    elif n < valores[0]:
        valores.insert(0, n)
        print('Valor adicionado na posição 0')
    elif n > valores[len(valores) - 1]:
        print('Valor adicionado ao final da lista!')
        valores.append(n)
    else:
        for pos, v in enumerate(valores):
            '''print(v)
            print(pos)''' #ME AJUDARAM A CHEGAR NO RACIOCÍNIO
            if n < v:
                valores.insert(pos, n)
                print(f'Foi adicionado na posição {pos}')
                break
print(valores)







'''valores = []
for c in range(0, 5):
    valor_atual = int(input('Digite um valor: '))
    if c == 0:
        valores.append(valor_atual)
    elif valor_atual > valores[len(valores) - 1]:
        valores.append(valor_atual)
    else:
        valores.insert(0, valor_atual)
for v in valores:
    print(v)'''

