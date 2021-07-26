""" Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while """

primeiroTermo=int(input('Digite o primeiro: '))
razao=int(input('Digite a razão: '))

contadora=1
termo=primeiroTermo

while contadora<=10:
    print('{} -> '.format(termo),end='')
    termo=termo+razao
    contadora=contadora+1
print('Fim')
