#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
catetooposto=float(input('Digite o valor do cateto oposto: '))
catetoadjacente=float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f}'.format(hypot(catetooposto,catetoadjacente)))
