""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as suas vogais. """

lista=('aprender','computador','mouse','teclado')

for c in lista:
    print(f'\nNa palavra {c.upper()} temos ',end='')
    for letra in c:
        if letra.lower() in 'aeiouAEIOU':
            print(letra,end=' ')
print('\n')
