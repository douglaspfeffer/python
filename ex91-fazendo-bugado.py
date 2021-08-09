# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogador1=randint(1,6)
jogador2=randint(1,6)
jogador3=randint(1,6)
jogador4=randint(1,6)

listaDicionario={'Jogador 1':jogador1,'Jogador 2':jogador2,'Jogador 3':jogador3,'Jogador 4':jogador4}

for k,v in listaDicionario.items():
    print(f'{k} tirou {v}')
    #sleep(2)


print(sorted(listaDicionario))
