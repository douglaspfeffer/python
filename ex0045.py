""" Crie um programa que faça o computador jogar Jokenpô com você. """

from random import choice
from time import sleep

usuario=str(input('Escolha entre pedra, papel e tesoura: ')).lower()

lista=['pedra','papel','tesoura']
computador=choice(lista)

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO')

if computador=='pedra' and usuario=='pedra' or computador=='papel' and usuario=='papel' or computador=='tesoura' and usuario=='tesoura':
    print("Empatamos!")
elif computador=='pedra' and usuario=='tesoura' or computador=='papel' and usuario=='pedra' or computador=='tesoura' and usuario=='papel':
    print('Você perdeu! Eu escolhi {}, e {} ganha de {}'.format(computador,computador,usuario))
elif computador=='pedra' and usuario=='papel' or computador=='papel' and usuario=='tesoura' or computador=='tesoura' and usuario=='pedra' :
    print('Você ganhou! Eu escolhi {}, e {} ganha de {}'.format(computador,usuario,computador))
else:
    print('Jogada inválida')
