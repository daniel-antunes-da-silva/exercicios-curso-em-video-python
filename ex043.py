peso = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura em metros? '))
imc = peso / (pow(alt, 2))
print(f'O seu IMC é: {imc:.2f}kg/m²')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso dentro da faixa ideal.')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade grau 1')
elif imc < 40:
    print('Obesidade grau 2')
elif imc >= 40:
    print('Obesidade grau 3')

