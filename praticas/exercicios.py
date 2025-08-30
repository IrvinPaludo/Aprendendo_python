import math
'''
numero = float(input('digite um numero: '))

print('o numero foi {}'.format(math.floor(numero)))'''

cateto_a= float(input('digite o primeiro cateto: '))
cateto_b= float(input('digite o segundo cateto: '))
#hipotenusa = ((cateto_a ** 2 ) + (cateto_b ** 2 )) **(1/2)
hipotenusa = (math.pow(cateto_a,2) + math.pow(cateto_b,2)) **(1/2)

print('A hipotenusa é: {}'.format(hipotenusa))