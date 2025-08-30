from random import  randint
from time  import sleep

n1 = randint(0 , 5 ) #sorteia o numero entre 0 e 5
print('-=- '*20)
n2 = int(input("digite um numero entre 0 e 5 : "))
print('-=- '*20)
print('--pensando--')
sleep(3)
if n1==n2:
    print('-=- você acertou :) -=-')
else:
    print('-=- você erro :( -=- ')
    print('O numero era {}, você falo {}'.format(n1,n2))