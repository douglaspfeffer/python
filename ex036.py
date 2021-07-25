""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado. """

valordacasa=float(input('Digite o valor da casa: '))
salario=float(input('Digite o seu salário: '))
anos=int(input('Em quantos anos irá pagar? '))
prestacao=valordacasa/(anos*12)

if prestacao<=salario*0.3:
    print('Seu empréstimo foi APROVADO! Sua prestação será de R${:.2f} por mês'.format(prestacao))
else:
    print('Seu empréstimo foi NEGADO! Sua prestação seria de R${:.2f} por mês'.format(prestacao))
