def notas(*n, sit=False):
    s = 0
    for c in n:
        s += c
    media = s / len(n)
    ficha = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': media}
    if sit:
        if media >= 7 and media <=10:
            ficha['Situação'] = 'Bom'
        elif media < 7 and media > 5:
            ficha['Situação'] = 'Razoável'
        elif media >= 0 and media <= 5:
            ficha['Situação'] = 'Péssimo'
    return ficha


resp = notas(5, 7, 9, 6, sit=True)
print(resp)
