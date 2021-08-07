""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente """

lista=[]
escolha=''

while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    escolha=str(input('Quer continuar? [S/N] '))
    if escolha in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    escolha2=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if escolha2==999:
        break
    if escolha2<=len(lista):
        print(f'Notas de {lista[escolha2][0]} são {lista[escolha2][1]}')
print('Fim')
