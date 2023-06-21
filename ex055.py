maior_atual = 0
menor_atual = 0
for c in range(1, 6):
    peso = float(input('Peso: '))
    if peso > maior_atual:
        maior_atual = peso
    if c == 1: #quando o contador pegar o primeiro peso, vai guardar como o menor
        menor_atual = peso
    if peso < menor_atual: #após guardar o primeiro peso como menor, vai sempre testar se o peso atual digitado é menor que o peso guardado como menor.
        menor_atual = peso
print(f'Maior peso: {maior_atual}kg \nMenor peso: {menor_atual}kg')