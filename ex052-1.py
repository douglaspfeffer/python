""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

numero=int(input('Digite um número inteiro qualquer: '))

primo=0

for c in range(1,numero+1):
    if numero%c==0:
        primo=primo+1

if primo==2:
    print('{} é um número primo!'.format(numero))
else:
    print('{} NÃO é um número primo!'.format(numero))
