valores = []
maior = menor = 0
posicao_menor = []
posicao_maior = []
for pos in range(0, 5):
    valores.append(int(input(f'Número para a posição {pos}: ')))
for c, v in enumerate(valores):
    if c == 0 or v >= maior:
        maior = v
        posicao_maior = c
    if v == maior:
        posicao_maior.append(c)
    if c == 0 or v <= menor:
        menor = v
        posicao_menor = c
    if v == menor:
        posicao_menor.append(c)

print(posicao_maior, posicao_menor)

    #print(f'Posição: {c}', end=', ')
    #print(f'Valor: {v}')




'''for c in range(len(valores)):
    if max(valores)
print(max(valores), min(valores))'''









#Também tá errado
'''valores = []
maior = [] #colocar dentro da lista as posições
menor = [] #colocar dentro da lista as posições
posicao_maior = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if valores[pos] == max(valores):
        maior = valores[pos]
    if valores[pos] == min(valores):
        menor = valores[pos]
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(posicao_maior)
'''
#TA ERRADO ESSE
'''valores = []
maiores = []
menores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
for pos, valor in enumerate(valores):
    print(pos, valor)
    if max(valores):
        maiores = [pos]
    if min(valores):
        menores = [pos]
print(f' Maior valor: {max(valores)} nas posições: {maiores}')
print(f' Menor valor: {min(valores)} nas posições: {menores}')'''