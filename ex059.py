""" Crie um programa que leia 2 valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso """

numero1=float(input('Digite o primeiro número qualquer: '))
numero2=float(input('Digite o segundo  número qualquer: '))

escolha=0

while escolha!=5:
    if escolha==0:
        print('\nO que você deseja?\n')
        print('[1] Somar                     [2] Multiplicar')
        print('[3] Maior número              [4] Novos números')
        print('[5] Sair do programa\n')
        escolha=int(input('Escolha sua opção: '))

    if escolha==1:
        soma=numero1+numero2
        print('A soma entre {} e {} é {}'.format(numero1,numero2,soma))
        escolha=0

    if escolha==2:
        multiplicacao=numero1*numero2
        print('A multiplicação entre {} e {} é {}'.format(numero1,numero2,multiplicacao))
        escolha=0

    if escolha==3:
        if numero1>numero2:
            print('O maior valor é o número {}'.format(numero1))
            escolha=0
        else:
            print('O maior valor é o número {}'.format(numero2))
            escolha=0

    if escolha==4:
        numero1=float(input('Digite o primeiro número qualquer: '))
        numero2=float(input('Digite o segundo  número qualquer: '))
        escolha=0
        
    if escolha>5:
        print('Opção inválida, tente novamente')
        escolha=0

print('Você saiu do programa')
