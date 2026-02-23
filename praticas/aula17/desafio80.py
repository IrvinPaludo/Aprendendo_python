num=[]

for n in range(0,5):
    d = int(input('Digite um valor: '))
    if n == 0:
        num.append(d)
        print(f'O {d} foi adicionado na posição {num.index(d)}')
    elif d > num[-1]:
        num.append(d)
        print(f'O {d} foi adicionado no final da lista')
        #print(f'O {d} foi adicionado na posição {num.index(d)}')
    else:
        c = 0
        while c < len(num):
            if d <= num[c]:
                num.insert(c,d)
                print(f'O {d} foi adicionado na posição {c}')
                break
            c+=1
            
print('-=-'*25)
print(num)
