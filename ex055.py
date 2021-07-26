""" Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos. """

maiorPeso=0
menorPeso=0

for c in range(1,5+1):
    peso=float(input('Digite o peso da pessoa {}: '.format(c)))
    if c==1:
        maiorPeso=peso
        menorPeso=peso
    else:
        if peso>maiorPeso:
            maiorPeso=peso
        if peso<menorPeso:
            menorPeso=peso

print('O maior peso é de {}Kg\nO menor peso é de {}Kg'.format(maiorPeso,menorPeso))
