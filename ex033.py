'''Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.'''

numero1=float(input('Digite o primeiro número: '))
numero2=float(input('Digite o segundo número: '))
numero3=float(input('Digite o terceiro número: '))

menor1e2=0
menor1e2e3=0
menor1e2e3f=0

maior1e2=0
maior1e2e3=0

'''Maior e menor entre 1 e 2'''
if(numero1>=numero2):
    maior1e2=numero1
    menor1e2=numero2
else:
    maior1e2=numero2
    menor1e2=numero1

'''Maior e menor entre 1 e 2'''
if(maior1e2>=numero3):
    maior1e2e3=maior1e2
    menor1e2e3=numero3
else:
    maior1e2e3=numero3
    menor1e2e3=maior1e2

'''Menor entre 1-2 e 3'''
if(menor1e2>=menor1e2e3):
    menor1e2e3f=menor1e2e3
else:
    menor1e2e3f=menor1e2

print('O menor número é {}\nO maior número é {}'.format(menor1e2e3f,maior1e2e3))
