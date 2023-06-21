def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end=' -> ')
        f = f * c
    return f


print(fatorial(5, show=True))
numero = int(input('Quer calcular o fatorial de qual número? '))
print(fatorial(numero, True))
