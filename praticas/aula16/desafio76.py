
mercado = ('leite',4.5,'pão',8,'lapis',1.75,'fogão',150.51)
           #str(input('Digite um prodito:')),int(input('Valor:')))

print('='*37)
print(f'{'Mercado':^37}')
print('='*37)

for n in range(0,len(mercado),2):
    print(f'{mercado[n]:.<30}'.capitalize()+'R$'+f'{mercado[n+1]:>5.2f}' )
    
