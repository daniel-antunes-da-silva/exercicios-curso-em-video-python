def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade > 16 and idade > 0:
        return 'Negado'
    elif 16 <= idade < 18 or idade >= 65:
        return 'Opcional'
    elif idade > 18:
        return 'Obrigatório'
    else:
        return 'Valor digitado foi incorreto'


anonasc = int(input('Qual seu ano de nascimento? '))
situacao = voto(anonasc)
print(f'O voto é {situacao}')
