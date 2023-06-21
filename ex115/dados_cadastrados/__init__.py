cores = {'limpa': '\033[m',
             'verde_negrito': '\033[1;32m',
             'vermelho_negrito': '\033[1;31m',
             'branco_negrito': '\033[1;97m',
             'azul_negrito': '\033[1;34m'}


def valida_cpf(cpf=''):
    from time import sleep
    cpf = cpf.strip()
    primeiro_digito = segundo_digito = 0
    if cpf == '':
        print('CPF não informado')
    elif '.' in cpf or '-' in cpf:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
    if len(cpf) == 11:
        pass
        #print('Pode ser que esse CPF seja válido... Deixa eu verificar!')
        #sleep(3)
    else:
        print('O CPF n tem 11 números.')
    try:
        int(cpf)
    except (TypeError, ValueError):
        print('Erro no tipo ou valor.')
    except Exception as causa:
        print(f'A causa do erro foi {causa.__cause__}')
    else:
        try:
            lista = []
            numeros_docpf = {} #primeiro o peso, depois o número.
            pos = 0
            #compondo o dicionario
            for c in range(10, 1, -1):
                numeros_docpf[c] = str(cpf)[pos]
                pos += 1
            lista.append(numeros_docpf.copy())
            #percorrendo o dicionário dentro da lista
            for k, v in lista[0].items():
                primeiro_digito = primeiro_digito + (k * int(v))
            primeiro_digito %= 11
            if primeiro_digito < 2:
                primeiro_digito = 0
            else:
                primeiro_digito = 11 - primeiro_digito
            numeros_docpf.clear()
            pos = 0
            #compondo outro dicionário
            for c in range(11, 1, -1):
                numeros_docpf[c] = str(cpf)[pos]
                pos += 1
            lista.append(numeros_docpf)
            #percorrendo o outro dicionário dentro da lista.
            for k, v in lista[1].items():
                segundo_digito = segundo_digito + (k * int(v))
            segundo_digito %= 11
            if segundo_digito < 2:
                segundo_digito = 0
            else:
                segundo_digito = 11 - segundo_digito
            #print(f'O primeiro digito é/deveria ser {primeiro_digito} e o segundo {segundo_digito}')
            cpf = str(cpf)
            if (str(primeiro_digito) == cpf[9]) and (str(segundo_digito) == cpf[10]):
                return True
            else:
                return False
        except Exception as erro:
            return erro.__class__


def menu():
    opcao = 0
    while opcao != '1' and opcao != '2' and opcao != '3':
        print(cores['azul_negrito'], '-'*40)
        print('             MENU PRINCIPAL')
        print('-'*40)
        print('[1] - Ver pessoas cadastradas')
        print('[2] - Cadastrar nova pessoa')
        print('[3] - Sair do sistema')
        print('-'*40, cores['verde_negrito'])
        opcao = input('Sua opção: ')
        if opcao == '1' or opcao == '2' or opcao == '3':
            print('-'*40)
            print(f'                Opção {opcao}')
            print('-'*40)
            return opcao
        else:
            print(cores['vermelho_negrito'], 'Opção inválida.')


def cadastro_pessoa():
    arquivo = open('dados.txt', 'a')
    dados = []
    print(cores['branco_negrito'])
    dados.append(input('Qual o seu nome? '))
    while True:
        try:
            dados.append(int(input('Qual a sua idade?')))
        except (ValueError, TypeError):
            print('Erro no valor ou tipo inserido.')
        except Exception as causa:
            print(f'Erro de causa {causa.__cause__}')
        else:
            break
    while True:
        cpf = str(input('CPF: '))
        if valida_cpf(cpf) == True:
            dados.append(cpf)
            break
    for dado in dados:
        arquivo.write(f'{dado}\n')
    print('Pessoa adicionada com sucesso!')


def mostrar_cadastro():
    arquivo = open('dados.txt', 'r')
    leitura = []
    for linha in arquivo.readlines():
        leitura.append(linha[0:len(linha)-1])
    print(cores['branco_negrito'], 'Nome        Idade        CPF')
    return leitura


'''d = cadastro_pessoa()
print(d)
'''