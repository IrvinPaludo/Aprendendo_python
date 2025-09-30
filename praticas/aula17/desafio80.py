num=[]

for n in range(0,5):
    d = int(input('Digite um valor: '))
    if n == 0:
        num.append(d)
    else:
        if d > num:
            num.insert(num.index(num),d)
        elif d < num :
            

print(num)