#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
nome1=input('Digite o nome do aluno 1: ')
nome2=input('Digite o nome do aluno 2: ')
nome3=input('Digite o nome do aluno 3: ')
nome4=input('Digite o nome do aluno 4: ')
print('O aluno sorteado foi: {}'.format(choice([nome1,nome2,nome3,nome4])))
