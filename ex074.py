""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. """

from random import randint

lista=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os números gerados aleatoriamente foram: {lista}')

print(f'O maior valor é {max(lista)} e o menor valor é {min(lista)}')
