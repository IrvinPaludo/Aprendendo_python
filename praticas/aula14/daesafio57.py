#for sexo != 'F':
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('qual é seu sexo: (M/F)')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print(f'dados invalidos{sexo}')
print(f'Dados sexo {sexo} valido')