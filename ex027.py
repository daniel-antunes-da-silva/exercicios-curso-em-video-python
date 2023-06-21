#nc = input('Digite seu nome completo: ')
#nc = nc.strip().split()
#print(nc)
#print('O primeiro nome é ', nc[0])
#tam = int(len(nc))
#print('O último nome é', nc[tam-1:tam]) #mostra o último nome. Ou seja, o tamanho na lista, ele vai da penultima posição,
# até a posição completa dela. Ou seja, ele varre a lista até certa posição.

#nc = str(input('Nome completo: ')).strip().title()
#ultimo = nc.rfind(' ')
#print('Primeiro nome: {}'.format(nc.split()[0]))
#print('Último nome: {}'.format(nc[ultimo:len(nc)]))

#talvez a melhor forma de fazer. Printa o nome da posição de len(tamanho do nome) -1, já que o python n vai até a posição final, e sim uma antes, por começar em 0.
nome = str(input('Seu nome: ')).split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é  {nome[len(nome) - 1]}')
