""" Faça um programa que calcula a soma entre todos os números pares que são múltiplos de 3 e que se encontram
no intervalo de 1 até 500 """

soma=0

for c in range(1,500+1):
    if c%2!=0:
        if c%3==0:
            soma=soma+c
print('A soma é {}'.format(soma))
