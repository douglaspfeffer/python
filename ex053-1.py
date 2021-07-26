""" Crie um programa que leia uma frase qualquer e diga se ela é um políndromo desconsiderando os espaços. """

frase=str(input('Digite uma frase qualquier: ')).strip().upper()
junto=str(frase.replace(' ',''))
fraseReversa=''

quantidadeLetras=len(junto)

for c in range(quantidadeLetras-1,-1,-1):
    fraseReversa=fraseReversa+junto[c]

if junto.upper()==fraseReversa.upper():
    print('A palavra -> {} <- é palíndromo'.format(frase))
else:
    print('A palavra -> {} <- NÃO é palíndromo'.format(frase))
