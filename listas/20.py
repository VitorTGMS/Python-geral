salario=[]
tabono=0
n=0
max_abono=0
while True:
    sal=float(input('Digite o valor do seu salário'))
    if sal==0:
        break
    while sal<0:
        sal=float(input('Valor do salário invalido\nDigite o valor do seu salário'))
    salario.append(sal)

for i in salario:
    abono=i*20/100
    if abono>max_abono:
        max_abono=abono
    if abono<100:
        n+=1
        abono=100
    
    tabono+=abono
    print('Salário - Abono')
    print('R$ {:>4}-R$ {:>4}'.format(i, abono))

print(f'Foram processados {len(salario)} colaboradores')
print(f'O total gasto com abonos: {tabono}')
print(f'O valor minímo pago a {n} colaboradores')
print(f'Maior valor de abono foi:{max_abono}')