r1 = float(input('Qual o comprimento da reta 1? '))
r2 = float(input('Qual o comprimento da reta 2? '))
r3 = float(input('Qual o comprimento da reta 3? '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;32mPode formar um triângulo! \033[m')
else:
    print('\033[1;31mNão pode formar um triângulo \033[m')
cores = {'limpa': '\033[m',
         'verde_negrito': '\033[1;32m',
         'vermelho_negrito': '\033[1;31m',
         'branco_negrito': '\033[1;97m',
         'azul_negrito': '\033[1;34m'}
