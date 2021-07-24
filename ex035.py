'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''

comprimentoReta1=float(input('Digite o comprimento da reta 1: ')) #3.5
comprimentoReta2=float(input('Digite o comprimento da reta 2: ')) #2.75
comprimentoReta3=float(input('Digite o comprimento da reta 3: ')) #4

if((comprimentoReta1+comprimentoReta2)>comprimentoReta3 and (comprimentoReta1+comprimentoReta3)>comprimentoReta2 and (comprimentoReta2+comprimentoReta3)>comprimentoReta1):
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
