# Faça um progerama que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separadores.
# Ex: 1834
# unidade=4
# dezena=3
# centena=8
# milhar=1

numero=int(input('Digite um número inteiro entre 0 e 9999: '))
unidade=numero%10
dezena=((numero-unidade)/10)%10
centena=((((numero-unidade)/10)-dezena)/10)%10
milhar=((((numero-unidade)/10)-dezena)/10)//10
print('Unidade: {:.0f}\nDezena: {:.0f}\nCentena: {:.0f}\nMilhar: {:.0f}'.format(unidade,dezena,centena,milhar))

'''código de júlia
valor = int(input("Digite um número inteiro entre 0 e 9999: "))
milhar = int(valor / 1000)
centena = int((valor%1000)/100)
dezena = int(((valor%1000)%100)/10)
unidade = int((((valor%1000)%100)%10))
print("milhar: {} centena {} dezena {} unidade {}".format(milhar, centena, dezena, unidade))'''

