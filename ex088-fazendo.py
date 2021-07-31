""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta. """

#from random import randint

lista=[]

jogosGerados=int(input('Quantos jogos serão gerados? '))

for linha in range(0,jogosGerados):
    for coluna in range(0,6):
        lista[linha][coluna]=int(input(f'Digite um valor para a linha {linha+1} coluna {coluna+1}: '))

for linha in range(0,jogosGerados):
    print()
    for coluna in range(0,6):
        print(f'{lista[linha][coluna]:^5}',end=' ')

print('\n')
