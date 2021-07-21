'''Escreva um programa que faça o cmputador 'pensar' em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random

numero=int(input('Digite um número inteiro de 0 a 5: '))

if (numero==random.randint(0,5)):
    print('Parabéns, você acertou! {} é o número que eu estava pensando!'.format(numero))
else:
    print('Você errou! Eu estava pensando no número {}'.format(random.randint(0,5)))