#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considarar os espaços)
#Quantas letras tem o primeiro nome

nome=str(input('Digite seu nome completo: '))
print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('O nome tem {} letras ao todo sem contar os espaços.'.format(len(nome)-len(nome.split())+1))
print('O primeiro nome tem {} letras.'.format(len(nome.split()[0])))

#mostra o primeiro nome print(nome.split()[0])
#mostra a quantidade de caracteres com espaço print(len(nome))
#mostra a quantidade de nomes len(nome.split())
#mostra o nome junto - print(nome.split())
