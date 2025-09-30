
num = []
par = []
imp = []
cp=0
ci=0
m='S'
while True:
    if m =='S':
        d = int(input('Digite um valor: '))
        num.append(d)
    elif m =='N':
        break
    m = str(input('Quer continuar:[S/N] ')).upper()
for n in num:
    if n % 2 == 0:
        par.append(n)
        cp+=1
    else:
        imp.append(n)
        ci+=1
print(f'Os numero digitados foram: {num}')
if cp > 1:
    print(f'Os numeros pares digitados foram {par}')
else:
    print(f'O numero par digitado foi {par}')
if ci > 1:
    print(f'Os numeros impares digitados foram {imp}')
else:
    print(f'O numero impar digitado foi {imp}')