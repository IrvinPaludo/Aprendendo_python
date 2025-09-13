n1 = 0
c = 0
n2 = 0
while n1 != 999:
    n1 = int(input('digite um numero: '))
    c +=1
    n2 += n1
print('Você digitou {} números e a soma deles é {}'.format(c-1,n2-999))