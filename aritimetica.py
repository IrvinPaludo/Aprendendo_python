''' Expreçoes
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1
'''
''' Ordem
1. ()
2. **
3. * / // %
4. + -
'''


n1 = int(input('Digite um numero: '))
#n2 = input('Digite um numero: ')
a = n1 - 1
d = n1 + 1

print('o numero é {}  seu anterior é {} e susesor {}'.format(n1,a,d))

n2 = int(input('Digite um numero: '))

print('o numero é {}'.format(n2))
print('o dobro do numero é {} \no triplo do numero é {}\na raiz quadrada do numero é {:.2f}'.format((n2*2),(n2*3),(n2**(1/2))))

n3 = int(input('digite a primeira nota: '))
n4 = int(input('digite a primeira nota: '))

print("A medi do aluno é : {}".format(((n3+n4)/2)))