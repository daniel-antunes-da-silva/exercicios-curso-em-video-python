from ex115.dados_cadastrados import menu, cadastro_pessoa, mostrar_cadastro

while True:
    resp = menu()
    if resp == '1':
        cadastradas = mostrar_cadastro()
        controle = 3
        count = 0
        for p in cadastradas:
            if count == controle:
                print()
                count = 0
            print(f'{p:<10}', end='   ')
            count += 1
        print()
    if resp == '2':
        cadastro_pessoa()
    if resp == '3':
        break
