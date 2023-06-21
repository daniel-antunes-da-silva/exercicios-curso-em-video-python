from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade, enquanto {menor} ainda não atingiram.')
