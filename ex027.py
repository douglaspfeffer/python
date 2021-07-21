'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro=Ana
último=Souza'''

nome=str(input('Digite seu nome completo: '))

print('Primeiro nome: {}\nÚltimo nome: {}'.format(nome.split()[0],nome.split()[len(nome.split())-1]))

''' print(nome.split()[0]) > nome na posição 0'''

'''print(len(nome.split())) > quantidade de nomes'''
