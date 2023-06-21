'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [ M ] / [ F ] : ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Dado inválido! Tente novamente!')
print(f'Sexo {sexo} registrado com sucesso!')'''

# Forma melhorada do que foi ensinado no vídeo.
sexo = str(input('Sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dado inválido. Digite novamente [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')
