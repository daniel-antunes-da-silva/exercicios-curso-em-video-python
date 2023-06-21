n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
opcao = 0
while opcao != '5':
    opcao = str(input('[1] - somar\n[2] - multiplicar\n[3] - maior\n[4] - novos números\n[5] - sair do programa\n'
                      'Sua escolha: '))
    if opcao == '1':
        print('Soma: ', n1 + n2, '\n', '---'*10)
    elif opcao == '2':
        print('Multiplicação: ', n1 * n2, '\n', '---'*10)
    elif opcao == '3':
        print(f'{n1} é o maior' if n1 > n2 else f'{n2} é o maior\n', '---'*10)
    elif opcao == '4':
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite o segundo número: '))
        print('---'*10)
    elif opcao != '5':
        print('Opção inválida! Tente novamente.\n', '---'*10)
    else:
        print('Programa finalizado por escolha do usuário!')
