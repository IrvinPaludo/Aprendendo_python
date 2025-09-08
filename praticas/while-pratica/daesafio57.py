#or sexo != 'F':
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('qual é seu sexo: (M/F)')).upper().strip()
    print(sexo)