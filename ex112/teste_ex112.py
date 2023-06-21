import moeda
from ex112.utilidadesCeV import dado

preco = dado.leiadinheiro('Qual o valor? R$')
moeda.resumo(preco, 35, 22)
