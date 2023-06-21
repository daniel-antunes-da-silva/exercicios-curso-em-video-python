times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR',
         'Atlético MG', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino',
         'Coritiba', 'Cuiabá', 'Grêmio', 'Bahia', 'Vasco')
print(times, len(times))
print(f'Os 5 primeiros colocados são: {times[:5]}')
#abaixo: ordem decrescente de posição.
print(f'Os últimos 4 colocados são {times[len(times):len(times)-5:-1]}, em ordem decrescente.')
print(f'Tabela em ordem alfabética: {sorted(times)}')
pos = str(input('Quer ver a posição de qual time? ')).capitalize()
print(f'A posição de {pos} é {times.index(pos) + 1}º')
