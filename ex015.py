km=float(input('Quantos Km foram percorridos pelo carro? '))
dia=int(input('Por quantos dias o carro foi alugado? '))
print('O preço a pagar por {}Km percorridos em {} dias é de R${:.2f}'.format(km,dia,(60*dia)+(0.15*km)))
