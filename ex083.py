""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta. """

lista=[]

expressao=str(input('Digite uma expressão qualquer: '))

for simbolo in expressao:

    if simbolo=='(':
        lista.append('(')
    
    elif simbolo==')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista)==0:
    print('\nSua expressão está válida\n')
else:
    print('\nSua expressão está errada\n')
