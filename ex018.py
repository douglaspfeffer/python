#Faça um programa que leia um ângulo qualquqer e mostre na tela o valor do seno, cosseno e tangente
#desse ângulo.
from math import sin,cos,tan,radians
angulo=float(input('Digite o ângulo: '))
print('O ângulo é {}\nO seno é {:.4f}\nO Cosseno é {:.4f}\nA tangente é {:.4f}'.format(angulo,sin(radians(angulo)),cos(radians(angulo)),tan(radians(angulo))))
