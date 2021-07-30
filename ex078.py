""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista. """

valores=[]

for c in range(1,5+1):
    valores.append(int(input('Digite um número: ')))

maiorValor=max(valores)
menorValor=min(valores)  

print(f'\nO maior valor é {max(valores)} na posição {valores.index(maiorValor)+1} e o menor valor é {min(valores)} na posição {valores.index(menorValor)+1}\n')
