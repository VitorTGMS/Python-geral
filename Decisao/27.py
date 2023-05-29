print(' '*17,'Até 5 Kg',' '*6,'Acima de 5 Kg')
print('Morango',' '*3, 'R$ 2,50 por Kg',' '*5, 'R$ 2,20 por Kg')
print('Maça',' '*6, 'R$ 1,80 por Kg',' '*5, 'R$ 1,50 por Kg')

mo=int(input('Digite o peso do morango'))
ma=int(input('Digite o peso da maça'))

if mo<=5:
    pmo=mo*2.5
else:
    pmo=mo*2.2

if ma<=5:
    pma=ma*1.8
else:
    pma=ma*1.5

total=pmo+pma

if total>25 or mo+ma>8:
    total=total+total*10/100
print('Total a pagar é:', total)