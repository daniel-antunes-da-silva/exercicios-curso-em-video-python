lista_completa = []
nomes = []
notas = []
while True:
    nome = str(input('Nome: '))
    nomes.append(nome)
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas.append(n1)
    notas.append(n2)
    nomes.append(notas[:])
    notas.clear()
    lista_completa.append(nomes[:])
    nomes.clear()
    verificacao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if verificacao == 'N':
        break
print('=' * 20)
print('Nº  NOME        MÉDIA')
print('-' * 20)
for c in range(0, len(lista_completa)):
    print(c, f'   {lista_completa[c][0]:^10}', f'   {((lista_completa[c][1][0] + lista_completa[c][1][1]) / 2):>3}')
print('-'*20)
#print(lista_completa) FOI IMPORTANTE PRA CHEGAR NO RESULTADO FINAL
while True:
    escolha = int(input('Mostrar nota de qual aluno? Digite 999 para interromper: '))
    if escolha == 999:
        break
    else:
        print(f'As nota de {lista_completa[escolha][0]} são {lista_completa[escolha][1]}')
print('-'*20)
print('Finalizando... Volte sempre!!!')
