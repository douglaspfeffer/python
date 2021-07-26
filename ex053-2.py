""" Crie um programa que leia uma frase qualquer e diga se ela é um políndromo desconsiderando os espaços. """

frase=str(input('Digite uma frase qualquier: '))
frase1=str(frase.replace(' ',''))

fraseReversa=frase1[::-1]

if frase1==fraseReversa:
    print('A palavra -> {} <- é palíndromo'.format(frase.upper()))
else:
    print('A palavra -> {} <- NÃO é palíndromo'.format(frase.upper()))
