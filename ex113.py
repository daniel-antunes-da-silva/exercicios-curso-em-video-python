def leiaint(msg=''):
    while True:
        try:
            if msg == '':
                n = int(input('Digite um número inteiro: '))
            else:
                n = int(input(msg))
        except (TypeError, ValueError):
            print('O tipo de dado digitado está errado.')
        except KeyboardInterrupt:
            n = 0
            print('Você decidiu não digitar nenhum número.')
            return n
        except Exception as causa:
            print(f'A causa do erro foi {causa.__cause__}')
        else:
            return n


def leiareal(msg=''):
    try:
        numero = float(input(msg))
    except (TypeError, ValueError):
        print('O tipo ou o valor digitado está errado.')
    except KeyboardInterrupt:
        print('Você decidiu não digitar nenhum número real.')
        numero = 0
        return numero
    else:
        return numero


inteiro = leiaint('Número inteiro: ')
real = leiareal('Número real: ')
print(f'O valor inteiro foi {inteiro}')
print(f'O valor real(float) foi {real}')


