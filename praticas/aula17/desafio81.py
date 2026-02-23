num=[]
m = 'S'
c=0
while True:
    if m =='S':
        d = int(input('Digite um valor: '))
        num.append(d)
        c+=1
    elif m == 'N':
        break
    m = str(input('Quer continuar: [S/N] ')).upper()
print('-=-'*15)
print(f'Você digitou {c} numeros')
num.sort(reverse=True)
print(f'A lista decrecente é: {num}')
if 5 in num:
    print('O numero 5 foi digitado')
else:
    print('O numero 5 não foi digitado')