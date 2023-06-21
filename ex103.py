#REFAZER ESSE EXERCÍCIO, FIZ DE UM JEITO MEIO BURRO...

def ficha(nome='', gols=0):
    if nome == '' and gols == '':
        return '<desconhecido>', 0
    elif nome == '':
        return '<desconhecido>', gols
    elif gols == '':
        return nome, 0
    return nome, gols


jogador = str(input('Nome: '))
gols = input('Gols: ')
if gols.strip() == '':
    gols = 0
elif gols.isnumeric():
    gols = int(gols)
dados = ficha(jogador, gols)
print(f'O jogador {dados[0]} possui {dados[1]} gols.')