''' Faça um programa que tenha uma função chamada área(), que receba 
as dimensões de um terreno retangular (largura e comprimento) e 
mostre a área do terreno.'''



def area(a,b):
    total = a*b
    print(f'A área de um terreno {a:.2}x{b:.2} é de {total}m²')
print('CONTROLE DE TERRENOS')
print('-'*30)

l = float(input('Qual é a Largura (m):'))
c = float(input('Qual é a comprimento (m):'))

area(l,c)
