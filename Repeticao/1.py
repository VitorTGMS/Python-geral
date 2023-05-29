nota=(float(input('Digite uma nota')))

while nota<0 or nota >10:
    print('nota invalida')
    nota=int(input())
print('Nota valida')