primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
termos = 11
tot_termos = 0
while c < termos:
    print(f'{primeiro} --> ', end='')
    primeiro = primeiro + r
    c += 1
    tot_termos += 1
    if c == termos:
        termos = int(input('Qts termos a mais? '))
        c = 0
print('Fim')
print(f'total de termos: {tot_termos}')
