
print('='*30)
print(f'{'Banco':^30}')
print('='*30)

valor = int(input('Qual valor você quer sacar? R$'))

total = valor
not50 = 0
not20 = 0
not10 = 0
not5 = 0
not1 = 0
while total >=50:
    total-=50
    not50+=1
if total >=20:
    while total >=20:
        total-=20
        not20+=1
if total >=10:
    while total >=10:
        total-=10
        not10+=1
if total >=5:     
    while total >=5:
        total-=5
        not5+=1
if total >=1:
    while total >=1:
        total-=1
        not10+=1
        
if not50 !=0:
    print(f'Total de {not50} notas de R$50')
if not20 !=0:
    print(f'Total de {not20} notas de R$20')
if not10 !=0:
    print(f'Total de {not10} notas de R$10')
if not5 !=0:
    print(f'Total de {not5} notas de R$5')
if not1 !=0:
    print(f'Total de {not1} notas de R$1')
print('='*30)
print(f'{'Volte sempre!':^30}')
print('='*30)