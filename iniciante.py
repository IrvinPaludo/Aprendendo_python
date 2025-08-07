coisa = input('digite alguma coisa: ')

print(coisa)

print(type(coisa))
print('é composto por alfanumericos',coisa.isalnum())
print('é composto por letras',coisa.isalpha())
print('é composto por letras minusculas',coisa.islower())
print('é composto por numeros',coisa.isnumeric())
print('é composto pela primeira letras maiusculas',coisa.istitle())