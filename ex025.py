'''Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome'''

nome=str(input('Digite seu nome completo: '))

'''nome.lower(). >> vai transformar a palavra 'silva' em minúsculo
e vai pesquisar pela palavra 'silva'
True=sim; False=não'''

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
