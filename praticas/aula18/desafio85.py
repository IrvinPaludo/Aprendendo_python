'''
Crie um programa onde possa se digitar 7 numeros e cadastre eles em 
ema lista que mantenha separado os valores pares e inpares . No final
mostre o valores em ordem crecente
'''

numeros = [[],[]]

n = 0
for p in range(1,8):
    while True:
        try:
            n = int(input(f'Digite o {p}° numero: '))
            if n % 2 == 0:
                numeros[0].append(n)
            
            else:
                numeros[1].append(n)
            break
        except:
            print('Erro')
numeros[0].sort
numeros[1].sort
print(f'Os numeros pares são: {numeros[0]}')
print(f'Os numeros impares são: {numeros[1]}')