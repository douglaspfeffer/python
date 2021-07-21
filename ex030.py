'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar'''

numero=int(input('Digite um número inteiro qualquer: '))

if (numero%2==0):
    print('{} é um número par'.format(numero))
else:
    print('{} é um número ímpar'.format(numero))
