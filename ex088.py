""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta. """

from random import randint
from time import sleep

lista=[]
jogos=[]

total=1

quantidadeJogos=int(input('Quantos jogos você quer que eu sorteie? '))

while total<=quantidadeJogos:
    contadora=0
        
    while True:
        numero=randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contadora=contadora+1
        if contadora>=6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total=total+1

print(f'\nSorteando {quantidadeJogos} jogos')

for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('\nBoa Sorte!\n')
