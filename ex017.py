import math
print('Vou te dizer o comprimento da hipotenusa, mas para isso, preciso de duas informações: ')
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
hip = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {hip}')
