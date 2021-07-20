#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
numero=float(input('Digite um número: '))
print('O número {} tem a porção inteira {}'.format(numero,trunc(numero)))
print('O número {} tem a porção inteira {}'.format(numero,int(numero)))
