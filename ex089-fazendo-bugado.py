""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente """

lista=[]
lista2=[]
escolha=''

nome=str(input('Nome: '))
lista.append(nome.capitalize())
nota1=float(input('Nota 1: '))
lista.append(nota1)
nota2=float(input('Nota 1: '))
lista.append(nota2)
media=(nota1+nota2)/2
lista.append(media)
contadora=1
escolha=str(input('Quer continuar? [S/N]'))


while True:

    if escolha=='s':
        nome=str(input('Nome: '))
        lista.append(nome.capitalize())
        nota1=float(input('Nota 1: '))
        lista.append(nota1)
        nota2=float(input('Nota 1: '))
        lista.append(nota2)
        media=(nota1+nota2)/2
        lista.append(media)
        contadora=contadora+1
        escolha=str(input('Quer continuar? [S/N]'))
    elif escolha=='n':
        break
    else:
        print('Escolha inválida, tente novamente.',end=' ')
        escolha=str(input('Quer continuar? [S/N]'))

for c in range(0,len(lista),4):
    print(f'Nome: {lista[c]}',end=' ')

for c in range(3,len(lista),3):
    print(f'Média: {lista[c]}')
    print()
