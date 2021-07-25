""" Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou o tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """

from datetime import date

anodenascimento=int(input('Digite a datra de nascimento: '))
anoatual=date.today().year
idade=anoatual-anodenascimento

if idade==18:
    print('Quem nasceu em {} precisa se alistar em {}'.format(anodenascimento,anodenascimento+18))
    print('É hora de se alistar! Você tem {} anos.'.format(idade))
elif idade<18:
    print('Quem nasceu em {} precisa se alistar em {}'.format(anodenascimento,anodenascimento+18))
    print('Ainda faltam {} anos para o seu alistamento'.format(18-idade))
else:
    print('Já passou o prazo de alistamento! Você tem {} anos'.format(idade-18))
    print('Você deveria ter se alistado em {}, há {} atrás'.format(anodenascimento+18,18-idade))
