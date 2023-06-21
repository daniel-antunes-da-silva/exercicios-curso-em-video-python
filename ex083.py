expre = []
abre = []
fecha = []
expre.append(str(input('Digite uma expressão que usa parênteses: ')))
for c in expre:
    for v in range(0, len(c)):
        #print(v) serviu para auxiliar na construção do código
        if c[v] == '(':
            abre.append(c[v])
        if c[v] == ')':
            fecha.append(c[v])
if len(abre) == len(fecha):
    print(f'A expressão {expre} está correta!')
else:
    print(f'A expressão {expre} está incorreta!')

#Serviu para auxiliar na construção do código
'''print(expre)
print(abre)
print(fecha)'''