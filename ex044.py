""" Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e
condição de pagamento:
- À vista dinheiro / cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros """

preco=float(input('Digite o preço do produto: '))
print('Escolha a forma de pagamento: ')
print('1- À vista dinheiro / cheque: 10% de desconto\n2- À vista no cartão: 5% de desconto')
print('3- Em até 2x no cartão: preço normal\n4- 3x ou mais no cartão: 20% de juros')
escolha=int(input())

desconto10p=preco*0.1
desconto5p=preco*0.05
juros20p=preco*0.2

if escolha==1:
    print('Sua escolha foi: À vista dinheiro / cheque: 10% de desconto')
    print('O valor a ser pago com 10% de desconto é de R${:.2f}'.format(preco-desconto10p))
elif escolha==2:
    print('Sua escolha foi: À vista no cartão: 5% de desconto')
    print('O valor a ser pago com 5% de desconto é de R${:.2f}'.format(preco-desconto5p))
elif escolha==3:
    print('Sua escolha foi: Em até 2x no cartão: preço normal')
    print('O valor a ser pago é de R${:.2f}'.format(preco))
elif escolha==4:
    print('Sua escolha foi: 3x ou mais no cartão: 20% de juros')
    parcelas=int(input('Deseja parcelar em quantas vezes? '))
    print('Sua compra será parcelada em {}x de {:.2f} com juros!'.format(parcelas,preco/parcelas))
    print('O valor total a ser pago será de de R${:.2f}'.format(preco+juros20p))
else:
    print('Escolha inválida')
