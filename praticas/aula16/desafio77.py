lista = ('Aprender','Programa','Linguagem','Python')

for n in lista:
    print(f'\nA palavra {n.upper()} tem as vogais:',end='')
    for l in n:
        if l.lower() in 'aeiou':
            print(l.lower(),end=' ')
    