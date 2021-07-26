""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

numero=int(input('Digite um número inteiro qualquer: '))

if numero%2!=0 and numero%3==0 or numero%2!=0 and numero/numero==1 and numero/1==numero or numero==2:
    print('{} é um número primo'.format(numero))
else:
    print('{} NÃO é um número primo'.format(numero))
