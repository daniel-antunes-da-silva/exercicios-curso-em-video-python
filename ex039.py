from datetime import date
ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
sexo = str(input('Sexo: H ou M?')).upper()
if sexo == 'H':
    if idade == 18:
        print('Está na hora de você se alistar!!')
    elif idade < 18:
        if idade == 17:
            print(f'Falta {18 - idade} ano para o seu alistamento, que será em {ano_atual + 1}')
        else:
            print(f'Faltam {18 - idade} anos para o seu alistamento, que será em {ano_atual + (18 - idade)}')
    else:
        if idade == 19:
            print('Já se passou 1 ano para o seu alistamento, você está atrasado!!')
        else:
            print(f'Já se passaram {idade - 18} anos para o seu alistamento, você está muito atrasado!')
else:
    print('Você é mulher, então não precisa se alistar!')
