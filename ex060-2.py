""" Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x6x2x1=120 """

numero=int(input('Digite um número inteiro qualquer: '))

print('{}! = '.format(numero),end='')

contadora=numero
fatorial=1

while contadora>0:
    print('{}'.format(contadora),end='')
    if contadora>1:
        print(' x ',end='')
    else:
        print(' = ',end='')
    fatorial=fatorial*contadora
    contadora=contadora-1

print('{}'.format(fatorial))
