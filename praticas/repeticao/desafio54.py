ma=0
me=0
for c in range(1,8):
    n = int(input(f'Pessoa {c} digite sua idade:'))
    if n >= 21:
        ma += 1
    else:
        me += 1

print(f'A {ma} pesoas de maior')

print(f'A {me} pesoas de menor')