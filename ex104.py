def leiaint(n):
    digitado = input(n)
    while True:
        try:
            digitado = int(digitado)
            break
        except:
            print('Não é um valor numérico')
            print('Erro!', end=' ')
            digitado = input(n)
    return digitado


numero = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
