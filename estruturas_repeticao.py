from time import sleep


i = int(input('inicio: '))
f = int(input('fim:'))
p = int(input('paso:'))
for c in range(i,f+1,p):
  print(c)
  sleep(0.5)
print('FIM!')