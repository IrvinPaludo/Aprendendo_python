
n = s = 0
while True:
    n = int(input('digite um numero:(999 para parar) '))
    if n ==999:
        break
    s += n
print(f'A soma foi {s}')