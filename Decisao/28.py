print(' '*20,'Até 5 Kg',' '*6,'Acima de 5 Kg')
print('File Duplo',' '*3, 'R$ 4,90 por Kg',' '*5, 'R$ 5,80 por Kg')
print('Alcatra',' '*6, 'R$ 5,90 por Kg',' '*5, 'R$ 6,80 por Kg')
print('Picanha',' '*6, 'R$ 6,90 por Kg',' '*5, 'R$ 7,80 por Kg')


fi=int(input('Digite o peso do File Duplo'))
al=int(input('Digite o peso da Alcatra'))
pi=int(input('Digite o peso da Picanha'))
if fi<=5:
    pfi=fi*4.9
else:
    pfi=fi*5.8

if al<=5:
    pal=al*5.9
else:
    pal=al*6.8
if pi<=5:
    ppi=pi*6.9
else:
    ppi=pi*7.8 
total=pal+ppi+pfi

print('Total a pagar é:', total)
print('Se a compra for feita no cartão Tabajara o total é:',round(total-total*5/100,2))