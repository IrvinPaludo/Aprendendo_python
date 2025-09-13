c=1
n = 0
while True:
    print('-=-'*25)
    n = int(input('Quer ver a tabuada de qual numero: '))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c+=1
    c=0
   
print('-=-'*25)
print('Você digitou um numero invalido')
print('Programa encerrado!')
    