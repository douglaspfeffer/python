'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%'''

salario=float(input('Digite o seu salário em R$: '))

if(salario>1250):
    print('O seu novo salário com o aumento de 10% é de {}'.format(salario+((10*salario)/100)))
else:
    print('O seu novo salário com o aumento de 15% é de {}'.format(salario+((15*salario)/100)))