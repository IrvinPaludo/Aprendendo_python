nome = str(input('Digite seu nome completo: ')).strip()


print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

print('seu nome tem Silva: {}'.format('silva'in nome.lower().split()))

