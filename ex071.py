print('--'*10, '\nCAIXA ELETRÔNICO\n', '--'*10)
valor = int(input('Valor a ser sacado? R$'))
totcinq = totvinte = totdez = totum = 0
while valor >= 50:
    valor -= 50
    totcinq += 1
while valor >= 20:
    valor -= 20
    totvinte += 1
while valor >= 10:
    valor -= 10
    totdez += 1
while valor >= 1:
    valor -= 1
    totum += 1
print(f'''{totcinq} notas de R$50.
{totvinte} notas de R$20. 
{totdez} notas de R$10 
{totum} notas de R$1''')
