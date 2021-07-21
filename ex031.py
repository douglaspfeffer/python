'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.'''

distancia=float(input('Digite a distância em Km: '))

if (distancia<=200):
    print('O valor da viagem para os {}Km percorridos é: R${}'.format(distancia,(distancia*0.5)))
else:
    print('O valor da viagem para os {}Km percorridos é: R${}'.format(distancia, (distancia * 0.45)))
