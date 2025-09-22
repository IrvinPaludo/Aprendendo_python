
while True:
    print('-=-'*25)
    n = int(input('Quer ver a tabuada de qual numero: '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
        c+=1

   
print('-=-'*25)
print('Você digitou um numero invalido')
print('Programa encerrado!')
    