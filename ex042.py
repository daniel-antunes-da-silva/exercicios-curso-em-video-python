r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Pode formar um triângulo!')
    if r1 == r2 == r3:
        print('Triângulo equilátero! Todos os lados iguais')
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
        print('Triângulo isósceles! Dois lados iguais')
    elif r1 != r2 != r3:
        print('Triângulo escaleno! Todos os lados diferentes')
else:
    print('Não pode formar um triângulo')
