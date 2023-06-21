#area da parede e quanto de tinta
lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar * alt
tinta_necessaria = area / 2
print(f'A área é {area:.0f}m² e a quantidade de tinta necessária para pintar a parede é de {tinta_necessaria}L')
