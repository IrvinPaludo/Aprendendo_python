nome = ''
preco = 0
menu = 'S'
gasto = 0
mais = 0
baraton = ''
baratop = 0
c = 0
print('-=-'*15)
print('       Loja')
print('-=-'*15)
while True:
    if menu ==  'S':
       
        nome = str(input('NOME DO PRODUTO: '))
        preco = float(input('Preço: '))
        if c == 0:
            baraton = nome
            baratop = preco
        if preco < baratop:
            baraton = nome
            baratop = preco

        gasto += preco
        c += 1 
        if preco > 1000:
            mais +=1
        #print('\n')
    menu = str(input('Quer continuar comprando: [S/N] ')).upper().strip()
    if menu == "N":
        break

print('-=-'*15)
print(f'O total das compras é R${gasto:.2f}')
print(f'Você comprou {mais} produtos acima de R$1000.00')
print(f'O produto mais barato foi ({baraton}):R${baratop:.2f}')