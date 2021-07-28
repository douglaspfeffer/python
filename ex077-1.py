""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as suas vogais. """

lista=('aprender','computador','mouse','teclado')

print('\n')

for c in range(0,len(lista)):
    
    print(f'\nA palavra {lista[c].upper()} tem as vogais -',end=' ')

    if 'a' in lista[c]:
        print('A',end=' ')

    if 'e' in lista[c]:
        print('E',end=' ')

    if 'i' in lista[c]:
        print('I',end=' ')

    if 'o' in lista[c]:
        print('O',end=' ')

    if 'u' in lista[c]:
        print('U',end=' ')

print('\n')
