""" Melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos """

primeiroTermo=int(input('Digite o primeiro: '))
razao=int(input('Digite a razão: '))

contadora=1
termo=primeiroTermo
totalTermos=0
maisTermos=10

while maisTermos!=0:
    totalTermos=totalTermos+maisTermos
    while contadora<=totalTermos:
        print('{} -> '.format(termo),end='')
        termo=termo+razao
        contadora=contadora+1
    print('Pausa')

    maisTermos=int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')
