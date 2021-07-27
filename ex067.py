""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo. """

contadora=1

while True:
    numero=int(input('\nVocêr quer ver a tabuada de qual valor? '))
    print('\n')
    if numero<0:
        break
    while contadora<=10:
        multiplicacao=numero*contadora
        print(f'{numero} x {contadora} = {multiplicacao}')
        contadora=contadora+1
    contadora=1
print('\nVocê digitou um número negativo. Programa encerrado!\n')
