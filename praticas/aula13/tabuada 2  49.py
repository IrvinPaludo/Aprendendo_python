from time import sleep
n = int(input('qual tabuada você quer? '))

for c in range (0,11):
    print('{} * {} = {} '.format(n,c,n*c))
    sleep(0.5)
