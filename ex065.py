resposta = 'S'
soma = 0
tot_n = 0
maior_atual = 0
menor_atual = 0
while resposta == 'S':
    n = int(input('Digite um número: '))
    tot_n += 1
    soma = soma + n
    if tot_n == 1:
        maior_atual = n
        menor_atual = n
    elif n > maior_atual:
        maior_atual = n
    elif n < menor_atual:
        menor_atual = n
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('Opção inválida!')
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()
media = soma / tot_n
print('Programa finalizado! ')
print(f'A média de todos os números digitados foi {media}')
print(f'O maior valor lido foi {maior_atual} e o menor {menor_atual}')
