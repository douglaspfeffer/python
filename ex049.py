""" Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
um laço for. """

numero=int(input('Digite um número: '))

print('A tabuada do número {} é:\n'.format(numero))

for c in range(1,10+1):
    print('{} x {:2} = {}'.format(numero,c,numero*c))
