c=0
c2=0
num=[]
for n in range(0,5):
    num.append(int(input(f'insiraum numero para a posição {n}: ')))

print(f'O mair numero foi {max(num)} e está na posiçâo ',end=(''))
for c,v in enumerate(num):#para cada valor {v} coloca um indice{c}
    if v == max(num):
        print(c,end='... ')

print(f'\nO menor numero foi {min(num)} e está na posiço ',end=(''))
for n in num:
    if n == min(num):
        print(c2,end='... ')
    c2+=1

