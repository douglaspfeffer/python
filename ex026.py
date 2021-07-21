'''Faça um programa que leia uma frase pelo teclado e mostre:
1) Quantas vezes aparece a letra A
2) Em que posição ela aparece a primeira vez
3) Em que posição ela aparece pela última vez'''

frase=str(input('Digite uma frase: '))
print('A letra "A" aparece {} vezes.'.format(frase.upper().strip().count('A')))

'''frase.upper().count('a') >> vai transformar a frase em maiúsculo e vai procurar a quantidade de letras 'a' na frase'''

print('A letra A aparece pela primeira vez na posição {}'.format(frase.upper().strip().find('A')+1))

'''vai procurar a primeira letra 'a' '''

print('A letra A aparece pela última vez na posição {}'.format(frase.upper().strip()''.rfind('A')+1))

'''vai procurar a última letra 'a' '''
