""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de ZERO até
VINTE. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. """

lista=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:

    numero=int(input('Digite um número inteiro entre 0 e 20: '))

    while numero<0 or numero>20:
        print('Tente novamente. ',end='')
        numero=int(input('Digite um número inteiro entre 0 e 20: '))

    print(f'\nO número {numero} por extensó é {lista[numero].capitalize()}\n')
    break
