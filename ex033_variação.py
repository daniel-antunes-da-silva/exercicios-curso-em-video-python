#n1 = int(input('Digite um número: '))
#n2 = int(input('Outro número: '))
#n3 = int(input('O tereciro número: '))
#lista = [n1, n2, n3]
#print('O maior valor é: ', max(lista))
#print(f'O menor valor é {min(lista)}')
#OUTRA FORMA ABAIXO:
n1 = int(input('Digite um número: '))
n2 = int(input('Outro número: '))
n3 = int(input('O tereciro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor} e o maior foi {maior}')
