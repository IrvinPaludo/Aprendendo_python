'''
Crie um programa onde possa se digitar 7 numeros e cadastre eles em 
ema lista que mantenha separado os valores pares e inpares . No final
mostre o valores em ordem crecente
'''

numeros = []
impar = []
par = []
n = 0
for p in range(1,8):
    n = int(input(f'Digite o {p}° numero: '))
    if n % 2 == 0:
        par.append(n)
       
    else:
        impar.append(n)
       


numeros.append(impar[:])
numeros.append(par[:])
#sorted(numeros)
print(f'Os numeros pares são: {sorted(numeros[1])}')
print(f'Os numeros impares são: {sorted(numeros[0])}')