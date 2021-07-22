'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

from datetime import date

ano=int(input('QUe ano quer analizar?\nOBS: Coloque 0 para analizar o ano atual: : '))

'''resto da divisão pegando as duas últimas casas decimais print(ano%100)'''

'''resto da divisão dividido por 4 der resto 0, então o ano é bissexto'''

'''Exceto múltiplos de 100 que não são múltiplos de 400'''

if(ano==0):
    ano=date.today().year

if (((ano%100)%4)==0 and (ano%100)!=0 or (ano%400)==0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
