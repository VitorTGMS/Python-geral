div=float(input('Digite o valor da divida'))
par=int(input('Digite oo numero de parcelas'))
parc=0

print('Quantidade de parcelas  % de juros sobre o valor inicial da divida')
print(1,' '*5,0)
print(3,' '*5,10)
print(6,' '*5,15)
print(9,' '*5,20)
print(12,' '*4,25)

for parc, jur in [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]:
    if parc<=par:
        vjur=div*jur/100
        vdiv=div+vjur
        vpar=vdiv/par
        vdiv=round(vdiv)
        vpar=round(vpar)
        print(vdiv,'|', vjur, '|', parc,'|', vpar)
    