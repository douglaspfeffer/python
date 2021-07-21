'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre a mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite'''

velocidade=float(input('Digite a velocidade em Km/h: '))

if (velocidade>80):
    print('Você foi multado!\nA muklta vai custar R${}!'.format((velocidade-80)*7))
else:
    print('Você está dentro da velocidade, portanto não foi multado.')
