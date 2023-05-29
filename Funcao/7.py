def valorPagamento(vpres, dias):
    if dias>0:
        vpres=vpres+vpres*0.03+vpres*dias*0.001
    return vpres
    
pres=[]
n=0
while True:
    vpres=float(input('Digite o valor da prestação\n'))
    if vpres==0:
        break
    dias=int(input('Digite a quantidade de dias\n'))
    
    print(f'O valor a ser pago é:{valorPagamento(vpres, dias)}')
    vpres=valorPagamento(vpres, dias)
    pres.append(vpres)
    

print('RELATORIO DO DIA')
for i,pres in enumerate(pres):
    print(f'{pres}')
