""" Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint

escolhaComputador=''
vitoria=0

while True:
    soma=0
    numeroUsuario=int(input('Digite um valor: '))
    numeroComputador=randint(0,10)
    escolhaUsuario=str(input('Par ou Impar [p/i] ')).lower().strip()
    soma=numeroUsuario+numeroComputador

    if escolhaUsuario=='p':
        if soma%2==0:
            vitoria=vitoria+1
            print('\nParabéns, você venceu!')
            print(f'Você escolheu {numeroUsuario} e eu escolhi {numeroComputador} e {soma} é PAR\n')
        else:
            print(f'\nVocê perdeu! Você venceu {vitoria} vezes')
            print(f'Você escolheu {numeroUsuario} e eu escolhi {numeroComputador} e {soma} é ÍMPAR\n')
            break
    
    if escolhaUsuario=='i':
        if soma%2!=0:
            vitoria=vitoria+1
            print('\nParabéns, você venceu!')
            print(f'Você escolheu {numeroUsuario} e eu escolhi {numeroComputador} e {soma} é ÍMPAR\n')
        else:
            print(f'\nVocê perdeu! Você venceu {vitoria} vezes')
            print(f'Você escolheu {numeroUsuario} e eu escolhi {numeroComputador} e {soma} é PAR\n')
            break
print('Fim')
