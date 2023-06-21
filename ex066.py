s = tot = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    tot += 1
print(f'O total de números digitados foi {tot} e a soma de todos eles {s}')
