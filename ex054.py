""" Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores. """

from datetime import date

anoatual=date.today().year
maioridade=0
minoridade=0

for c in range(1,7+1):
    anodenascimento=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if anoatual-anodenascimento>=18:
        maioridade=maioridade+1
    else:
        minoridade=minoridade+1
print('\n{} pessoas atingiram a MAIORIDADE\n{} pessoas ainda são MENORES de 18\n'.format(maioridade,minoridade))
