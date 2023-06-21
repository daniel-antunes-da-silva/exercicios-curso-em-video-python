from urllib import request
url = 'http://www.pudim.com.br'
try:
    tentativa = request.urlopen(url)
except Exception as causa:
    print(f'Não consegui acessar o site.')
else:
    print('Consegui acessar o site.')
    print(tentativa.read())