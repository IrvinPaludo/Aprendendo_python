
n = s = c = 0
while True :
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s+=n
    c+=1
print(f'Você digitou {c} numeros e a soma foi {s}')
print('Acabo')