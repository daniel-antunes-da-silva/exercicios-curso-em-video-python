from time import sleep
import playsound
print('-=-' * 30)
print('\033[34mOlá, seja bem-vindo(a) ao sistema de empréstimo bancário para compra de casas! \033[m')
print('-=-' * 30)
print(f'Antes de prosseguirmos para saber se você está apto a receber o empréstimo, preciso de algumas informações.')
valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
vp = valor / (anos * 12) #valor da prestação
print(f'O valor da prestação mensal é R${vp:.2f}')
print('\033[35mAguardando a análise...\033[m')
sleep(3)
if vp > sal * 30 / 100:
    print(f'\033[31mDesculpe, mas o empréstimo foi negado! O valor da prestação é superior a 30% do seu salário, '
          f'ou seja, maior que {(sal * 30 / 100):.2f}\033[m')
elif vp <= sal * 30 / 100:
    print('\033[32mQue legal!!! Seu empréstimo foi aprovado, e em breve constará na sua conta. Aproveite!\033[m')
    playsound.playsound(r'C:\Users\Daniel\Downloads\natural.mp3') # música pra comemorar kkk
