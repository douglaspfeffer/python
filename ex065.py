""" Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores  """

continuar=''
media=0
contador=0
menorNumero=0
maiorNumero=0

numero=int(input('Digite um número inteiro qualquer: '))

menorNumero=numero
maiorNumero=numero

while not continuar=='n':
    media=media+numero
    contador=contador+1
    continuar=str(input('Deseja continuar? [s/n]: '))
    if continuar=='s':
        numero=int(input('Digite um número inteiro qualquer: '))
        if numero>maiorNumero:
            maiorNumero=numero
        else:
            menorNumero=numero
print('\nA média dos números digitados é: {}'.format(media/contador))
print('O maior número é {} e o menor número é {}\n'.format(maiorNumero,menorNumero))
