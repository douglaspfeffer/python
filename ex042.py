""" Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes """

comprimentoReta1=float(input('Digite o comprimento da reta 1: ')) #3.5
comprimentoReta2=float(input('Digite o comprimento da reta 2: ')) #2.75
comprimentoReta3=float(input('Digite o comprimento da reta 3: ')) #4

if((comprimentoReta1+comprimentoReta2)>comprimentoReta3 and (comprimentoReta1+comprimentoReta3)>comprimentoReta2 and (comprimentoReta2+comprimentoReta3)>comprimentoReta1):
    print('Os segmentos acima PODEM formar um triângulo')
    if comprimentoReta1==comprimentoReta2 and comprimentoReta2==comprimentoReta3:
        print('O triângulo a ser formado é um triângulo EQUILÁTERO')
    elif comprimentoReta1==comprimentoReta2 and comprimentoReta2!=comprimentoReta3 or comprimentoReta1==comprimentoReta3 and comprimentoReta1!=comprimentoReta2:
        print('O triângulo a ser formado é um triângulo ISÓSCELES')
    else:
        print('O triângulo a ser formado é um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
