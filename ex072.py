'''a variavel mostra o numero na tupla na posição digitada'''
#escrever por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(extenso)
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 > n > 20:
        n = int(input('Opção inválida! Digite um número entre 0 e 20: '))
    else:
        print(f'O número {n} por extenso é {extenso[n]}.')
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp == 'N':
            print('Programa encerrando...')
            break
