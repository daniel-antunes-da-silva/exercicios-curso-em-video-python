p = float(input('Qual o preço do produto em R$? '))
nv = p - (p * 5/100)
print(f'O valor que você vai pagar, com o desconto de 5% do cartão da loja, é de R${nv:.2f}')
