def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def aumentar(valor, porcentagem, show=False):
    resultado = valor + (valor * porcentagem / 100)
    if show:
        return moeda(resultado)
    return resultado


def diminuir(valor, porcentagem, show=False):
    resultado = valor - (valor * porcentagem / 100)
    if show:
        return moeda(resultado)
    return resultado


def metade(valor, show=False):
    resultado = valor / 2
    if show:
        return moeda(resultado)
    return resultado


def dobro(valor, show=False):
    resultado = valor * 2
    if show:
        return moeda(resultado)
    return resultado





'''def moeda(n, show=True):
    if show:
        n = f'R${n:.0f},00'
    return n
'''


def resumo(x, aumento=0, diminuicao=0):
    resultados = {'Dobro do preço: ': dobro(x, show=True),
                  'Metade do preço: ': metade(x, show=True),
                  f'Aumento de {aumento}%: ': aumentar(x, aumento, True),
                  f'Diminuição de {diminuicao}%: ': diminuir(x, diminuicao, True)}
    print('='*20)
    print('   RESUMO DO VALOR   ')
    print('=' * 20)
    print(f'Preço analisado:  {moeda(x)}')
    for k, v in resultados.items():
        print(f'{k:>5}', f'{v:>10}')
    print('--'*20)
