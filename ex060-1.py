""" Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x6x2x1=120 """

from math import factorial

numero=int(input('Digite um número inteiro qualquer: '))
print('{}! = {}'.format(numero,factorial(numero)))
