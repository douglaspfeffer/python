""" Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício, indo de
10 até 0, com uma pasa de 1 segundo entre eles. """

from time import sleep

print('CONTAGEM REGRESSIVA:\n')
sleep(1)
for c in range(10,0-1,-1):
    print(c)
    sleep(1)
print('\033[31mESTOURANDO OS FOGOS DE ARTIFÍCIOS!')
