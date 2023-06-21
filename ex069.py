tot_maior = tot_homem = tot_mulher = 0
print('--'*12)
print('CADASTRE UMA PESSOA')
print('--'*12)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ M / F ]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [ M / F ]: ')).strip().upper()
    if idade > 18:
        tot_maior += 1
    if sexo == 'M':
        tot_homem += 1
    if sexo == 'F' and idade < 20:
        tot_mulher += 1
    resp = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    while resp != 'N' and resp != 'S':
        resp = str(input('Quer continuar? [ S / N ]: ')).strip().upper()
    if resp == 'N':
        print('Programa encerrado por escolha do usuário.')
        break
print(f'''Total de pessoas com mais de 18 anos: {tot_maior}!
Ao todo temos {tot_homem} homens cadastrados
Temos {tot_mulher} mulheres com menos de 20 anos''')

