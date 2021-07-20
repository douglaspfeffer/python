# Faça um progerama que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separadores.
# Ex: 1834
# unidade=4
# dezena=3
# centena=8
# milhar=1

'''numero=int(input('Digite um número inteiro entre 0 e 9999: '))
unidade=numero%10
#123 = 3
dezena=((numero-unidade)/10)%10
#((123-3)/10)%10 = ((120)/10)%10 = (12%10)=2
centena=(((numero-unidade)/10)-dezena)/10
#(((123-3)/10)-2)/10 = (((120)/10)-2)/10 = ((12-2)/10) = (10/10) = 1
#milhar=centena%10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
#print('Centena: {}'.format(milhar))

print('Unidade: {}')
print('Dezena: {}')
print('Centena: {}')
print('Milhar: {}')'''

valor = int(input("Digite um número inteiro entre 0 e 9999: "))
milhar = int(valor / 1000)
centena = int((valor%1000)/100)
dezena = int(((valor%1000)%100)/10)
unidade = int((((valor%1000)%100)%10))
print("milhar: {} {} {} {}".format(milhar, centena, dezena, unidade))

