""" Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que 
agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer. """

from random import randint
from time import sleep

palpites=0

usuario=0

computador=randint(0,10)

while usuario!=computador:
    usuario=int(input('Digite um número inteiro de 0 a 10: '))
    print('PROCESSANDO...')
    print('Você errou, tente outra vez! ',end='')
    sleep(3)
    palpites=palpites+1

if (usuario==computador):
    print('Parabéns, você acertou! {} é o número que eu estava pensando!'.format(usuario))
    print('Foram necessários {} palpites até você acertar!'.format(palpites))

