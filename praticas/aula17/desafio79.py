
d=0
n=[]
m='S'

while True:
    if m =='S':
        d=int(input('Digite um valor: '))
        if d in n:
            print('O valor esta duplicado, não sera adicionado')
        else:
            print('Valor adicionado com sucesso!')
            n.append(d)
    elif m=='N':
        break
    else:
        print('Valor invalido')

    m = str(input('Quer continuar: S/N ')).upper()

print('-=-'*25)
print(f'Os valores digitados foram: {sorted(n)}')