num=[]

for n in range(0,5):
    d = int(input('Digite um valor: '))
    if n == 0:
        num.append(d)
    elif d > num[-1]:
        num.append(d)
    else:
        c = 0
        while c < len(num):
            if d <= num[c]:
                num.insert(c,d)
                break
            c+=1
            
print('-=-'*25)
print(num)
