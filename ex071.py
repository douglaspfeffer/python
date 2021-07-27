""" Crie um programa que simule o financiamento de um CAIXA ELETRÔNICO. No início, pergunte o usuário
qual será o VALOR A SER SACADO (número inteiro) e o programa vai informar quantas CÉDULAS de cada valor
serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1 """

contador50=0
contador50Resto=0
contador20=0
contador20Resto=0
contador10=0
contador10Resto=0
contador1=0
contador1Resto=0

while True:
    valor=int(input('\nQuanto você quer sacar? R$ ')) #85

    if valor>=50: #85
        if valor//50>=1: #1
            contador50=valor//50 #1
            print(f'Total de {contador50} cédulas de R$50')
            if valor%50!=0: #35
                contador50Resto=valor%50 #35
                valor=contador50Resto #35

    if valor<50 and valor>=20:
        if valor<50:
            contador20Resto=valor%20 #15
            contador20=valor//20 #1
            valor=contador20Resto #15
        print(f'Total de {contador20} cédulas de R$20') #funcionando
    
    if valor<20 and valor>=10:
        if valor<20:
            contador10Resto=valor%10 #5
            contador10=valor//10 #1
            valor=contador10Resto #5
        print(f'Total de {contador10} cédulas de R$10') #funcionando
    
    if valor<10 and valor>=1:
        if valor<10:
            contador1Resto=valor%1 #0
            contador1=valor//1 #5
        print(f'Total de {contador1} cédulas de R$1') #funcionando
