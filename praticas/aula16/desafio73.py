
from time import sleep

coloca =('Flamengo','Cruzeiro','Palmeiras','Mirassol','Botafogo','Bahia','São Paulo',
         'Fluminense','Bragantino','Corinthians','Ceará','Grêmio','Internacional',
         'Santos','Atlético Mineiro','Vasco da Gama','Vitória','Juventude','Fortaleza',
         'Recife')
print('-=-'*10)
print(f'{'Brasileirão':^30}')

print('-=-'*10)
while True:
    
    m = int(input('O que voce quer saber\n[1]Os 5 primeiros \n[2]Os ultimos 4 \n[3]A lista dos times \n[4]A posição do seu time\n[5]Para sair\n'))
    if m !=5:
        print( '-=-'*10 )
    if m==1:
        print(coloca[:6])
        break
    elif m==2:
        print(coloca[-4:])
        break
    elif m==3:
        alfabet = sorted(coloca)
        print(alfabet)
        break
    elif m==4:
        meu = str(input('Qual é seu time: ')).strip().capitalize()
        print(f'O Seu time esta na {coloca.index(meu)+1}ª posisão')
        break
    elif m==5:
        break
    else:
        
        print('Opção invalida')
        sleep(1)
print('-=-'*10)