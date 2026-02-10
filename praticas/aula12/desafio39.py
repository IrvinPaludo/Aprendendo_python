ano = 2026
print('Alistamento')
idade = ano - int(input('Qual o ano de seu nacimento? '))

if idade == 18:
    print('Você presisa se alistar!')
elif idade > 18:
    print('Você deveria ter se alistado')
    print(f'Você esta atrasado {idade-18} anos')
else:
    print(f'Você precisa se alistar da qui a {18-idade} anos')
