
num=int(input('Digite um nuúmero inteiro : '))
print('Para qual base você quer converter:\n' \
'[1] Binario\n' \
'[2] Octal\n' \
'[3] Hexadecimal')
while True:
    m= int(input(''))
    if m == 1:
        num = bin(num)
        break        
    elif m == 2:
        num = oct(num)
        break
    elif m == 3:
        num = hex(num)
        break
    else :
        print('valor invalido \nTente de novo')
        
print(f'O valor ficou: {num [2:]}')