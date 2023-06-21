tot_idade = 0
mv = 0
nmv = ''
tot_m = 0
for c in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M] / [F]: ')).upper()
    tot_idade = tot_idade + idade
    if mv < idade and sexo == 'M':
        mv = idade
        nmv = nome
    if sexo == 'F' and idade < 20:
        tot_m += 1
media = tot_idade / 4
print(f'Média de idades: {media:.0f} anos\n', '---' * 10)
print(f'O home mais velho é: {nmv.title()}, com {mv} anos.\n', '---' * 10)
print(f'{tot_m} é o total de mulheres com menos de 20 anos.\n', '---' * 10)
