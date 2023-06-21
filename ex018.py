import math
print('Vou te dizer o valor do seno, cosseno e tangente de um ângulo... para isso:')
a = float(input('Digite o ângulo: '))
a = math.radians(a) #conversão do valor em graus digitado, para radiano, pois a fórmula original do módulo utiliza radiano.
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)
print(f'Seno: {sen:.2f}, cosseno: {cos:.2f}, tangente: {tan:.2f}')
